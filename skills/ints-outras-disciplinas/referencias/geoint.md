# GEOINT — mapas, satélite, ambiente e transporte

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026. Complementa **osint-midia-e-ativos**: pistas visuais e fontes de imagem em A5, cronolocalização em A6, aeronaves e embarcações na parte D. Aqui entram as ferramentas e suas condições.

**Sigilo.** Todo mapa on-line recebe o endereço, a coordenada ou o IP digitado. Para local investigado, usar **QGIS offline** com dados do IBGE e extratos do OSM. Street View, Earth e Wayback registram a consulta. Captura de mapa ou satélite é indício: registrar data e hora, URL, data da imagem e hash.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| QGIS | Livre (GPLv2+) | SIG completo, offline | https://www.qgis.org | Local; só camadas web (XYZ/WMS) enviam a área a terceiro |
| OpenStreetMap | Grátis (ODbL) | Base cartográfica colaborativa | https://www.openstreetmap.org | Atribuição obrigatória; busca e IP chegam à OSMF |
| IBGE Geociências | Grátis, sem cadastro | Malhas territoriais, setores, cartas, nomes geográficos | https://geoftp.ibge.gov.br | Baixar e usar offline evita envio; portal ibge.gov.br deu 403 (NÃO VERIFICADO) |
| Google Earth Pro | Grátis (preço NÃO VERIFICADO) | Globo 3D com imagens históricas e KML | https://www.google.com/earth/about/versions/ | **Download encerra em 25/06/2027**: guardar instalador e versão no laudo; termos limitam reuso |
| Google Street View | Grátis, sem conta | Imagens 360° com datas anteriores | https://www.google.com/streetview/ | Envia o local ao Google; termos proíbem download em massa |
| Mapillary | Grátis (conta para alguns serviços; CC BY-SA; API com token) | Imagens de rua colaborativas | https://www.mapillary.com | Operado pela Meta; envio a terceiro |
| KartaView | Grátis (CC BY-SA 4.0) | Alternativa ao Mapillary | https://kartaview.org | Site não carregou; "ativo" só por fonte secundária: NÃO VERIFICADO |
| Esri World Imagery Wayback | Grátis para navegar; termos Esri (gratuidade NÃO VERIFICADA na página) | Versões do mapa de satélite desde 2014 | https://livingatlas.arcgis.com/wayback/ | Envia a consulta à Esri |
| Bellingcat OSM Search | Grátis (licença e conta NÃO VERIFICADAS) | Feições OSM próximas entre si, para foto sem coordenada | https://osm-search.bellingcat.com | Termos digitados vão a Mapbox e Firebase; há auto-hospedagem (~700 GB) |
| Overpass Turbo | Grátis | Consultas ao OSM por tipo de feição | https://overpass-turbo.eu | Consulta vai a terceiro |
| SunCalc | Grátis | Posição do sol e sombras | https://www.suncalc.org | Resultado é faixa de horário |
| ShadeMap | Freemium (preço NÃO VERIFICADO) | Sombras por data e hora | https://shademap.app | Envio do local a terceiro NÃO VERIFICADO |
| Nominatim | Grátis (até 1 req/s) | Geocodificação sobre o OSM | https://nominatim.openstreetmap.org | **Nunca** endereço de investigado: envia a terceiro |
| uMap | Livre (AGPLv3) | Mapas temáticos sobre OSM | https://umap-project.org | Na instância pública o mapa fica em terceiro; para sigilo, auto-hospedar |
| Kepler.gl | Livre (MIT) | Muitos pontos e rotas | https://kepler.gl | Processamento local e mapas-base de terceiros NÃO VERIFICADOS |
| GRASS GIS | Livre (GPL-2.0+) | Geoprocessamento raster e vetorial | https://grass.osgeo.org | Curva de aprendizado alta |
| INPE TerraBrasilis (PRODES e DETER) | Grátis (CC BY-SA 4.0), sem conta | Desmatamento anual e alertas | https://terrabrasilis.dpi.inpe.br | DETER Pantanal e Amazônia não florestal é experimental; área mínima e defasagem próprias |
| INPE Queimadas | Grátis, CSV sem login | Focos de calor por estado, bioma e município | https://terrabrasilis.dpi.inpe.br/queimadas/portal/ | Foco de calor não é incêndio confirmado. Portal migrou de queimadas.dgi.inpe.br |
| MapBiomas | Grátis (CC BY 4.0) | Uso e cobertura do solo desde 1985 | https://brasil.mapbiomas.org | Landsat 30 m; GeoTIFF suspenso, dados no Earth Engine |
| MapBiomas Alerta | Grátis (cadastro NÃO VERIFICADO como obrigatório) | Laudos de desmatamento com imagens de antes e depois | https://plataforma.alerta.mapbiomas.org | Alerta surge 30 a 180 dias após a detecção; laudo em lote exige vínculo institucional |
| Copernicus Browser (Sentinel) | Grátis | Imagens de 10 m, revisita de dias | https://browser.dataspace.copernicus.eu | Revisita e nuvens limitam o que se vê |
| NASA FIRMS | Grátis; Earthdata Login para baixar | Focos de calor quase em tempo real | https://www.earthdata.nasa.gov/data/tools/firms | Suomi NPP parou: usar NOAA-20 ou NOAA-21 |
| NASA Worldview | Grátis; login só para baixar | Imagens diárias globais | https://worldview.earthdata.nasa.gov | Contexto regional, não alvo urbano |
| INPE Programa BIG | Grátis (login NÃO VERIFICADO) | CBERS e Amazonia-1 | https://data.inpe.br/big/ | Portal experimental |
| USGS EarthExplorer | Grátis (conta para baixar) | Landsat e outros acervos | https://earthexplorer.usgs.gov | Landsat 30 m, revisita de 16 dias |
| Google Earth Engine | Só não comercial (conta e projeto Google Cloud) | Análise geoespacial em nuvem | https://earthengine.google.com/noncommercial/ | Enquadramento de polícia civil NÃO VERIFICADO; uso governamental operacional é cobrado |
| Global Nature Watch | NÃO VERIFICADO | Alertas de perda de vegetação | https://globalnaturewatch.org | Ex-Global Forest Watch (domínio antigo redireciona) |
| Vantor Open Data (ex-Maxar) | Só não comercial (CC BY-NC 4.0) | Imagens de alta resolução de desastres | https://vantor.com/company/open-data-program | Só eventos ativados; não serve para local livre |
| ESA SNAP | Livre (GPL-3) | Processar Sentinel, Landsat e radar | https://step.esa.int/main/download/snap-download/ | Curva de aprendizado |
| ANAC, RAB | Grátis, sem conta | Aeronave por matrícula | https://aeronaves.anac.gov.br/aeronaves/cons_rab.asp | O endereço antigo (sistemas.anac.gov.br) redireciona; retorno de proprietário NÃO VERIFICADO. Prova: certidão da ANAC |
| Marinha (DPC), documentos válidos | Grátis, sem login | Embarcação por IMO, inscrição ou nome | https://dpc1.marinha.mil.br/sisgevi/consultainternet/relat_documentos_validos_internet_criterio_selecao.asp | Exige digitar código exibido na página; consulta por CPF/CNPJ NÃO VERIFICADA. Prova: certidão da Marinha |
| Equasis | Grátis (cadastro) | Segurança e histórico de navios e empresas | https://www.equasis.org | Captcha e API NÃO VERIFICADOS |
| OpenSky Network | Grátis com conta (anônimo limitado) | ADS-B com trajetos e histórico | https://opensky-network.org | 400 créditos/dia anônimo, 4.000 com conta; só OAuth2 |
| airplanes.live | Só uso pessoal não comercial | ADS-B comunitário | https://airplanes.live | API de 1 req/s; condições NÃO VERIFICADAS (página deu 403) |
| adsb.lol | Grátis (preço não declarado) | Dados ADS-B brutos diários | https://www.adsb.lol | Chave, limites e licença NÃO VERIFICADOS |
| ADS-B Exchange | Mapa NÃO VERIFICADO; API e histórico pagos | ADS-B sem filtro | https://globe.adsbexchange.com | Histórico só por contrato |
| Flightradar24 | Freemium (7 dias de histórico no grátis) | Rastreio e reprodução de voos | https://www.flightradar24.com | Plano Business: 3 anos ou 730 dias (fontes conflitam) |
| FlightAware | Freemium | Status de voos | https://www.flightaware.com | AeroAPI Personal: sem histórico, só uso pessoal ou acadêmico |
| VesselFinder e MarineTraffic | Freemium | Mapa AIS | https://www.vesselfinder.com ; https://www.marinetraffic.com | VesselFinder grátis: trajeto de 1 dia. MarineTraffic: limites NÃO VERIFICADOS. Destino e ETA são digitados à mão |
| Global Fishing Watch | Só não comercial (conta e token) | Atividade pesqueira e identidade de embarcações | https://globalfishingwatch.org/our-apis/ | Limites e profundidade histórica NÃO VERIFICADOS |

## Não use
- **Planet NICFI e Sentinel Hub EO Browser**: encerrados ou substituídos (usar Copernicus Browser).
- **What3words**: usar latitude e longitude em peça (algoritmo e licença NÃO VERIFICADOS). **Wikimapia**: conteúdo não validado.
- **Imagem comercial de alta resolução**: paga (Soar a 50 cm; Apollo Mapping por cotação, gratuidade da busca NÃO VERIFICADA).
- Posição de rastreador não é prova: registrar UTC e URL e requisitar certidão à ANAC ou à Marinha.
