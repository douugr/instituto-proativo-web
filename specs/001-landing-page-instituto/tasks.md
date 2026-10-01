---

description: "Task list for Landing Page do Instituto Pró-Ativo"
---

# Tasks: Landing Page do Instituto Pró-Ativo

**Input**: Design documents from `/specs/001-landing-page-instituto/`

**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [research.md](research.md), [data-model.md](data-model.md), [contracts/](contracts/), [quickstart.md](quickstart.md)

**Tests**: A spec não pede testes automatizados de código (não há lógica). A validação é feita por `html-validate` + `lychee` no CI (configurados no Setup) e pelo roteiro de aceite do [quickstart.md](quickstart.md) §5, referenciado no fim de cada história.

**Organization**: Tarefas agrupadas por user story. Quase todo o conteúdo vive em um único arquivo (`site/index.html`) e um único CSS (`site/css/styles.css`); por isso tarefas da mesma história no mesmo arquivo **não** são [P]. Histórias diferentes editam seções diferentes do `index.html` e podem ser feitas em sequência rápida ou por pessoas diferentes com cuidado no merge.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependência pendente)
- **[Story]**: História da spec (US1–US5)

## Path Conventions

- Site publicado: `site/` (raiz do GitHub Pages)
- CI: `.github/workflows/pages.yml`; configs na raiz do repositório
- Materiais de origem (fora do repo, só leitura):
  - Brasão: `design-sources/brasao.webp` (copiado da sessão para o repositório)
  - Infográfico de recursos/contrapartidas: `design-sources/infografico-recursos.webp` (só referência de conteúdo)
  - `~/Downloads/A5 - Convite Projeto 2 (Panfletos (Retrato)) (4).pdf`
  - `~/Downloads/Apresentação comercial para empresas moderno cinza (2).pdf`
  - `~/Downloads/apresentacao-instituto-proativo.pptx.pdf`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Estrutura de pastas, configs de validação e pipeline de publicação

- [X] T001 Criar a estrutura de pastas `site/css/`, `site/js/`, `site/assets/brand/`, `site/assets/img/` e `.github/workflows/` conforme plan.md (usar `.gitkeep` onde a pasta ficar vazia por enquanto)
- [X] T002 [P] Criar `.htmlvalidate.json` na raiz com `{"extends": ["html-validate:recommended"]}` e ajustes mínimos (permitir `data-*`, `target="_blank"` com `rel="noopener"`, atributos `integrity`/`crossorigin`)
- [X] T003 [P] Criar `lychee.toml` na raiz: timeout 20 s, 2 tentativas, aceitar status 200/429, excluir `^mailto:`, `^tel:`, `wa\.me`, `instagram\.com` (bloqueiam robôs), `gc\.zgo\.at` e `institutoproativo\.com\.br` (o próprio domínio: canonical/og/JSON-LD só respondem depois do primeiro deploy e da propagação do DNS — sem essa exclusão a validação bloquearia o primeiro deploy)
- [X] T004 [P] Criar `.github/workflows/pages.yml`: gatilhos `push` em `main`, `pull_request` para `main` e `workflow_dispatch`; permissões `contents: read`, `pages: write`, `id-token: write`; `concurrency: pages`; job `validate` (checkout, `npx --yes html-validate@9 "site/**/*.html"`, `lycheeverse/lychee-action@v2` com `--config lychee.toml site`, e passo shell que falha se `grep -RniE "\\b(bronze|prata|ouro|master)\\b|R\\$ ?(500|1\\.000|2\\.000)" site` encontrar algo); job `deploy` (só em `push`/`workflow_dispatch` na `main`, `needs: validate`, `environment: github-pages`) com `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3` (`path: site`) e `actions/deploy-pages@v4`
- [X] T005 [P] Copiar o brasão para `site/assets/brand/brasao-source.webp` (fonte acima) e gerar com Python/Pillow (venv no scratchpad) `site/assets/brand/brasao.png` (largura 600 px, transparente), `brasao.webp` (600 px), `icon-32.png`, `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png` (fundo azul-marinho `#0F2350` com o brasão centralizado nos ícones) e `site/favicon.ico` (16/32/48); remover `brasao-source.webp` depois
- [X] T006 [P] Extrair as fotos dos PDFs em `~/Downloads` (pymupdf, `page.get_images()` + renderização das páginas com fotos quando a imagem estiver composta) para uma pasta temporária no scratchpad; selecionar ~12–18 fotos úteis (tatame/aulas, crianças treinando, equipe, medalhas, espaço) e anotar em `site/assets/img/README.md` a origem (arquivo + página) e o uso previsto de cada uma
- [X] T007 Otimizar as fotos selecionadas no T006 para `site/assets/img/<nome>-{480,960,1600}.{webp,jpg}` (Pillow; qualidade WebP 75 / JPEG 78; ≤ 200 KB cada, hero ≤ 300 KB; não ampliar além do original) e registrar `width`×`height` de cada uma em `site/assets/img/README.md`
- [X] T008 [P] Gerar `site/assets/brand/og-image.jpg` 1200×630 (fundo azul-marinho, brasão à esquerda, texto "Instituto Pró-Ativo — Jiu-Jitsu Para Todos" em branco/dourado, ≤ 300 KB) com Pillow

