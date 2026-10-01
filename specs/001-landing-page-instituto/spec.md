# Feature Specification: Landing Page do Instituto Pró-Ativo

**Feature Branch**: `001-landing-page-instituto`

**Created**: 2026-10-01

**Status**: Draft

**Input**: User description: "Landing page para o Instituto Pro Ativo, com base nos materiais compartilhados (panfleto A5 'Convite Projeto', apresentação institucional e apresentação comercial). Não incluir por enquanto a seção de 'Cotas de patrocínio'."

## Contexto

O **Instituto Pró-Ativo** é uma Organização da Sociedade Civil (OSC) sediada em Ourinhos/SP que promove cidadania, educação e qualidade de vida para crianças e adolescentes em situação de vulnerabilidade, usando o esporte educacional — principalmente o jiu-jitsu — como ferramenta de transformação social. Seu projeto principal é o **Projeto Jiu-Jitsu Para Todos**, iniciado em 2015 (Prof. Humberto Betão, *in memoriam*, e Sensei Ismaile Santos), que desde 2021 também acolhe crianças com TEA, TDAH e outros desafios de desenvolvimento.

A landing page é o primeiro ponto de contato digital do instituto: deve contar essa história, transmitir credibilidade e converter visitantes (famílias, empresários, profissionais, voluntários, parceiros institucionais) em contatos.

**Fontes de conteúdo**: panfleto A5 "Existem crianças que só precisam de uma oportunidade", apresentação institucional (reunião de alinhamento estratégico), apresentação comercial para empresas, infográfico "Para onde vão os recursos / Contrapartidas" e o brasão oficial do instituto.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Conhecer o instituto e sua causa (Priority: P1)

Um visitante (por exemplo, um empresário que recebeu o convite impresso e escaneou o QR code, ou alguém que veio do Instagram) acessa a página e, em poucos segundos, entende quem é o Instituto Pró-Ativo, o que faz, para quem e por quê — e sente confiança na seriedade da organização.

**Why this priority**: Sem compreensão e confiança na causa, nenhuma outra ação (contato, apoio, matrícula) acontece. É o núcleo da página.

**Independent Test**: Exibir a página a uma pessoa que não conhece o instituto; após rolar a página, ela consegue explicar o que o instituto faz, para quem, onde, desde quando e citar ao menos um diferencial (inclusão de crianças atípicas, linhagem técnica, equipe multidisciplinar).

**Acceptance Scenarios**:

1. **Given** um visitante acessando a página pela primeira vez, **When** ele visualiza a primeira dobra (hero), **Then** vê o nome/brasão do Instituto Pró-Ativo, uma mensagem de impacto (ex.: "Existem crianças que só precisam de uma oportunidade") e uma chamada clara para ação.
2. **Given** um visitante rolando a página, **When** chega à seção de história, **Then** encontra a trajetória do projeto (início em 2015 com 8 alunos, continuidade na pandemia, inclusão de TEA/TDAH desde 2021, linhagem Eddy North Fighter / Gracie).
3. **Given** um visitante interessado na proposta, **When** lê as seções "O desafio social", "O que fazemos" e "Metodologia", **Then** entende o problema enfrentado, as frentes de atuação (Esporte, Educação, Desenvolvimento humano, Família e escola) e os pilares formativos.

---

### User Story 2 - Entrar em contato com o instituto (Priority: P1)

Um visitante que se interessou (potencial apoiador, voluntário, família ou parceiro) encontra facilmente como falar com o instituto e inicia o contato com um clique.

**Why this priority**: É a principal conversão da página; sem ela, o interesse gerado se perde.

**Independent Test**: A partir de qualquer ponto da página, o visitante chega a um canal de contato (WhatsApp, telefone, e-mail ou Instagram) em no máximo 1 clique/toque.

**Acceptance Scenarios**:

