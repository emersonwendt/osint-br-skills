# SIGINT — transmissões abertas e emissores

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Limite legal.** Aqui só entram **transmissões abertas** e a **identificação de emissores**. Interceptar comunicação depende de ordem judicial: Lei 9.296/1996, arts. 1º e 10 (a ordem do juiz competente é exigida, e realizar interceptação sem autorização é crime): https://www.planalto.gov.br/ccivil_03/leis/l9296.htm, acesso em 15/11/2026. **Ferramentas de captura de comunicação privada não entram.** Capacidade técnica de demodular voz digital não autoriza captar comunicação privada ou de segurança pública.

Registro de sinal recebido: data e hora em **UTC**, frequência, equipamento, antena e hash do arquivo. É fonte aberta indiciária. Prova de autoria ou de uso exige diligência de campo, requisição ou perícia oficial; a consulta pública à Anatel não substitui ofício.

Salvo indicação, as ferramentas de recepção exigem **hardware SDR**.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| Anatel, Spectrum-E (licenciamento) | Grátis; sem login na página pública | Estações licenciadas: Fistel, frequência, local, antena, validade | https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php | Filtros por faixa, UF, município e raio; exporta CSV/XLSX; aviso de manutenção visto; download completo exige autocadastro |
| Signal Identification Wiki | Grátis, leitura sem conta | Catálogo de sinais com áudio e cascata | https://www.sigidwiki.com | Licença do conteúdo NÃO VERIFICADA; rodapé de 06/08/2024 |
| WiGLE | Só não comercial (conta e chave para API; busca web sem conta NÃO VERIFICADA) | Wi-Fi georreferenciado por SSID ou BSSID | https://wigle.net | Base colaborativa e desatualizável: indício, não prova |
| KiwiSDR e WebSDR (receptores públicos) | Grátis (receptores de voluntários) | Ondas curtas pelo navegador | https://www.websdr.org | Sem hardware próprio. Acesso depende de cada operador; lista do KiwiSDR NÃO VERIFICADA |
| Artemis | Livre (GPL-3.0) | Identificar sinal por filtros, com banco offline | https://aresvalley.com | Banco alinhado ao sigidwiki; sem conta |
| Inspectrum | Livre (GPL-3.0) | Analisar gravações IQ | https://github.com/miek/inspectrum | Não exige rádio; aceita metadados SigMF |
| SigMF | Grátis (CC-BY-SA 4.0) | Padrão de metadados de gravações | https://sigmf.org | Não é programa de análise |
| SDR++ | Livre (GPL-3.0) | Receptor SDR leve | https://www.sdrpp.org | Distribuição por build nightly |
| SDR# | Grátis (licença e código NÃO VERIFICADOS) | Receptor SDR para Windows | https://airspy.com/download/ | Última revisão listada: 01/01/2025 |
| Gqrx | Livre (GPL-3.0) | Receptor SDR com interface Qt | https://gqrx.dk | v2.17.7 de 27/05/2025 |
| GNU Radio | Livre (GPL-3.0) | Montar receptores e analisadores | https://www.gnuradio.org | Curva de aprendizado alta |
| readsb e dump1090-fa | Livre (GPL-3.0; GPL-2.0) | Decodificar ADS-B (1090 MHz) | https://github.com/wiedehopf/readsb ; https://github.com/flightaware/dump1090 | Exige antena; aeronave militar pode não aparecer |
| AIS-catcher | Livre (GPL-3.0) | Receber AIS de navios | https://github.com/jvde-github/AIS-catcher | Exige antena VHF |
| rtl_433 | Livre (GPL-2.0) | Sensores ISM: meteorologia, medidores, TPMS | https://github.com/merbanan/rtl_433 | Sensor de terceiro pode revelar dado pessoal: tratar com cautela |
| dumpvdl2 e acarsdec (fork f00b4r0) | Livre (GPL-3.0; GPL-2.0) | Mensagens aeronáuticas VDL2 e ACARS | https://github.com/szpajder/dumpvdl2 ; https://github.com/f00b4r0/acarsdec | Conteúdo operacional de companhia: avaliar o enquadramento legal antes de usar |
| fldigi e WSJT-X | Livre (GPL) | Modos digitais de radioamador | https://wsjtx.github.io/wsjtx/ ; https://sourceforge.net/projects/fldigi/ | Transmitir em faixa de radioamador exige outorga (não conferida); a recepção não está em questão |
| OpenWebRX+ | Livre (AGPL-3.0) | Receptor SDR acessado por navegador | https://github.com/luarvique/openwebrx | Traz demodulador de voz digital (DMR, P25): não autoriza captar comunicação |
| SDRangel | Livre (GPL-3.0) | Plataforma SDR modular | https://github.com/f4exb/sdrangel | Idem: demodulador de voz digital incluído |
| rtl_power | Livre (GPL-2.0+) | Ocupação do espectro, sem demodular conteúdo | https://github.com/osmocom/rtl-sdr | Exige RTL-SDR; wiki do Osmocom bloqueou a leitura |
| Kismet | Livre (GPL-2.0) | Inventário passivo de Wi-Fi e Bluetooth | https://www.kismetwireless.net | Exige adaptador em modo monitor; **captura de conteúdo de terceiros depende de ordem judicial** |
| Sparrow-WiFi | Livre (GPL-3.0) | Analisador de Wi-Fi e BLE | https://github.com/ghostop14/sparrow-wifi | Só varredura passiva; **não usar o plugin Falcon** |
| Wireshark | Livre (GPL-2.0) | Analisar capturas de pacotes | https://www.wireshark.org | Só captura própria ou entregue legalmente (ordem judicial, perícia); hash e custódia |
| SigDigger | Livre (GPL-3.0 pelo site; LGPL-3.0 no GitHub) | Analisador digital de sinais | https://batchdrake.github.io/SigDigger/ | Versão formal 0.3.0 de 2022; captura ao vivo exige SDR com SoapySDR |

## Não use
- **Interceptação**: decodificadores de GSM e LTE, IMSI catchers, voz troncalizada (OP25, DSD+, Trunk Recorder), pager. Só com ordem judicial.
- **Quebra de criptografia, desautenticação, jamming**: fora do catálogo.
- **Broadcastify** (NÃO VERIFICADO): retransmite feeds de segurança pública. Não adotar sem análise de base legal e dos termos de uso.
- **Arquivados**: Universal Radio Hacker, acarsdec original, OpenWebRX original; RTLSDR-Scanner (2018).