**Checkpoint**: Estrutura, assets base e pipeline prontos

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Esqueleto da página, identidade visual e comportamento global de que todas as histórias dependem

**⚠️ CRITICAL**: Nenhuma história começa antes desta fase

- [X] T009 Criar `site/index.html` com: `<!doctype html>`, `<html lang="pt-BR">`, `<head>` completo conforme [contracts/seo-metadata.md](contracts/seo-metadata.md) (charset, viewport, title, description, canonical, theme-color, Open Graph, Twitter Card, ícones, manifest, preconnects, JSON-LD `NGO`), Google Fonts Barlow 400/500/600 + Barlow Semi Condensed 700/800 com `display=swap`, Bootstrap 5.3.x CSS e Bootstrap Icons 1.11.x do jsDelivr **com `integrity` SRI correto** (obter o hash oficial da versão escolhida) e `crossorigin="anonymous"`, `css/styles.css`; antes de `</body>`: `bootstrap.bundle.min.js` (SRI) e `js/main.js` com `defer`; script GoatCounter **comentado** conforme [contracts/contact-links.md](contracts/contact-links.md)
- [X] T010 Em `site/index.html`, montar o esqueleto do `<body>`: skip-link `#conteudo`; `<header>` com navbar Bootstrap fixa (`navbar-expand-lg`, fundo azul-marinho, brasão `assets/brand/brasao.webp` 48 px + "Instituto Pró-Ativo", menu com Quem somos/Nossa história/O que fazemos/Metodologia/Equipe/Impacto/Como apoiar/Contato apontando para as âncoras do contrato, botão "Fale conosco" → `#contato`); `<body data-bs-spy="scroll" data-bs-target="#menu-principal">`; `<main id="conteudo">` com as 14 `<section>` vazias na ordem e com os `id`s de [contracts/page-structure.md](contracts/page-structure.md), cada uma com `aria-labelledby` para seu título; `<footer>` vazio com `id="rodape"`
- [X] T011 [P] Criar `site/css/styles.css` com: tokens `--pa-navy #0F2350`, `--pa-gold #E8B423`, `--pa-white`, `--pa-gray #F2F3F5`, cores do coração (vermelho, amarelo, azul, verde); sobrescrita de `--bs-primary`, `--bs-body-font-family` (Barlow), `--bs-body-color`, `--bs-link-color`; títulos em Barlow Semi Condensed 800 caixa alta; classes utilitárias `.section` (padding vertical responsivo, `scroll-margin-top` igual à altura do header), `.section--alt` (fundo cinza), `.section--dark` (fundo azul-marinho, texto branco), `.eyebrow` (rótulo dourado), `.divider-gold`, `.btn-gold` (fundo dourado, texto azul-marinho, foco visível), `.card-icon` (ícone em círculo azul-marinho como no infográfico); `.skip-link` (visível só no foco); `:focus-visible` com contorno dourado de 3 px; `html { scroll-behavior: smooth }` desligado em `@media (prefers-reduced-motion: reduce)`; `@media print` ocultando header fixo e botão flutuante; garantir contraste AA (dourado só como texto sobre azul-marinho)
- [X] T012 [P] Criar `site/js/main.js` (≤ 1 KB, sem dependências além do Bootstrap): preencher `[data-ano-atual]` com o ano corrente; ao clicar em `.nav-link` dentro de `#menu-principal` em telas < 992 px, fechar o collapse via `bootstrap.Collapse.getOrCreateInstance(...).hide()`; tudo dentro de `DOMContentLoaded` e sem erros se o Bootstrap não carregar
- [X] T013 [P] Criar `site/CNAME` (`institutoproativo.com.br`), `site/robots.txt`, `site/sitemap.xml` e `site/site.webmanifest` conforme [contracts/seo-metadata.md](contracts/seo-metadata.md)
- [X] T014 [P] Criar `site/404.html` autossuficiente (doctype, `lang="pt-BR"`, mesmo Bootstrap/fontes/`css/styles.css` com caminhos absolutos `/css/...`, brasão, "Página não encontrada" e botão "Voltar para o início" → `/`, `meta name="robots" content="noindex"`)
- [X] T015 Rodar `python3 -m http.server 8000 --directory site` e as validações do [quickstart.md](quickstart.md) §3; corrigir erros de HTML/links do esqueleto em `site/index.html`

