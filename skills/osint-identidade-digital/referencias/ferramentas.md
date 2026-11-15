# Ferramentas de identidade digital, por seletor

Material de apoio da skill **osint-identidade-digital**, com ferramentas conferidas em página oficial ou repositório em 15/11/2026. As tabelas seguem a ordem de prioridade do roteiro (mais usadas, simples e gratuitas primeiro). Gratuidade e limites mudam: confirme no site antes de adotar em rotina.

Marcas: **[L]** roda na sua máquina · **[C]** exige cadastro na própria ferramenta (nunca conta do alvo) · **[F]** freemium · **[⚠]** envia o seletor a terceiro · **[M]** consulta manual por causa de captcha · **\*** gratuidade não confirmada em página oficial · **NV** não verificado em página oficial.

Sintaxe e opções: use o README da versão instalada e registre o comando exato no manifesto (osint-preservacao-evidencias). Esta tabela não reproduz opções de linha de comando que a conferência não abriu.

## 1. Username
| Ferramenta | Gratuidade | O que faz | URL | Condição e alerta |
|---|---|---|---|---|
| Maigret [L] | Livre (MIT) | Username em milhares de sites, com extração de perfil | https://github.com/soxoj/maigret | Resultado nasce não confirmado |
| Sherlock [L] | Livre (MIT) | Username em centenas de redes | https://github.com/sherlock-project/sherlock | Idem |
| Blackbird [L] | Livre (licença não declarada) | Username e e-mail em 600+ sites | https://github.com/p1ngul1n0/blackbird | **IA opcional desligada.** Usa a lista WhatsMyName, arquivada em 09/11/2026 e congelada |
| Social Analyzer [L] | Livre (AGPL-3.0) | Perfis em cerca de 1.000 sites, com metadados | https://github.com/qeeqbox/social-analyzer | **Desligar "Special Detections"** |

## 2. E-mail
| Ferramenta | Gratuidade | O que faz | URL | Condição e alerta |
|---|---|---|---|---|
| Gravatar, API de perfis [⚠] | Grátis; sem chave 100 req/h, com chave 1.000 req/h (só o endpoint de perfis); conta só para obter a chave | Perfil público ligado ao hash do e-mail | https://docs.gravatar.com/api/profiles/rest-api/ | Hash **SHA-256** do e-mail normalizado; a documentação diz "Don't use MD5!". Sem chave, a resposta omite campos (fuso, idiomas, links, contatos) e limita contas verificadas a 4. Envia o hash ao Gravatar |
| Epieos [C][F][⚠] | Freemium (conta) | Busca reversa de e-mail (o catálogo cita também telefone) | https://epieos.com | Preço só em fonte secundária. O PLAYBOOK não o põe na linha de telefone: confirme antes de usar nesse seletor |
| Holehe [L] | Livre | E-mail cadastrado em sites | https://github.com/megadose/holehe | Sem commit desde 09/2024. Só módulos que não disparem mensagem ao titular; a verificação não indica quais: NV |
| GitHub Search | Grátis; conta gratuita para buscar código | Usuários, commits e código em repositórios públicos | https://docs.github.com/en/rest/search/search (web: https://github.com/search) | Código exige login, mesmo em repositório público: **fora**. Commits: só branch padrão, `author-email:` e `committer-email:` com e-mail completo; busca por 10 req/min sem login e 30 com login. Usuários: `in:email` só acha e-mail público. Login na busca web de usuários e commits: NV |
| Hunter.io [C][F] | Freemium (50 créditos/mês; conta) | E-mails corporativos de um domínio | https://hunter.io | Só domínio corporativo |

## 3. Telefone
| Ferramenta | Gratuidade | O que faz | URL | Condição e alerta |
|---|---|---|---|---|
| ABR Telecom, Consulta Número [M] | Grátis (licença NV) | Operadora atual e portabilidade | https://consultanumero.abrtelecom.com.br | reCAPTCHA: só manual, feito por você |
| PhoneInfoga [L] | Livre (GPL-3.0) | País, operadora e tipo de linha | https://github.com/sundowndev/phoneinfoga | "Stable but unmaintained": usar só o scanner local |