1. **Given** um visitante em qualquer seção, **When** aciona a chamada principal ("Fale conosco" / "Quero fazer parte"), **Then** é levado à seção de contato ou diretamente a um canal de conversa.
2. **Given** um visitante em um celular, **When** toca no número de WhatsApp/telefone, **Then** o aplicativo correspondente é aberto com o número preenchido.
3. **Given** um visitante na seção de contato, **When** visualiza as informações, **Then** vê telefones (Orlando e Ismaile), e-mail, perfis do Instagram (@institutoproativo, @projetojjparatodos, @eddynorthfight.ourinhos) e endereço do espaço atual.

---

### User Story 3 - Entender como apoiar e o impacto do apoio (Priority: P2)

Um empresário, profissional ou cidadão quer saber de que formas pode contribuir (além de dinheiro), para onde vão os recursos e que resultados o instituto busca, para decidir se vai se envolver.

**Why this priority**: Converte interesse em engajamento qualificado; depende da compreensão (US1) e do contato (US2) já estarem disponíveis.

**Independent Test**: Um visitante consegue listar ao menos três formas de apoiar e explicar para onde vão os recursos captados, sem que a página exiba valores de cotas de patrocínio.

**Acceptance Scenarios**:

1. **Given** um visitante na seção "Como fazer parte", **When** lê o conteúdo, **Then** vê formas de apoio: conhecimento/voluntariado profissional, estrutura, investimento na manutenção/expansão, divulgação e conexões.
2. **Given** um visitante na seção de destinação de recursos, **When** lê o conteúdo, **Then** vê os destinos prioritários (estruturação do novo espaço; água, energia, internet e limpeza; custos fixos; materiais esportivos; apoio administrativo; atividades de integração e formação) e as etapas de crescimento (1. Estruturar o novo espaço; 2. Garantir funcionamento contínuo; 3. Ampliar equipe e dedicação).
3. **Given** um visitante na seção de impacto, **When** lê os indicadores, **Then** vê números-chave do projeto e as metas (ex.: chegar a 100 crianças por ano; visão de até 200 alunos em 5 anos) e os indicadores monitorados (frequência escolar, evolução comportamental, participação familiar, progressão técnica).
4. **Given** qualquer visitante, **When** percorre toda a página, **Then** não encontra valores nem descrição das cotas Bronze/Prata/Ouro/Master.

---

### User Story 4 - Confiar na equipe e na governança (Priority: P2)

Um potencial apoiador ou uma família quer verificar quem conduz o projeto e se o ambiente é seguro e bem gerido.

**Why this priority**: Credibilidade é decisiva tanto para famílias (segurança das crianças) quanto para empresas (segurança jurídica e reputacional).

**Independent Test**: O visitante identifica os responsáveis pelo projeto e ao menos três garantias de segurança/conformidade.

**Acceptance Scenarios**:

1. **Given** um visitante na seção de equipe, **When** visualiza o conteúdo, **Then** vê Ismaile Santos (idealizador, faixa preta 1º grau, federado CBJJP), Fernando Santim, César Evaristo e Orlando Weber (instrutores), com seus papéis.
2. **Given** um visitante na seção de segurança e governança, **When** lê o conteúdo, **Then** vê: professores federados, exame toxicológico periódico, antecedentes criminais verificados, certificação em primeiros socorros, formação para atuação com TEA/TDAH, equipe multidisciplinar de apoio, conselho fiscal, contabilidade permanente e estatuto com abrangência nacional.
3. **Given** um visitante na seção "Rede de apoio", **When** lê o conteúdo, **Then** vê as parcerias (psicologia, saúde, educação, assistência, universidade/laboratório Unifio, escolas, CRAS, conselho tutelar).

---

### User Story 5 - Ver as contrapartidas para empresas apoiadoras (Priority: P3)

Uma empresa quer saber, de forma geral, que visibilidade e retorno institucional tem ao apoiar o instituto (sem entrar em valores de cotas).

**Why this priority**: Útil para captação empresarial, mas o detalhamento comercial completo (cotas) foi explicitamente adiado.