**Checkpoint**: Página navegável (menu, âncoras, rodapé vazio), identidade visual aplicada, CI verde

---

## Phase 3: User Story 1 - Conhecer o instituto e sua causa (Priority: P1) 🎯 MVP

**Goal**: O visitante entende quem é o instituto, o que faz, para quem, onde, desde quando e por que é confiável

**Independent Test**: [quickstart.md](quickstart.md) §5 itens 2, 3 (seções 1–6 e 13) e 15 — uma pessoa que não conhece o instituto explica o que ele faz, para quem, onde e desde quando, e cita um diferencial

- [X] T016 [US1] Implementar a seção `#inicio` (hero) em `site/index.html` (FR-004): fundo azul-marinho com foto de aula em `<picture>` (overlay escuro para contraste, `fetchpriority="high"`, sem lazy), brasão `brasao.webp`, `<h1>` "Existem crianças que só precisam de uma oportunidade", complemento "— e pessoas dispostas a caminhar com elas", subtítulo "Esporte educacional como ferramenta de transformação social", CTA primário `.btn-gold` "Quero fazer parte" (link WhatsApp principal com `data-goatcounter-click="whatsapp-hero"`, formato exato de [contracts/contact-links.md](contracts/contact-links.md)) e CTA secundário "Conheça o projeto" → `#quem-somos`; tudo legível em 320 px sem rolar além da primeira dobra
- [X] T017 [US1] Implementar `#quem-somos` em `site/index.html` (FR-005): eyebrow "QUEM SOMOS", `<h2>` "Quem somos", texto sobre a OSC em Ourinhos/SP (missão: cidadania, educação e qualidade de vida pelo esporte educacional, tendo o jiu-jitsu como principal ferramenta), público prioritário (6 a 17 anos, rede pública, vulnerabilidade social, incluindo atípicos, encaminhados por escolas, CRAS e conselho tutelar), apresentação do Projeto Jiu-Jitsu Para Todos ("Formando atletas. Construindo caráter. Transformando histórias.") e faixa de 3 destaques: "2015 — início do projeto", "60 — crianças e adolescentes atendidos hoje", "6 a 17 — anos de idade" (marcar o bloco com comentário `<!-- NÚMEROS DE IMPACTO: atualizar também em #impacto -->`)
- [X] T018 [US1] Implementar `#historia` em `site/index.html` (FR-006): `<h2>` "Tudo começou com um tatame"; narrativa curta em 3–4 parágrafos ou linha do tempo (2015: início com 8 alunos por iniciativa do Prof. Humberto Betão, *in memoriam*, e seus alunos, entre eles o Sensei Ismaile Santos, à frente de forma voluntária; diferentes espaços e a pandemia sem interromper as atividades; 2021: acolhimento de crianças com TEA, depois TDAH, dificuldades de comunicação e não verbais; hoje: mais de uma década); bloco "Linhagem" (bandeira da equipe Eddy North Fighter, Mestre Eddy North faixa coral 8º grau CBJJP, aluno de Reylson Gracie — filho de Carlos Gracie — e graduado pelo Grande Mestre Joe Moreira 9º grau); foto com `alt` descritivo e `loading="lazy"`
- [X] T019 [US1] Implementar `#desafio` em `site/index.html` (FR-007): `.section--alt`, `<h2>` "O desafio social", frase introdutória, 4 cartões com ícone (falta de acesso ao esporte e atividades extracurriculares; exposição à violência e à ociosidade; baixa autoestima e dificuldade de disciplina; risco de evasão escolar) e fechamento "Sem oportunidades adequadas, esses jovens ficam mais vulneráveis…"
- [X] T020 [US1] Implementar `#o-que-fazemos` em `site/index.html` (FR-008): `<h2>` "Da quadra à sala de aula", grade responsiva (1 col → 2 → 4) com 4 cartões: Esporte (jiu-jitsu por faixa etária e nível técnico, pilates, yoga, aula coletiva mensal de integração), Educação (informática, aulas experimentais em escolas parceiras e APAEs, palestras sobre disciplina e cidadania), Desenvolvimento humano (equipe multidisciplinar — psicologia, terapia ocupacional, fonoaudiologia, fisioterapia — para típicos e atípicos), Família e escola (anamnese de cada caso, monitoramento de frequência e notas, reuniões periódicas com gestores e famílias)
- [X] T021 [US1] Implementar `#metodologia` em `site/index.html` (FR-009, FR-010): `<h2>` "Mais que esporte, uma ferramenta de transformação"; 4 pilares com ícone e descrição curta (Disciplina e respeito — formação de caráter; Foco, persistência e superação — desenvolvimento pessoal; Trabalho em equipe — cooperação e convivência; Autocontrole emocional — equilíbrio emocional); lista da metodologia (aulas 3x/semana por faixa etária e nível; controle de frequência e acompanhamento da evolução técnica e comportamental; turmas de crianças atípicas em grupos menores com apoio multidisciplinar; professor qualificado + monitor; integração com as famílias); sub-bloco `<h3>` "Formação técnica e projeção esportiva" (graduação estruturada e federada; campeonatos e eventos; desenvolvimento técnico progressivo; identificação de talentos) com a frase "O projeto não apenas inclui. Ele prepara e projeta."
- [X] T022 [US1] Implementar `#citacao` em `site/index.html` (FR-017): `.section--dark`, `<blockquote>` com "Formamos pessoas. Antes de formar atletas." e linha de apoio "No tatame, crianças aprendem muito mais do que golpes. Aprendem respeito, disciplina e a acreditar em si mesmas."; foto de fundo opcional com overlay
- [X] T023 [US1] Ajustar em `site/css/styles.css` os estilos específicos de hero, faixa de destaques, linha do tempo, cartões e blockquote criados no T016–T022, verificando 320/375/768/1280 px sem rolagem horizontal
- [X] T024 [US1] Validar US1: [quickstart.md](quickstart.md) §3 e §5 itens 2, 3 e 10 localmente; corrigir o que falhar em `site/index.html`/`site/css/styles.css`

