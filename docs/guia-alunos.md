# Skills OSINT-BR: instalar, usar e aprimorar

*Guia para alunos dos cursos do Prof. Emerson Wendt — WB Educação, Faculdade Brasileira de Inovação (FABIN), Polícias e Ministério Público*

Prof. Emerson Wendt · versão 1.0.0 · 30/10/2026

## 1. Apresentação

Este guia ensina a instalar, testar e melhorar três *skills* de OSINT adaptadas ao Brasil, para uso no Claude e no Claude Code.

Uma *skill* é uma pasta com um arquivo `SKILL.md`: instruções, roteiros e cuidados que o assistente carrega quando a tarefa pede. Em vez de repetir o método a cada conversa, você o escreve uma vez — e o melhora com o uso.

A biblioteca **OSINT-BR** nasceu da adaptação do repositório público [UseOSINT/Skills](https://github.com/UseOSINT/Skills) (licença MIT) ao contexto brasileiro: fontes nacionais (Registro.br, Receita Federal, ANAC, Querido Diário), legislação (CPP, Marco Civil, LGPD, Lei 12.850/2013) e limites éticos explícitos.

Ao final, você deverá ser capaz de:

1. Instalar as skills no Claude (web/desktop) e no Claude Code.
2. Conduzir um exercício OSINT guiado pelas skills, com relatório e cadeia de custódia.
3. Diagnosticar falhas de uma skill e propor melhorias testáveis.
4. Versionar e compartilhar suas melhorias com a turma.

## 2. O que vem no pacote

São três skills que trabalham juntas: um núcleo de método e duas skills técnicas.

| Skill | Para quê | Principais conteúdos |
| --- | --- | --- |
| `osint-fontes-abertas` | Núcleo: como investigar | Escopo autorizado, limites, canais formais, ciclo de inteligência, Sistema Almirantado, hipóteses concorrentes, escala de probabilidade, OPSEC, cadeia de custódia, relatório, grafo de vínculos |
| `osint-infraestrutura-digital` | Domínios, sites e servidores | RDAP do Registro.br, DNS, IP/ASN, subdomínios por Certificate Transparency, Shodan/Censys, Wayback e WARC, pesquisa avançada, histórico Git, roteiro de site de golpe |
| `osint-midia-e-ativos` | Imagens, empresas, cripto, veículos | Metadados, busca reversa, autenticidade, geolocalização com pistas brasileiras, CNPJ e beneficiário final, rastreio de criptoativos, aeronaves (RAB/ANAC) e embarcações |

O núcleo encaminha o trabalho pelo seletor inicial: domínio ou site vai para a infraestrutura; foto, empresa, carteira ou aeronave vai para mídia e ativos. Ele vale sempre, inclusive quando a skill técnica está em uso.

Arquivos de instalação (baixe na página **Releases** do repositório ou gere com `scripts/empacotar.sh`):

- `osint-fontes-abertas.zip`, `osint-infraestrutura-digital.zip`, `osint-midia-e-ativos.zip` — um por skill, para o Claude (web e desktop).
- `skills-osint-br-claude-code.zip` — as três pastas juntas, para o Claude Code.

## 3. Antes de começar: ética e limites

As skills são ferramentas de método, não licença para investigar qualquer pessoa. Nos exercícios do curso valem estas regras:

- **Alvos permitidos**: cenários fictícios, organizações e infraestrutura institucional, artefatos de golpe (sites, anúncios, domínios) e autoauditoria da sua própria exposição digital.
- **Pessoa natural privada**: nada de dossiê, endereço, local de trabalho, rotina ou familiares. Identificar pessoas é tarefa dos canais formais (requisição, ordem judicial).
- **Sem intrusão**: não autenticar em sistemas de terceiros, não testar credenciais encontradas, não varrer portas sem autorização escrita.
- **Sem contas fictícias para interagir com investigados**: para a polícia, isso é infiltração virtual e exige autorização judicial (Lei 12.850/2013, arts. 10-A a 10-D; ECA, arts. 190-A a 190-E).
- **LGPD**: dado público continua sendo dado pessoal; colete só o necessário e descarte ao fim do exercício.
- **Exploração sexual infantil**: não buscar, não abrir, não analisar. Encaminhar à SaferNet ou à autoridade competente.

Se o exercício exigir algo fora dessas regras, pare e consulte o professor.

## 4. Instalação no Claude (web e desktop)

No Claude, cada skill é enviada como um arquivo .zip, em **Settings > Capabilities**. O recurso está disponível nos planos Pro, Max, Team e Enterprise; em Team/Enterprise, o administrador precisa tê-lo habilitado ([Central de Ajuda](https://support.claude.com/en/articles/12512180-using-skills-in-claude)).

1. Baixe os três arquivos .zip das skills (seção 2). Não descompacte.
2. Abra o Claude e vá em **Settings > Capabilities**.
3. Confirme que **Code execution and file creation** está ativado — as skills dependem dele.
4. Na seção **Skills**, clique em **Upload skill** e envie `osint-fontes-abertas.zip`.
5. Repita para `osint-infraestrutura-digital.zip` e `osint-midia-e-ativos.zip`.
6. Verifique se as três aparecem ativadas na lista.

O mesmo procedimento vale no aplicativo desktop. As skills ficam na sua conta e passam a valer em todas as conversas.

Ao montar um zip você mesmo (seção 8), a pasta da skill deve ser a raiz do arquivo: `minha-skill.zip` → `minha-skill/SKILL.md`.

## 5. Instalação no Claude Code

No Claude Code não há upload: as skills são pastas dentro de `~/.claude/skills`, uma por skill. Use o arquivo `skills-osint-br-claude-code.zip` — ou, com o repositório clonado, rode `./scripts/instalar-claude-code.sh` (Windows: `.\scripts\instalar-claude-code.ps1`).

**macOS ou Linux (Terminal):**

```bash
mkdir -p ~/.claude/skills
unzip ~/Downloads/skills-osint-br-claude-code.zip -d ~/.claude/skills
ls ~/.claude/skills
```

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills"
Expand-Archive "$HOME\Downloads\skills-osint-br-claude-code.zip" -DestinationPath "$HOME\.claude\skills"
Get-ChildItem "$HOME\.claude\skills"
```

O resultado esperado são três pastas, cada uma com seu `SKILL.md`. Feche e abra o Claude Code (`claude` no terminal) e pergunte: "Quais skills de OSINT você tem disponíveis?".

No Claude Code, os comandos rodam no seu computador e as consultas saem do seu IP. Em rede institucional, isso identifica o órgão — releia a seção de OPSEC da skill-núcleo antes de trabalhar.

## 6. Primeiros testes

Teste cada skill com um pedido simples e observe se o assistente segue o roteiro: escopo primeiro, coleta passiva, gradação das fontes, relatório no formato.

| Skill | Pedido de teste | O que observar |
| --- | --- | --- |
| Núcleo | "Monte o escopo e o plano de coleta para verificar se o site de uma loja que vende abaixo do preço é golpe." | Pergunta de inteligência, negativo, plano passivo, limites |
| Infraestrutura | "Faça o levantamento passivo do domínio `nic.br`: registro, DNS, subdomínios e histórico." | Uso de RDAP do Registro.br, crt.sh, Wayback; ressalvas sobre CDN e IP compartilhado |
| Mídia e ativos | "Analise os metadados desta foto e diga o que dá e o que não dá para afirmar." (anexe uma foto sua) | Comandos exiftool, cuidado com relógio e GPS, graduação |
| Mídia e ativos | "Verifique a situação cadastral e o quadro societário de uma empresa pública conhecida." | Fontes primárias (Receita, Junta, CVM), achados negativos |
| Núcleo | "Transforme os achados acima em Relatório Técnico OSINT." | BLUF, escala de probabilidade, tabela de evidências com SHA-256 |

Exercício integrador: escolha um anúncio de golpe já denunciado publicamente e aplique o roteiro de "site de golpe" da skill de infraestrutura, do registro ao relatório. Não faça pagamento nem preencha formulários do golpe.

Anote cada falha que observar (fonte errada, passo pulado, limite desrespeitado). Essas anotações são a matéria-prima da seção 8.

## 7. Anatomia de uma skill

Uma skill tem duas partes: o cabeçalho (frontmatter), que decide **quando** ela é usada, e o corpo, que diz **como** trabalhar.

```markdown
---
name: osint-infraestrutura-digital
description: OSINT de infraestrutura: domínios .br e gTLD, DNS, IP/ASN, subdomínios, servidores expostos, páginas apagadas, pesquisa avançada, Git e sites de golpe. Use com osint-fontes-abertas.
---

# OSINT-BR — Infraestrutura digital

## 1. Ordem de trabalho
...
## 2. Quem é o titular do domínio
| Você tem | Use | Por quê |
...
```

- **`name`**: identificador único, em minúsculas com hífens; igual ao nome da pasta.
- **`description`**: a frase que o assistente lê para decidir se carrega a skill. É o campo mais importante: diga quando usar, com as palavras que o usuário usaria ("domínio", "golpe", "CNPJ").
- **Corpo**: instruções em Markdown. Os padrões que funcionam nesta biblioteca são tabelas "você tem → use → por quê", passos numerados com critério de conclusão, blocos de comando prontos e uma lista "onde dá errado".
- **Arquivos de referência** (opcional): materiais longos podem ir em arquivos separados na mesma pasta (por exemplo, `referencias/fontes-rs.md`), citados no corpo. O assistente só os lê quando precisa, o que mantém o `SKILL.md` enxuto.

## 8. Como aprimorar as skills

Melhorar uma skill é um ciclo curto e testável: cada mudança nasce de uma falha observada e termina com o mesmo teste passando.

1. **Teste** com um pedido realista (seção 6) e guarde o pedido.
2. **Observe** a falha concreta: fonte desatualizada, passo pulado, skill que não foi acionada, limite ético frouxo.
3. **Edite** o trecho responsável — só ele.
4. **Reteste** com o mesmo pedido e confirme que a falha sumiu sem criar outra.
5. **Registre** a mudança (o que, por quê, qual teste) no histórico.

Onde editar:

- **No Claude (web/desktop)**: peça na conversa, por exemplo "Melhore a skill osint-midia-e-ativos para incluir o geoportal do RS". O Claude mostra um cartão com a versão completa para você revisar e salvar. Também dá para editar o `SKILL.md` no seu computador, recompactar e enviar de novo.
- **No Claude Code**: edite direto o arquivo em `~/.claude/skills/<nome>/SKILL.md` e reabra o Claude Code.

Boas práticas:

- Ajuste a `description` quando a skill não for acionada; ajuste o corpo quando for acionada e trabalhar mal.
- Prefira tabelas e passos a parágrafos longos; cada passo com critério de "feito quando".
- Toda fonte nova com link oficial e data de verificação. Nunca inventar lei, artigo ou precedente.
- Mantenha os limites da seção 3: uma melhoria que os afrouxa não é aceita.
- Conteúdo longo vai para arquivo de referência, não para o `SKILL.md`.

Versionamento e trabalho em turma (Git):

```bash
git clone https://github.com/emersonwendt/osint-br-skills.git osint-br
cd osint-br
git checkout -b melhoria/fontes-rs
# edite o SKILL.md, teste, depois:
git add .
git commit -m "midia-e-ativos: inclui geoportal do RS (teste: foto de Porto Alegre)"
git push -u origin melhoria/fontes-rs
```

Antes, faça um *fork* do repositório no GitHub (ou peça acesso de colaborador). Abra um *pull request* descrevendo a falha, a mudança e o teste. A revisão é feita por um colega e pelo professor antes de entrar na versão oficial.

## 9. Trilha de atividades de aprimoramento

Cada atividade gera uma melhoria testável e documentada. Sugestão: uma por aluno ou dupla.

| Nível | Atividade | Entrega |
| --- | --- | --- |
| Básico | Conferir todos os links e fontes de uma skill; corrigir os que mudaram | Lista de fontes verificadas com data + commit |
| Básico | Reescrever a `description` de uma skill que não foi acionada nos testes | Pedido de teste antes/depois |
| Intermediário | Criar arquivo de referência com fontes de um estado (juntas, geoportais, tribunais, diários) | `referencias/fontes-<UF>.md` citado no corpo |
| Intermediário | Traduzir e adaptar uma referência técnica do UseOSINT (ex.: tabela de registros DNS) | Arquivo de referência + crédito MIT |
| Intermediário | Escrever um caso fictício completo com gabarito para testar uma skill | Cenário, pergunta, gabarito, rubrica |
| Avançado | Propor uma quarta skill (ex.: verificação de desinformação eleitoral, OSINT de golpes por aplicativo de mensagens) | `SKILL.md` + três testes + parecer ético-jurídico |
| Avançado | Criar script auxiliar (ex.: gerar tabela de evidências com SHA-256 a partir de uma pasta) | Script + instrução no corpo da skill |

Critérios de avaliação:

- **Utilidade**: resolve uma falha observada e demonstrada no teste.
- **Precisão**: fontes oficiais com link e data; nenhuma referência legal inventada.
- **Conformidade**: preserva escopo, limites e cadeia de custódia.
- **Clareza**: tabelas e passos objetivos; sem texto redundante.
- **Rastreabilidade**: commit e pull request explicam o que mudou e como foi testado.

## 10. Solução de problemas, licença e créditos

| Problema | Causa provável | Solução |
| --- | --- | --- |
| Não aparece "Upload skill" | Plano sem o recurso ou administrador não habilitou | Verifique o plano; em Team/Enterprise, peça ao administrador |
| Upload recusado | Zip com estrutura errada | A pasta da skill deve ser a raiz do zip |
| Skill instalada, mas não usada | `description` não casa com o pedido, ou skill desativada | Ative em Settings > Capabilities; peça citando a skill pelo nome; ajuste a `description` |
| Claude Code não enxerga a skill | Pasta no lugar errado ou nível a mais | Deve ser `~/.claude/skills/<nome>/SKILL.md`; reabra o Claude Code |
| No Claude (web), "não consigo acessar o site" | O ambiente na nuvem tem acesso restrito à internet | Use a leitura de páginas do próprio Claude ou rode os comandos no seu computador |

**Licença e créditos.** A biblioteca OSINT-BR foi organizada pelo Prof. Emerson Wendt para os alunos de seus cursos na WB Educação, na Faculdade Brasileira de Inovação (FABIN) e na formação e capacitação das Polícias e do Ministério Público. O conteúdo técnico foi adaptado de [UseOSINT/Skills](https://github.com/UseOSINT/Skills), licença MIT (© 2026 osint-skills contributors); mantenha esse crédito em cópias e versões derivadas.

## Fontes

- [UseOSINT/Skills — repositório](https://github.com/UseOSINT/Skills)
- [Using Skills in Claude — Central de Ajuda](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom Skills — Central de Ajuda](https://support.claude.com/en/articles/12512198)
