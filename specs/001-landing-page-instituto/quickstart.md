# Quickstart: Landing Page do Instituto Pró-Ativo

Guia para rodar localmente, validar, configurar o GitHub Pages com o domínio `institutoproativo.com.br` e conferir a página publicada. Contratos de referência: [page-structure](contracts/page-structure.md), [contact-links](contracts/contact-links.md), [seo-metadata](contracts/seo-metadata.md).

## 1. Pré-requisitos

- Git e acesso ao repositório `douugr/instituto-proativo-web`
- Python 3 (para servir o site localmente) — já vem no macOS
- Opcional para validar localmente: Node.js 20+ (`npx html-validate`) e `lychee` (`brew install lychee`)
- Acesso de administrador ao repositório no GitHub e ao painel do **Registro.br**

## 2. Rodar localmente

```bash
python3 -m http.server 8000 --directory site
```

Abrir `http://localhost:8000`. (Abrir o `index.html` direto pelo Finder também funciona, mas o servidor reproduz melhor o GitHub Pages.)

## 3. Validar localmente (as mesmas verificações do CI)

```bash
npx --yes html-validate@9 "site/**/*.html"
```

```bash
lychee --config lychee.toml site
```

```bash
grep -RniE "\\b(bronze|prata|ouro|master)\\b|R\\$ ?(500|1\\.000|2\\.000)" site && echo "FALHA: menção a cotas" || echo "OK: sem cotas"
```

**Esperado**: nenhum erro de HTML, nenhum link quebrado, "OK: sem cotas".

## 4. Configurar o GitHub Pages (uma única vez)

### 4.1 Visibilidade do repositório

O repositório está **privado**. No plano gratuito do GitHub, o Pages só funciona em repositório **público**.

- GitHub → repositório → **Settings → General → Danger Zone → Change visibility → Make public**
- (Alternativa: assinar GitHub Pro e manter privado.)

### 4.2 Fonte de publicação

- **Settings → Pages → Build and deployment → Source: GitHub Actions**
- O workflow `.github/workflows/pages.yml` publica a pasta `site/` a cada push na `main`.

### 4.3 Verificar o domínio na sua conta (recomendado — protege contra "sequestro" do domínio)

1. GitHub → foto do perfil → **Settings → Pages → Add a domain** → `institutoproativo.com.br`
2. O GitHub mostra um registro **TXT** (nome `_github-pages-challenge-douugr`, valor gerado).
3. Criar esse TXT no Registro.br (passo 4.4) e voltar para clicar **Verify**.

### 4.4 DNS no Registro.br

Registro.br → **Meus domínios → institutoproativo.com.br → DNS → Editar zona** (se aparecer "Utilizar DNS do Registro.br", ative-o primeiro). Criar:

| Tipo | Nome | Valor |
|------|------|-------|
| A | (vazio / @) | `185.199.108.153` |
| A | (vazio / @) | `185.199.109.153` |
| A | (vazio / @) | `185.199.110.153` |
| A | (vazio / @) | `185.199.111.153` |
| AAAA | (vazio / @) | `2606:50c0:8000::153` |
| AAAA | (vazio / @) | `2606:50c0:8001::153` |
| AAAA | (vazio / @) | `2606:50c0:8002::153` |
| AAAA | (vazio / @) | `2606:50c0:8003::153` |
| CNAME | `www` | `douugr.github.io.` |
| TXT | `_github-pages-challenge-douugr` | (valor do passo 4.3) |

Remover registros A/CNAME antigos do apex ou do `www` que apontem para outro lugar (ex.: página de "domínio estacionado").

Conferir a propagação:

```bash
dig +short institutoproativo.com.br A
```

```bash
dig +short www.institutoproativo.com.br CNAME
```

**Esperado**: os quatro IPs `185.199.10x.153` e `douugr.github.io.`

### 4.5 Domínio personalizado e HTTPS

1. **Settings → Pages → Custom domain**: `institutoproativo.com.br` → **Save**.
2. Aguardar "DNS check successful" (minutos a algumas horas).
3. Marcar **Enforce HTTPS** (fica disponível após o certificado ser emitido; pode levar até 24 h).

### 4.6 Primeira publicação

Abrir um Pull Request de `001-landing-page-instituto` para `main`. O workflow roda as validações no PR; após o merge, roda de novo e publica. Acompanhar em **Actions → Deploy GitHub Pages**.

### 4.7 Estatística (GoatCounter)

1. Criar conta em `https://www.goatcounter.com/signup` com o código `institutoproativo`.
2. Em **Settings** do GoatCounter, preencher o domínio `institutoproativo.com.br`.
3. Descomentar o `<script data-goatcounter>` no `site/index.html` (se ainda estiver comentado) e publicar.

## 5. Roteiro de aceite (após publicar)

| # | Verificação | Esperado | Spec |
|---|-------------|----------|------|
| 1 | Abrir `http://institutoproativo.com.br` e `https://www.institutoproativo.com.br` | Ambos terminam em `https://institutoproativo.com.br/` com cadeado | FR-022 |
| 2 | Ler a primeira dobra no celular | Brasão, mensagem principal e botão "Quero fazer parte" visíveis sem rolar | US1-1, FR-004 |
| 3 | Rolar a página inteira | Todas as 14 seções na ordem do contrato; nenhuma menção a cotas | US1, US3-4, SC-007 |
| 4 | Tocar no botão flutuante de WhatsApp (celular) | Abre o WhatsApp com (14) 99681-6005 e a mensagem padrão | US2-2, FR-003 |
| 5 | Mesmo teste no desktop | Abre o WhatsApp Web em nova aba; a página continua aberta | Edge case, FR-023 |
| 6 | Testar todos os links da seção Contato | WhatsApp, telefone, e-mail, 3 Instagrams e mapa funcionam | SC-006 |
| 7 | Navegar só com teclado (Tab/Enter) | "Pular para o conteúdo" aparece; foco sempre visível; menu e links acessíveis | FR-021 |
| 8 | Lighthouse (modo mobile) | Performance ≥ 90, Acessibilidade ≥ 95, Boas práticas ≥ 95, SEO ≥ 95 | SC-003, SC-005 |
| 9 | axe DevTools | Zero problemas críticos/sérios | SC-005 |
| 10 | DevTools → responsivo em 320, 375, 768, 1280 px | Sem rolagem horizontal; textos legíveis; menu colapsa no celular | SC-004, FR-020 |
| 11 | DevTools → Network "Fast 4G", cache desativado | Primeira dobra legível em ≤ 3 s; total transferido ≤ 1,5 MB | SC-003 |
| 12 | DevTools → Application → Cookies | Nenhum cookie criado pelo site | FR-024 |
| 13 | Colar o link no WhatsApp | Pré-visualização com título, descrição e imagem | FR-022 |
| 14 | Painel do GoatCounter após alguns acessos/cliques | Visitas e eventos `whatsapp-*`, `email`, `instagram-*` aparecem | FR-024, SC-008 |
| 15 | Teste com 5 pessoas que não conhecem o instituto | ≥ 4 explicam o que o instituto faz, para quem e onde em ≤ 2 min | SC-001 |

## 6. Atualizar conteúdo depois

- Editar `site/index.html` (números de impacto e contatos estão em blocos comentados e únicos — ver [data-model.md](data-model.md)).
- Novas fotos: otimizar para WebP/JPEG em 480/960/1600 px e colocar em `site/assets/img/`.
- Commit → PR → merge na `main` → publicação automática.
