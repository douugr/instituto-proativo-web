# Research: Landing Page do Instituto Pró-Ativo

**Feature**: `001-landing-page-instituto` | **Date**: 2026-10-01

Decisões técnicas que resolvem os pontos em aberto do Technical Context. Restrições dadas pelo usuário: HTML + CSS + JavaScript (só quando necessário), Bootstrap para responsividade, hospedagem no GitHub Pages do repositório `douugr/instituto-proativo-web` e domínio próprio `institutoproativo.com.br` (já registrado em nome do usuário).

---

## R1. Versão e forma de carregar o Bootstrap

- **Decision**: Bootstrap **5.3.x** (última 5.3 estável) carregado do CDN jsDelivr com `integrity` (SRI) e `crossorigin="anonymous"`; somente `bootstrap.min.css` e `bootstrap.bundle.min.js` (inclui Popper). Ícones com **Bootstrap Icons 1.11.x** pelo mesmo CDN.
- **Rationale**: Sem etapa de build (o site é HTML puro). jsDelivr é rápido no Brasil, tem cache compartilhado e SRI garante integridade. O bundle JS é necessário apenas para o menu colapsável (navbar) e o scrollspy, ambos acionados por atributos `data-bs-*` — sem JS próprio.
- **Alternatives considered**:
  - *Copiar os arquivos do Bootstrap para o repositório*: elimina dependência externa, mas exige atualização manual e não traz ganho relevante.
  - *Compilar Bootstrap via Sass para customizar variáveis*: exigiria Node/build; a identidade visual é obtida sobrescrevendo as variáveis CSS do Bootstrap (`--bs-*`) em `css/styles.css`.

## R2. Publicação no GitHub Pages

- **Decision**: Publicar via **GitHub Actions** (fonte "GitHub Actions" nas configurações de Pages), com o workflow oficial `actions/configure-pages` → `actions/upload-pages-artifact` (pasta `site/`) → `actions/deploy-pages`, disparado por push na branch `main` e manualmente (`workflow_dispatch`).
- **Rationale**: O repositório também contém `specs/`, `.specify/` e `.claude/`. Publicar a raiz da branch exporia esses arquivos no domínio público. Com Actions, apenas `site/` é publicado, e o mesmo workflow pode rodar validações antes do deploy.
- **Alternatives considered**:
  - *Deploy from branch → `main` `/ (root)`*: publicaria arquivos internos.
  - *Deploy from branch → `main` `/docs`*: funciona sem Actions, mas "docs" confunde com documentação e não permite validação antes do deploy.
  - *Branch `gh-pages` separada*: mais um ponto de manutenção, sem vantagem.

## R3. Visibilidade do repositório (BLOQUEIO DE CONFIGURAÇÃO)

- **Finding**: O repositório `douugr/instituto-proativo-web` está **privado**. GitHub Pages em repositório privado só está disponível nos planos pagos (GitHub Pro, Team ou Enterprise). No plano Free, o Pages exige repositório **público**.
- **Decision**: Tornar o repositório **público** (recomendado), a menos que a conta do usuário seja GitHub Pro. O site publicado é público de qualquer forma; o conteúdo do repositório (specs e código do site) não contém segredos.
- **Rationale**: Custo zero e configuração mais simples. Antes de abrir o repositório, verificar que nenhum arquivo contém dados sensíveis (o conteúdo atual é só documentação de especificação e o site).
- **Alternatives considered**: *Manter privado com GitHub Pro* (≈ US$ 4/mês); *hospedar em outro serviço* (descartado pelo usuário).

## R4. Domínio próprio `institutoproativo.com.br` (Registro.br)

