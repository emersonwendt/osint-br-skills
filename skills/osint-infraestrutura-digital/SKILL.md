---
name: "osint-infraestrutura-digital"
description: "OSINT de infraestrutura: domínios .br e gTLD, DNS, IP/ASN, subdomínios, servidores expostos, páginas apagadas, pesquisa avançada, Git e sites de golpe. Use com osint-fontes-abertas."
---

# OSINT-BR — Infraestrutura digital

Parte da biblioteca OSINT-BR. Escopo, limites legais, graduação de fontes, custódia e relatório estão em **osint-fontes-abertas** — aplicar sempre. Adaptado de UseOSINT/Skills (MIT, © 2026 osint-skills contributors). Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

**Regra de ouro**: passivo por padrão. Consultar registros, CT, DNS público, arquivos e índices não toca o alvo. Força bruta de DNS, varredura de portas, `AXFR` e sondagem HTTP **são ativos** — só com autorização escrita. Nunca usar credencial encontrada.

## 1. Ordem de trabalho (domínio ou site)
1. Registro e DNS (seção 2).
2. Ampliar o espaço de nomes: CT + DNS passivo + arquivos (seções 3 e 5).
3. Resolver candidatos: resolve / CNAME (aponta fornecedor) / não resolve.
4. Infraestrutura: IP, ASN, serviços observados (seção 4).
5. Conteúdo, histórico, código, stack (seções 5–7).
6. Mapa pronto? Registro, nomes, IPs, histórico e titular verificados — ou lacunas declaradas.
7. Seletores do titular → canal correto (empresa → osint-midia-e-ativos; pessoa → só via canal formal).

## 2. Quem é o titular do domínio
| Você tem | Use | Por quê |
|---|---|---|
| Domínio .br | RDAP do Registro.br: `https://rdap.registro.br/domain/{dominio}` | O .br exige CPF/CNPJ do titular; o RDAP traz titular, datas, status, nameservers |
| Titular PJ (CNPJ) | `https://rdap.registro.br/entity/{CNPJ}` | Lista o titular e permite pivô para outros domínios dele; depois, CNPJ na Receita |
| gTLD (.com, .net…) | RDAP via `https://rdap.org/domain/{dominio}` ou `lookup.icann.org`; depois o registrador | Registro "thin": datas e status no registry, contatos no registrador |
| Contato mascarado | WHOIS histórico + DNS passivo | O mascaramento não é retroativo nas bases históricas |
| IP ou ASN brasileiro | RDAP do Registro.br (`/ip/{ip}`, `/autnum/{asn}`) — o NIC.br administra a numeração no Brasil | Mostra o detentor do bloco, não o dono do site |
| Domínio recém-criado | Data de criação + registrador + NS | Idade curta + registrador de atacado = sinal clássico de phishing |

Campos RDAP que importam:
- `events`: registration, expiration, last changed, transfer (transferência recente = histórico anterior só em bases históricas).
- `status`: `clientHold` (registrador suspendeu), `serverHold` (registro suspendeu — muitas vezes ordem legal), `redemptionPeriod`/`pendingDelete` (expirando).
- `entities[].roles`, `nameservers`, `secureDNS`.
Pessoa física titular de .br: tratar nome e CPF como dado pessoal, minimizar e não pivotar para a vida privada (osint-fontes-abertas, seção 1).

Armadilhas: titular pode ser revendedor, agência ou serviço de privacidade; domínio expirado e re-registrado zera a data de criação (histórico longo no arquivo + criação recente = mudou de mãos); MX e NS identificam fornecedor, não dono; squatters copiam SPF/MX do alvo; domínio estacionado não tem infraestrutura do dono.

### Passe de DNS
```bash
dig +short exemplo.com.br A; dig +short exemplo.com.br NS
dig exemplo.com.br MX +noall +answer
dig exemplo.com.br SOA +noall +answer      # mailbox do responsável; serial AAAAMMDDnn
dig exemplo.com.br TXT +short              # SPF e tokens de verificação = inventário de SaaS
dig _dmarc.exemplo.com.br TXT +short
dig exemplo.com.br CAA +short
dig -x 203.0.113.10 +short
```
Não basear nada em `ANY`. Registros TXT envelhecem: presente no SPF = "foi configurado", não "em uso". Cada resolvedor é um ponto de vista (geoDNS, split-horizon).

