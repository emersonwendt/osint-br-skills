---
name: "osint-preservacao-evidencias"
description: "Use para preservar página, arquivo ou vídeo de fonte aberta em cópia local, com SHA-256 e manifest.jsonl de custódia, sem expor caso sigiloso. Complementa osint-fontes-abertas (seção 7)."
---

# OSINT-BR — Preservação de evidências

Contribuição de Alan Douglas Silva (Professor na WB Educação) à biblioteca OSINT-BR, organizada pelo Prof. Dr. Emerson Wendt. Ferramentas conferidas em página oficial ou repositório em 15/11/2026. Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

Parte da biblioteca OSINT-BR. Escopo, limites, OPSEC e a **base legal da custódia** (CPP, arts. 158-A a 158-F; ABNT NBR ISO/IEC 27037) estão em **osint-fontes-abertas**, seções 1, 6 e 7: aplicar sempre, sem repetir aqui. Esta skill cobre o que vem depois da decisão de preservar: **como capturar, onde guardar, como registrar e como conferir**.

## 1. Quando usar
- Ao encontrar o que pode virar prova: preserve **antes** de analisar. Site de golpe some em horas (osint-infraestrutura-digital, seção 8, passo 1).
- Ao citar página, arquivo ou vídeo em relatório: o relatório aponta para um E-xxx do manifesto, não para a URL viva.
- Ao baixar ou receber arquivo (anexo, mídia, documento).
- **Não é para**: monitorar página no tempo, varrer um site, entrar em plataforma que exige login. Isso fica fora dos limites (ETICA.md).

## 2. Regra de sigilo (decida antes de capturar)
Caso sigiloso é o que tem grau de sigilo ou investigação em curso (osint-fontes-abertas, seção 8, "Identificação"). Na dúvida, trate como sigiloso.

| Ação | O que acontece | Caso sigiloso |
|---|---|---|
| Consultar capturas já existentes no Wayback (`web.archive.org`) | Não publica nada. O provedor vê a consulta, como em qualquer serviço on-line | Permitido; em sigilo estrito, avalie antes |
| "Save Page Now" do Wayback | **Cria captura pública** da URL investigada | **Proibido** |
| Consultar capturas já existentes no archive.today (`archive.ph`) | Não publica nada | Permitido; em sigilo estrito, avalie antes |
| **Acionar** captura nova no archive.today | **Publica** a URL investigada | **Proibido** |
| Ferramenta local (seção 3) | O dado não sai da sua máquina | Permitido |
| Site de captura ou conversão on-line | Envia a URL ou o arquivo a terceiro | Evitar: use a ferramenta local |

- **Caso sigiloso: preserve só localmente.**
- Caso aberto: faça a cópia local primeiro. Só depois, e por decisão de quem conduz o caso, envie a um arquivo público. Registre o envio em `obs` do manifesto.
- É a mesma regra da seção 7 do núcleo: consultar arquivo público é seguro; **acionar** captura nova publica a URL.
- Colar a URL do alvo em chat ou e-mail faz o serviço acessá-la (pré-visualização): não faça (núcleo, seção 6).

## 3. Roteiro de captura por situação
Antes de qualquer captura:
1. Escopo e sigilo definidos (seção 2; núcleo, seção 1).
2. Pasta do caso criada (seção 4).
3. Navegador com perfil limpo, **sem sessão logada** (núcleo, seção 6). Captura direta chega ao servidor do alvo e aparece nos logs dele.
4. Página que exige login: **pare**. Não entre, não use cookie de sessão.
5. Se houver várias requisições ao mesmo domínio, espere pelo menos 1 s entre elas.

| Você tem | Use | Por quê |
|---|---|---|
| Página simples, só texto e imagens | SingleFile (cópia legível) + `wget --warc-file` (prova da transferência) | HTML único abre em qualquer lugar; o WARC guarda a troca HTTP |
| Página com JavaScript, rolagem infinita, conteúdo que carrega ao navegar | ArchiveWeb.page; SingleFile como cópia legível | Grava o que o navegador renderizou, em alta fidelidade |
| Poucas URLs pedidas, em lote | ArchiveBox ou Browsertrix Crawler, só com as URLs pedidas | Uma configuração para o lote; veja as condições abaixo |
| Vídeo público | yt-dlp, só sem login | Baixa o vídeo e os metadados, localmente |
| Arquivo em URL (PDF, DOCX, imagem) | `wget --warc-file` | O arquivo vem com a resposta HTTP que o entregou |
| Arquivo recebido (anexo, mídia, pen drive) | Hash direto, sem abrir | O hash prova o que você recebeu, antes de qualquer alteração |
| Página que já saiu do ar | Capturas do Wayback (osint-infraestrutura-digital, seção 5) | Baixe a captura com `id_` e registre a URL da captura |

