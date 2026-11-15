# MEDINT e BIOINT — saúde pública e genômica

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Só fontes agregadas ou de registro institucional.** Dado de saúde e dado genético individuais são dados pessoais sensíveis (LGPD, art. 5º, II: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm, acesso em 15/11/2026). O acesso depende de ordem judicial ou requisição institucional, com perícia oficial.

Painel, atlas e agregado com poucos casos por município podem reidentificar pessoa: não cruzar com dado nominal sem base legal. Notícia, alerta e print não são prova conclusiva: registrar URL, data e hora de acesso e hash, e confirmar na fonte oficial.

| Ferramenta ou fonte | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| CNES | Grátis; consulta pública sem login visível | Estabelecimentos e profissionais de saúde | https://cnes.datasus.gov.br | Pesquisa de profissional exige ao menos dois nomes; recursos não migrados em cnes2.datasus.gov.br |
| ANVISA, Sistema de Consultas | Grátis (NÃO VERIFICADO: o portal deu 403) | Produtos registrados e irregulares, AFE, BPF, bulário | https://www.gov.br/anvisa/pt-br/sistemas/sistema-de-consultas | Produtos irregulares: registros desde nov/2020; repetir o teste no navegador |
| OpenDataSUS | Grátis, sem login (CC BY-ND 3.0) | Conjuntos abertos do SUS e API | https://dadosabertos.saude.gov.br | Conferir em cada conjunto se é agregado ou microdado anonimizado |
| DATASUS TabNet | Gratuidade não declarada; sem login | Mortalidade, nascidos vivos, internações, agravos (SINAN) | https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ | Dado tabulado; tabnet.datasus.gov.br recusou conexão (NÃO VERIFICADO) |
| Observatório de Arboviroses | Grátis, sem login | Painel de dengue e outras arboviroses | https://www.gov.br/saude/pt-br/composicao/svsa/cnie/observatorio-de-arboviroses | Dado agregado; painel de SRAG só por busca (NÃO VERIFICADO) |
| OPAS PLISA e OMS GHO | Grátis; PLISA em CC BY-NC 3.0 IGO | Indicadores de saúde por país | https://www.who.int/data/gho ; https://opendata.paho.org/en | PLISA é não comercial: conferir uso em peça; sem data de atualização |
| NCBI GenBank e BLAST | Grátis, sem restrição de uso | Sequências públicas de DNA; busca por similaridade | https://www.ncbi.nlm.nih.gov/genbank/ ; https://blast.ncbi.nlm.nih.gov/Blast.cgi | Sequência, não pessoa; desde 16/06/2026 não aceita dado genômico pessoal de particular |
| STRBase (NIST) | NÃO VERIFICADO | Referência de marcadores STR forenses | https://strbase.nist.gov | Conteúdo não carregou; frequências populacionais, sem perfil de pessoa |
| ClinicalTrials.gov | Grátis (NÃO VERIFICADO: a página não carregou) | Registro de ensaios clínicos | https://clinicaltrials.gov | Termos de uso não lidos |
| CDC WONDER, ECDC, Our World in Data | Grátis (ECDC CC BY 4.0; OWID CC BY) | Estatística de saúde de EUA, Europa e global | https://wonder.cdc.gov/ ; https://atlas.ecdc.europa.eu/public/index.aspx ; https://ourworldindata.org/health | WONDER tem restrições de uso; atlas do ECDC não carregou na verificação |
| Nextstrain e GISAID | Nextstrain grátis (AGPL); GISAID grátis com cadastro e acordo | Filogenia e genômica de patógenos | https://nextstrain.org ; https://gisaid.org | GISAID veda repasse a quem não é usuário autorizado e exige créditos aos laboratórios |
| ProMED, HealthMap, BEACON, Global.health | ProMED freemium (5 artigos/mês); demais NÃO VERIFICADOS | Alertas de surto por notícias e relatos | https://promedmail.org ; https://healthmap.org/en/ ; https://beaconbio.org ; https://www.global.health | Sinal de imprensa, não confirmação oficial. Global.health traz linha-lista anonimizada, com banner desatualizado |

## Não use
- **Dado individual identificável**: prontuário, SINAN e vacinação com identificação, bancos de perfis genéticos e de DNA. Só por ordem judicial ou requisição, com perícia oficial.
- **Sequência genômica de pessoa** em serviço público de submissão.
- **Alerta de surto por notícia** como confirmação oficial.