**Independent Test**: O visitante identifica as contrapartidas gerais oferecidas e que o apoio pode ser feito por pessoa física ou jurídica, em qualquer valor.

**Acceptance Scenarios**:

1. **Given** um visitante empresarial, **When** chega à seção de contrapartidas, **Then** vê: divulgação em materiais institucionais, redes sociais, banners e eventos, ações presenciais e relatórios de impacto social.
2. **Given** qualquer visitante, **When** lê a seção de apoio, **Then** é informado de que pode apoiar com qualquer valor, como pessoa física (CPF) ou jurídica (CNPJ), e é direcionado ao contato.

---

### Edge Cases

- **Acesso via celular a partir do QR code do material impresso**: a página deve ser plenamente legível e utilizável em telas pequenas, que são o cenário mais provável.
- **Conexão lenta (3G/rede móvel fraca)**: o conteúdo textual e as chamadas para ação devem aparecer mesmo antes de todas as imagens carregarem.
- **Imagem não carregada**: deve existir texto alternativo descritivo; a mensagem da seção não pode depender exclusivamente da imagem.
- **Dispositivo sem WhatsApp instalado** (ex.: desktop): o link de WhatsApp deve continuar funcional (versão web) e o telefone/e-mail devem estar visíveis como alternativa.
- **Visitante com deficiência visual ou navegação por teclado**: toda a página e as chamadas para ação devem ser navegáveis e compreensíveis por tecnologias assistivas.
- **Números divergentes entre materiais** (ex.: 60 vs. 42 alunos atendidos): a página deve exibir um único conjunto consistente de números — ver FR-012.
- **Visitante procurando valores de patrocínio**: como as cotas não estão na página, a seção de apoio deve orientá-lo a entrar em contato para receber a proposta.

## Requirements *(mandatory)*

### Functional Requirements

**Estrutura e identidade**

- **FR-001**: A página MUST ser uma página única (one-page), em português do Brasil, com seções acessíveis por navegação interna (menu com âncoras).
- **FR-002**: A página MUST exibir o brasão oficial do Instituto Pró-Ativo e seguir a identidade visual dos materiais (azul-marinho, dourado/amarelo e branco, com as cores do coração-quebra-cabeça como acento).
- **FR-003**: A página MUST manter uma chamada para ação principal visível na primeira dobra e um acesso ao contato disponível durante a rolagem (ex.: menu fixo ou botão flutuante de WhatsApp).

**Seções de conteúdo** (ordem sugerida)

