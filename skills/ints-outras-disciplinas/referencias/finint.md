# FININT — sanções, mercado, sociedades estrangeiras e criptoativos

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Dados bancários, fiscais e relatórios do COAF não são fonte aberta.** Dependem de afastamento de sigilo por ordem judicial ou de requisição ou intercâmbio institucional. As ferramentas abaixo servem à triagem e à escolha de alvos de diligência.

Não se repete aqui o que **osint-midia-e-ativos** já traz: CNPJ, QSA, Juntas, INPI, CEIS/CNEP, PNCP (parte B) e o método de rastreio de cripto (parte C). Aqui entram as condições de uso das demais fontes.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| Banco Central: dados abertos, IF.data, consulta de PAS | Grátis, sem login observado; relação de instituições em ODbL | Instituição autorizada, balancetes, situação de processo sancionador | https://dadosabertos.bcb.gov.br ; https://www3.bcb.gov.br/ifdata/ | PAS exige o número do processo e mostra só os atos; lista oficial de PSAV NÃO VERIFICADA |
| CVM, dados abertos | Grátis (ODbL) | Fundos, companhias, regulados, processos sancionadores | https://dados.cvm.gov.br | Sancionadores: só os que chegaram à citação; consultas pontuais em tela NÃO VERIFICADAS |
| GLEIF (busca de LEI) | Grátis, sem registro | Entidade jurídica e relações de controle | https://search.gleif.org | Só entidades com LEI; termos e licença NÃO VERIFICADOS |
| OpenSanctions | Freemium: busca e lote grátis, sem conta, uso não comercial (CC BY-NC 4.0) | Sanções, PEPs e pessoas de interesse agregados | https://www.opensanctions.org | **Gratuidade para a polícia NÃO confirmada** (chave gratuita só para jornalismo, ONGs, pesquisa e instituições da Ucrânia, Geórgia e Moldávia): consultar o suporte. Triagem de conformidade é uso comercial |
| OFAC Sanctions List Search | Grátis, sem conta | Lista SDN dos EUA | https://sanctionssearch.ofac.treas.gov ; https://ofac.treasury.gov/sanctions-list-service | Lista de outro país, sem efeito direto no Brasil; o segundo link traz os arquivos |
| Lista consolidada do CSNU | Grátis | Sanções do Conselho de Segurança da ONU | https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list ; https://scsanctions.un.org/resources/xml/en/consolidated.xml | O segundo link é o arquivo XML; lista é de organismo internacional, conferir a internalização no Brasil na fonte oficial |
| ICIJ Offshore Leaks | Grátis (ODbL; conteúdo CC BY-SA 3.0, citar o ICIJ) | Entidades, intermediários e beneficiários offshore | https://offshoreleaks.icij.org | Dados até 2020; **presença de nome não indica ilícito** |
| OpenCorporates | Freemium (login gratuito NÃO VERIFICADO); API paga | Registros societários de mais de 140 jurisdições | https://opencorporates.com | Cobertura do Brasil NÃO VERIFICADA (para CNPJ, usar a Receita); bloqueia ritmo de acesso alto |
| SEC EDGAR | Grátis, sem conta | Documentos de empresas listadas nos EUA | https://www.sec.gov/edgar/search/ | Máximo de 10 req/s, com User-Agent identificado; sem empresas só brasileiras |
| OCCRP Aleph | Restrito (conta; jornalistas, pesquisadores e ativistas: NÃO VERIFICADO) | Registros societários e documentos de investigação | https://aleph.occrp.org | Polícia não é público declarado; site deu 403 |
| mempool.space, Etherscan, Blockchair, Tronscan | Etherscan: API grátis com chave (3 chamadas/s, 100 mil/dia); Blockchair: chave grátis só não comercial e acadêmica; demais NÃO VERIFICADO | Endereços e transações de Bitcoin, Ethereum, Tron e outras | https://mempool.space ; https://etherscan.io ; https://blockchair.com ; https://tronscan.org | Rótulo de carteira é declaração do serviço. Blockchair e Tronscan deram 401 e 403 na verificação |
| WalletExplorer | Grátis (preço não informado) | Agrupamento de carteiras Bitcoin | https://www.walletexplorer.com | Só Bitcoin; atualizado até o bloco 975712 (13/11/2026) |
| Chainabuse | Busca declarada aberta; conta NÃO VERIFICADA | Denúncias de golpes com cripto | https://www.chainabuse.com | Operado pela TRM Labs; denúncia é relato de terceiro |
| Arkham e Breadcrumbs | Freemium; limites NÃO VERIFICADOS | Rótulos e grafos de carteiras | https://arkm.com ; https://www.breadcrumbs.app | Deram 403; rótulo de terceiro é indício e exige confirmação por perícia |
| GraphSense | Livre (MIT), instalação própria | Grafo de transações, agrupamento e etiquetas | https://graphsense.org | Exige Cassandra e nó do blockchain; cobre BTC, BCH, LTC, ZEC, ETH e TRX |

## Não use
- **Serviços baseados em dados vazados de clientes**: fora por licitude e LGPD.
- **Aleph de código aberto**: descontinuado (último commit em 19/12/2025).
- **Chainalysis, TRM, Elliptic e Crystal**: só pagos, fora do escopo gratuito.

Coincidência de nome em lista de sanção é indício e gera falso positivo por homônimo. Registrar fonte, data e hash da captura. Exchange autorizada pelo BCB é o ponto de saída para a requisição (núcleo, seção 4).
