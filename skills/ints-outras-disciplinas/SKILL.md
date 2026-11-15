---
name: "ints-outras-disciplinas"
description: "Porta de entrada para CYBINT, DNINT, DFIR, FININT, GEOINT, IMINT, TECHINT, MASINT, MEDINT, HUMINT e SIGINT: ferramentas gratuitas e limites de cada uma. Use com osint-fontes-abertas."
---

# OSINT-BR — Outras disciplinas de inteligência

Contribuição de Alan Douglas Silva (Professor na WB Educação) à biblioteca OSINT-BR, organizada pelo Prof. Dr. Emerson Wendt. Ferramentas conferidas em página oficial ou repositório em 15/11/2026. Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

Parte da biblioteca OSINT-BR. Escopo, limites legais, graduação de fontes, custódia e relatório estão em **osint-fontes-abertas**: aplicar sempre. Esta skill não ensina técnica nova. Ela diz, para cada disciplina, **o que se faz em fonte aberta, o que não se faz** e **qual ferramenta gratuita usar**, com a condição de uso de cada uma.

## Quando usar
- A pergunta de inteligência pede mais que o OSINT clássico: ameaça cibernética, rede, exame de mídia, sanção, mapa, satélite, patente, áudio, saúde pública, entrevista, espectro de rádio.
- Você precisa saber **até onde a fonte aberta vai** antes de pedir requisição, ordem judicial ou perícia.
- Já existe skill para o assunto? Use-a primeiro (tabela de encaminhamento abaixo). Esta skill complementa.

## Regras que valem para todas as disciplinas
1. **Só fonte aberta e coleta passiva.** Sem login na plataforma-alvo, contorno de captcha, dado ou credencial vazada, reconhecimento facial, contato com o alvo, varredura ativa, força bruta, crawling ou monitoramento contínuo.
2. **Consultar índice é passivo; enviar é expor.** Enviar arquivo, imagem, URL ou endereço a serviço que publica a consulta (sandbox gratuita, nova varredura no urlscan.io, FotoForensics, archive.today, "Save Page Now" do Wayback) entrega o caso. Todo serviço on-line vê o que você consulta. Caso sigiloso: ferramenta **local**.
3. **Triagem não é perícia.** Exame de dispositivo, de voz, de imagem, de vídeo e de DNA com fim probatório é perícia oficial, com cadeia de custódia (CPP, arts. 158-A a 158-F).
4. **Saída de ferramenta é pista**, nunca prova (osint-fontes-abertas, seção 5): rótulo de carteira, score de detector, base colaborativa, resultado de IA.
5. **Capacidade técnica não é autorização.** O programa que decodifica não autoriza captar.
6. **Pessoa natural privada**: só nos casos da seção 1 do núcleo. Identificar quem está por trás de IP, conta ou carteira é tarefa dos canais formais (núcleo, seção 4).
7. **Gratuidade muda.** A coluna *Gratuidade* de cada referência vem da pesquisa de 15/11/2026. Item marcado **NÃO VERIFICADO** não foi confirmado em página oficial: conferir no navegador antes de adotar.

## Disciplina → fonte aberta → o que NÃO é fonte aberta → onde ler
| Disciplina | O que se faz em fonte aberta | O que NÃO é fonte aberta (exige requisição, ordem judicial ou perícia) | Onde ler |
|---|---|---|---|
| OSINT: domínios, DNS, IP, subdomínios, servidores expostos, páginas apagadas | Registro, CT, DNS público, arquivos, índices | Varredura, força bruta, `AXFR`; titular de IP/conta | **osint-infraestrutura-digital** |
| OSINT: empresas, beneficiário final, cripto, aeronaves e navios | Registros públicos, exploradores, ADS-B/AIS | Beneficiário final declarado à Receita; KYC de exchange | **osint-midia-e-ativos** (partes B, C, D) |
| SOCMINT: perfis, usuários, plataformas | Conteúdo público, sem login | Conta, dados cadastrais, conteúdo privado | **osint-identidade-digital** |
| CYBINT e DNINT: ameaças e redes | Reputação de hash, IP e URL em índices; BGP, ASN, relays Tor | Identificação do assinante por IP; acesso a sistema; dado vazado | `referencias/cybint-dnint.md` |
| DFIR: forense digital e mobile | Triagem em cópia, com hash | Exame de dispositivo apreendido; quebra de senha ou bloqueio | `referencias/forense-digital.md` |
| FININT: sanções, mercado, sociedades estrangeiras, cripto | Listas de sanções, CVM, BCB, GLEIF, exploradores de blockchain | Dado bancário, fiscal e do COAF | `referencias/finint.md` (+ **osint-midia-e-ativos**, partes B e C) |
| GEOINT: mapas, satélite, ambiente, transporte | SIG, imagens abertas, alertas do INPE, ADS-B, AIS | Certidão de ANAC e Marinha para prova; imagem comercial de alta resolução (paga) | `referencias/geoint.md` (+ **osint-midia-e-ativos**, A5 e D) |
| IMINT: imagem e vídeo | Ferramentas locais, busca reversa, C2PA | Laudo de autenticidade; comparação facial | `referencias/imint.md` (+ **osint-midia-e-ativos**, parte A) |
| TECHINT: equipamentos e patentes | Homologação Anatel, FCC ID, bases de patentes, desmontagens | Exame de aparelho apreendido; quebra de proteção técnica | `referencias/techint.md` |
| MASINT: sinais físicos e acústicos | Catálogos sísmicos, radiação, descargas, espectrograma | Comparação de voz, acústica e ENF com fim probatório | `referencias/masint.md` |
| MEDINT e BIOINT: saúde e genômica | Estatística agregada, cadastros institucionais, sequências públicas | Prontuário, SINAN nominal, vacinação identificada, perfil genético | `referencias/medint-bioint.md` |
| HUMINT: fontes humanas e entrevistas | Transcrição local, anotação, análise estruturada | Infiltração, identidade fictícia, contato com investigado | `referencias/humint.md` |
| SIGINT: rádio e espectro | Transmissões abertas, emissores licenciados, Wi-Fi visível | Interceptação de comunicação (Lei 9.296/1996) | `referencias/sigint.md` |