**Checkpoint**: MVP — a página conta a história e transmite a causa; o CTA do hero já leva ao WhatsApp

---

## Phase 4: User Story 2 - Entrar em contato com o instituto (Priority: P1)

**Goal**: Qualquer ponto da página leva a um canal de contato em ≤ 1 clique

**Independent Test**: [quickstart.md](quickstart.md) §5 itens 4, 5 e 6 — botão flutuante abre WhatsApp (14) 99681-6005 com mensagem padrão; todos os links da seção Contato funcionam no celular e no desktop

- [X] T025 [US2] Implementar `#contato` em `site/index.html` (FR-018): `.section--dark`, `<h2>` "Fale conosco"; cartão de destaque "WhatsApp do Instituto (14) 99681-6005" com botão `.btn-gold` "Conversar no WhatsApp" (`whatsapp-contato`); lista de canais secundários com ícones e textos visíveis — Orlando (14) 98108-6430 e Ismaile (14) 98827-4004 (cada um com link WhatsApp e `tel:`), e-mail, 3 Instagrams, endereço "R. Celestino Lopes Bahia, 1051 – Vila São Luiz, Ourinhos/SP, CEP 19911-205 (espaço cedido CRAS-1)" com link "Ver no mapa"; todos os `href`, `target`, `rel` e `data-goatcounter-click` exatamente como em [contracts/contact-links.md](contracts/contact-links.md); texto oculto "(abre em nova aba)" nos links externos
- [X] T026 [US2] Adicionar o botão flutuante de WhatsApp em `site/index.html` (após `</footer>`): `<a class="whatsapp-float">` com ícone `bi-whatsapp`, `aria-label` do contrato, `data-goatcounter-click="whatsapp-flutuante"`
- [X] T027 [US2] Implementar o `<footer id="rodape">` em `site/index.html`: brasão pequeno, frase "Investir no Pró-Ativo é investir em transformação, disciplina & cidadania.", links rápidos (Instagram ×3, e-mail, WhatsApp principal), "© <span data-ano-atual>2026</span> Instituto Pró-Ativo · Ourinhos/SP" e "Projeto Jiu-Jitsu Para Todos"
- [X] T028 [US2] Estilizar em `site/css/styles.css`: `.whatsapp-float` (fixo no canto inferior direito, 56×56 px mínimo, fundo verde WhatsApp `#25D366` com ícone escuro para contraste AA ou ícone branco sobre `#128C7E`, sombra, `z-index` acima do conteúdo e abaixo do menu aberto, margem segura em iOS com `env(safe-area-inset-bottom)`), seção de contato e rodapé; `padding-bottom` no rodapé para o botão flutuante não cobrir o conteúdo final
- [X] T029 [US2] Validar US2: [quickstart.md](quickstart.md) §5 itens 4–6 no navegador local (celular emulado e desktop) e conferir que `href` de todos os links de contato batem com o contrato

