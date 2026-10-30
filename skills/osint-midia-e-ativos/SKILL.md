---
name: "osint-midia-e-ativos"
description: "OSINT de mídia e ativos: origem, autenticidade, metadados e geolocalização de imagens; empresas/CNPJ e beneficiário final; cripto; aeronaves e navios. Use com osint-fontes-abertas."
---

# OSINT-BR — Mídia e ativos

Parte da biblioteca OSINT-BR. Escopo, limites legais, graduação de fontes, custódia e relatório estão em **osint-fontes-abertas** — aplicar sempre. Adaptado de UseOSINT/Skills (MIT, © 2026 osint-skills contributors). Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

Limite específico: **não identificar pessoas por semelhança facial** nem usar buscadores de reconhecimento facial para identificar particulares. Pessoas que aparecem em imagens são terceiros: tarjar quando não forem objeto da pergunta.

---
## PARTE A — Imagens e vídeos

### A1. Fluxo completo (onde e quando foi feita, é autêntica?)
1. **Escopo e nível de publicação**: decidir antes que precisão será divulgada (coordenada exata ou só região).
2. **Cópia íntegra**: obter a cópia menos processada; SHA-256; somente leitura; registrar de onde veio. Nunca girar, recortar ou reabrir-salvar antes de extrair metadados.
3. **Metadados** (A2).
4. **Proveniência**: primeira publicação conhecida (A3).
5. **Geolocalização visual** (A5).
6. **Cronolocalização** (A6).
7. **Autenticidade** (A4).
8. **Graduar** local, tempo e autenticidade: confirmado (três feições independentes + teste de falsificação), provável (duas), só região, **excluído** (basta uma feição incompatível com o local alegado), não resolvido.
9. **Expressar**: coordenada + raio em metros; posição e direção da câmera separadas da posição do objeto; horário como faixa local; data como faixa; feições comparadas com links das imagens de referência; premissas.

### A2. Metadados
| Você tem | Faça |
|---|---|
| Foto baixada de rede social | Espere nada — plataformas recodificam; buscar original (A3) |
| Foto de fórum, CMS, link direto | `exiftool` completo — GPS sobrevive mais do que se imagina |
| Anexo de WhatsApp/Telegram | Enviado como foto = recodificado; como documento = geralmente intacto |
| DOCX/XLSX/PPTX | exiftool + descompactar (autores, revisões, comentários, imagens internas com EXIF) |
| PDF | exiftool + parser estrutural (Producer, revisões incrementais, anexos) |
| Foto de agência/imprensa | Blocos IPTC/XMP (crédito, legenda, local) |
| Vídeo | exiftool `-ee` + `ffprobe` |
```bash
exiftool -G1 -a -u -g1 arquivo.jpg        # tudo, agrupado
exiftool -time:all -G1 -a -s arquivo.jpg  # todos os carimbos de tempo
exiftool -gps:all -n arquivo.jpg          # GPS em graus decimais
exiftool -b -ThumbnailImage arquivo.jpg > miniatura.jpg   # miniatura pode mostrar a versão antes da edição
exiftool -r -csv -filename -datetimeoriginal -createdate -modifydate -make -model -software PASTA > triagem.csv
ffprobe -show_format -show_streams video.mp4
```
Ler: `DateTimeOriginal` (disparo) vs `CreateDate`/`ModifyDate`; `OffsetTime*`; `Make/Model/SerialNumber` (liga arquivos ao mesmo aparelho); `Software`/histórico XMP (cadeia de edição); `Author`/`LastModifiedBy` em documentos. Cuidados: ausência não prova nada; presença só prova que alguém escreveu um valor; relógio da câmera costuma estar errado; print carrega metadados do aparelho que printou; **não usar visualizadores online** (é enviar a evidência a terceiros). Rodar exiftool e ffprobe localmente (Claude Code) ou sobre arquivos enviados (Claude web/desktop).

