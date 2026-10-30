---
name: "osint-fontes-abertas"
description: "Use para investigação OSINT: método, escopo legal brasileiro, OPSEC, cadeia de custódia e relatório; encaminha para as skills de infraestrutura e de mídia/ativos."
---

# OSINT-BR — Núcleo: método, lei, custódia e relatório

Skill-núcleo da biblioteca OSINT-BR, organizada pelo Prof. Emerson Wendt para os alunos de seus cursos (WB Educação, Faculdade Brasileira de Inovação — FABIN, Polícias e Ministério Público). Vale para casos reais, verificação, perícia/assistência técnica, pesquisa acadêmica e preparo de aulas. Responder em português do Brasil, com rigor metodológico e linguagem técnico-jurídica.

Biblioteca:
- **osint-fontes-abertas** (esta) — escopo, método, análise, OPSEC, custódia, relatório, grafo, uso didático.
- **osint-infraestrutura-digital** — domínios, DNS, IP/ASN, subdomínios, servidores expostos, páginas apagadas, pesquisa avançada, Git, sites de golpe.
- **osint-midia-e-ativos** — imagens/vídeos (origem, autenticidade, metadados, geolocalização), empresas e beneficiário final, criptoativos, aeronaves e embarcações.

Adaptado e traduzido, com fontes e direito brasileiros, a partir de UseOSINT/Skills (licença MIT, © 2026 osint-skills contributors). Uso sujeito a ETICA.md e AVISO-LEGAL.md do repositório.

## Vocabulário
- **Seletor** — um dado identificável: domínio, IP, e-mail, nome de usuário, telefone, carteira, hash, CNPJ, matrícula de aeronave, IMO.
- **Pivô** — transformar um seletor em novos seletores. A investigação é uma cadeia de pivôs, e cada pivô é uma chance de "trocar de alvo" sem perceber.

## 1. Escopo autorizado (antes de qualquer coleta)
Registrar por escrito:
1. **Alvo** — a entidade específica e os discriminadores que a separam de homônimos.
2. **Objetivo** — a pergunta de inteligência (seção 2).
3. **Dentro do escopo** — tipos de seletor, fontes, se há interação.
4. **Fora do escopo** — o que não será feito.
5. **Base legal e jurisdição** — quem autorizou e com que fundamento.
Sem autorização identificável: parar. Investigação não autorizada não se conserta com bom relatório.

### Limites inegociáveis
- **Sem intrusão**: não autenticar em sistemas do alvo, não testar credenciais encontradas, não explorar vulnerabilidades, não fazer engenharia social, não usar dados de vazamento para acessar contas.
- **Pessoa natural privada**: não montar dossiê, não localizar endereço residencial, local de trabalho, rotina, familiares, saúde, religião ou orientação. Pessoas naturais entram apenas como: (a) autoauditoria do próprio usuário ou de quem o autorizou expressamente; (b) figura pública na atuação pública; (c) identificadores usados no próprio ato ilícito (perfil-golpe, número do falso gerente, chave Pix, domínio), sem estender à vida privada de quem estiver por trás. Identificar a pessoa real é tarefa dos canais formais (seção 4).
- **Exploração sexual infantil**: não buscar nem analisar conteúdo; orientar encaminhamento (SaferNet, autoridade competente).
- **Publicidade não é permissão**: agregar dados pessoais públicos é tratamento de dados (LGPD). Mesmo sob o art. 4º, III (segurança pública/investigação), valem necessidade, proporcionalidade e minimização.

## 2. Pergunta respondível
"Levantar tudo sobre X" não tem condição de parada. Reescrever com alvo, decisão que alimenta e o que a encerraria.
| Vago | Respondível |
|---|---|
| Investigue esta empresa | O fornecedor desta nota tem sócio oculto vinculado a empresa inidônea e opera no endereço declarado? |
| Veja este domínio | `exemplo.com.br` é operado pelo mesmo grupo do site de phishing, em infraestrutura compartilhada? |
| Essa foto é verdadeira? | A foto mostra o local e a data alegados na postagem? |
Escrever também o **negativo**: que achado significaria "não". Se nada puder significar "não", a pergunta é infalseável.

