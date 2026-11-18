# Instruções para agentes (Claude, Codex, Copilot etc.)

Site estático do Instituto Pró-Ativo. Visão geral, estrutura e como validar: [README.md](README.md). Plano técnico: [specs/001-landing-page-instituto/plan.md](specs/001-landing-page-instituto/plan.md).

## Regra obrigatória: o site existe em 3 idiomas

| Idioma | Arquivo | `lang` | URL |
| --- | --- | --- | --- |
| Português (original) | `site/index.html` | `pt-BR` | `/` |
| Inglês | `site/en/index.html` | `en` | `/en/` |
| Espanhol (América Latina) | `site/es/index.html` | `es-419` | `/es/` |

**Qualquer alteração de conteúdo ou de estrutura em uma página deve ser feita nas três, no mesmo commit/PR.** Isso vale para textos, títulos, `alt` de imagens, `aria-label`, troca ou inclusão de fotos, novas seções, links, números de impacto, contatos e metadados (`<title>`, `description`, Open Graph, JSON-LD).

O português é a fonte. Ao receber um pedido de mudança (normalmente escrito em português), aplique em `site/index.html` e traduza para `site/en/index.html` e `site/es/index.html`. Se o pedido vier só para um idioma (ex.: "corrija esta frase em inglês"), confirme se o conteúdo das outras versões também precisa mudar.

O CI roda `python3 .github/scripts/check-i18n.py`, que falha se as três páginas tiverem seções, âncoras, imagens, links externos ou eventos do GoatCounter diferentes. Ele **não** confere o texto: a tradução é responsabilidade de quem altera.

### Detalhes técnicos das páginas traduzidas

- Ficam em subpastas, então todo caminho local leva `../` (`../assets/...`, `../css/styles.css`, `../js/main.js`, `../favicon.ico`, `../site.webmanifest`). Âncoras (`#secao`) e IDs **não** são traduzidos: são iguais nas três páginas.
- Eventos do GoatCounter levam sufixo do idioma: `data-goatcounter-click="whatsapp-hero"` (pt), `whatsapp-hero-en`, `whatsapp-hero-es`.
- Mensagem pronta do WhatsApp (`?text=`) e assunto do e-mail (`?subject=`) são traduzidos e codificados para URL.
- Telefone exibido: `(14) 99681-6005` em português; `+55 14 99681-6005` em inglês e espanhol.
- `<link rel="canonical">` e `og:url` apontam para a URL do próprio idioma; o bloco de `hreflang` é igual nas três páginas; `og:locale` é `pt_BR`, `en_US` ou `es_LA`.
- Seletor de idioma: `<details class="lang-switch">` dentro do menu, com `aria-current="page"` no idioma atual. Funciona sem JavaScript (o `js/main.js` só o fecha ao clicar fora ou apertar Esc).
- Página nova no futuro (ex.: `/transparencia/`)? Criar também `/en/transparencia/` e `/es/transparencia/`, com `hreflang`, e incluir no `sitemap.xml`.

### Glossário e decisões de tradução

Mantenha consistência com o que já está nas páginas:

| Português | Inglês | Espanhol (LATAM) |
| --- | --- | --- |
| Instituto Pró-Ativo | Instituto Pró-Ativo (não traduzir) | Instituto Pró-Ativo |
| Projeto Jiu-Jitsu Para Todos | Jiu-Jitsu Para Todos Project (nome da marca; na 1ª menção do hero: "(Jiu-Jitsu for Everyone)") | Proyecto Jiu-Jitsu Para Todos |
| tatame | mat | tatami |
| quimono | gi | kimono |
| faixa preta 1º grau | 1st-degree black belt | cinturón negro 1.er grado |
| faixa coral / vermelha | coral belt / red belt | cinturón coral / rojo |
| Mestre Eddy | **Mestre** Eddy (ver aviso abaixo) | Maestro Eddy |
| Grande Mestre | Grandmaster | Gran Maestro |
| Sensei, Professor (título) | Sensei, Professor | Sensei, Profesor |
| aulão | open class | clase abierta |
| crianças atípicas | neurodivergent children | niños neurodivergentes |
| TEA / TDAH | ASD / ADHD | TEA / TDAH |
| CRAS | CRAS (public social assistance centers) | CRAS (centros públicos de asistencia social) |
| conselho tutelar | Child Protection Council | Consejo Tutelar |
| APAEs | APAEs (special-needs education associations) | APAEs (asociaciones de educación especial) |
| anamnese | intake assessment | evaluación inicial |
| pessoa física (CPF) / jurídica (CNPJ) | individual / company | persona / empresa |
| Lei de Incentivo ao Esporte / FIA | Brazilian tax incentives (Sports Incentive Law / FIA children's fund) | incentivos fiscales brasileños (Ley de Incentivo al Deporte / FIA) |
| Ourinhos/SP | Ourinhos, São Paulo (Brazil) | Ourinhos, São Paulo (Brasil) |

Espanhol: use o espanhol neutro da América Latina com tratamento **tú** ("Conoce", "Contáctanos"), sem "vosotros".

> **Aviso: palavra "master" em inglês.** O CI bloqueia qualquer ocorrência das palavras `bronze`, `prata`, `ouro` e `master` (regra FR-019, contra menção às cotas de patrocínio). Por isso o título do Mestre Eddy fica em português ("Mestre Eddy") na versão em inglês, e "Grand Master" se escreve "Grandmaster". Em espanhol, "Maestro", "oro" e "plata" não são bloqueados, mas cotas de patrocínio continuam proibidas em qualquer idioma.

## Outras regras do projeto

- Trabalhe em branch (`NNN-descricao`) e abra PR para `main`; o merge publica no GitHub Pages.
- Fotos: versões `.webp` e `.jpg` em `site/assets/img/`, com `width`, `height` e `alt` descritivo (nos 3 idiomas); registrar a origem em `design-sources/README.md`.
- Antes de abrir o PR: `npx --yes html-validate@9 "site/**/*.html"` e `python3 .github/scripts/check-i18n.py`.
