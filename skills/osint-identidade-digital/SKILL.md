---
name: "osint-identidade-digital"
description: "OSINT de identidade digital: roteiros por username, e-mail, telefone, perfil público e Telegram/Reddit, com validação do acerto. Use com osint-fontes-abertas; particular só nos casos do núcleo."
---

# OSINT-BR — Identidade digital (SOCMINT)

Contribuição de Alan Douglas Silva (Professor na WB Educação) à biblioteca OSINT-BR, organizada pelo Prof. Dr. Emerson Wendt. Ferramentas conferidas em página oficial ou repositório em 15/11/2026. Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

Parte da biblioteca OSINT-BR. Escopo, limites legais, graduação de fontes, escala de probabilidade, OPSEC, custódia e relatório estão em **osint-fontes-abertas**: aplicar sempre. Aqui estão só os roteiros por seletor de identidade e a validação do acerto. Tabela completa de ferramentas, links e condições: `referencias/ferramentas.md`.

**Regra de ouro**: coleta passiva, em fonte aberta, sem login. Todo resultado de ferramenta nasce **não confirmado**. A conta existir é fato; ser do alvo é inferência.

Marcas: **[L]** roda na sua máquina · **[C]** exige cadastro na própria ferramenta (nunca conta do alvo) · **[F]** freemium (declare o plano no manifesto) · **[⚠]** envia o seletor a terceiro (só dado não sigiloso) · **[M]** consulta manual sua, por causa de captcha · **\*** gratuidade não confirmada em página oficial.

## 1. Quando usar e quando não
Pessoa natural privada só entra nos casos da seção 1 do núcleo:
1. **Autoauditoria** do próprio usuário ou de quem o autorizou expressamente.
2. **Figura pública**, na atuação pública.
3. **Identificadores do próprio ato ilícito** (perfil-golpe, número do falso gerente, e-mail do phishing), sem estender à vida privada de quem estiver por trás.

Fora disso, o caminho é o canal formal (núcleo, seção 4). Não use esta skill para: montar dossiê; achar endereço, local de trabalho, rotina, familiares, saúde, religião ou orientação; descobrir "quem é" o titular de conta ou número. Seguidores e seguidos de particular não se coletam: revelam vínculos e familiares.

**Encerre o ramo e registre só a ocorrência** se aparecer menor de idade ou dado pessoal sensível (LGPD, art. 5º, II: [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), acesso em 15/11/2026). Material de abuso sexual infantil: não abrir, anotar só a URL e encaminhar à SaferNet ou à autoridade (núcleo, seção 1).

**Limites desta skill**: sem login ou cookies na plataforma-alvo; sem contornar captcha, bloqueio ou limite de taxa; sem dado ou credencial vazada; sem reconhecimento facial; sem contato (não seguir, curtir, enviar solicitação ou mensagem, nem entrar em grupo); sem perfil falso; sem varredura ativa, crawling ou monitoramento contínuo.

## 2. Antes de buscar
1. **Escopo**: qual dos três casos da seção 1 autoriza esta busca? Se nenhum, pare.
2. **Discriminadores**: escreva o que o alvo verdadeiro tem (cidade, profissão, idioma, período de atividade) e o que não pode ter. Depois que um candidato aparece, os discriminadores somem.
3. **Critério de pronto**: "a conta X pertence ao titular do e-mail Y?" fecha em confirmado ou rejeitado, ou quando as fontes previstas se esgotarem, documentadas.
4. **Baseline**: uma ou duas checagens manuais e baratas antes de qualquer ferramenta.
5. **Sigilo**: o seletor vai a serviço de terceiro? Caso sigiloso usa só ferramenta [L].
6. **Ritmo**: pelo menos 1 s entre requisições ao mesmo domínio; em erro 5xx, até 3 novas tentativas com espera crescente; em 429, uma só e apenas se o `Retry-After` permitir; depois registre **BLOQUEADA** e passe à próxima ferramenta. Bloqueio não se contorna.

## 3. Roteiros por seletor
A ordem é de prioridade: as mais usadas, simples e gratuitas primeiro. Percorra e pare quando o critério de pronto for atingido.

