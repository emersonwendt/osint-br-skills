# HUMINT — apoio a entrevistas, fontes e análise

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

Aqui a ferramenta apoia o analista: **transcreve, anota, organiza vínculos e testa hipóteses**. Ela não aborda pessoa. **Infiltração e identidade fictícia dependem de autorização judicial**, como o núcleo já diz (Lei 12.850/2013, arts. 10-A a 10-D; ECA, arts. 190-A a 190-E). Observação passiva de conteúdo público não é infiltração. Contato com o investigado fica fora desta skill.

**Sigilo de fonte.** Usar o fluxo local (whisper.cpp, diagrams.net desktop, yEd, Joplin sem sincronização) e evitar exportação e sincronização em nuvem. A escolha de cada ferramenta cabe à chefia e ao encarregado de dados.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| whisper.cpp | Livre (MIT) | Transcrição de áudio, local, com versão para Windows | https://github.com/ggml-org/whisper.cpp | Modelos baixados uma vez; transcrição automática exige revisão humana |
| Whisper (OpenAI) | Livre (MIT) | Transcrição em Python, na própria máquina | https://github.com/openai/whisper | Exige Python e ffmpeg; uso offline após baixar o modelo NÃO VERIFICADO |
| oTranscribe | Livre (MIT) | Transcrição manual no navegador | https://otranscribe.com | Áudio e texto ficam no navegador; **exportar ao Google Drive envia à nuvem** |
| Obsidian | Grátis, inclusive uso profissional (código fechado) | Anotações de caso em Markdown | https://obsidian.md/pricing | Notas locais; o Sync pago é opcional |
| Joplin | Livre (AGPL-3.0 ou posterior) | Anotações com criptografia de ponta a ponta | https://github.com/laurent22/joplin | Local por padrão; sincronização é opcional |
| diagrams.net (draw.io) | Livre (Apache-2.0; desktop GPL-3.0) | Diagramas de vínculos | https://www.drawio.com | Desktop não envia o diagrama; verifica atualização diariamente (desativável) |
| yEd | Grátis, inclusive uso comercial (proprietário) | Grafo de vínculos com layout automático | https://www.yworks.com/products/yed | Local (Java); o yEd Live (online) não foi avaliado |
| TimelineJS3 | Livre (MPL-2.0) | Linhas do tempo para relatório | https://github.com/NUKnightLab/TimelineJS3 | O fluxo padrão usa Google Sheets (nuvem); há formato JSON alternativo |
| ArkhamMirror (módulo ACH) | Livre (MIT) | Matriz de hipóteses concorrentes, local | https://github.com/mantisfury/ArkhamMirror | Recursos opcionais (OpenAI, Groq, TinEye, SerpAPI) enviam dados à nuvem; exige Docker ou PostgreSQL; projeto de 2025 |
| A Tradecraft Primer (CIA) | Grátis (PDF público) | Técnicas analíticas estruturadas | https://www.cia.gov/resources/csi/books-monographs/a-tradecraft-primer | Guia, não software; termos de uso NÃO VERIFICADOS |
| Red Teaming Handbook (MoD, Reino Unido) | Grátis (OGL v3.0) | Análise crítica e contestação de hipóteses | https://www.gov.uk/government/publications/a-guide-to-red-teaming | Guia, não software; menção expressa a ACH na página não localizada |
| Modelo PEACE (College of Policing) | NÃO VERIFICADO | Entrevista investigativa não acusatória, em cinco fases | https://www.college.police.uk/app/investigation/investigative-interviewing | Página deu 403: gratuidade, licença e texto das fases NÃO VERIFICADOS |

## Não use
- **Identidade fictícia e infiltração**: só com autorização judicial; fora do catálogo.
- **ACH parado ou arquivado**: Open Synthesis (arquivado), ACH de Burton (parado desde 2012), ACH do PARC (endereço de download inacessível).
- **Nuvem para material de fonte sigilosa**: sincronização e exportação em serviço de terceiro.

Hipóteses concorrentes e matriz ACH: núcleo, seção 5. Grafo de vínculos: núcleo, seção 9. Transcrição é dado tratado: revisar com o áudio e indicar a origem (núcleo, seção 7).