## 3. Ciclo de inteligência
1. **Planejamento** — plano de coleta: para cada subpergunta, o indicador, a fonte/skill, se é passiva, e o plano B se vier vazia. Passivo primeiro: registros, arquivos, logs públicos antes de qualquer coisa que toque o alvo.
2. **Coleta** — preservando à medida que coleta (seção 6).
3. **Processamento** — normalizar, deduplicar, datar (America/Sao_Paulo e UTC), registrar origem de cada dado.
4. **Análise** — graduação de fontes, hipóteses concorrentes, controle de vieses.
5. **Difusão** — relatório (seção 7).

### Encaminhamento por seletor inicial
| Você tem | Vá para |
|---|---|
| Domínio, site, URL, IP, e-mail corporativo (domínio) | osint-infraestrutura-digital |
| Site/anúncio de golpe, chave Pix ou link de pagamento exibidos | osint-infraestrutura-digital (roteiro de golpe) |
| Foto, vídeo, print, documento (metadados) | osint-midia-e-ativos |
| Empresa, CNPJ, marca, nota fiscal | osint-midia-e-ativos |
| Carteira/transação cripto | osint-midia-e-ativos |
| Aeronave (PR-, PP-, PT-, PS-, PU-) ou embarcação (IMO/MMSI) | osint-midia-e-ativos |
| Nome de usuário, e-mail ou telefone de particular | Só autoauditoria ou artefato do golpe (seção 1); caso contrário, canal formal |
Sem ponto de partida claro: comece pelo seletor **único e indexado** (domínio e e-mail vencem nome e apelido).

## 4. Canais formais (o que o OSINT não substitui)
Indicar no relatório as diligências que fecham as lacunas:
- **Preservação cautelar imediata** de registros junto a provedores (Marco Civil, art. 13, §2º — conexão; art. 15, §2º — aplicações), antes do pedido de acesso.
- **Dados cadastrais** por autoridade competente (Marco Civil, art. 10, §3º; Lei 12.850/2013, art. 15).
- **Registros de conexão/acesso e conteúdo**: ordem judicial (Marco Civil, arts. 10, §1º e §2º, e 22).
- **Instituições financeiras/PSPs** (Pix, contas de passagem): requisição/ordem conforme o caso; MED do Pix pela vítima junto ao seu banco.
- **Exchanges** autorizadas pelo BCB (Res. BCB 519, 520 e 521/2025, em vigor desde 02/02/2026): KYC e cooperação.
- **Cooperação internacional**: Convenção de Budapeste (Decreto 11.491/2023), inclusive preservação expedita.

## 5. Análise
### Graduação de fontes (Sistema Almirantado)
Letra para a **fonte** (A inteiramente idônea … E inidônea; F não avaliável) e número para a **informação** (1 confirmada por fonte independente … 5 improvável; 6 não avaliável), graduados separadamente, em todo achado retido. Gradue a fonte que você efetivamente tocou, não a que ela diz citar: certidão da Junta = B2; matéria jornalística sobre a certidão = no máximo B2; post anônimo repetindo a matéria = D3, e não é corroboração nova.

### Hipóteses concorrentes (ACH)
Listar todas as hipóteses, inclusive as tediosas (homônimo; conta vendida; IP de hospedagem compartilhada; nominee/laranja). Matriz evidência × hipótese, perguntando só se a evidência é **inconsistente** com cada hipótese. Vence a com menos inconsistências, não a com mais apoio. Evidência consistente com todas não tem valor diagnóstico.

### Onde dá errado
- **Viés de confirmação**: os discriminadores somem depois que um candidato aparece. Antes de buscar, escreva atributos que o alvo verdadeiro tem e os que não pode ter.
- **Reporte circular**: três fontes concordam porque copiaram a mesma origem (mesmo erro de digitação, mesma base de broker). Independente = coleta diferente, não site diferente.
- **Dado velho como atual**: registre a data de observação ao lado de todo fato.
- **Deriva de seletor**: cinco pivôs de 90% cada = cara ou coroa. Após cada pivô, diga qual seletor confirmado liga o novo ao alvo.
- **Saída de ferramenta como prova**: lista de enumerador, score de reconhecimento facial, match de agregador são pistas.