### 3.1 Username
| Passo | Ferramenta | Condição de uso |
|---|---|---|
| 1 | Baseline: `"usuario_exemplo"` entre aspas em dois buscadores; abrir o perfil que o caso cita | Sempre. Se já responde, não rode ferramenta |
| 2 | [Maigret](https://github.com/soxoj/maigret) [L] | Primeira ferramenta: milhares de sites, extrai dados do perfil |
| 3 | [Sherlock](https://github.com/sherlock-project/sherlock) [L] | Cobertura de centenas de redes. Acerto que as duas ferramentas repetem é a mesma pista, não corroboração |
| 4 | [Blackbird](https://github.com/p1ngul1n0/blackbird) [L] | Só se 2 e 3 deixaram lacuna. **IA opcional desligada.** Usa a lista WhatsMyName, congelada (seção 7) |
| 5 | [Social Analyzer](https://github.com/qeeqbox/social-analyzer) [L] | Idem. **"Special Detections" desligadas** |
| 6 | Bio, links e avatar dos perfis que passaram na validação (seção 4) | Só daqui saem pivôs |

### 3.2 E-mail
| Passo | Ferramenta | Condição de uso |
|---|---|---|
| 1 | Baseline: o endereço entre aspas em dois buscadores | Sempre |
| 2 | [Gravatar, API de perfis](https://docs.gravatar.com/api/profiles/rest-api/) [⚠] | Consulta por **hash SHA-256** do e-mail normalizado (minúsculas, sem espaços); a documentação veda MD5. Sem chave: 100 requisições/hora e campos omitidos. Envia o hash ao Gravatar |
| 3 | [Epieos](https://epieos.com) [C][F][⚠] | Cadastro seu, não do alvo. Preço só em fonte secundária: confirme o plano antes. Não digite e-mail de caso sigiloso |
| 4 | [Holehe](https://github.com/megadose/holehe) [L] | Sem commit desde 09/2024. Só módulos que **não disparem mensagem ao titular**; a verificação de 15/11/2026 não apurou quais são: sem certeza, não execute |
| 5 | [GitHub Search](https://docs.github.com/en/rest/search/search) | Commits por `author-email:` e `committer-email:` (e-mail completo; só branch padrão); usuários por `in:email` (só e-mail público). **Busca de código exige login: fora** |
| 6 | [Hunter.io](https://hunter.io) [C][F] | Só e-mail corporativo de um domínio (50 créditos/mês) |
| 7 | Perfis e domínios achados | Perfil: seção 4. Domínio: **osint-infraestrutura-digital** |

```bash
printf '%s' 'usuario_exemplo@exemplo.com.br' | tr '[:upper:]' '[:lower:]' | sha256sum
```
```powershell
[BitConverter]::ToString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes('usuario_exemplo@exemplo.com.br'))).Replace('-','').ToLower()
```
Busca de commits no GitHub (digitar na busca de commits):
```
author-email:usuario_exemplo@exemplo.com.br
committer-email:usuario_exemplo@exemplo.com.br
```
E-mail de commit é dado pessoal: minimizar. Autoria de commit é autodeclarada (osint-infraestrutura-digital, seção 7). Hash sem perfil no Gravatar é ausência de resultado, não prova de que o e-mail não existe.

### 3.3 Telefone
| Passo | Ferramenta | Condição de uso |
|---|---|---|
| 1 | Baseline: o número entre aspas, nos formatos abaixo, e menções indexadas | Sempre |
| 2 | [ABR Telecom, Consulta Número](https://consultanumero.abrtelecom.com.br) [M] | Operadora atual e portabilidade. **reCAPTCHA: você mesmo, manualmente.** A skill não resolve captcha |
| 3 | [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) [L] | Sem manutenção; **só o scanner local**. Entrega país, operadora e tipo de linha |

```
"(11) 90000-0000"   "11 90000-0000"   "11900000000"   "+55 11 90000-0000"   "+5511900000000"
```
Operadora não é titular, e número não é pessoa. Titular se obtém por dados cadastrais de autoridade competente (núcleo, seção 4). No relatório, mascare o número, salvo se for o artefato do golpe. WhatsApp: nenhuma ferramenta verificada atende sem conta na plataforma.

### 3.4 Perfil público em plataforma
| Passo | Ferramenta | Condição de uso |
|---|---|---|
| 1 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) [L] | Vídeo e metadados de YouTube, Facebook, Instagram, TikTok e X. **Sem cookies do navegador**; se pedir login, BLOQUEADA. Extratores `instagram:user` e `tiktok:tag/sound/effect` constam como quebrados. LinkedIn: só eventos e Learning |
| 2 | [Instaloader](https://github.com/instaloader/instaloader) [L] | **Só perfil público, sem login.** Hashtags, stories e perfil privado exigem login: fora. A documentação cita erro 429 e limites mais rígidos no acesso anônimo: recuar e parar. Projeto não oficial |
| 3 | [gallery-dl](https://codeberg.org/mikf/gallery-dl) [L] | **Sem cookies.** Na prática o login tende a ser exigido (não verificado): se exigir, BLOQUEADA. Código no Codeberg |
| 4 | [Zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) + [4CAT](https://github.com/digitalmethodsinitiative/4cat) [L] | Captura passiva do que o seu navegador recebe: navegue **sem login e sem interagir**. A análise exige instância 4CAT própria (Docker) |
| 5 | [Meta Ad Library](https://www.facebook.com/ads/library/) e [Google Ads Transparency Center](https://adstransparency.google.com/) | Quando o perfil ou a página anuncia (golpe, campanha). Login e cobertura no Brasil não verificados; o provedor vê a consulta |
| 6 | [Social Blade](https://socialblade.com/) [F]\* | Histórico de crescimento. Estimativa de ganho não é dado verificado; o alvo vai a terceiro |

LinkedIn: não há ferramenta gratuita estável sem login. Leia manualmente só o que abre sem login e preserve (seção 5). YouTube em volume: [YouTube Data API v3](https://developers.google.com/youtube/v3) (conta Google e chave; cota de 10.000 unidades/dia e 100 buscas/dia, lidas na documentação).

### 3.5 Canal de mensageria e fórum
| Plataforma | Ordem | Condição de uso |
|---|---|---|
| Telegram | `t.me/s/‹canal›` → [Telegago](https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg) → [TGStat](https://tgstat.com) | Só canal público com visualização web, sem conta. Telegago é busca do Google (o termo vai ao Google; índice pode estar desatualizado). TGStat só sem login: a política prevê transferência de dados a órgãos russos (Bellingcat) |
| Reddit | [Arctic Shift](https://arctic-shift.photon-reddit.com) → [Reveddit](https://www.reveddit.com) | Sem conta. Arctic Shift sem garantia de disponibilidade (429). Alcance atual do Reveddit não verificado |
| Discord e WhatsApp | Nenhuma ferramenta verificada | Entrar em grupo privado ou servidor, usar convite achado por dork ou perfil dissimulado é infiltração: depende de autorização judicial (núcleo, seção 6) |
| Fóruns | Ver `referencias/ferramentas.md` | Disboard e Boardreader: gratuidade e termos não verificados |

```
https://t.me/s/canal_exemplo
```
O que o índice mostra pode já ter sido removido da origem: preserve antes de citar.

### 3.6 Análise de rede
Só depois de validar os nós (seção 4). Grafo local: **Gephi** ou **NetworkX** (núcleo, seção 9). Serviços hospedados (InfraNodus, OSoMeNet, Media Cloud) recebem o texto ou o termo consultado: nada dos autos. Pontuação de bot, métrica de rede e ranking de narrativa são indício, não prova de autoria nem de coordenação. Lista completa em `referencias/ferramentas.md`.

## 4. Validar um acerto de enumeração
Saída de ferramenta é pista, não prova (núcleo, seção 5). **Username, nome ou foto iguais, isolados, nunca bastam.**

1. **Abra a URL real** de cada acerto e confira na própria página. Ferramenta de varredura dá falso positivo e falso negativo.
2. **Separe natureza**: "a conta existe em A e em B" é fato observado, com URL, data e hora; "A e B são do mesmo titular" é inferência.
3. **Conte só elementos independentes** (não se copiam nem derivam da mesma publicação): e-mail ou link público, bio cruzada, vínculo institucional ou declarado, cronologia compatível, geolocalização pública, conteúdo autoral consistente, imagem autoral que não seja rosto nem banco de imagens. Gradue a fonte pelo que ela é (autodeclaração de titular não verificado) e a informação pelo que você corroborou, em separado (Almirantado, núcleo, seção 5).
4. **Teste as hipóteses concorrentes**: homônimo, reutilização de username, conta de fã ou paródia, conta comprometida, perfil abandonado, imagem copiada, conteúdo republicado.
5. **Refute**: faça ao menos uma diligência que derrubaria a hipótese principal (idioma, fuso, conta criada depois do fato).
6. **Pivote só de vínculo confirmado ou provável**, e diga qual seletor confirmado liga o novo ao alvo. Conta não confirmada recebe diligência de validação, não pivô. Padrão sem outro limite no escopo: profundidade 2.

| Você tem | Grau do achado (núcleo, seção 5) |
|---|---|
| Mesmo username em duas plataformas | Conta existe nas duas (fato). Mesmo titular: **não confirmado** |
| Bio de A aponta para B | **Provável**, falta um elemento independente |
| E-mail da bio de A igual ao de registro público de B, mais uma imagem autoral igual nas duas | **Confirmado** (dois elementos independentes) |
| "Segue a página da empresa, logo trabalha lá" | Hipótese não confirmada: teste em fonte institucional |
| Elemento contraditório (idioma, época, local) | **Rejeitado**, com o motivo registrado |

Grau mede a evidência; probabilidade usa só a escala do núcleo, e as duas vão no relatório, sem misturar termo e percentual na mesma frase. Vincular contas não atribui autoria, dolo ou conduta: investigado não é autor. Identificar a pessoa real é diligência formal.

## 5. Preservar o perfil
Preserve **antes de pivotar**: perfil apaga, muda de nome e some. Registre URL, handle, nome exibido, bio e links, data e hora (America/Sao_Paulo e UTC), ferramenta, versão e comando exatos, e SHA-256 de cada arquivo. Método, captura local e manifesto: **osint-preservacao-evidencias**. Pré-visualização de link em chat ou e-mail acessa a URL do alvo (núcleo, seção 6): não cole.

**Sigilo**: caso sigiloso não envia o perfil a archive.today nem ao "Save Page Now" do Wayback: ambos publicam a consulta. Use captura local.

## 6. Onde dá errado
- **Saída de ferramenta como prova**: lista de enumerador é pista. A mesma pista repetida por duas ferramentas não é corroboração.
- **Deriva de seletor**: cada pivô sem vínculo confirmado soma incerteza. Cinco pivôs de 90% são cara ou coroa.
- **Dado velho como atual**: registre a data de observação ao lado de cada fato.
- **Ferramenta pede login ou cookies**: pare e registre BLOQUEADA. Não use conta sua, de terceiro ou "de pesquisa" na plataforma-alvo.
- **Ferramenta sem manutenção** (Holehe, PhoneInfoga, Telepathy): site mudou e o resultado está errado sem avisar.
- **Notificar o alvo**: ferramenta que dispara mensagem de recuperação ou convite ao titular é contato. Na dúvida, não execute.
- **Seletor enviado a terceiro**: Gravatar, Epieos, Telegago, TGStat, Social Blade e bibliotecas de anúncios veem o que você digita.
- **Foto de banco de imagens** ou avatar genérico "confirmando" identidade: não confirma.
- **Operadora tomada por titular**: a operadora é da linha, não da pessoa.
- **Dado de terceiros** (amigos, familiares, comentaristas) entrando no caso: exclua e tarje.
- **Resultado vazio** é "não encontrado em <fonte>, com <consulta>, em <data>", nunca prova de inexistência.

## 7. Não use
| Ferramenta | Motivo |
|---|---|
| GHunt, Toutatis, Osintgram, twscrape | Exigem cookies ou sessão da conta Google, do Instagram ou pool de contas do X |
| h8mail, Have I Been Pwned, GoSearch, OsintHunter | Usam dado ou sinal de vazamento (senha vazada, HudsonRock); OsintHunter ainda varre 400+ sites e insiste sob limite de taxa |
| user-scanner | Imitação de TLS e rotação de proxy; a opção `--hudson` consulta logs de infostealer |
| NebulaOSINT | Sondagem em massa de 223 sites; projeto imaturo |
| ignorant | Imita o aplicativo móvel |
| PimEyes, FaceCheck.ID | Reconhecimento facial |
| Truecaller, Sync.me, Getcontact | Bases colaborativas de contatos |
| Telethon, Telepathy, tg-archive | Exigem conta do Telegram, que vincula o número ao investigador |
| Nitter, visualizadores do Instagram | Nitter arquivado; visualizadores violam termos, expõem o alvo e não geram custódia |

**WhatsMyName**: a lista foi **arquivada em 09/11/2026 e ficou congelada** ([repositório](https://github.com/WebBreacher/WhatsMyName)). Ferramenta que depende dela, como o Blackbird, não enxerga sites novos nem mudanças posteriores. Não a cite como cobertura atual.

## 8. Ambiente de execução
Ferramentas [L] rodam na máquina do usuário (Claude Code), e o tráfego sai do IP local: OPSEC no núcleo, seção 6. No Claude web/desktop, gere os comandos para o usuário rodar; a nuvem não alcança esses sites (núcleo, seção 10).