**Print de tela** entra em `capturas/` como ilustração, nunca como única evidência (núcleo, seção 7).

### 3.1 SingleFile — Livre (AGPL-3.0)
Extensão e linha de comando. Salva a página completa em um único HTML, localmente. https://github.com/gildas-lormeau/SingleFile
- **Condição**: sem WARC e sem hash próprio. O hash é por sua conta (script da seção 4).
- Grave em `capturas/`.

### 3.2 Webrecorder ArchiveWeb.page — Livre (AGPL-3.0)
Extensão de navegador que grava a navegação em alta fidelidade, local (formato WACZ). v0.17.1 (04/09/2026). https://github.com/webrecorder/archiveweb.page
- **Condição**: grava o que você navega. Navegue **só a página pedida**, sem login, e encerre a gravação ao terminar.
- Grave o arquivo gerado em `capturas/`.

### 3.3 wget `--warc-file` — Livre (GPL)
Grava o download em WARC, com digest por registro. https://www.gnu.org/software/wget/manual/wget.html
```bash
wget --version
cd capturas
wget --warc-file=evidencia-001 --page-requisites --no-parent https://exemplo.com.br/precos
```
- **Condição**: o digest interno do WARC é **SHA-1** por padrão. Registre também o **SHA-256** do arquivo WARC pelo script.
- O WARC é a evidência. Os arquivos soltos que o wget cria ao lado são cópia de trabalho.
- Confira o nome e a extensão que o wget gravou antes de registrar.
- Para um arquivo único, use a mesma opção com a URL do arquivo, dentro de `raw/`.

### 3.4 ArchiveBox — Livre (MIT)
Arquivador web auto-hospedado (HTML, PDF, mídia). v0.9.77 (27/10/2026). https://github.com/ArchiveBox/ArchiveBox
- **Condição**: **desative o envio ao archive.org, se houver, antes da primeira captura**: enviar a URL a um serviço público viola a seção 2. A verificação de 15/11/2026 não detalhou a opção. Confira na documentação oficial como desligar e teste com URL de exemplo.
- Registre no manifesto os arquivos que ele gerar para a URL.

### 3.5 Browsertrix Crawler — Livre (AGPL-3.0)
Crawler de alta fidelidade, em Docker. https://github.com/webrecorder/browsertrix-crawler
- **Condição**: faz varredura recursiva no alvo. Use **só nas URLs pedidas, com profundidade limitada à página pedida**. A opção que limita escopo e profundidade está na documentação oficial: confira e teste antes. Sem limite configurado, não rode.
- Crawling livre, monitoramento e varredura estão fora do escopo (ETICA.md).

### 3.6 yt-dlp — Livre (Unlicense)
Baixa vídeo e metadados de YouTube, Facebook, Instagram, TikTok e X, localmente. Release 2026.10.26. https://github.com/yt-dlp/yt-dlp
```bash
yt-dlp --version
yt-dlp "https://exemplo.com.br/video/123"
```
- **Condição**: **sem login**. Instagram, Facebook e X tendem a exigir cookies do navegador (não verificado). Se exigir, **pare**: usar cookies é entrar na plataforma-alvo.
- Alguns extratores estão marcados como quebrados. Se falhar, registre `resultado: "falha"` e não contorne.
- Para salvar também os metadados, veja `yt-dlp --help`. Grave tudo em `raw/`.
- Depois, `ffprobe` e `exiftool` locais (osint-midia-e-ativos, A2). Não use visualizador de metadados on-line.

### 3.7 Arquivo baixado ou recebido
1. Grave em `raw/` e calcule o hash **antes de abrir**.
2. Marque como somente leitura: `attrib +R arquivo` (Windows) ou `chmod a-w arquivo` (Linux e macOS). Evita acidente, não é proteção forense.
3. Trabalhe em **cópia**; o original fica intocado (núcleo, seção 7).
4. Arquivo suspeito de malware: não o envie a sandbox nem ao VirusTotal. No VirusTotal, só **busca** pelo hash, conforme a verificação de 15/11/2026.