## 4. Perfil público em plataforma
| Ferramenta | Gratuidade | O que faz | URL | Condição e alerta |
|---|---|---|---|---|
| yt-dlp [L] | Livre (Unlicense) | Vídeo e metadados de YouTube, Facebook, Instagram, TikTok e X | https://github.com/yt-dlp/yt-dlp | Login não é requisito nas listagens; aceita cookies do navegador, e Instagram, Facebook e X tendem a exigi-los (NV): **sem cookies**. Extratores `instagram:user`, `tiktok:tag`, `tiktok:sound` e `tiktok:effect` "Currently broken". LinkedIn só com eventos e Learning. Release 2026.10.26 |
| Instaloader [L] | Livre (MIT) | Posts e metadados do Instagram | https://github.com/instaloader/instaloader (docs: https://instaloader.github.io/) | Perfil público baixa sem login; hashtags, stories e perfil privado **exigem login: fora**. Documentação cita erro 429 e limites mais rígidos no acesso anônimo. Projeto não oficial. Release v4.16 (26/10/2026) |
| gallery-dl [L] | Livre (GPL-2.0) | Mídia de Instagram, Facebook, X e TikTok (sem LinkedIn e YouTube) | https://codeberg.org/mikf/gallery-dl (espelho: https://github.com/mikf/gallery-dl) | A tabela oficial lista autenticação por cookies; na prática o login tende a ser necessário (NV): **sem cookies**. Desenvolvimento no Codeberg. Release 1.32.20 (data NV) |
| Zeeschuimer + 4CAT [L] | Livre (MPL 2.0) | Extensão do Firefox captura enquanto você navega; 4CAT analisa | https://github.com/digitalmethodsinitiative/zeeschuimer ; https://github.com/digitalmethodsinitiative/4cat | Captura só o que o navegador recebe: navegue sem login. Instagram (posts e reels), TikTok, X, Threads; LinkedIn via Zeeschuimer consta no 4CAT (NV na prática). Análise exige instância 4CAT própria (Docker) |
| Meta Ad Library | Grátis | Anúncios ativos no Facebook e no Instagram | https://www.facebook.com/ads/library/ (visão geral: https://transparency.meta.com/researchtools/ad-library-tools) | Login e cobertura no Brasil NV (a página do Facebook retornou 403). Anúncios sociais, eleitorais e políticos ficam 7 anos. API exige autorização. O provedor vê a consulta |
| Google Ads Transparency Center | Grátis | Anunciantes verificados e seus anúncios no Google, YouTube e Display | https://adstransparency.google.com/ | Busca por nome ou site, com filtro de data e região. Login não indicado como requisito. Seção eleitoral com Brasil: NV |
| Social Blade [F]\* | Freemium (preços NV) | Histórico de crescimento de canais e perfis | https://socialblade.com/ | Site bloqueou a leitura automática; cobertura por plataforma NV. Estimativa de ganho não é dado verificado. O alvo vai a terceiro |
| YouTube Data API v3 | Grátis com cota; exige conta Google e chave | API oficial de vídeos, canais e comentários | https://developers.google.com/youtube/v3 | Conta Google e projeto no Google Cloud, não login no YouTube; dado público dispensa OAuth. Cota lida: 10.000 unidades/dia e 100 chamadas `search.list`/dia. Sujeita aos termos da API |
| InVID-WeVerify | Livre (MIT) | Extensão: quadros-chave, metadados e busca reversa de vídeo e imagem | https://github.com/AFP-Medialab/verification-plugin | Algumas funções enviam URL ou imagem a terceiros [⚠]. Login na plataforma-alvo: NV |
| YouTube Metadata (mattw.io) | Grátis (preço NV) | Metadados de vídeo, playlist e canal a partir do link | https://mattw.io/youtube-metadata/ | Usa a API do YouTube (cota pode esgotar) e consulta Filmot e Wayback. Geolocalização é declarada pelo autor. Atividade do repositório NV. Envia o alvo a terceiro [⚠] |
| TikTok Commercial Content Library | Grátis; API só para pesquisadores aprovados | Anúncios e conteúdo comercial do TikTok | https://library.tiktok.com/ (API: https://developers.tiktok.com/products/commercial-content-api) | Página abriu vazia: login e cobertura NV. A API informa só países da UE: sem cobertura do Brasil confirmada |
| Meta Content Library | Grátis, acesso restrito | Conteúdo público de Facebook, Instagram, Threads e canais do WhatsApp | https://transparency.meta.com/researchtools/meta-content-library | Exige vínculo com instituição acadêmica ou de pesquisa sem fins lucrativos; órgão policial provavelmente inelegível (inferência). Fora do roteiro |