- **Decision**:
  - Domínio canônico: **`institutoproativo.com.br`** (sem www); `www.institutoproativo.com.br` redireciona automaticamente para ele (o GitHub Pages faz isso quando os dois estão configurados).
  - DNS no Registro.br (modo "DNS do Registro.br" ou "Editar zona"):
    - `A` para o apex: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
    - `AAAA` para o apex: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
    - `CNAME` `www` → `douugr.github.io.`
  - **Verificar o domínio** no GitHub (Settings da conta → Pages → Add a domain) com o registro `TXT` `_github-pages-challenge-douugr` fornecido pelo GitHub, para impedir que terceiros reivindiquem o domínio.
  - Em Settings → Pages: Custom domain `institutoproativo.com.br` e **Enforce HTTPS** ligado (certificado Let's Encrypt emitido automaticamente após a propagação do DNS, normalmente minutos a algumas horas; até 24 h).
  - Manter também um arquivo `site/CNAME` com `institutoproativo.com.br` como registro no código (com deploy via Actions, a configuração que vale é a das Settings, mas o arquivo documenta o domínio e não causa problemas).
- **Rationale**: Configuração oficial do GitHub para domínio apex + www; o Registro.br permite registros A/AAAA/CNAME/TXT no próprio painel.
- **Alternatives considered**: *Usar `www` como canônico* (exige só CNAME, mas o endereço curto é o que aparece nos materiais impressos); *DNS na Cloudflare* (desnecessário neste momento).

## R5. Estatística de acesso sem cookies (FR-024)

- **Decision**: **GoatCounter** (goatcounter.com), plano gratuito, com um script assíncrono `count.js` e contagem de cliques via atributo `data-goatcounter-click` nos links de contato.
- **Rationale**: Não usa cookies nem guarda dados pessoais, dispensando aviso de consentimento (LGPD); é gratuito para organizações sem fins lucrativos/uso pessoal; o painel mostra visitas, origem e contagem de cliques por evento; contagem de cliques é declarativa (sem JS próprio).
- **Alternatives considered**:
  - *Cloudflare Web Analytics*: também sem cookies e gratuito, mas não conta cliques em links (eventos).
  - *Plausible*: excelente, mas pago.
  - *Google Analytics 4*: exige aviso de cookies, descartado na clarificação.
- **Dependência do usuário**: criar uma conta GoatCounter (ex.: código `institutoproativo` → `institutoproativo.goatcounter.com`). Até isso acontecer, o script fica comentado/desativado sem quebrar a página.

## R6. Tipografia

- **Decision**: **Barlow** (texto, 400/500/600) e **Barlow Semi Condensed** (títulos, 700/800) do Google Fonts, com `preconnect` e `display=swap`; fallback `system-ui, sans-serif`.
- **Rationale**: Os materiais usam uma sans-serif geométrica/condensada em caixa alta nos títulos (estilo "PARA ONDE VÃO OS RECURSOS"); a família Barlow reproduz esse visual, tem bom suporte a acentos do português e boa leitura no celular.
- **Alternatives considered**: *Bebas Neue* para títulos (só caixa alta, sem pesos, menos flexível); *Montserrat* (visual menos próximo dos materiais).

## R7. Imagens

- **Decision**:
  - Fontes: brasão (PNG enviado pelo usuário) e fotos extraídas dos PDFs fornecidos (panfleto A5 e apresentação comercial), complementadas por fotos que o instituto enviar.
  - Formato: **WebP** com fallback **JPEG** via `<picture>`; larguras de 480/960/1600 px com `srcset`/`sizes`; brasão em PNG com transparência (e versões 192/512 px para ícones).
  - `loading="lazy"` e `decoding="async"` em tudo abaixo da primeira dobra; a imagem do hero com `fetchpriority="high"` e sem lazy.
  - `width`/`height` sempre declarados para evitar saltos de layout.
  - Meta: cada imagem ≤ 200 KB (hero ≤ 300 KB); página inteira ≤ 1,5 MB no primeiro carregamento.
  - Otimização feita uma vez, localmente (ex.: `cwebp`/Squoosh), sem build no CI.
- **Rationale**: Atende SC-003 (primeira dobra em até 3 s em 4G) e a edge case de conexão lenta.

## R8. JavaScript

- **Decision**: Nenhum JS próprio obrigatório. Usar apenas:
  - `bootstrap.bundle.min.js` (menu colapsável; scrollspy por `data-bs-spy`);
  - script do GoatCounter;
  - um pequeno `js/main.js` (≤ 1 KB) para: ano corrente no rodapé e fechar o menu móvel ao clicar em um link de âncora.
- **Rationale**: O usuário pediu JS só se necessário; o conteúdo e todos os links funcionam sem JS (progressive enhancement). Rolagem suave via CSS (`scroll-behavior: smooth`, respeitando `prefers-reduced-motion`).

## R9. Conteúdo: inline no HTML vs. arquivo de dados

- **Decision**: Todo o conteúdo fica **escrito diretamente no `index.html`**, organizado por seções com comentários claros. Números de impacto e contatos ficam em pontos únicos e fáceis de achar (ver `data-model.md`).
- **Rationale**: Melhor para SEO e para a página funcionar sem JS; o volume de conteúdo é pequeno e muda pouco; não há painel administrativo no escopo.
- **Alternatives considered**: *JSON + renderização por JS* (pior SEO e dependência de JS); *gerador de site estático (Jekyll/11ty)* (adiciona build e complexidade sem necessidade).

## R10. Links de contato

- **Decision**:
  - WhatsApp: `https://wa.me/5514996816005?text=<mensagem codificada>` com mensagem padrão "Olá! Conheci o Instituto Pró-Ativo pelo site e gostaria de saber mais." (funciona no celular e no WhatsApp Web no desktop).
  - Telefone: `tel:+5514981086430` (Orlando) e `tel:+5514988274004` (Ismaile); também `wa.me` para cada um.
  - E-mail: `mailto:contato.institutoproativo@gmail.com?subject=Contato%20pelo%20site`.
  - Instagram: `https://www.instagram.com/<perfil>/`.
  - Endereço: link para Google Maps (busca pelo endereço) — sem mapa embutido (evita cookies de terceiros e peso).
  - Links externos com `target="_blank" rel="noopener"` (FR-023).
- **Rationale**: Atende FR-018, FR-023, SC-006 e a edge case de dispositivo sem WhatsApp.

## R11. SEO e compartilhamento (FR-022)

- **Decision**: `<title>` e `meta description` próprios; Open Graph e Twitter Card com imagem 1200×630 (`og-image.jpg`); `link rel="canonical"` para `https://institutoproativo.com.br/`; `lang="pt-BR"`; dados estruturados JSON-LD `NGO` (nome, logo, endereço, telefone, e-mail, `sameAs` com os Instagrams); `robots.txt` e `sitemap.xml`; favicons (`favicon.ico`, `icon.svg`/PNG 32, `apple-touch-icon.png` 180) e `site.webmanifest`.

## R12. Acessibilidade (FR-021, SC-005)

- **Decision**: WCAG 2.1 AA — link "Pular para o conteúdo"; um único `<h1>` e hierarquia `h2`/`h3` por seção; landmarks (`header`, `nav`, `main`, `footer`); contraste mínimo 4.5:1 (dourado sobre branco **não** é usado para texto pequeno; em texto usar azul-marinho ou dourado sobre azul-marinho); foco visível; `alt` descritivo; ícones decorativos com `aria-hidden="true"`; botão flutuante com `aria-label`; respeitar `prefers-reduced-motion`.

## R13. Validação / testes

- **Decision**: Sem testes unitários (não há lógica). Validação em três camadas:
  1. **CI (GitHub Actions, antes do deploy)**: `html-validate` no HTML e verificação de links internos/externos com `lychee` (falha bloqueia o deploy).
  2. **Manual antes de cada publicação**: Lighthouse (mobile) com metas Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95; axe DevTools sem erros críticos; teste em 320 px, 375 px, 768 px, 1280 px.
  3. **Roteiro de aceite**: `quickstart.md`, mapeado para as user stories e success criteria.
- **Rationale**: Proporcional a um site estático de uma página; cobre SC-003 a SC-007.

## R14. Fluxo de branches e deploy

- **Decision**: Desenvolvimento na branch `001-landing-page-instituto`; Pull Request para `main`; o merge em `main` dispara o deploy. O workflow também roda as validações em PRs (sem deploy).
- **Rationale**: Evita publicar trabalho incompleto; o histórico de publicação fica no GitHub.