## Você tem → vá para
| Você tem | Vá para | Por quê |
|---|---|---|
| Hash, IP ou URL suspeitos | `cybint-dnint.md` | Reputação em índice, sem enviar o arquivo |
| Domínio ou site | **osint-infraestrutura-digital** | RDAP, CT, histórico já estão lá |
| IP ou ASN, rota BGP, relay Tor | `cybint-dnint.md` | Complementa o passe de IP da skill de infraestrutura |
| Disco, celular ou memória já periciados ou extraídos legalmente | `forense-digital.md` | Triagem e linha do tempo |
| Nome de empresa ou CNPJ | **osint-midia-e-ativos**, parte B | Fontes brasileiras já listadas |
| Nome em lista de sanção, empresa estrangeira, cadeia de controle | `finint.md` | Sanções, LEI, registros societários |
| Endereço de carteira | **osint-midia-e-ativos**, parte C | Método; `finint.md` traz os limites das ferramentas |
| Foto sem coordenada | **osint-midia-e-ativos**, A5; depois `geoint.md` | Pistas visuais primeiro, ferramentas depois |
| Área com queimada ou desmatamento | `geoint.md` | INPE, MapBiomas, FIRMS |
| Matrícula de aeronave ou IMO de navio | **osint-midia-e-ativos**, parte D; `geoint.md` | Registro oficial e fontes de rastreio |
| Imagem ou vídeo suspeito de edição ou IA | `imint.md` | Ferramentas locais; detector não é prova |
| Modelo de rádio, roteador ou celular | `techint.md` | Homologação e FCC ID provam o modelo, não o exemplar |
| Áudio, sismo, radiação, descarga atmosférica | `masint.md` | Espectrograma e catálogos |
| Indicador de saúde pública ou sequência de patógeno | `medint-bioint.md` | Só dado agregado |
| Entrevista, relato de fonte, hipótese concorrente | `humint.md`; núcleo, seção 5 | Apoio à análise |
| Emissor de rádio, rede Wi-Fi, gravação IQ | `sigint.md` | Identificação de emissor, sem captar conteúdo |
| Nome de usuário, e-mail, telefone | **osint-identidade-digital** | Só nos casos da seção 1 do núcleo |

## Como usar
1. **Disciplina**: ler a pergunta de inteligência (núcleo, seção 2) e escolher a linha da tabela.
2. **Escopo**: registrar alvo, limites e base legal antes de abrir qualquer ferramenta (núcleo, seção 1).
3. **Ferramenta**: abrir a referência, escolher da lista de cima para baixo (mais usadas, simples e gratuitas primeiro). Preferir a ferramenta **local** à on-line. Ler a coluna *Cuidado*.
4. **Preservar**: hash SHA-256, data e hora em UTC e local, ferramenta e versão, consulta exata (núcleo, seção 7; captura local e manifesto: **osint-preservacao-evidencias**).
5. **Graduar**: fonte e informação pelo Almirantado; o resultado da ferramenta entra como pista (núcleo, seção 5).
6. **Fechar a lacuna**: o que a fonte aberta não responde vira diligência formal (núcleo, seção 4).

## Onde dá errado
- **Gratuito não é sigiloso.** Tradutor, mapa, buscador reverso e detector veem o que você envia.
- **Ferramenta que "funciona" ainda pode ser vedada.** Decodificador de voz digital e captura de Wi-Fi de terceiros dependem de ordem judicial.
- **Triagem tratada como laudo.** Resultado de IPED, Autopsy, Praat ou detector de deepfake não substitui perícia oficial.
- **Rótulo de terceiro como fato.** Carteira rotulada, homônimo em lista de sanções e alerta de surto por notícia são indícios.
- **Dado agregado reidentifica.** Painel de saúde com poucos casos por município pode apontar pessoa: não cruzar com dado nominal.
- **Projeto parado ou encerrado.** Cada referência traz a lista "Não use" com o motivo.
- **Gratuidade vencida.** Limite, plano e termo mudam; item **NÃO VERIFICADO** exige conferência antes de entrar em rotina.

## Fonte oficial
- Lei 9.296/1996, arts. 1º e 10 (interceptação depende de ordem do juiz competente; realizá-la sem autorização é crime): https://www.planalto.gov.br/ccivil_03/leis/l9296.htm, acesso em 15/11/2026.
- Lei 13.709/2018 (LGPD), art. 5º, II (dado de saúde, genético e biométrico é sensível): https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm, acesso em 15/11/2026.
- Demais dispositivos: os já citados em **osint-fontes-abertas**.