**Checkpoint**: US1 + US2 = página publicável com o mínimo de valor (história + conversão)

---

## Phase 5: User Story 3 - Entender como apoiar e o impacto do apoio (Priority: P2)

**Goal**: O visitante conhece as formas de apoio, para onde vão os recursos e o impacto buscado — sem cotas

**Independent Test**: [quickstart.md](quickstart.md) §5 item 3 — visitante lista ≥ 3 formas de apoio e os destinos dos recursos; o grep de cotas no §3 retorna "OK: sem cotas"

- [X] T030 [US3] Implementar `#impacto` em `site/index.html` (FR-012): `<h2>` "Impacto e metas"; grade de indicadores **atuais** (2015 início; +10 anos de atuação; 60 atendidos hoje; 6 a 17 anos; 3x aulas por semana) e grade de **metas** claramente rotulada "Nossas metas" (100 crianças por ano; +100 famílias impactadas; 300 aulas por ano; 75% de frequência; até 200 alunos em 5 anos) — valores de [data-model.md](data-model.md) §4, bloco marcado com o comentário `<!-- NÚMEROS DE IMPACTO -->`; lista "Indicadores que acompanhamos" (frequência escolar, evolução comportamental, participação familiar, progressão técnica); 3 colunas de benefícios: Desenvolvimento educacional (disciplina e responsabilidade, redução da evasão escolar, melhoria no comportamento e rendimento, rotina e comprometimento), Fortalecimento familiar e social (aproximação das famílias, ambiente seguro no contraturno, redução da exposição à ociosidade e risco, vínculos positivos), Desenvolvimento emocional e cidadão (autocontrole, respeito às regras e à hierarquia, trabalho em equipe, formação de caráter e valores)
- [X] T031 [US3] Implementar `#como-apoiar` em `site/index.html` (FR-014): `<h2>` "Como você pode fazer parte"; texto "Por que você está recebendo este convite?" resumido (empresários, profissionais, educadores, líderes — "grandes transformações não acontecem sozinhas; elas são construídas por pessoas"); 6–7 cartões de formas de apoio (contribuir com conhecimento; apoiar com estrutura; fortalecer com experiência profissional/voluntariado; investir na manutenção e expansão; divulgar; conectar e abrir portas); destaque "Você pode apoiar com qualquer valor, como pessoa física (CPF) ou jurídica (CNPJ)."; nota breve "Apoio via incentivo fiscal (Lei de Incentivo ao Esporte / FIA) em processo de validação — fale conosco para saber mais." **sem percentuais nem exemplos**; CTA `.btn-gold` "Quero apoiar" (WhatsApp principal, `whatsapp-como-apoiar`) e link secundário "Prefere e-mail?" (`mailto` do contrato)
- [X] T032 [US3] Implementar `#recursos` em `site/index.html` (FR-015): `.section--alt`, `<h2>` "Para onde vão os recursos"; coluna com 6 destinos com ícones em círculo azul-marinho (estruturação do novo espaço — `bi-house`; água, energia, internet e limpeza — `bi-droplet`; custos fixos de funcionamento — `bi-gear`; materiais esportivos e de uso contínuo; apoio administrativo da operação — `bi-clipboard`; atividades de integração e formação — `bi-people`); coluna "Como o projeto cresce em etapas" com 3 passos numerados em dourado (1. Estruturar o novo espaço — garantir o funcionamento do novo espaço; 2. Garantir funcionamento contínuo — ampliar qualidade, alcance e regularidade; 3. Ampliar equipe e dedicação conforme a base se consolida — remuneração de professores, monitores e apoio administrativo)
- [X] T033 [US3] Estilizar em `site/css/styles.css` os números de impacto (valor grande em Barlow Semi Condensed, rótulo "meta"), cartões de apoio e a trilha numerada de etapas (linha dourada vertical no mobile, horizontal ≥ 992 px)
- [X] T034 [US3] Validar US3: grep de cotas do [quickstart.md](quickstart.md) §3, leitura das seções `#impacto`, `#como-apoiar`, `#recursos` em 320 px e 1280 px