### IP e ASN
```bash
whois -h whois.cymru.com " -v 203.0.113.10"   # ASN, prefixo, país
```
IP de nuvem ou hospedagem compartilhada liga o domínio a milhares de inquilinos: **"mesmo IP" não é atribuição**. Só vira evidência com sub-alocação nominal ou bloco pequeno em nome do alvo.

## 3. Subdomínios (Certificate Transparency)
Todo certificado aceito por navegador está em logs públicos e append-only.
```bash
curl -s 'https://crt.sh/?q=%25.exemplo.com.br&output=json' | jq -r '.[].name_value' | sed 's/^\*\.//' | sort -u
curl -s 'https://crt.sh/?q=Empresa+Exemplo+Ltda&output=json' | jq -r '.[].name_value'   # busca por organização
```
- O campo SAN é o prêmio: poucos nomes relacionados = mesmo serviço/administrador; nomes de domínios registráveis diferentes no mesmo certificado = mesmo operador (aquisições, marcas irmãs). Dezenas de nomes sem relação = certificado de CDN/hospedagem: **são outros clientes**.
- Curinga (`*.exemplo`) esconde; minerar o período anterior ao curinga e usar DNS passivo e arquivos.
- CT é histórico, não inventário: nomes mortos, CAs internas e certificados de origem ficam de fora.
- Teste de DNS curinga antes de confiar em força bruta: resolver `zzq7x-inexistente.exemplo.com.br`.
- Agregadores (subfinder, amass) e resolução (dnsx) rodam na máquina do usuário; `httpx` e força bruta são ativos.
- Desconfiar de typosquats que aparecem como se fossem do alvo: conferir o domínio registrável letra a letra.

## 4. Servidores expostos
| Você tem | Use |
|---|---|
| Um IP | Shodan host ou `https://internetdb.shodan.io/{ip}` (gratuito) |
| Bloco/ASN | Shodan `net:` / `asn:` com facetas de porta |
| Site atrás de CDN | Censys (junção certificado→host) para achar a origem |
| Certificado ou página característica | Hash de favicon, CN/serial do certificado, JARM, string única do HTML |
Ler com cuidado: data de varredura em todo registro; CVE é inferência por versão; `org:` é registro de rede, não propriedade; honeypots poluem; plataformas divergem e planos gratuitos truncam. Telas e banners expostos contêm dados pessoais: minimizar. Exposição relevante → notificar o contato de abuso do bloco e, no Brasil, o CERT.br.

## 5. Páginas apagadas e arquivos
| Situação | Vá para |
|---|---|
| URL que hoje dá 404 | Wayback, depois archive.today |
| "O que o site dizia antes de X" | CDX da Wayback com `collapse=digest` (datas em que o conteúdo mudou) |
| Página com muito JavaScript ou post de rede social | archive.today (DOM renderizado) |
| Wayback com exclusão | archive.today, depois Common Crawl |
| Caminhos e subdomínios desconhecidos | CDX com `matchType=domain` |
| Evidência que não pode se perder | Capturar você mesmo (WARC) e enviar a dois arquivos |
```bash
curl -s 'http://web.archive.org/cdx/search/cdx?url=exemplo.com.br/*&output=json&fl=original&collapse=urlkey'
curl -s 'http://web.archive.org/cdx/search/cdx?url=exemplo.com.br/quem-somos&output=json&collapse=digest&fl=timestamp,digest,statuscode'
curl -s 'https://web.archive.org/web/20190412093000id_/http://exemplo.com.br/precos' > precos-2019.html   # id_ = bytes originais
wget --warc-file=evidencia-001 --page-requisites --no-parent https://exemplo.com.br/precos
```
Recupera: equipes antigas, preços e termos anteriores, contatos antigos, textos antes da edição, arquivos esquecidos, dono anterior do domínio. Cuidados: ausência de captura não é evidência; captura ≠ data de publicação; render pode misturar recursos de datas diferentes; captura após troca de dono reflete o comprador; nunca aceitar print de página arquivada — conferir a captura.

