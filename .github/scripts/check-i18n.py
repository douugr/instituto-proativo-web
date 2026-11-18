#!/usr/bin/env python3
"""Confere se as versões traduzidas do site acompanham a versão em português.

As três páginas (site/index.html, site/en/index.html e site/es/index.html)
precisam ter a mesma estrutura: as mesmas seções e âncoras, as mesmas imagens,
os mesmos links externos e os mesmos eventos de clique do GoatCounter. Se
alguém alterar só uma delas, esta verificação falha no CI.

Uso: python3 .github/scripts/check-i18n.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "site"
PAGES = {
    "pt": (ROOT / "index.html", "pt-BR", ""),
    "en": (ROOT / "en" / "index.html", "en", "../"),
    "es": (ROOT / "es" / "index.html", "es-419", "../"),
}

errors = []


def fail(msg):
    errors.append(msg)


def images(html, prefix):
    found = re.findall(r'(?:src|srcset)="([^"]+)"', html)
    paths = []
    for attr in found:
        for part in attr.split(","):
            url = part.strip().split(" ")[0]
            if url.startswith("http"):
                continue
            if prefix and url.startswith(prefix):
                url = url[len(prefix):]
            paths.append(url)
    return paths


def external_links(html):
    # Só links clicáveis (<a>); canonical/og:url mudam de propósito em cada idioma.
    links = re.findall(r'<a\s[^>]*href="(https?://[^"]+)"', html)
    # O texto da mensagem do WhatsApp muda conforme o idioma; o que importa é o número.
    return [re.sub(r"\?text=.*", "", u) for u in links]


def clicks(html, lang):
    names = re.findall(r'data-goatcounter-click="([^"]+)"', html)
    suffix = "" if lang == "pt" else f"-{lang}"
    if suffix:
        bad = [n for n in names if not n.endswith(suffix)]
        if bad:
            fail(f"[{lang}] eventos do GoatCounter sem o sufixo {suffix}: {bad}")
        names = [n[: -len(suffix)] for n in names if n.endswith(suffix)]
    return names


data = {}
for lang, (path, html_lang, prefix) in PAGES.items():
    if not path.exists():
        fail(f"[{lang}] arquivo não encontrado: {path.relative_to(ROOT.parent)}")
        continue
    html = path.read_text(encoding="utf-8")
    if f'<html lang="{html_lang}">' not in html:
        fail(f'[{lang}] esperado <html lang="{html_lang}">')
    if prefix:
        raw = re.findall(r'(?:src|srcset|href)="((?:assets|css|js)/[^"]*)"', html)
        if raw:
            fail(f"[{lang}] caminhos sem '../' (quebram na subpasta): {raw[:3]}")
    for hl in ("pt-BR", "en", "es-419", "x-default"):
        if f'rel="alternate" hreflang="{hl}"' not in html:
            fail(f'[{lang}] falta <link rel="alternate" hreflang="{hl}">')
    if 'class="lang-switch"' not in html:
        fail(f"[{lang}] falta o seletor de idioma (.lang-switch)")
    data[lang] = {
        "ids": re.findall(r'\sid="([^"]+)"', html),
        "seções": re.findall(r"<section\b[^>]*\sid=\"([^\"]+)\"", html),
        "âncoras internas": re.findall(r'href="(#[^"]*)"', html),
        "imagens": images(html, prefix),
        "links externos": external_links(html),
        "eventos GoatCounter": clicks(html, lang),
        "textos alternativos (alt)": len(re.findall(r"\salt=", html)),
    }

if "pt" in data:
    for lang in ("en", "es"):
        if lang not in data:
            continue
        for key, ref in data["pt"].items():
            got = data[lang][key]
            if got != ref:
                if isinstance(ref, list):
                    missing = [x for x in ref if x not in got]
                    extra = [x for x in got if x not in ref]
                    detail = f"faltando {missing[:5]} / sobrando {extra[:5]}" if (missing or extra) else "ordem diferente"
                else:
                    detail = f"pt={ref} {lang}={got}"
                fail(f"[{lang}] {key} diferente da versão em português: {detail}")

if errors:
    print("Traduções fora de sincronia com site/index.html:\n")
    for e in errors:
        print(" -", e)
    print("\nAtualize site/en/index.html e site/es/index.html junto com a versão em português (ver AGENTS.md).")
    sys.exit(1)

print("OK: português, inglês e espanhol com a mesma estrutura.")