### 3.8 Outras ferramentas do catálogo
- **hashdeep** (livre, domínio público): calcula e audita hashes de pastas inteiras (seção 5). https://github.com/jessek/hashdeep
- **Linkwarden** (livre, AGPL-3.0, auto-hospedado): favoritos com cópia em PDF, HTML e captura de tela. https://github.com/linkwarden/linkwarden. Condição de envio externo **não verificada**: confirme antes de usar em caso sigiloso.

## 4. Pasta do caso e manifest.jsonl
```
evidencias/<caso>/
├── raw/        bruto como recebido (arquivo baixado, vídeo, JSON, saída de ferramenta); nunca editado
├── capturas/   HTML do SingleFile, WARC/WACZ, print de página inteira
├── notas/      análise, decisões, pivôs descartados, progresso.md
└── manifest.jsonl
```
- Nomes sem espaço, com data: `20261115_exemplo-precos.html`. **Depois de registrado, o arquivo não muda de nome nem de lugar**: o manifesto guarda o caminho.
- Uma linha por artefato, com estas chaves:

| Chave | O que registrar |
|---|---|
| `id` | `E-001`, `E-002`… (o script atribui) |
| `url`, `titulo`, `status_http` | URL consultada, título da página, código HTTP observado |
| `coletado_em_brt`, `coletado_em_utc` | Horário da coleta, com fuso (o script grava) |
| `publicado_ou_atualizado_em` | Data que a **fonte** informa; captura não é data de publicação |
| `ferramenta`, `versao`, `plano` | Ferramenta, versão e plano: `gratuito`, `freemium` ou `conta` |
| `comando` | Comando exato. **Nunca** inclua chave de API ou senha |
| `seletor_origem` | Seletor ou E-xxx de onde esta coleta partiu |
| `sha256`, `arquivos` | SHA-256 completo; caminho relativo do arquivo |
| `resultado` | `ok`, `vazio`, `falha` ou `bloqueada` |
| `obs` | Observação. Envio a arquivo público, hora real da captura, ressalvas |

**Negativo também é evidência.** Registre com `resultado: "vazio"` e `obs` no formato "não encontrado em `<fonte>`, com `<consulta>`, em `<data>`". Nunca como prova de inexistência. Se houver print ou saída da busca vazia, registre o arquivo junto.

### Script `scripts/manifesto.py`
Python 3.10+, só biblioteca padrão, **sem rede**. Lê os arquivos e **só acrescenta linhas** ao manifesto; nunca altera nem apaga evidência. Não é pacote nem serviço: é um arquivo único, com comentários, que se lê em poucos minutos.

**Registrar** (logo após gravar o arquivo):
```bash
python scripts/manifesto.py registrar evidencias/caso-exemplo capturas/20261115_exemplo-precos.html --url https://exemplo.com.br/precos --status-http 200 --ferramenta SingleFile --versao "<versão>" --comando "<comando exato>" --seletor-origem exemplo.com.br
```
- Um registro por arquivo, com códigos seguidos. O horário é o do **registro**, em Brasília e UTC.
- Caminho relativo vale a partir de onde você está ou, se não existir, a partir da pasta do caso. O arquivo precisa estar **dentro** da pasta do caso.
- Arquivo já registrado é **recusado**: nova captura, novo nome.
- Negativo, sem arquivo (exige `--obs`):
```bash
python scripts/manifesto.py registrar evidencias/caso-exemplo --resultado vazio --url https://exemplo.com.br/removida --obs "não encontrado em Wayback, com a URL indicada, em 15/11/2026"
```
- Opções: `--url`, `--titulo`, `--status-http`, `--publicado-em`, `--ferramenta`, `--versao`, `--plano`, `--comando`, `--seletor-origem`, `--resultado`, `--obs`.
- Se faltar a base de fusos (Windows sem `tzdata`), usa -03:00 fixo e avisa. Para o fuso nomeado: `python -m pip install tzdata`.

**Conferir** (seção 5):
```bash
python scripts/manifesto.py conferir evidencias/caso-exemplo
```
Saída de cada linha: `ÍNTEGRO`, `DIVERGENTE`, `AUSENTE`, `SEM ARQUIVO` (negativo) ou `INVÁLIDO`. Código de saída **0** se tudo confere; **1** se houver divergente, ausente ou inválido; **2** se a pasta ou o manifesto não puderem ser lidos.

Como confirmar que funcionou: rode `registrar`, depois `conferir` (deve dar código 0 e `ÍNTEGRO`), e compare o hash com `Get-FileHash -Algorithm SHA256 arquivo` (Windows) ou `sha256sum arquivo` (Linux).