- **FR-004**: **Hero** — MUST apresentar o nome do instituto, a mensagem "Existem crianças que só precisam de uma oportunidade — e pessoas dispostas a caminhar com elas" (ou variação aprovada), o subtítulo "Esporte educacional como ferramenta de transformação social" e CTA(s) para contato/apoio.
- **FR-005**: **Quem somos** — MUST descrever o instituto como OSC, sua missão, público atendido (crianças e adolescentes de 6 a 17 anos da rede pública em vulnerabilidade, incluindo atípicos, encaminhados por escolas, CRAS e conselho tutelar) e o Projeto Jiu-Jitsu Para Todos como iniciativa principal.
- **FR-006**: **Nossa história** — MUST narrar a trajetória "Tudo começou com um tatame": início em 2015 com 8 alunos (Prof. Humberto Betão *in memoriam* e Sensei Ismaile Santos), continuidade durante a pandemia, inclusão de crianças com TEA desde 2021 e depois TDAH/não verbais, e a linhagem técnica (equipe Eddy North Fighter, Mestre Eddy North faixa coral 8º grau, ligação com Reylson Gracie e Grande Mestre Joe Moreira).
- **FR-007**: **O desafio social** — MUST listar os desafios enfrentados pelo público: falta de acesso a esporte/atividades extracurriculares, exposição à violência e ociosidade, baixa autoestima e dificuldade de disciplina, risco de evasão escolar.
- **FR-008**: **O que fazemos** — MUST apresentar as quatro frentes: Esporte (jiu-jitsu por faixa etária e nível, pilates, yoga, aula coletiva mensal), Educação (informática, aulas experimentais em escolas parceiras e APAEs, palestras), Desenvolvimento humano (equipe multidisciplinar) e Família e escola (anamnese, monitoramento de frequência e notas, reuniões periódicas).
- **FR-009**: **Metodologia / Pilares** — MUST apresentar os quatro pilares formativos (Disciplina e respeito; Foco, persistência e superação; Trabalho em equipe; Autocontrole emocional) e os elementos da metodologia (aulas 3x por semana por faixa etária/nível, acompanhamento de frequência e evolução, turmas atípicas em grupos menores, integração familiar).
- **FR-010**: **Formação técnica e projeção esportiva** — MUST mencionar o sistema de graduação estruturado e federado, participação em campeonatos e eventos e identificação de talentos ("O projeto não apenas inclui. Ele prepara e projeta.").
- **FR-011**: **Equipe** — MUST apresentar Ismaile Santos (idealizador), Fernando Santim, César Evaristo e Orlando Weber (instrutores), com papel resumido de cada um, e espaço para foto.
- **FR-012**: **Impacto e metas** — MUST exibir números-chave e metas: 2015 (início), ~10 anos de atuação, faixa etária 6–17, alunos atendidos hoje (valor a ser confirmado — ver Assumptions), meta de 100 crianças/ano, +100 famílias impactadas, 300 aulas/ano, 75% de frequência, visão de até 200 alunos em 5 anos; além dos indicadores monitorados (frequência escolar, evolução comportamental, participação familiar, progressão técnica) e dos benefícios por eixo (educacional, familiar/social, emocional/cidadão).
- **FR-013**: **Segurança, governança e rede de apoio** — MUST apresentar as garantias de segurança e conformidade, a estrutura institucional (conselho fiscal, diretoria voluntária, contabilidade permanente, estatuto com abrangência nacional, núcleo piloto em Ourinhos/SP) e a rede de apoio/parcerias (psicologia, saúde, educação, assistência, Unifio, escolas, CRAS, conselho tutelar).
- **FR-014**: **Como fazer parte** — MUST apresentar as formas de apoio (conhecimento, estrutura, experiência profissional, investimento, divulgação, conexões, voluntariado), a mensagem de que é possível apoiar com qualquer valor como pessoa física ou jurídica, e um CTA para contato.
- **FR-015**: **Para onde vão os recursos** — MUST listar os destinos prioritários dos recursos e as três etapas de crescimento do projeto.
- **FR-016**: **Contrapartidas** — MUST listar as contrapartidas gerais (divulgação em materiais institucionais, redes sociais, banners e eventos, ações presenciais, relatórios de impacto social), sem valores nem níveis de cota.
- **FR-017**: **Citação/fechamento emocional** — SHOULD incluir uma frase de impacto (ex.: "Formamos pessoas. Antes de formar atletas." e/ou "Investir no Pró-Ativo é investir em transformação, disciplina & cidadania.").
- **FR-018**: **Contato e rodapé** — MUST exibir telefones (14) 98108-6430 (Orlando) e (14) 98827-4004 (Ismaile) com links para WhatsApp/ligação, e-mail contato.institutoproativo@gmail.com (link de e-mail), Instagram @institutoproativo, @projetojjparatodos e @eddynorthfight.ourinhos (links externos), endereço R. Celestino Lopes Bahia, 1051 – Vila São Luiz, Ourinhos/SP, CEP 19911-205 (espaço cedido CRAS-1), e o nome do instituto com ano corrente no rodapé.

**Escopo excluído**

- **FR-019**: A página MUST NOT exibir a seção "Cotas de patrocínio" (Bronze R$ 500, Prata R$ 1.000, Ouro R$ 2.000, Master sob proposta) nem seus benefícios detalhados nesta versão.

**Qualidade e acesso**