### Escala de probabilidade (usar só ela)
| Termo | Faixa |
|---|---|
| Quase certo | ≥ 95% |
| Altamente provável | 80–95% |
| Provável | 55–80% |
| Chances aproximadamente iguais | 45–55% |
| Improvável | 20–45% |
| Altamente improvável | 5–20% |
| Remoto | < 5% |
Não misturar termo e percentual na mesma frase. Banir "possivelmente", "não se pode descartar", "pode/poderia", "sugere", "supostamente".
**Probabilidade ≠ confiança.** Confiança (alta/moderada/baixa) mede a qualidade da evidência; declarar as duas, com o motivo da confiança.

### Grau do achado
- **Confirmado** — duas fontes de coleta independente, ou um registro primário autoritativo (certidão, registro oficial), sem contradição.
- **Provável** — uma fonte forte, ou várias fracas que passaram no teste de circularidade, com alternativas testadas.
- **Não confirmado** — pista única. Dizer isso; não promover em silêncio.
- **Rejeitado** — contraditado. Registrar o porquê.

### Quando parar
Quando a pergunta estiver respondida no grau que a decisão exige, ou documentado que as fontes abertas não a respondem e o que responderia (requisição, ordem judicial, oitiva). "Não foi possível estabelecer X, consultados A, B e C" é entrega legítima. Cruzar o limite do escopo exige nova autorização.

## 6. OPSEC do investigador
| Situação | Postura |
|---|---|
| Registros públicos, arquivos, CT, consultas processuais | Navegador comum. |
| Ver o site público do alvo | Perfil de navegador limpo, VPN, sem sessões logadas. |
| Alvo monitora a própria infraestrutura ou é tecnicamente capaz | VM dedicada, saída não identificável, disciplina de horário. |
| Crime organizado, risco físico | Tudo acima + hardware compartimentado e colega ciente. |
- Superfícies de atribuição: ASN (rede corporativa ou institucional entrega o órgão), impressão digital do navegador, idioma/fuso, horário de atividade, **pré-visualização de links** (colar a URL do alvo em chat/e-mail faz o serviço acessá-la).
- Separação absoluta: nada de telefone, e-mail de recuperação, meio de pagamento, senha ou perfil sincronizado em comum entre identidade real e ambiente de pesquisa.
- **Contas fictícias e interação** — no Brasil, a polícia só pode atuar com identidade dissimulada em interação com investigados mediante autorização judicial (infiltração virtual: Lei 12.850/2013, arts. 10-A a 10-D; ECA, arts. 190-A a 190-E). Observação passiva de conteúdo público não é infiltração. Para particulares (advogados, peritos, jornalistas), perfis falsos violam termos de uso e podem configurar ilícito: avaliar caso a caso. Esta skill não orienta criação de personas para interagir com alvos.
- Graduar a própria exposição: limpa (nada tocou a infraestrutura do alvo) · contato anônimo · contato pseudônimo · atribuído.

## 7. Preservação e cadeia de custódia
Base: CPP, arts. 158-A a 158-F; ABNT NBR ISO/IEC 27037 (identificação, coleta, aquisição e preservação de evidência digital).
- Para cada evidência: URL ou ferramenta e consulta exata; data/hora com fuso; método; ferramenta e versão; responsável.
- Preferir o original (HTML, cabeçalhos, arquivos de mídia, WARC) ao print. Print é ilustração, não prova: a jurisprudência tem exigido integridade e cadeia de custódia para capturas de tela — conferir os precedentes atuais antes de citar.
- Hash SHA-256 de todo arquivo (`sha256sum arquivo` no Linux; `shasum -a 256 arquivo` no macOS; `Get-FileHash -Algorithm SHA256` no Windows). Original intocado, trabalho em cópia.
- Arquivar ao citar (Wayback e archive.today) e manter cópia local: arquivos públicos também são removidos.
- Coleta feita por ferramenta automatizada ou IA deve ser revalidada por agente humano antes de uso probatório.

