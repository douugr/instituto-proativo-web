# Contract: SEO, Compartilhamento e Arquivos Públicos

Atende FR-022 e a decisão R11 de [research.md](../research.md).

## `<head>` do `index.html`

| Elemento | Valor |
|----------|-------|
| `<html lang>` | `pt-BR` |
| `<meta charset>` / `viewport` | `utf-8` / `width=device-width, initial-scale=1` |
| `<title>` | `Instituto Pró-Ativo – Jiu-Jitsu Para Todos em Ourinhos/SP` (≤ 60 caracteres) |
| `meta description` | `Esporte educacional que transforma vidas: o Instituto Pró-Ativo atende crianças e adolescentes em Ourinhos/SP com o Projeto Jiu-Jitsu Para Todos. Saiba como apoiar.` (≤ 160 caracteres) |
| `link rel=canonical` | `https://institutoproativo.com.br/` |
| `meta theme-color` | `#0F2350` |
| `og:type` / `og:locale` | `website` / `pt_BR` |
| `og:title` / `og:description` | iguais a title/description (podem ser mais curtos) |
| `og:url` | `https://institutoproativo.com.br/` |
| `og:image` | `https://institutoproativo.com.br/assets/brand/og-image.jpg` (1200×630, ≤ 300 KB) + `og:image:alt` |
| `twitter:card` | `summary_large_image` |
| Ícones | `favicon.ico`, `assets/brand/icon-32.png`, `assets/brand/apple-touch-icon.png` (180), `site.webmanifest` (192/512) |
| Preconnect | `https://cdn.jsdelivr.net`, `https://fonts.googleapis.com`, `https://fonts.gstatic.com` (crossorigin) |

## JSON-LD

```json
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Instituto Pró-Ativo",
  "url": "https://institutoproativo.com.br/",
  "logo": "https://institutoproativo.com.br/assets/brand/icon-512.png",
  "email": "contato.institutoproativo@gmail.com",
  "telephone": "+55-14-99681-6005",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "R. Celestino Lopes Bahia, 1051 - Vila São Luiz",
    "addressLocality": "Ourinhos",
    "addressRegion": "SP",
    "postalCode": "19911-205",
    "addressCountry": "BR"
  },
  "sameAs": [
    "https://www.instagram.com/institutoproativo/",
    "https://www.instagram.com/projetojjparatodos/"
  ]
}
```

## Arquivos na raiz de `site/`

| Arquivo | Conteúdo |
|---------|----------|
| `CNAME` | `institutoproativo.com.br` (uma linha) |
| `robots.txt` | `User-agent: *` / `Allow: /` / `Sitemap: https://institutoproativo.com.br/sitemap.xml` |
| `sitemap.xml` | Uma URL: `https://institutoproativo.com.br/` |
| `site.webmanifest` | `name`, `short_name` "Pró-Ativo", ícones 192/512, `theme_color` e `background_color` |
| `404.html` | Mensagem curta + link para `/` + mesmo CSS |

## Validação

- Pré-visualização do link no WhatsApp mostra título, descrição e imagem.
- Ferramentas de depuração de compartilhamento (ex.: Facebook Sharing Debugger) leem `og:image` sem erros.
- Validador de dados estruturados (Schema Markup Validator) sem erros.