## 6. Pesquisa avançada (dorks)
- Google: maior índice, operadores menos fiéis. Bing: `site:` mais literal, tem `ip:`. Yandex: imagens e conteúdo do Leste Europeu. Mojeek/Brave/Marginalia: rastreadores próprios.
- Operadores úteis: `site:`, `-site:`, `filetype:`/`ext:`, `intitle:`, `inurl:`, aspas para literal, `before:`/`after:` (data inferida, não confiável).
- Material do alvo fora do próprio site: `"exemplo.com.br" -site:exemplo.com.br`, CNPJ entre aspas, `site:gov.br "Empresa Exemplo"`.
- Índices especializados: código (GitHub, grep.app), documentos (Scribd, Issuu, SlideShare), código-fonte de páginas (PublicWWW), arquivos (CDX, Common Crawl).
- Fontes brasileiras indexáveis: DOU (`site:in.gov.br`), diários municipais (Querido Diário — queridodiario.ok.org.br), portais de transparência, consultas processuais públicas.
- Zero resultado = um índice disse não. `site:` nunca enumera tudo. Resultados mudam por localização e personalização. Automação em buscadores quebra (CAPTCHA) e viola termos.

## 7. Histórico Git
| Você tem | Comece por |
|---|---|
| Organização | Membros públicos e repositórios pessoais deles |
| Desenvolvedor (usuário) | E-mails de commit em todos os repositórios |
| Suspeita de credencial vazada | Varredura do clone espelho, todas as refs |
| String específica (host interno, prefixo de chave) | `git log -S` |
```bash
git clone --mirror https://github.com/org-exemplo/repo.git repo.git
git --git-dir=repo.git log --all --format='%an <%ae>' | sort -u
trufflehog git file://./repo.git
gitleaks detect --source=. -v
git log --all --diff-filter=D --name-only --format='%H %aI %an'
```
O que sobrevive à exclusão: segredos removidos do HEAD seguem no histórico; commits em redes de fork; gists "secretos" são só não listados; logs de CI públicos. Cuidados: autoria de commit é autodeclarada; bots dominam contagens; fuso do commit é indício fraco; fixtures de teste parecem credenciais; chaves publicáveis não são vazamento. **Nunca autenticar com credencial encontrada** — nem para "testar"; reportar ao responsável. `.git` exposto em servidor web: acessar só com autorização.
Clonar e analisar repositórios públicos numa pasta própria do caso (funciona também no Claude web, que acessa o GitHub).

## 8. Roteiro: site, anúncio ou perfil de golpe (falso gerente, falsa central, investimento, loja falsa)
1. **Preservar já**: URL, captura integral, HTML/WARC, SHA-256, horário — sites de golpe somem em horas.
2. **Registro**: RDAP (.br ou gTLD), idade, registrador, NS, status; histórico de titular.
3. **Hospedagem**: IP, ASN, CDN; Censys/Shodan para origem e servidores irmãos.
4. **Irmãos da operação**: SAN de certificados, IDs de Google Analytics/Tag Manager/pixel, favicon hash, trechos de HTML/JS idênticos, mesmo template — ligar sites da mesma quadrilha.
5. **Divulgação**: Biblioteca de Anúncios da Meta e Google Ads Transparency Center (anunciante, período, criativos).
6. **Fluxo financeiro exibido**: chave Pix, QR Code, intermediador de pagamento, carteira cripto, CNPJ citado no rodapé (verificar na Receita — golpes usam CNPJ de terceiros). Não efetuar pagamento nem iniciar transação para "ver o nome".
7. **Histórico**: Wayback/archive.today; versões anteriores podem expor operadores.
8. **Encaminhamentos**: preservação junto a registrador/hospedagem/plataforma; abuso ao registrador e ao Registro.br; CERT.br; para a vítima, BO e contestação/MED junto ao próprio banco; para a autoridade, requisições a PSP, provedores e plataformas (osint-fontes-abertas, seção 4).

## 9. Ambiente de execução
- **Claude Code**: RDAP, crt.sh, CDX, Shodan e Censys podem ser consultados direto do terminal; todo acesso sai do IP local (OPSEC na skill osint-fontes-abertas).
- **Claude (web/desktop)**: ler RDAP, crt.sh, CDX e páginas públicas pela leitura de páginas do Claude; o shell na nuvem alcança GitHub e pacotes, mas não esses sites.
- Ferramentas ativas ou de enumeração em massa (força bruta de DNS, httpx, varredura) só com autorização escrita no escopo.