**Checkpoint**: Página completa para captação de apoio (sem cotas)

---

## Phase 6: User Story 4 - Confiar na equipe e na governança (Priority: P2)

**Goal**: O visitante identifica quem conduz o projeto e as garantias de segurança e gestão

**Independent Test**: [quickstart.md](quickstart.md) §5 item 3 — visitante cita os 4 membros da equipe e ≥ 3 garantias de segurança/conformidade

- [X] T035 [US4] Implementar `#equipe` em `site/index.html` (FR-011): `<h2>` "Nosso time", texto curto sobre o Instituto como OSC; 4 cartões ([data-model.md](data-model.md) §3) — Ismaile Santos (Idealizador · Professor faixa preta 1º grau, federado CBJJP), Fernando Santim (Instrutor · treinos, viagens e parcerias), César Evaristo (Instrutor · treinos e projetos dentro e fora do tatame), Orlando Weber (Instrutor · treinos, marca e metodologia kids, sob supervisão do sensei responsável); foto se extraída no T006, senão avatar circular azul-marinho com iniciais em dourado (`aria-hidden`)
- [X] T036 [US4] Implementar `#confianca` em `site/index.html` (FR-013): `<h2>` "Segurança, governança e rede de apoio"; 3 colunas — "Segurança e conformidade" (professores federados CBJJP; exame toxicológico periódico; antecedentes criminais verificados; certificação em primeiros socorros; formação para atuação com TEA e TDAH), "Equipe multidisciplinar de apoio" (assessoria jurídica; assistência social; educador físico; nutricionista; psicólogos parceiros), "Cultura e compromisso" (ética e transparência; ambiente seguro e inclusivo; acompanhamento pedagógico; acompanhamento familiar; formação continuada); bloco "Estrutura institucional" (conselho fiscal constituído; diretoria voluntária; contabilidade permanente; estatuto com abrangência nacional; núcleo piloto em Ourinhos/SP); bloco "Rede de apoio" (Psicologia • Saúde • Educação • Assistência • Parceiros; parcerias com profissionais, universidade e laboratório da Unifio, estudantes em formação, escolas, CRAS e conselho tutelar, "sempre com acompanhamento técnico e coordenação responsável")
- [X] T037 [US4] Estilizar em `site/css/styles.css` os cartões da equipe (foto/avatar circular com borda dourada) e as listas com ícone de check da seção de confiança
- [X] T038 [US4] Validar US4: leitura das seções `#equipe` e `#confianca` em 320 px e 1280 px; `alt` das fotos da equipe com nome e papel

**Checkpoint**: Credibilidade completa

---

## Phase 7: User Story 5 - Ver as contrapartidas para empresas apoiadoras (Priority: P3)

**Goal**: Empresa identifica as contrapartidas gerais sem valores de cotas

**Independent Test**: [quickstart.md](quickstart.md) §5 item 3 — visitante identifica as 5 contrapartidas e que pode apoiar como PF ou PJ; grep de cotas OK

- [X] T039 [US5] Implementar `#contrapartidas` em `site/index.html` (FR-016): `<h2>` "Contrapartidas", subtítulo "Visibilidade da marca, associação à causa e presença nas ações do Instituto."; 5 itens com ícones (`bi-megaphone` Divulgação em materiais institucionais; `bi-phone` Redes sociais; `bi-flag` Banners e eventos; `bi-people-fill` Ações presenciais; `bi-bar-chart` Relatórios de impacto social); linha final "Quer saber como sua empresa pode participar? Fale com a gente." com link para `#contato`; **sem** níveis nem valores
- [X] T040 [US5] Estilizar `#contrapartidas` em `site/css/styles.css` (faixa cinza como no infográfico, ícones grandes azul-marinho, 2 col mobile → 5 col ≥ 992 px) e rodar o grep de cotas do [quickstart.md](quickstart.md) §3

**Checkpoint**: Todas as histórias implementadas

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Desempenho, acessibilidade, estatística, documentação e publicação

