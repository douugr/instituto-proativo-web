# Implementation Plan: Landing Page do Instituto Pró-Ativo

**Branch**: `001-landing-page-instituto` | **Date**: 2026-10-01 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-landing-page-instituto/spec.md`

## Summary

Landing page de uma única página, em português, que apresenta o Instituto Pró-Ativo e o Projeto Jiu-Jitsu Para Todos (história, desafio social, atuação, metodologia, equipe, impacto, governança, formas de apoio, destinação de recursos e contrapartidas) e converte visitantes em contatos, principalmente pelo WhatsApp (14) 99681-6005. Cotas de patrocínio ficam de fora.

Abordagem técnica: site estático em **HTML5 + CSS + Bootstrap 5.3** (CDN com SRI), com JavaScript mínimo, sem etapa de build. O código do site fica em `site/` e é publicado no **GitHub Pages via GitHub Actions** (validação de HTML e links antes do deploy) no domínio **institutoproativo.com.br** (DNS no Registro.br, HTTPS obrigatório). Estatísticas de visitas e cliques sem cookies com **GoatCounter**. Detalhes e alternativas em [research.md](research.md).

## Technical Context

**Language/Version**: HTML5, CSS3 (custom properties), JavaScript ES2020 (mínimo, opcional)

**Primary Dependencies**: Bootstrap 5.3.x (CSS + bundle JS) e Bootstrap Icons 1.11.x via jsDelivr com SRI; Google Fonts (Barlow, Barlow Semi Condensed); GoatCounter (estatística sem cookies)

**Storage**: N/A (conteúdo estático no HTML; nenhum dado de visitante armazenado)

**Testing**: `html-validate` e `lychee` (links) no GitHub Actions; Lighthouse e axe DevTools manuais; roteiro de aceite em [quickstart.md](quickstart.md)

**Target Platform**: Navegadores modernos (2 últimas versões de Chrome, Safari iOS, Firefox, Edge, Samsung Internet), mobile-first a partir de 320 px; hospedagem GitHub Pages

**Project Type**: Site estático (landing page de uma página)

**Performance Goals**: Primeira dobra visível em ≤ 3 s em 4G (SC-003); Lighthouse mobile Performance ≥ 90; peso total do primeiro carregamento ≤ 1,5 MB

**Constraints**: Sem etapa de build; sem cookies (FR-024); WCAG 2.1 AA (FR-021); conteúdo e links funcionam sem JavaScript; sem rolagem horizontal ≥ 320 px (SC-004); nenhuma menção às cotas de patrocínio (FR-019)

**Scale/Scope**: 1 página com ~14 seções, ~15–25 imagens otimizadas; tráfego baixo/moderado (regional), dentro dos limites do GitHub Pages (100 GB/mês de banda, site ≤ 1 GB)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

O arquivo `.specify/memory/constitution.md` ainda é o template padrão, sem princípios definidos. **Não há gates a avaliar → PASS.**

Princípios seguidos mesmo sem constituição formal (podem virar a constituição do projeto via `/speckit-constitution`):

| Princípio | Como o plano atende |
|-----------|---------------------|
| Simplicidade (YAGNI) | Sem framework JS, sem build, sem backend, uma página |
| Acessibilidade e mobile-first | WCAG 2.1 AA, Bootstrap responsivo, testes em 320–1280 px |
| Privacidade (LGPD) | Sem formulários, sem cookies, estatística agregada |
| Desempenho | Imagens WebP responsivas, lazy loading, orçamento de 1,5 MB |
| Publicação segura | Só `site/` é publicado; validação no CI antes do deploy; HTTPS obrigatório; domínio verificado |

**Re-check pós-design (Phase 1)**: PASS — nenhum item do design adiciona complexidade além do necessário; nenhuma violação a justificar.

## Project Structure

### Documentation (this feature)

```text
specs/001-landing-page-instituto/
├── plan.md              # Este arquivo
├── research.md          # Phase 0 — decisões técnicas
├── data-model.md        # Phase 1 — conteúdo/entidades da página
├── quickstart.md        # Phase 1 — rodar localmente, validar, configurar Pages e DNS
├── contracts/
│   ├── page-structure.md    # Seções, âncoras, ordem e conteúdo obrigatório
│   ├── contact-links.md     # Formato dos links de contato e eventos de estatística
│   └── seo-metadata.md      # Metadados, Open Graph, JSON-LD, arquivos de SEO
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 (/speckit-tasks — ainda não criado)
```

### Source Code (repository root)

```text
site/                           # Raiz publicada no GitHub Pages
├── index.html                  # Página única com todas as seções
├── CNAME                       # institutoproativo.com.br
├── robots.txt
├── sitemap.xml
├── site.webmanifest
├── favicon.ico
├── 404.html                    # Página simples com link para a home
├── css/
│   └── styles.css              # Identidade visual (sobrescreve variáveis --bs-*), componentes próprios
├── js/
│   └── main.js                 # Ano no rodapé; fecha menu móvel ao clicar em âncora
└── assets/
    ├── brand/                  # brasão (png), ícones 32/180/192/512, og-image.jpg (1200×630)
    └── img/                    # fotos otimizadas (webp + jpg, 480/960/1600 px)

.github/
└── workflows/
    └── pages.yml               # Validação (html-validate, lychee) + deploy no GitHub Pages

.htmlvalidate.json              # Regras do html-validate
lychee.toml                     # Configuração do verificador de links (exclusões, timeout)
README.md                       # Como rodar, publicar e atualizar conteúdo
```

**Structure Decision**: Site estático em `site/` (raiz publicada), separado de `specs/`, `.specify/` e `.claude/` para que só o site vá ao ar. Sem `src/`/`tests/` tradicionais: não há código com lógica a testar; a validação é feita por ferramentas no CI e pelo roteiro do `quickstart.md`.

## Configuração do GitHub Pages (resumo — passo a passo em quickstart.md)

1. **Visibilidade**: o repositório está **privado**. No plano gratuito, o Pages exige repositório **público** → tornar público (ou ter GitHub Pro).
2. **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. **Verificar o domínio** na conta (Settings → Pages → Add a domain) com o TXT `_github-pages-challenge-douugr` no Registro.br.
4. **DNS no Registro.br**: 4 registros `A` + 4 `AAAA` no apex e `CNAME www → douugr.github.io.`
5. **Settings → Pages → Custom domain**: `institutoproativo.com.br` → aguardar o check de DNS → marcar **Enforce HTTPS**.
6. Fazer merge na `main` → o workflow `pages.yml` valida e publica.

## Riscos e dependências externas

| Item | Responsável | Impacto se faltar |
|------|-------------|-------------------|
| Tornar o repositório público (ou GitHub Pro) | Usuário | Pages não pode ser ativado |
| Acesso ao painel do Registro.br para DNS | Usuário | Site só disponível em `douugr.github.io/instituto-proativo-web` |
| Conta GoatCounter | Usuário | Estatísticas desativadas (site funciona normalmente) |
| Fotos em boa resolução (equipe, aulas) | Instituto | Uso das imagens extraídas dos PDFs, com qualidade menor |
| Revisão final dos textos e números | Instituto | Publicação com o conteúdo dos materiais atuais |

## Complexity Tracking

Sem violações — seção não aplicável.