### A3. Origem da imagem (busca reversa)
| Você tem | Comece por |
|---|---|
| Cena de rua, objeto, texto na imagem, ponto turístico | Google Lens (faz OCR — às vezes o texto já é a resposta) |
| Região específica de uma foto poluída | Bing Visual Search (recorte e repita) |
| Foto de imprensa, meme, algo possivelmente antigo | TinEye (ordena pela mais antiga, acha versões modificadas) |
| Conteúdo do Leste Europeu/Ásia Central | Yandex |
| Conteúdo chinês | Baidu |
- Recortar e espelhar; testar várias resoluções.
- "Semelhante" não é "a mesma". Primeira indexação ≠ primeira publicação: estabelecer a mais antiga com data e arquivá-la.
- Banco de imagens contamina atribuição (a "foto do CEO" de site de golpe costuma ser stock).
- Imagem gerada por IA não tem origem a encontrar.
- Enviar imagem sigilosa a buscador comercial é vazamento: avaliar antes.

### A4. Autenticidade
| Afirmação testada | Faça primeiro | Não isto |
|---|---|---|
| "Mostra o evento X no lugar Y" | Origem (A3) e geolocalização (A5) | Filtro forense — recontextualização não deixa rastro no pixel |
| "Foto não alterada" | Análise de sinal na cópia menos processada | Analisar print ou download de rede social |
| "Fulano disse isso em vídeo" | Proveniência, consistência áudio-vídeo, bordas do rosto quadro a quadro | Score de detector |
| "Gerada por IA" | Física de câmera ausente, estrutura incoerente de objetos | Veredito de detector isolado |
| "Este print é verdadeiro" | Layout, fontes, versão da interface; o registro original, se existir | Forense de imagem (prints falsos são feitos no navegador) |
- Checagens que se sustentam: sombras e iluminação coerentes, geometria e pontos de fuga, reflexos, texto legível coerente.
- ELA: alto índice de falso positivo; nunca sozinha.
- C2PA/Content Credentials: presença é informativa; ausência quase nada significa.
- Sinais duráveis de IA: incoerência estrutural que exige modelo de mundo (placas ilegíveis, arquitetura impossível, objetos fundidos). Sinais que envelhecem (dedos, dentes): checar, não apoiar-se.
- Vídeo: contêiner e encoder, perda por recodificação, sincronia labial, acústica do ambiente; extrair quadros-chave para busca reversa.
- "Não detectada manipulação" não é "autêntica". Foto real pode ser totalmente enganosa (enquadramento, encenação). Desmentido detalhado amplifica a peça original: dosar a divulgação.

### A5. Geolocalização — pistas e o caso brasileiro
Ordenar pistas antes de buscar:
1. Nomes próprios legíveis (comércio, rua, órgão), **CNPJ em fachada ou veículo**, telefones com **DDD** (dois dígitos → região), CEP.
2. Placas de veículos: padrão Mercosul (desde 2018) ou **antiga cinza com município e UF impressos** — pista fortíssima quando legível. Não usar placa para identificar pessoa.
3. Idioma e grafia (ã, õ, ç → português; Brasil × Portugal decidido por outras pistas).
4. Sinalização de trânsito brasileira (CTB/Contran); faixa amarela separa sentidos opostos, branca o mesmo sentido.
5. Infraestrutura: postes de concreto (seção duplo-T ou circular), caixas d'água de fibra azul nos telhados, muros altos com grades/concertina, calçadas em pedra portuguesa, ônibus com nome de empresa e linha.
6. Arquitetura, telhados, vegetação (cuidado: ipês, palmeiras-imperiais e eucaliptos são ornamentais/plantados em todo lugar), relevo e linha do horizonte (decisivo só com região candidata).
Fontes de imagem:
| Fonte | Quando |
|---|---|
| Google Earth (desktop) | Satélite com linha do tempo histórica (datar construção/demolição) |
| Google Street View | Boa cobertura urbana no Brasil; "máquina do tempo" com capturas datadas |
| Mapillary / KartaView | Rural e periferia sem Street View |
| Esri Wayback | Segunda linha do tempo histórica independente |
| Sentinel-2 (Copernicus) | 10 m, revisita de dias: datar mudanças (queimada, enchente, estrada nova) |
| INPE (BDQueimadas, DETER/PRODES), MapBiomas | Focos de calor datados, desmatamento, uso do solo |
| NASA FIRMS | Anomalias térmicas com horário |
| IBGE, INDE e geoportais estaduais/municipais | Ortofotos e bases oficiais, muitas vezes com resolução superior |
| SICAR (consulta pública) | Polígonos de imóveis rurais (sem expor titulares) |
| OpenStreetMap + Overpass | Consulta por tipo de feição (torres, linhas de transmissão, trilhas) |
Armadilhas: comparar imagens de datas diferentes; compressão "inventa" letras; reflexos invertem; composições; fronteiras quebram lógica de pista única; a alegação condiciona o olhar — buscar ativamente o lugar alternativo.