- **FR-020**: A página MUST ser responsiva e totalmente utilizável em celulares, tablets e desktops.
- **FR-021**: A página MUST atender às diretrizes de acessibilidade WCAG 2.1 nível AA (contraste, textos alternativos, navegação por teclado, hierarquia de títulos).
- **FR-022**: A página MUST ter título, descrição e imagem de pré-visualização adequados para compartilhamento em redes sociais e WhatsApp, e ser indexável por buscadores.
- **FR-023**: Links externos (Instagram, WhatsApp) MUST abrir sem que o visitante perca a página do instituto.

### Key Entities

- **Seção de conteúdo**: bloco temático da página (título, texto, itens, imagem opcional, CTA opcional).
- **Membro da equipe**: nome, papel, descrição curta, foto.
- **Indicador de impacto**: rótulo, valor numérico, descrição/contexto (atual ou meta).
- **Canal de contato**: tipo (WhatsApp, telefone, e-mail, Instagram, endereço), valor, responsável (quando houver).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Em teste com 5 pessoas que não conhecem o instituto, ao menos 4 conseguem explicar em até 2 minutos de navegação o que o instituto faz, para quem e onde.
- **SC-002**: A partir de qualquer ponto da página, o visitante chega a um canal de contato em no máximo 1 clique/toque.
- **SC-003**: O conteúdo principal da primeira dobra fica visível em até 3 segundos em uma conexão móvel 4G típica.
- **SC-004**: A página não apresenta rolagem horizontal nem texto ilegível em telas a partir de 320px de largura.
- **SC-005**: A página passa em uma verificação automatizada de acessibilidade sem erros críticos e todas as imagens informativas possuem texto alternativo.
- **SC-006**: 100% dos links de contato (WhatsApp, telefone, e-mail, Instagram) funcionam corretamente em celular e desktop.
- **SC-007**: Nenhuma menção a valores ou níveis de cotas de patrocínio aparece na página.
- **SC-008**: Após a publicação, o instituto passa a receber contatos identificados como vindos do site (meta qualitativa a acompanhar pelos responsáveis).

## Assumptions

- **Público**: famílias da região de Ourinhos/SP, empresários, profissionais liberais, educadores, potenciais voluntários e parceiros institucionais; o acesso será majoritariamente via celular (QR code dos impressos e Instagram).
- **Idioma**: apenas português do Brasil nesta versão.
- **Contato sem formulário**: a conversão será feita por links diretos (WhatsApp, telefone, e-mail, Instagram); não haverá formulário nem armazenamento de dados de visitantes nesta versão, evitando necessidade de tratamento de dados pessoais (LGPD).
- **Números de impacto**: os materiais divergem quanto ao número atual de alunos (60 na apresentação institucional, 42 na comercial, "dezenas" no panfleto). Até confirmação do instituto, a página usará "60 crianças e adolescentes atendidos" (material mais recente/institucional) e as metas (100/ano; até 200 em 5 anos), com os valores facilmente ajustáveis.
- **Imagens**: serão usadas as fotos e o brasão já existentes nos materiais fornecidos; fotos da equipe e das aulas deverão ser fornecidas pelo instituto em boa resolução. Imagens de crianças pressupõem autorização de uso de imagem dos responsáveis, já obtida pelo instituto.
- **Doação online**: não haverá processamento de pagamentos ou doações na página nesta versão; o apoio financeiro é tratado via contato direto.
- **Lei de Incentivo ao Esporte / FIA**: como a validação na LIE ainda está em andamento (horizonte de 3 anos) e o tema está ligado à proposta comercial, a explicação detalhada de incentivos fiscais fica fora desta versão, junto com as cotas.
- **Conteúdo editável**: textos e números poderão ser revisados pelo instituto antes da publicação; a página não precisa de um painel de administração nesta versão.
- **Hospedagem e domínio**: o instituto providenciará (ou aprovará) um domínio e hospedagem; isso não bloqueia a especificação.
