# Instituto Pró-Ativo — Landing page

Site institucional do **Instituto Pró-Ativo** e do **Projeto Jiu-Jitsu Para Todos** (Ourinhos/SP), publicado em **https://institutoproativo.com.br**.

Página única em HTML + CSS + Bootstrap 5.3, sem etapa de build, hospedada no GitHub Pages.

## Estrutura

```text
site/                 # tudo o que vai ao ar (raiz do GitHub Pages)
  index.html          # a página em português, com todas as seções
  en/index.html       # versão em inglês
  es/index.html       # versão em espanhol (América Latina)
  css/styles.css      # identidade visual (cores, fontes, componentes)
  js/main.js          # ano no rodapé, fechamento do menu no celular e do seletor de idioma
  assets/brand/       # brasão, ícones, imagem de compartilhamento
  assets/img/         # fotos otimizadas (webp + jpg)
  404.html, CNAME, robots.txt, sitemap.xml, site.webmanifest
design-sources/       # materiais de origem (não publicados) e origem das fotos
specs/                # especificação, plano e tarefas (Spec Kit)
.github/workflows/    # validação + publicação automática
```

## Rodar localmente

```bash
python3 -m http.server 8000 --directory site
```

Abrir http://localhost:8000.

## Validar (as mesmas verificações do CI)

```bash
npx --yes html-validate@9 "site/**/*.html"
```

```bash
python3 .github/scripts/check-i18n.py   # EN e ES acompanham o português
```

```bash
lychee --config lychee.toml --root-dir "$PWD/site" "site/**/*.html"
```

A publicação também é bloqueada se o site mencionar as cotas de patrocínio (Bronze/Prata/Ouro/Master), que estão fora do escopo desta versão.

## Publicar

1. Fazer as alterações em uma branch e abrir um Pull Request para `main` — o CI valida HTML, links e conteúdo.
2. Ao fazer merge na `main`, o workflow **Deploy GitHub Pages** publica a pasta `site/` automaticamente.

Configuração inicial do GitHub Pages, do domínio no Registro.br e do HTTPS: ver [specs/001-landing-page-instituto/quickstart.md](specs/001-landing-page-instituto/quickstart.md), seção 4.

## Atualizar conteúdo

> **O site tem 3 idiomas.** Toda alteração em `site/index.html` precisa ser feita também em `site/en/index.html` e `site/es/index.html` (caminhos com `../`, eventos do GoatCounter com sufixo `-en`/`-es`). Regras, glossário e detalhes em [AGENTS.md](AGENTS.md).

- **Textos**: editar `site/index.html` e as traduções em `site/en/` e `site/es/`; cada seção começa com um comentário `<!-- ===== N. NOME ===== -->`.
- **Números de impacto**: blocos marcados com `<!-- NÚMEROS DE IMPACTO -->` (aparecem em *Quem somos* e em *Impacto*); a fonte dos valores está em [data-model.md](specs/001-landing-page-instituto/data-model.md).
- **Contatos**: seção `#contato`, rodapé e botões de WhatsApp (procure por `wa.me/5514996816005`).
- **Fotos**: gerar versões `.webp` e `.jpg` (480 px e até 960/1600 px) em `site/assets/img/`, sempre com `width`, `height` e `alt` descritivo; registrar a origem em `design-sources/README.md`.
- **Estatísticas**: visitas e cliques nos contatos ficam em https://institutoproativo.goatcounter.com (sem cookies). Para contar cliques num link novo, adicione `data-goatcounter-click="nome-do-evento"`.
