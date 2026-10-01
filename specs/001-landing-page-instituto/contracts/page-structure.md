# Contract: Estrutura da Página

Contrato de UI do `site/index.html`: ordem das seções, âncoras (estáveis — usadas no menu, em links externos e em QR codes) e conteúdo obrigatório. Requisitos de origem entre parênteses.

## Esqueleto

```text
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header>  navbar fixa no topo: brasão + nome · menu (colapsa < 992 px) · botão "Fale conosco"
<main id="conteudo">  seções abaixo, nesta ordem
<footer>  contato + redes + copyright "© <ano> Instituto Pró-Ativo"
  └ <a class="whatsapp-float">  botão flutuante de WhatsApp (canal principal), fixo na tela; dentro do footer para ficar em um landmark
```

## Seções (ordem obrigatória)

| # | `id` | Menu | Título (h1/h2) | Conteúdo obrigatório | Req. |
|---|------|------|----------------|----------------------|------|
| 1 | `inicio` | — | h1: "Existem crianças que só precisam de uma oportunidade" | Brasão; complemento "— e pessoas dispostas a caminhar com elas"; subtítulo "Esporte educacional como ferramenta de transformação social"; CTA primário "Quero fazer parte" (WhatsApp principal); CTA secundário "Conheça o projeto" (`#quem-somos`) | FR-003, FR-004 |
| 2 | `quem-somos` | Quem somos | Quem somos | OSC em Ourinhos/SP; missão; público (6–17 anos, rede pública, vulnerabilidade, atípicos; encaminhados por escolas, CRAS e conselho tutelar); Projeto Jiu-Jitsu Para Todos; destaques numéricos (2015, 100+ atendidos, 6–17) | FR-005 |
| 3 | `historia` | Nossa história | Tudo começou com um tatame | 2015, 8 alunos, Prof. Humberto Betão (in memoriam), Sensei Ismaile Santos; pandemia; TEA desde 2021, depois TDAH e não verbais; linhagem Eddy North Fighter → Reylson Gracie / Joe Moreira | FR-006 |
| 4 | `desafio` | — | O desafio social | 4 desafios (acesso, violência/ociosidade, autoestima/disciplina, evasão escolar) | FR-007 |
| 5 | `o-que-fazemos` | O que fazemos | Da quadra à sala de aula | 4 frentes: Esporte, Educação, Desenvolvimento humano, Família e escola | FR-008 |
| 6 | `metodologia` | Metodologia | Mais que esporte, uma ferramenta de transformação | 4 pilares; aulas 3x/semana por faixa etária e nível; acompanhamento; turmas atípicas menores; integração familiar; bloco "Formação técnica e projeção esportiva" ("O projeto não apenas inclui. Ele prepara e projeta.") | FR-009, FR-010 |
| 7 | `equipe` | Equipe | Nosso time | 4 membros (data-model §3) | FR-011 |
| 8 | `impacto` | Impacto | Impacto e metas | Indicadores (data-model §4), metas identificadas como meta, indicadores monitorados, benefícios por eixo (educacional, familiar/social, emocional/cidadão) | FR-012 |
| 9 | `confianca` | — | Segurança, governança e rede de apoio | Garantias (federados CBJJP, toxicológico, antecedentes, primeiros socorros, formação TEA/TDAH); equipe multidisciplinar de apoio; estrutura institucional (conselho fiscal, diretoria voluntária, contabilidade, estatuto nacional, núcleo piloto Ourinhos); rede de apoio (psicologia, saúde, educação, assistência, Unifio, escolas, CRAS, conselho tutelar) | FR-013 |
| 10 | `como-apoiar` | Como apoiar | Como você pode fazer parte | Formas de apoio; "qualquer valor, PF (CPF) ou PJ (CNPJ)"; menção breve ao incentivo fiscal em validação; CTA WhatsApp principal | FR-014 |
| 11 | `recursos` | — | Para onde vão os recursos | 6 destinos; 3 etapas de crescimento | FR-015 |
| 12 | `contrapartidas` | — | Contrapartidas | 5 contrapartidas, sem valores nem níveis | FR-016 |
| 13 | `citacao` | — | (sem h2; `<blockquote>`) | "Formamos pessoas. Antes de formar atletas." e/ou "Investir no Pró-Ativo é investir em transformação, disciplina & cidadania." | FR-017 |
| 14 | `contato` | Contato | Fale conosco | Todos os canais (contracts/contact-links.md); WhatsApp principal em destaque | FR-018 |

## Regras de validação

- Exatamente um `<h1>`; cada seção 2–12 e 14 tem um `<h2>`; nenhum nível pulado.
- Todos os `id`s acima existem e são únicos; todo link `href="#..."` aponta para um `id` existente.
- Busca por "Bronze", "Prata", "Ouro", "Master", "R$ 500", "R$ 1.000", "R$ 2.000" no HTML final retorna **zero** ocorrências (FR-019, SC-007).
- Menu fixo não cobre o título ao navegar por âncora (`scroll-margin-top` nas seções).
- Ordem de tabulação segue a ordem visual; foco sempre visível.

## Identidade visual (tokens CSS em `css/styles.css`)

| Token | Valor | Uso |
|-------|-------|-----|
| `--pa-navy` | `#0F2350` (aprox. dos materiais) | Fundo do header/footer/seções escuras, texto de títulos |
| `--pa-gold` | `#E8B423` | Destaques, botões sobre fundo escuro, divisores |
| `--pa-white` | `#FFFFFF` | Fundo principal |
| `--pa-gray` | `#F2F3F5` | Fundo de seções alternadas |
| `--pa-red/yellow/blue/green` | cores do coração-quebra-cabeça | Acentos pontuais (ícones, ilustrações) |

Contraste: texto sobre dourado sempre azul-marinho; dourado como cor de texto só sobre azul-marinho.