## 5. Conferir a integridade depois
Rode `conferir` em quatro momentos: antes de citar a evidência no relatório; antes de entregar; depois de copiar ou compactar a pasta; ao receber o caso de outra pessoa.

| Resultado | O que fazer |
|---|---|
| `ÍNTEGRO` | Nada. Anote a data da conferência em `notas/` |
| `DIVERGENTE` | **Não** corrija o manifesto nem substitua o arquivo. Descubra o motivo (arquivo aberto e salvo, cópia interrompida, antivírus). Recupere o original de cópia de segurança. Registre a ocorrência em `notas/` |
| `AUSENTE` | Procure o arquivo (movido? renomeado?). Se foi perdido, recapture com **novo E-xxx** e explique no relatório |
| `INVÁLIDO` | Linha fora do padrão: preserve o manifesto como está e corrija em cópia, documentando |

- **Lote grande**: hashdeep calcula e audita pastas inteiras com SHA-256; os modos estão em `hashdeep -h`. Última versão 4.4; o último push foi em 20/09/2025, com poucas atualizações. É conferência adicional; o `manifest.jsonl` continua sendo o registro.
- O manifesto prova que o arquivo é o mesmo **desde o registro**. Não prova que a origem é autêntica nem que ninguém mexeu antes. Ao entregar, informe também o SHA-256 do próprio `manifest.jsonl`.
- No relatório, a tabela mostra os 12 primeiros caracteres do hash; o completo fica no manifesto (núcleo, seção 8).
- Coleta feita por ferramenta ou por IA precisa de revalidação humana antes de uso probatório (núcleo, seção 7). O script registra; quem confere é você.

## 6. Onde dá errado
- **Registrar tarde**: o script grava a hora do registro, não a da captura. Se registrou depois, escreva a hora real em `obs`.
- **Relógio da máquina errado**: toda hora do manifesto sai errada. Confira o horário do sistema antes de capturar.
- **Hash só no print**: print sem original (HTML, WARC) é ilustração.
- **WARC com SHA-1**: o digest interno do wget não basta. Registre o SHA-256 do arquivo.
- **Arquivo aberto e salvo**: Word, visualizador de imagem ou antivírus podem alterar o arquivo. Calcule o hash antes de abrir.
- **Renomear ou mover depois de registrar**: o manifesto passa a apontar para o vazio (`AUSENTE`).
- **Editar o manifesto à mão**: apaga a credibilidade da cadeia. Correção vai em linha nova ou em `notas/`.
- **Captura logada**: sessão do navegador mostra conteúdo diferente do público e pode expor dados da conta usada. Perfil limpo, sem login.
- **ArchiveBox com envio ao archive.org ligado**: publica a URL investigada. Teste antes do caso.
- **Crawler sem limite**: vira varredura do alvo. Só as URLs pedidas.
- **Comando com chave**: `--comando` vai para o manifesto, que será anexado ao relatório. Mascare segredos.
- **Dois registros ao mesmo tempo**: o script não trava o manifesto. Uma pessoa por vez por pasta.
- **Pasta em nuvem sincronizada** (OneDrive, Drive): o caso sigiloso sai da máquina. Guarde em disco local ou em local autorizado.
- **Ferramenta fora desta lista**: faça antes a checagem de "Ferramenta fora das skills" (núcleo, seção 10).

## 7. Não use
| Ferramenta | Motivo |
|---|---|
| Captura nova no archive.today em caso sigiloso | Publica a URL investigada |
| "Save Page Now" do Wayback em caso sigiloso | Cria captura pública |
| Hunchly | Pago; fora do critério gratuito |
| Scrapy, Heritrix | Crawling |
| changedetection.io, Visualping como "preservação" | É monitoramento contínuo, não preservação |

Em caso aberto, enviar a arquivo público é decisão de quem conduz, com registro em `obs`.

## 8. Ambiente de execução
- **Claude Code (máquina local)**: as ferramentas e o script rodam no seu computador. Confira com `where` (Windows) ou `which` (Linux) e peça confirmação antes de instalar algo. O tráfego sai do IP local (núcleo, seção 6).
- **Claude (web/desktop)**: o ambiente de código na nuvem não captura páginas do alvo e não guarda o caso. Use-o para gerar os comandos e conferir arquivos enviados; rode a captura e o registro na sua máquina.
