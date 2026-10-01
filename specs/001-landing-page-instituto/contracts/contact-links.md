# Contract: Links de Contato e Eventos de Estatística

Formato obrigatório de cada link de contato (FR-003, FR-018, FR-023, FR-024, SC-002, SC-006).

## Links

| Canal | `href` | Atributos | `data-goatcounter-click` |
|-------|--------|-----------|---------------------------|
| WhatsApp principal (botão flutuante) | `https://wa.me/5514996816005?text=Ol%C3%A1!%20Conheci%20o%20Instituto%20Pr%C3%B3-Ativo%20pelo%20site%20e%20gostaria%20de%20saber%20mais.` | `target="_blank" rel="noopener" aria-label="Conversar no WhatsApp com o Instituto Pró-Ativo"` | `whatsapp-flutuante` |
| WhatsApp principal (CTA do hero) | mesmo `href` | `target="_blank" rel="noopener"` | `whatsapp-hero` |
| WhatsApp principal (seção Como apoiar) | mesmo `href` | `target="_blank" rel="noopener"` | `whatsapp-como-apoiar` |
| WhatsApp principal (seção Contato) | mesmo `href` | `target="_blank" rel="noopener"` | `whatsapp-contato` |
| Telefone principal | `tel:+5514996816005` | — | `tel-principal` |
| E-mail | `mailto:contato.institutoproativo@gmail.com?subject=Contato%20pelo%20site` | — | `email` |
| Instagram Instituto | `https://www.instagram.com/institutoproativo/` | `target="_blank" rel="noopener"` | `instagram-instituto` |
| Instagram Projeto | `https://www.instagram.com/projetojjparatodos/` | `target="_blank" rel="noopener"` | `instagram-projeto` |
| Instagram Equipe | `https://www.instagram.com/eddynorthfight.ourinhos/` | `target="_blank" rel="noopener"` | `instagram-equipe` |
| Endereço (mapa) | `https://www.google.com/maps/search/?api=1&query=R.%20Celestino%20Lopes%20Bahia%2C%201051%2C%20Ourinhos%20-%20SP` | `target="_blank" rel="noopener"` | `mapa` |
| Botão "Fale conosco" do menu | `#contato` | — | — (navegação interna) |

## Regras

- O único telefone exibido é o do instituto, (14) 99681-6005. Telefones pessoais de membros da equipe **não** aparecem na página.
- Texto visível dos números no formato nacional: `(14) 99681-6005`.
- Links externos que abrem nova aba informam isso a leitores de tela (ícone com texto oculto "abre em nova aba" ou `aria-label`).
- O botão flutuante: canto inferior direito, ≥ 56×56 px de área de toque, não cobre o rodapé nem o conteúdo final (margem inferior no `footer`), oculto na impressão.
- Nenhum link de contato depende de JavaScript.
- Nenhum dado pessoal em query string além da mensagem padrão fixa do WhatsApp.

## Estatística (GoatCounter)

```html
<script data-goatcounter="https://institutoproativo.goatcounter.com/count"
        async src="https://gc.zgo.at/count.js"></script>
```

- Conta visualizações de página automaticamente (sem cookies).
- Conta cliques em elementos com `data-goatcounter-click="<evento>"` (eventos da tabela acima).
- O código `institutoproativo` depende da conta criada pelo usuário; enquanto não existir, o `<script>` fica comentado.
- Não contar visitas em `localhost` (comportamento padrão do GoatCounter).