## 8. Relatório (Relatório Técnico de Inteligência OSINT)
Regras de redação:
- Separar **observação** ("o registro consultado em 30/10/2026 indica…"), **inferência** ("o mesmo e-mail de titular aparece nos dois domínios, logo…") e **avaliação** ("avalia-se como provável, confiança moderada, que…"). "Aparenta ser" é inferência disfarçada de observação.
- **BLUF**: resposta à pergunta no primeiro parágrafo, com probabilidade e confiança.
- **Achados negativos** com escopo e data ("sem registro no CEIS/CNEP em consulta de 30/10/2026"). Distinguir "consultado, ausente" de "não foi possível consultar". Registrar candidatos rejeitados.
- **Método reproduzível**: ferramentas e versões, consultas exatas, cobertura das bases, idiomas, limitações.
- **Minimização**: excluir terceiros não envolvidos; nunca publicar CPF completo, dados bancários, credenciais. Tarjar com registro do motivo.

Estrutura:
1. Identificação (número, data, solicitante, analista, grau de sigilo, destinatários).
2. Pergunta de inteligência e BLUF.
3. Escopo, base legal, limites e o que não foi feito.
4. Metodologia (fontes, ferramentas, versões, período).
5. Achados (fonte, data/hora, grau Almirantado, referência à evidência).
6. Análise (hipóteses, ACH, lacunas, probabilidade e confiança).
7. Achados negativos e candidatos rejeitados.
8. Conclusões e diligências sugeridas (inclusive as que dependem de ordem judicial).
9. Anexos: tabela de evidências com SHA-256, capturas, linha do tempo, grafo de vínculos.

Formato por público: autoridade/gestor = uma página de BLUF; processo judicial = corpo só de observações, inferências rotuladas, cadeia de custódia por item; passagem de caso = grafo + plano de coleta + becos sem saída. Entregar como documento (Docs) por padrão; Word/PDF se pedido.

## 9. Grafo de vínculos
- Um nó por entidade real; apelido é atributo, não nó. Conjunto fechado de tipos de aresta (registrou, hospeda, é sócio de, transferiu para, publicou…).
- Fonte e grau vão **na aresta**. Aresta inferida desenhada diferente da observada.
- Cuidado: hospedagem/registrador/CDN compartilhados não são relação; grafo bonito persuade além da evidência; métricas de centralidade em grafo incompleto enganam.
- Ferramentas: tabelas de nós/arestas + Graphviz ou Gephi (até ~200 nós); Neo4j para consultas de caminho; Maltego se houver licença. No ambiente do Claude, networkx gera o grafo a partir de CSV.

## 10. Ambiente de execução
**Claude Code (máquina local)** — os comandos rodam no computador do usuário, com acesso à rede: exiftool, dig, jq, subfinder, amass, dnsx e a CLI do Shodan podem ser usados, se instalados. Verificar com `which` antes de usar e pedir confirmação antes de instalar algo. O tráfego sai do IP local (ver OPSEC, seção 6) — rede institucional identifica o órgão.

**Claude (web/desktop)** — o ambiente de código roda na nuvem, com acesso restrito à internet (em geral, só repositórios de pacotes e GitHub). Coletar na web pela busca e leitura de páginas do próprio Claude; usar o shell para analisar **arquivos enviados** (exiftool, sha256sum, networkx, jq) e gerar comandos para o usuário rodar na própria máquina.

Em ambos: passividade por padrão (força bruta de DNS, varredura de portas e sondagem HTTP só com autorização escrita) e nada de contornar bloqueios com proxies, caches ou espelhos.

## 11. Uso didático (Pós IA Investigação e Inteligência)
- Exercícios com alvos fictícios ou institucionais, nunca particulares reais.
- Cada exercício: objetivo de aprendizagem, cenário, pergunta de inteligência, fontes permitidas, gabarito comentado, rubrica.
- Conectar, quando útil, ao referencial teórico do curso (Luhmann — abertura cognitiva do sistema jurídico a novas fontes de prova; Wiener — retroalimentação no ciclo de inteligência), sem inventar citações.