- [X] T041 Revisar todas as `<img>`/`<picture>` em `site/index.html`: `alt` descritivo (ou `alt=""` se decorativa), `width`/`height`, `loading="lazy"` + `decoding="async"` fora do hero, `srcset`/`sizes` corretos; ícones `<i class="bi ...">` com `aria-hidden="true"`
- [X] T042 Auditoria de acessibilidade com axe DevTools e navegação só por teclado ([quickstart.md](quickstart.md) §5 itens 7 e 9); corrigir contraste, ordem de foco, hierarquia de títulos e rótulos em `site/index.html`/`site/css/styles.css`
- [ ] T043 Lighthouse mobile e teste "Fast 4G" ([quickstart.md](quickstart.md) §5 itens 8 e 11); ajustar pesos de imagem em `site/assets/img/` e carregamento em `site/index.html` até Performance ≥ 90, Acessibilidade/Boas práticas/SEO ≥ 95 e ≤ 1,5 MB
- [X] T044 [P] Conferir que nenhum cookie é criado (DevTools → Application) e que a página funciona com JavaScript desativado (conteúdo e links) — [quickstart.md](quickstart.md) §5 item 12
- [X] T045 [P] Escrever `README.md` na raiz: o que é o projeto, estrutura (`site/`, `specs/`), como rodar localmente, como validar, como publicar (PR → merge na `main`), como atualizar números/contatos/fotos e link para [quickstart.md](quickstart.md) para configuração de DNS/Pages
- [ ] T046 Remover `.gitkeep` desnecessários, rodar as validações finais do [quickstart.md](quickstart.md) §3, commitar e abrir Pull Request de `001-landing-page-instituto` para `main` com resumo das seções e checklist do §5
- [ ] T047 Após o merge e o deploy: executar o roteiro de aceite completo do [quickstart.md](quickstart.md) §5 no domínio (itens 1–14; item 1 depende do DNS no Registro.br e do Enforce HTTPS feitos pelo usuário)
- [ ] T048 Quando o usuário criar a conta GoatCounter (`institutoproativo`): descomentar o script em `site/index.html`, publicar e validar o item 14 do [quickstart.md](quickstart.md) §5

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: sem dependências. T007 depende de T006.
- **Foundational (Phase 2)**: depende do Setup (usa brasão T005 e estrutura T001). T010 depende de T009; T015 depende de T009–T014. **Bloqueia todas as histórias.**
- **US1 (Phase 3)**: depende da Phase 2 e das fotos (T007).
- **US2 (Phase 4)**: depende só da Phase 2 — independente de US1 (o CTA do hero é de US1, mas o contato funciona sozinho).
- **US3, US4, US5 (Phases 5–7)**: dependem só da Phase 2; independentes entre si.
- **Polish (Phase 8)**: depende das histórias que forem publicadas. T047 depende do merge (T046) e do DNS (usuário). T048 depende da conta GoatCounter (usuário).

### User Story Dependencies

```text
Setup ─▶ Foundational ─┬─▶ US1 (P1) ─┐
                       ├─▶ US2 (P1) ─┼─▶ Polish ─▶ PR/merge ─▶ deploy ─▶ aceite
                       ├─▶ US3 (P2) ─┤
                       ├─▶ US4 (P2) ─┤
                       └─▶ US5 (P3) ─┘
```

### Within Each User Story

- Marcação HTML da seção → estilos em `styles.css` → validação da história.
- Todas as tarefas de uma história editam o mesmo `index.html`: executar em sequência.

### Parallel Opportunities

- Setup: T002, T003, T004, T005, T006, T008 em paralelo (arquivos diferentes); T007 após T006.
- Foundational: T011, T012, T013, T014 em paralelo após T009/T010 começarem (arquivos diferentes).
- Histórias: com mais de uma pessoa, US1–US5 podem ser feitas em paralelo, cada uma na sua `<section>` de `site/index.html` (cuidado com conflitos de merge em `styles.css` — separar blocos por comentário de seção).
- Polish: T044 e T045 em paralelo.

---

## Parallel Example: Setup

```bash
# Em paralelo (arquivos distintos):
Task: "T002 Criar .htmlvalidate.json"
Task: "T003 Criar lychee.toml"
Task: "T004 Criar .github/workflows/pages.yml"
Task: "T005 Gerar brasão e ícones em site/assets/brand/"
Task: "T006 Extrair fotos dos PDFs"
Task: "T008 Gerar og-image.jpg"
```

## Parallel Example: Foundational

```bash
# Após T009/T010:
Task: "T011 site/css/styles.css (tokens e base)"
Task: "T012 site/js/main.js"
Task: "T013 CNAME, robots.txt, sitemap.xml, site.webmanifest"
Task: "T014 site/404.html"
```