LinkedIn: não há ferramenta gratuita estável e sem login.

## 5. Mensageria e fóruns
| Ferramenta | Gratuidade | O que faz | URL | Condição e alerta |
|---|---|---|---|---|
| Visualização web `t.me/s/‹canal›` | Grátis (recurso oficial) | Mensagens de canais públicos no navegador | https://t.me/s/telegram (exemplo do formato) | Sem conta. Só canal público com web preview; algumas postagens pedem o aplicativo |
| Telegago [⚠] | Grátis (Google Programmable Search) | Busca conteúdo público indexado de t.me, com operadores do Google | https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg | Sem conta no Telegram. Resultados podem estar desatualizados; alguns links ocultos para IP da UE; cookies de rastreamento. O termo vai ao Google |
| TGStat [⚠] | Freemium | Estatísticas de canais públicos | https://tgstat.com | **Sem login.** A política prevê transferência de dados a órgãos russos (Bellingcat) |
| Arctic Shift | Grátis (doações opcionais); API e dumps | Arquivo de posts e comentários do Reddit | https://arctic-shift.photon-reddit.com | Sem conta. Sem garantia de disponibilidade; limites dinâmicos (429). Aceita pedidos de remoção |
| Reveddit | Livre (GPL-3.0) | Conteúdo removido por moderação no Reddit | https://www.reveddit.com | Sem conta. Depende do Pushshift; alcance atual NV (guias secundários dizem que não mostra o que o próprio usuário apagou) |
| Lyzem [⚠] | Gratuidade NV (abre sem login) | Busca canais, grupos e páginas Telegraph | https://lyzem.com | Sem conta no Telegram. Termos e limites NV. Fora do roteiro principal |
| Telemetry [C][F][⚠] | Freemium: 15 buscas/dia (25 resultados) | Busca booleana em mensagens, canais e grupos públicos | https://www.telemetryapp.io/ | Cadastro por e-mail; planos pagos só em fonte secundária. Não confundir com Telemetr.io (NV). Fora do roteiro principal |
| Disboard | NV (site retornou 403) | Diretório de servidores do Discord, por tags | https://disboard.org | Descrição em fontes secundárias; acesso, termos e raspagem NV |
| Boardreader | Gratuidade NV | Busca em fóruns públicos | https://boardreader.com | Limites e termos NV |

Qualquer índice pode conter conteúdo já removido da origem: preserve antes de citar. Serviço de terceiro recebe o termo pesquisado: não digite identificador de investigado real sem avaliar o sigilo.

## 6. Análise de rede e narrativa (depois de validar os nós)
| Ferramenta | Gratuidade | URL | Condição e alerta |
|---|---|---|---|
| Gephi [L] | Livre (GPL) | https://gephi.org/ | Release 0.11.4 (01/11/2026) |
| NetworkX [L] | Livre (BSD 3 cláusulas) | https://networkx.org/ | Versão 3.7 (21/09/2026); exige Python |
| 4CAT | Livre (MPL 2.0) | https://4cat.nl/ | Local se instalado em Docker. O servidor da universidade é restrito a vinculados à UvA |
| Gephi Lite | Livre (GPL v3) | https://gephi.org/gephi-lite | Processamento local no navegador: NV |
| Cytoscape [L] | Livre (licença exata NV) | https://cytoscape.org/ | Local e offline |
| Orange Data Mining [L] | Livre (GPL-3.0 ou superior) | https://orangedatamining.com/ | Versão 3.41.0 |
| NodeXL Basic | Edição gratuita; registro em nodexl.com | https://www.smrfoundation.org/nodexl/ | Só Windows com Excel 2016 ou superior; licença da Basic NV |
| OSoMeNet [⚠] | NV (login e preço não constam) | https://osome.iu.edu/tools | Hospedado; sucessor do Hoaxy |
| Google Fact Check Explorer [⚠] | NV (API exige chave) | https://toolbox.google.com/factcheck/explorer | Serviço do Google; API em https://developers.google.com/fact-check/tools/api |
| Media Cloud [C][⚠] | Gratuito por cota (4.000 requisições/semana); planos pagos | https://search.mediacloud.org/ | Hospedado. Repositório `backend` arquivado (28/01/2022) |
| InfraNodus [F][⚠] | Freemium (3 grafos, 3 conversas de IA, arquivos até 1 MB) | https://infranodus.com/ | Envia o texto ao servidor da empresa (UE); evitar conteúdo sigiloso |
| Junkipedia | NV como gratuito: acesso por candidatura, com mensalidade (valor não divulgado) | https://www.junkipedia.org/ | Elegibilidade de órgão policial NV. Fora do roteiro |

