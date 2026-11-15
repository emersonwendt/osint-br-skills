# MASINT — medições e assinaturas

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Comparação de voz, análise acústica e ENF (frequência da rede elétrica no áudio) com fim probatório são perícia oficial.** As ferramentas servem à triagem e ao indício. Trabalhar sempre em cópia do original, com hash. Dado de rede cidadã (Raspberry Shake, Safecast, Blitzortung) pode ser descartado ou corrigido pelo operador: confirmar o fato em fonte institucional (USP, USGS) antes de citar.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| Audacity | Livre | Editor de áudio com espectrograma | https://www.audacityteam.org | Editar altera o áudio: só em cópia. Verificação de atualização ativa por padrão (aviso de privacidade consultado refere-se à série 3.x) |
| Sonic Visualiser | Livre | Espectrograma em camadas, com anotação | https://www.sonicvisualiser.org | Não substitui perícia |
| Praat | Grátis (código-fonte público) | Fonética: espectrograma, pitch, formantes | https://www.fon.hum.uva.nl/praat/ | Valor só indiciário |
| USGS Earthquake Catalog | Grátis; sem conta nem chave citadas | Sismos por tempo, área, magnitude e profundidade | https://earthquake.usgs.gov/fdsnws/event/1/ | Até 20.000 eventos por consulta; página de busca não abriu: NÃO VERIFICADA |
| Centro de Sismologia da USP (RSBR) | Grátis (cadastro não citado) | Sismos no Brasil: catálogo, boletim e ondas | https://moho.iag.usp.br/eq/ ; https://moho.iag.usp.br/rq/ | Boletim defasa 2 a 3 anos; o segundo link dá acesso aos dados de ondas |
| ObsPy | Livre (Python) | Ler, filtrar e baixar dados sísmicos | https://docs.obspy.org | Exige Python |
| EarthScope (Wilber 3) | Grátis; conta obrigatória para baixar a partir de 15/12/2026 | Ondas sísmicas globais | https://ds.iris.edu/wilber3/find_event | Cotas por hora e dia desde 26/10/2026 |
| Raspberry Shake | Só não comercial | Sismo e infrassom de sensores cidadãos | https://manual.raspberryshake.org/fdsn.html | Licença veda uso comercial e redistribuição; sem controle de qualidade; defasagem de 30 min |
| Safecast | Grátis (CC0) | Radiação medida por voluntários | https://map.safecast.org | Cobertura no Brasil NÃO VERIFICADA |
| Blitzortung | Grátis para ver; uso comercial proibido | Descargas atmosféricas em tempo real | https://www.blitzortung.org/en/ | Sem arquivo para terceiros (NÃO VERIFICADO); indício, não prova |
| EURDEP | Grátis | Dose gama ambiental | https://remon.jrc.ec.europa.eu/About/Rad-Data-Exchange | Só Europa; histórico de até 35 dias |
| Sentinel-5P (Copernicus) | Grátis (cadastro para baixar não esclarecido) | Gases atmosféricos | https://dataspace.copernicus.eu | Consultar no Copernicus Browser |
| hum-catcher | Livre (MIT) | Frequência da rede elétrica no áudio (ENF) | https://github.com/sch24r/hum-catcher | Imaturo (v0.1.1, desenvolvedor único, sem validação independente); base de referência da rede brasileira (60 Hz) NÃO CONFIRMADA |

## Não use
- **Inativos**: Spek (2023), ENFormant (2023), enf-matching (2022), openenf (2023). Não há opção gratuita madura para ENF confirmada.
- **CTBTO**: dados só para Estados (NÃO VERIFICADO em página aberta).
- **INPE/ELAT** (descargas no Brasil, https://www.inpe.br/elat): página deu erro 500, acesso NÃO VERIFICADO. Não citar até conferir no navegador.
