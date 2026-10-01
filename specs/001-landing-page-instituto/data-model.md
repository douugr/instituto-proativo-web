# Data Model: Landing Page do Instituto Pró-Ativo

**Feature**: `001-landing-page-instituto` | **Date**: 2026-10-01

Não há banco de dados nem dados de visitantes. Este documento descreve as **entidades de conteúdo** que o `site/index.html` exibe, seus campos e regras de validação, para que o conteúdo seja consistente e fácil de atualizar. Todos os valores abaixo vêm da spec e das clarificações.

---

## 1. Seção (`Section`)

Bloco temático da página. A lista e a ordem estão em [contracts/page-structure.md](contracts/page-structure.md).

| Campo | Tipo | Regras |
|-------|------|--------|
| `id` | âncora (kebab-case, sem acento) | Único na página; usado no menu (`#id`) |
| `title` | texto | Exatamente um `<h2>` por seção (hero usa o único `<h1>`) |
| `eyebrow` | texto curto, opcional | Rótulo acima do título (ex.: "QUEM SOMOS") |
| `body` | parágrafos/listas | Textos dos materiais; sem valores de cotas (FR-019) |
| `items[]` | lista de `Item` | Cartões/ícones da seção |
| `image` | `Image`, opcional | A mensagem da seção não pode depender só da imagem |
| `cta` | `ContactChannel`/âncora, opcional | Rótulo de ação claro (ex.: "Quero fazer parte") |
| `inMenu` | booleano | Se aparece no menu principal |

## 2. Item (`Item`)

Elemento repetido dentro de uma seção (pilar, frente de atuação, garantia, destino de recurso, contrapartida).

| Campo | Tipo | Regras |
|-------|------|--------|
| `icon` | nome Bootstrap Icons | Decorativo: `aria-hidden="true"` |
| `title` | texto | Obrigatório |
| `description` | texto, opcional | ≤ 60 palavras |

## 3. Membro da equipe (`TeamMember`)

| Campo | Tipo | Valores |
|-------|------|---------|
| `name` | texto | Ismaile Santos · Fernando Santim · César Evaristo · Orlando Weber |
| `role` | texto | Idealizador · Instrutor · Instrutor · Instrutor |
| `description` | texto | Ismaile: Professor faixa preta 1º grau (federado CBJJP). Fernando: desenvolvimento dos treinos, viagens e parcerias. César: desenvolvimento dos treinos, projetos dentro e fora do tatame. Orlando: desenvolvimento dos treinos, marca e metodologia kids, sob supervisão do sensei responsável |
| `photo` | `Image`, opcional | Sem foto → avatar com iniciais (não deixar espaço vazio) |

## 4. Indicador de impacto (`ImpactMetric`)

| Campo | Tipo | Regras |
|-------|------|--------|
| `value` | texto numérico | Exibido em destaque |
| `label` | texto | Descrição curta |
| `kind` | `atual` \| `meta` | Metas devem ser identificadas como meta no texto |

**Valores (fonte única — atualizar só aqui no HTML):**

| value | label | kind |
|-------|-------|------|
| 2015 | início do projeto | atual |
| +10 anos | de atuação | atual |
| 60 | crianças e adolescentes atendidos hoje | atual |
| 6 a 17 | anos — faixa etária atendida | atual |
| 3x | aulas de jiu-jitsu por semana | atual |
| 100 | crianças por ano | meta |
| +100 | famílias impactadas diretamente | meta |
| 300 | aulas por ano | meta |
| 75% | de frequência | meta |
| até 200 | alunos em 5 anos | meta |

**Indicadores monitorados** (lista, sem valor): frequência escolar, evolução comportamental, participação familiar, progressão técnica.

## 5. Canal de contato (`ContactChannel`)

Formato dos links em [contracts/contact-links.md](contracts/contact-links.md).

| type | label | value | responsável | destaque |
|------|-------|-------|-------------|----------|
| whatsapp | WhatsApp do Instituto | (14) 99681-6005 | — | **principal** (botão fixo + CTA do hero) |
| whatsapp/tel | Orlando | (14) 98108-6430 | Orlando Weber | secundário |
| whatsapp/tel | Ismaile | (14) 98827-4004 | Ismaile Santos | secundário |
| email | E-mail | contato.institutoproativo@gmail.com | — | secundário |
| instagram | Instituto | @institutoproativo | — | secundário |
| instagram | Projeto | @projetojjparatodos | — | secundário |
| instagram | Equipe | @eddynorthfight.ourinhos | — | secundário |
| address | Endereço | R. Celestino Lopes Bahia, 1051 – Vila São Luiz, Ourinhos/SP, CEP 19911-205 (espaço cedido CRAS-1) | — | secundário |

**Regras**: exatamente um canal `principal`; todo canal tem `analyticsEvent` (ver contrato); números exibidos no formato `(DD) 9XXXX-XXXX`, links no formato internacional `55DD9XXXXXXXX`.

## 6. Imagem (`Image`)

| Campo | Tipo | Regras |
|-------|------|--------|
| `src` | caminho em `assets/img/` | WebP + fallback JPEG via `<picture>` |
| `srcset` | 480w / 960w / 1600w | Fotos de conteúdo |
| `alt` | texto | Obrigatório e descritivo; `alt=""` só para imagens decorativas |
| `width`/`height` | inteiros | Obrigatórios (evitar salto de layout) |
| `loading` | `lazy` \| `eager` | `eager` + `fetchpriority="high"` só no hero |
| `size` | KB | ≤ 200 KB (hero ≤ 300 KB) |

Autorização de imagem: todas as fotos dos materiais atuais podem ser usadas (Clarifications da spec).

## Relacionamentos

```text
Page 1──* Section 1──* Item
               │ 0..1 Image
               │ 0..1 CTA ──> ContactChannel | âncora
Section "equipe"   1──* TeamMember 0..1 Image
Section "impacto"  1──* ImpactMetric
Section "contato"  1──* ContactChannel
```

Não há transições de estado (conteúdo estático).