### A6. Cronolocalização
- Sombras: direção e comprimento com altura conhecida (SunCalc) → faixa de horário e época.
- Brasil tem quatro fusos (UTC-2 em Fernando de Noronha, UTC-3, UTC-4, UTC-5 no Acre e parte do Amazonas) e **não tem horário de verão desde 2019** — atenção a material anterior.
- Clima e eventos datáveis (chuva registrada, obra, evento público, focos de calor INPE/FIRMS).
- Data como faixa, nomeando a feição que excluiu as demais.

---
## PARTE B — Empresas e beneficiário final

### B1. Resolver a entidade jurídica
| Você tem | Caminho |
|---|---|
| Site | Rodapé, termos, política de privacidade (CNPJ costuma aparecer); conferir na Receita |
| Marca/nome fantasia | INPI (busca de marcas → titular); Receita (nome fantasia) |
| Nota, boleto, contrato | CNPJ, IE, endereço — verificar todos; não confiar no papel timbrado |
| Companhia aberta | CVM (dados.cvm.gov.br; documentos no sistema da CVM/B3) |
| Grupo | Achar uma empresa do grupo e percorrer a cadeia nos dois sentidos |

### B2. Fontes brasileiras
| Fonte | Para quê |
|---|---|
| Receita Federal — comprovante de inscrição e situação cadastral | Situação (ativa, inapta, baixada), abertura, CNAE, endereço, capital |
| Dados abertos do CNPJ (Receita) | QSA em massa (sócios, qualificação, entrada); permite cruzar sócios entre empresas |
| Juntas Comerciais (REDESIM) | Certidão simplificada e atos arquivados (contrato social, alterações) — às vezes pagos |
| CVM e B3 | Formulário de referência, controladores, fatos relevantes |
| INPI | Titular de marcas e patentes |
| Portal da Transparência (CEIS, CNEP, CEPIM) e Certidão Consolidada do TCU | Sanções e inidoneidade |
| PNCP e portais de compras | Contratos públicos (fonte de terceiros sobre porte e atividade real) |
| DOU e Querido Diário | Atos oficiais, contratos, nomeações, sanções municipais |
| Consultas processuais dos tribunais e DataJud (CNJ) | Litígios, recuperação judicial, falência |
| Agregadores privados (JusBrasil, Escavador etc.) | Pistas — confirmar na fonte primária; atenção à LGPD |
| OpenCorporates, GLEIF (LEI), ICIJ Offshore Leaks, OpenSanctions, OCCRP Aleph | Estruturas internacionais, sanções, offshore |
Beneficiário final declarado à Receita **não é público**: obtê-lo exige requisição/ordem judicial ou informação do COAF (Lei 9.613/1998). O QSA público traz CPF de sócio mascarado: usar para desambiguar, não para expor.

### B3. Sinais de empresa de fachada ("laranja", "noteira")
Abertura recente; capital social irrisório para o faturamento aparente; CNAE incompatível com a atividade; endereço de escritório virtual ou residencial compartilhado por muitas empresas; sócio único com dezenas de CNPJ ou perfil econômico incompatível (MEI); situação "inapta"; troca frequente de sócios; site genérico sem histórico (verificar no arquivo); mesmo contador/endereço/telefone de empresas sancionadas. Pontuar cada indicador com fonte; indicadores são pistas, não conclusão.

### B4. Armadilhas
Registrado ≠ verificado; dados defasados por natureza; homônimos e variações de razão social; registro errado (federal × estadual × municipal); "nada consta" pode ser busca na base errada; mídia adversa tem viés de idioma e região.

---
## PARTE C — Criptoativos