Botometer original foi desativado com o fim do acesso gratuito à API do X (cerca de 31/05/2023); o Botometer X é só arquivo de pontuações pré-calculadas. Hoaxy foi incorporado ao OSoMeNet. Resultado de rede, pontuação de bot ou ranking de narrativa é indício, não prova de autoria ou coordenação.

## 7. Não use, por seletor
| Ferramenta | Motivo |
|---|---|
| GHunt | Exige cookies de conta Google |
| Toutatis, Osintgram | Exigem sessão (login) do Instagram |
| twscrape | Pool de contas do X |
| DiscordChatExporter e afins | Token de conta |
| Telethon, Telepathy, tg-archive | Exigem conta do Telegram (número de telefone, `api_id`/`api_hash`): login na plataforma-alvo e vínculo do número ao investigador. Telepathy sem manutenção desde 07/2024; tg-archive o autor não mantém mais; Telethon migrou para o Codeberg |
| tgkit Channel Finder | O endereço do serviço foi tratado como ameaça por antivírus comercial em 15/11/2026; sem confirmação de que seja seguro, fica fora |
| h8mail | Retorna senhas vazadas |
| Have I Been Pwned, Hudson Rock, EmailRep | Dado ou sinal de vazamento |
| GoSearch | Consulta HudsonRock e ProxyNova por padrão e quebra hashes |
| OsintHunter | Consulta vazamentos; varre 400+ sites; "Smart retries" insiste sob limite de taxa; projeto imaturo (criado em 21/10/2026) |
| NebulaOSINT | Dispara requisições simultâneas a 223 sites (sondagem em massa); projeto imaturo |
| user-scanner | Imitação de TLS e rotação de proxy; `--hudson` consulta logs de infostealer |
| ignorant | Imita o aplicativo móvel (cadastro de telefone em Amazon, Instagram e Snapchat) |
| Truecaller, Sync.me, Getcontact | Bases colaborativas de contatos |
| PimEyes, FaceCheck.ID | Reconhecimento facial (biometria é dado sensível) |
| Nitter | Arquivado em 09/10/2026; a X Corp exigiu a retirada de instâncias |
| Picuki, Imginn | Visualizadores de Instagram: violam termos, expõem o alvo, sem cadeia de custódia (situação atual NV) |
| Pyrogram | Arquivado em 23/12/2024 |
| WhatsMyName | Lista JSON de cerca de 691 sites (CC BY-SA 4.0), **arquivada em 09/11/2026 e congelada** (https://github.com/WebBreacher/WhatsMyName). Afeta o Blackbird |

Entrar em grupo privado de WhatsApp ou Discord, usar convite achado por dork ou por ator pago do Apify, ou agir com perfil dissimulado é infiltração e depende de autorização judicial (núcleo, seção 6). Não há ferramenta nesta lista para isso.

## 8. O que a verificação de 15/11/2026 deixou em aberto
- Condições de licença de Blackbird, Holehe e Epieos (preço), e quais módulos do Holehe não disparam mensagem ao titular.
- Login exigido por Meta Ad Library, TikTok Commercial Content Library, Disboard e Boardreader; cobertura do Brasil nas bibliotecas de anúncios.
- Alcance atual do Reveddit e disponibilidade do Arctic Shift.
