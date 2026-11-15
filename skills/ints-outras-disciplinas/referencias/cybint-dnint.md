# CYBINT e DNINT — ameaças cibernéticas e redes

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026. Domínio, DNS, RDAP, CT (crt.sh), Shodan/Censys e Wayback já estão em **osint-infraestrutura-digital**: não se repetem aqui.

**Regra de sigilo.** Consultar um índice (hash, IP, domínio, URL já indexada) é passivo. Enviar arquivo ou URL a sandbox ou a varredura pública publica o caso e pode avisar o autor do artefato. Em caso sigiloso: consulta por hash e ferramenta local.

Geolocalização de IP é aproximada. ASN e prefixo indicam o provedor, não a pessoa. Identificar o assinante exige requisição ou ordem judicial ao provedor, com data, hora e fuso (UTC) do acesso (núcleo, seção 4).

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| CyberChef | Livre (Apache-2.0) | Decodificar e converter dados (base64, hash, XOR, regex) | https://github.com/gchq/CyberChef | Processa localmente, sem enviar ao servidor; pode rodar offline |
| RIPEstat | Grátis, sem conta | Roteamento, ASN, prefixos, WHOIS e histórico de IP | https://stat.ripe.net/docs/02.data-api/ | Acima de 1.000 consultas/dia exige registrar `sourceapp`; 8 conexões simultâneas por IP |
| Team Cymru IP-to-ASN | Grátis, sem conta | IP para ASN e prefixo, em lote | https://www.team-cymru.com/ip-asn-mapping | Dados BGP a cada 4 h; whois individual em massa é bloqueado (usar DNS); não serve para geolocalização |
| VirusTotal | Não comercial (conta e chave; 4 req/min, 500/dia) | Reputação de hash, URL e IP | https://www.virustotal.com | Só consulta; **não enviar arquivo** de caso |
| AbuseIPDB | Freemium (conta; 1.000 consultas/dia) | Reputação de IP por denúncias da comunidade | https://www.abuseipdb.com | Veda uso comercial e revenda; denúncia é indício |
| urlscan.io | Freemium | Busca em varreduras já feitas | https://urlscan.io | **Não submeter** varredura nova: expõe a URL |
| abuse.ch (URLhaus, MalwareBazaar, ThreatFox) | Grátis, "fair use"; exige Auth-Key gratuita | URLs, amostras e IOCs de malware | https://abuse.ch | Uso lucrativo pode exigir assinatura; Feodo Tracker está inoperante |
| GreyNoise Community | Freemium (conta; 50 buscas/semana) | Varredura em massa × ataque direcionado | https://www.greynoise.io | E-mail pessoal (Gmail) pode não liberar chave; sem feeds |
| AlienVault OTX (LevelBlue) | Não comercial (conta) | Pulses de IOCs, API e TAXII | https://otx.alienvault.com | EULA veda uso comercial; DNS passivo não confirmado |
| NVD API (NIST) | NÃO VERIFICADO (gratuidade não confirmada em página oficial) | CVE e vulnerabilidades | https://nvd.nist.gov/developers/start-here | CVE por versão de banner é inferência |
| MaxMind GeoLite2 | Grátis (conta e chave de licença) | Geolocalização aproximada de IP, base local | https://dev.maxmind.com/geoip/geolite2-free-geolocation-data/ | 30 downloads/dia, 1.000 consultas/dia; precisão de poucos a 1.000 km; atribuição |
| IPinfo Lite | Grátis (token; cadastro NÃO VERIFICADO) | IP para país e ASN | https://ipinfo.io/pricing | Só país; atribuição obrigatória |
| LACNIC, delegações | Grátis, sem conta | Blocos IP e ASN alocados à região | https://ftp.lacnic.net/pub/stats/lacnic/ | Arquivo diário; mostra o detentor do bloco, não o dono do site |
| bgp.tools | Grátis para consulta; monitoramento pago; conta NÃO VERIFICADO | ASN, prefixo, BGP quase em tempo real | https://bgp.tools | Exige User-Agent identificado; raspar HTML pode gerar banimento |
| Hurricane Electric BGP Toolkit | NÃO VERIFICADO (acesso público; gratuidade não declarada) | AS, prefixos, peers, RPKI | https://bgp.he.net | Limites e termos não confirmados |
| PeeringDB | Grátis | Redes, IXPs e contatos de operadores | https://www.peeringdb.com | Dado declarado pelo próprio operador; conta para API NÃO VERIFICADO |
| Robtex | Grátis na web; API 10 req/h por IP | DNS reverso, IP, ASN | https://www.robtex.com | DNS passivo NÃO VERIFICADO |
| ExoneraTor | Grátis, sem conta | O IP era relay Tor em certa data? | https://metrics.torproject.org/exonerator.html | Indica o relay, **não o usuário**; cobertura temporal NÃO VERIFICADO |
| Tor Metrics, Relay Search, Onionoo | Grátis (CC0) | Relays e bridges por IP e fingerprint | https://metrics.torproject.org | Endereços de bridges são sanitizados |
| subfinder | Livre (MIT) | Subdomínios por fontes passivas | https://github.com/projectdiscovery/subfinder | Rodar só no modo passivo |
| OWASP Amass | Livre (Apache-2.0) | Mapeamento de ativos | https://github.com/owasp-amass/amass | **Sem** `-active` e **sem** `-brute` |
| dnsx | Livre (MIT) | Resolver lista de nomes já obtidos | https://github.com/projectdiscovery/dnsx | **Sem** `-d`/`-w` (força bruta) e sem `-axfr` |
| gau / waybackurls | Livre | URLs históricas de um domínio | https://github.com/lc/gau | Consulta arquivos, não o alvo |
| waymore | Livre (MIT) | URLs históricas de Wayback, Common Crawl, OTX e URLScan | https://github.com/xnl-h4ck3r/waymore | Idem |
| DNSDumpster | Freemium (conta) | Hosts e registros DNS de um domínio | https://dnsdumpster.com | Limites NÃO VERIFICADOS em M |
| SecurityTrails | Freemium; condição NÃO VERIFICADO | DNS histórico | https://securitytrails.com | Confirmar plano antes de contar com histórico |
| BuiltWith | Freemium | Tecnologias de um site | https://builtwith.com | Stack indica fornecedor, não dono |
| Wappalyzer | Freemium (conta; 50 consultas/mês); NÃO VERIFICADO | Tecnologias de um site | https://www.wappalyzer.com | Limite não confirmado em página oficial |
| PublicWWW | Freemium (top 1 milhão grátis) | Busca reversa por código-fonte e IDs de analytics | https://publicwww.com | Cobertura limitada no plano grátis |
| ZoomEye | Freemium (conta NÃO VERIFICADO; 5 resultados/dia) | Ativos expostos já indexados | https://www.zoomeye.ai | Sem varredura sob demanda |
| web-check | Livre (MIT) | Painel de análise de site | https://github.com/Lissy93/web-check | **Só auto-hospedado** e sem `ports`, `trace-route` e `tls-connection` |
| Ahmia | Grátis (acesso aos serviços exige Tor Browser) | Busca de serviços onion indexados | https://ahmia.fi | Pode listar conteúdo ilícito: só em ambiente isolado, sem baixar nem guardar; abuso sexual infantil, encerrar e encaminhar (SaferNet/autoridade). Usar só o endereço onion divulgado em ahmia.fi (há clone falso) |
| Triage (tria.ge) | Grátis, só uso não comercial (conta) | Sandbox de malware | https://tria.ge | Envio gratuito é **público**; só amostra que já é pública |
| ANY.RUN (Community) | Grátis (conta); VM de 60 s, arquivo de 16 MB | Sandbox interativo | https://any.run | Análise privada só em plano pago; tratar como pública |
| Hybrid Analysis | Grátis (conta) | Sandbox estático e dinâmico | https://www.hybrid-analysis.com | Tratar como pública (NÃO VERIFICADO em página oficial) |
| MISP | Livre (AGPL-3.0) | Correlacionar e compartilhar indicadores | https://www.misp-project.org | Autohospedado |
| OpenCTI | Community em Apache-2.0; módulos Enterprise sob licença | Plataforma de ameaças com grafo STIX | https://github.com/OpenCTI-Platform/opencti | Arquivos com cabeçalho Enterprise não são livres em produção |
| YARA / YARA-X | YARA BSD-3-Clause; YARA-X: NÃO VERIFICADO | Regras para classificar malware | https://github.com/VirusTotal/yara-x | YARA em manutenção; YARA-X é o sucessor |
| Sigma | Regras sob DRL 1.1 | Regras de detecção em logs | https://github.com/SigmaHQ/sigma | Licença das ferramentas de conversão NÃO VERIFICADO |

## Não use
- **Sandbox gratuita com arquivo ou URL de caso sigiloso**: a submissão é pública.
- **Dado ou credencial vazada**: h8mail, GoSearch (consulta HudsonRock e ProxyNova), OsintHunter.
- **Varredura ativa, força bruta ou crawling**: Osmedeus, Photon, WhatWeb, httpx (sondagem de hosts), S3Scanner, cloud_enum, CloudBrute, Scrapy, Heritrix, NebulaOSINT.
- **Encerrados ou parados**: BGPView (encerramento só por relato de terceiro), TheHive 3 e 4 (arquivados), Feodo Tracker (conjuntos vazios).