---

## Implementation Strategy

### MVP First (US1 + US2)

1. Phase 1 Setup → Phase 2 Foundational (CI verde).
2. Phase 3 US1 → validar (história e causa compreensíveis).
3. Phase 4 US2 → validar (contato em 1 clique).
4. **PARAR E PUBLICAR**: as seções vazias de US3–US5 devem ser **ocultadas** (remover do menu e do HTML) se o MVP for publicado antes delas — nada de seção vazia no ar.

### Incremental Delivery

1. MVP (US1 + US2) → publicar.
2. + US3 (como apoiar, recursos, impacto) → publicar.
3. + US4 (equipe, governança) → publicar.
4. + US5 (contrapartidas) → publicar.
5. Polish (Lighthouse, a11y, README) → publicação final e aceite.

### Recomendação

Por ser uma página única e pequena, o caminho mais simples é implementar todas as fases em sequência na branch `001-landing-page-instituto` e publicar uma vez (T046), usando os checkpoints só como pontos de validação.

---

## Notes

- [P] = arquivos diferentes, sem dependência pendente.
- Números de impacto e contatos: fonte única em [data-model.md](data-model.md); no HTML, blocos marcados com comentários.
- Nenhuma tarefa pode introduzir cotas de patrocínio (FR-019) — o CI bloqueia.
- Commitar ao fim de cada fase/história.

---

## Implementation Notes (2026-10-01)

- **T005**: o brasão original tem fundo branco; o fundo foi removido (transparência) antes de gerar `brasao.*`, ícones e favicon. Também foi gerada `brasao-160.*` para o cabeçalho/rodapé.
- **T006/T007**: as notas de origem das fotos ficaram em `design-sources/README.md` (e não em `site/assets/img/README.md`) para não publicar documentação interna (achado I2 do `/speckit-analyze`). Fotos do panfleto A5 vêm com filtro esverdeado e não foram usadas; 16 fotos coloridas da apresentação comercial foram otimizadas. Tamanhos: 480 px + tamanho nativo (até 960/1600 px).
- **T009**: Bootstrap **5.3.8** e Bootstrap Icons **1.13.1** (versões estáveis atuais), com SRI. O `preload` da imagem do hero foi removido: fazia o celular baixar duas versões da foto; a `<img>` usa `fetchpriority="high"`.
- **T004/T015**: `html-validate` fixado na **v9** (a v11 exige Node 22+ e quebraria no CI com Node 20). Regra `doctype-style` desligada (`<!doctype html>` minúsculo é válido).
- **T010**: menu expande a partir de **1200 px** (`navbar-expand-xl`) — com 8 itens, o `lg` quebrava os rótulos em duas linhas. Linhas `g-5` viraram `g-4 g-lg-5` para não vazar em 320 px.
- **T011/T042**: `--pa-gold-dark` escurecido para `#8a6400` (contraste AA em texto sobre fundo claro); números das etapas em azul-marinho sobre dourado.
- **T026**: botão flutuante de WhatsApp fica **dentro** do `<footer>` (axe: todo conteúdo dentro de landmarks); continua fixo na tela.
- **T030**: texto de abertura de `#impacto` usa "60 crianças e adolescentes" (não "dezenas"), conforme Clarifications. Classificação metas vs. atuais segue o data-model (achado A1 ainda pendente de confirmação do instituto).
- **T035**: os materiais não identificam quem é quem nas fotos; a equipe usa avatares com iniciais até o instituto enviar retratos identificados.
- **Verificações locais feitas**: html-validate sem erros; grep de cotas OK; axe-core 4.10 (WCAG 2.1 AA + best practices) com **0 violações**; nenhum cookie; 0 âncoras quebradas, 0 imagens/recursos com erro, 0 erros de console; sem rolagem horizontal em 320/375/768/1280 px; menu móvel fecha ao navegar; ~700 KB no primeiro carregamento no celular.
- **T044**: sem JavaScript, todo o conteúdo e os links continuam funcionando (o único JS próprio preenche o ano e fecha o menu; o menu móvel não abre sem JS, mas o botão "Fale conosco", o botão flutuante e todas as âncoras são links simples).
- **Pendentes**: T043 (Lighthouse não disponível neste ambiente — rodar no Chrome DevTools), T046 (commit/PR — aguardando aprovação), T047 (depende do DNS no Registro.br) e T048 (depende da conta GoatCounter).