### C1. Triagem
| Você tem | Comece por |
|---|---|
| Endereço | Identificar a rede pelo formato (bc1/1/3 = Bitcoin; 0x = EVM; T… = Tron) e abrir no explorador |
| Hash de transação | Visão da transação: entradas, saídas, taxa, bloco |
| Endereço 0x | Conferir o mesmo endereço em todas as redes EVM |
| Nome ENS | Resolver e checar o registro reverso |
| Carteira de golpe/extorsão | Explorador + bases de denúncia de golpes (vítimas, primeira aparição) |
| Print de carteira | Transcrever à mão e validar checksum (endereços-isca parecidos são plantados) |
Exploradores: mempool.space e Blockchair (Bitcoin), Etherscan e similares (EVM), Tronscan (USDT na Tron — muito comum em golpes no Brasil).

### C2. Método
1. Rede e tipo de endereço.
2. Ler o endereço: entradas, saídas, primeiras e últimas transações, contrapartes.
3. Modelo mental da rede: UTXO (Bitcoin) × contas (EVM/Tron).
4. Agrupamento: **entrada comum** (forte, salvo CoinJoin); detecção de troco (fraca); reutilização de endereço.
5. **Saída para o mundo real**: depósito em exchange (endereço de depósito por cliente) — é aí que o OSINT entrega o pedido formal. Exchanges autorizadas pelo BCB (Res. BCB 519, 520 e 521/2025, em vigor desde 02/02/2026, regulamentando a Lei 14.478/2022) têm KYC e dever de cooperação.
6. Reconhecer serviços e contratos pelo padrão (mixers, pontes, DEX).
Onde a trilha quebra: CoinJoin, pools de mistura, pontes e swaps (não quebram criptograficamente, mas exigem seguir em outra rede), moedas de privacidade (parada). Análise de "taint" depois disso é escolha de modelo, não medição.
Armadilhas: envenenamento de endereço; dusting; rótulos de exploradores são declarações de terceiros; atribuição de empresas de análise não é auditável; contratos movem valor de quem nunca os tocou; horário = horário do bloco.
Grau: confirmado = fato on-chain; provável = cluster por entrada comum sem CoinJoin; não confirmado = troco, rótulo único, inferência.
Registrar em tabela: hash, rede, de, para, valor, data/hora UTC e local, fonte, grau.

---
## PARTE D — Aeronaves e embarcações
| Você tem | Resolva para | Por quê |
|---|---|---|
| Matrícula brasileira (PP-, PR-, PS-, PT-, PU-) | Consulta ao RAB da ANAC (sistemas.anac.gov.br/aeronaves/cons_rab.asp) + código ICAO hex | RAB traz situação, operador, proprietário/operador registrado; matrícula muda com venda |
| Número de voo/callsign | A aeronave daquele trecho | Callsign é por voo |
| Código ICAO hex | — | Seletor durável transmitido pelo ADS-B |
| Nome de navio | Número IMO | Nome muda; casco não |
| MMSI | IMO | MMSI muda com troca de bandeira |
| Embarcação brasileira | Tribunal Marítimo (registro de propriedade) e Capitanias dos Portos (inscrição) | Propriedade e inscrição oficiais |
- ADS-B (ADS-B Exchange, Flightradar24, OpenSky): cobertura depende de receptores; aeronaves militares/estatais e programas de privacidade somem; agregadores filtram de forma diferente.
- AIS (MarineTraffic, VesselFinder): transponder operado pela tripulação; destino e ETA são digitados à mão; **desligar o AIS é o achado**.
- Sem dado = nenhum receptor ouviu. Aeronave não é passageiro: não inferir quem estava a bordo.
- Proprietário pessoa jurídica → Parte B. Proprietário pessoa física → só canal formal.

---
## Pivôs
| Novo seletor | Vá para |
|---|---|
| Domínio/site em imagem, filing ou registro | osint-infraestrutura-digital |
| Empresa em fachada, nota, registro de aeronave/navio, exchange | Parte B |
| Carteira em site, post ou repositório | Parte C |
| Aeronave ou navio visível em imagem | Parte D |
| Pessoa natural | osint-fontes-abertas, seção 1 (limites) e 4 (canais formais) |
| Rede de entidades | osint-fontes-abertas, seção 9 (grafo) |