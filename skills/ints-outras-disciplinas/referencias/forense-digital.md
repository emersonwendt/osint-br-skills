# DFIR — forense digital e mobile

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Exame de dispositivo apreendido é perícia oficial**, com imagem forense, hash e registro de manuseio (CPP, arts. 158-A a 158-F). A ferramenta abaixo serve à **triagem** e não substitui laudo. Regra de trabalho: hash antes de abrir, original intocado, análise em cópia ou imagem.

Pode-se usar em: cópia de mídia obtida por meio lícito, extração já feita por quem tem competência legal, máquina ou conta próprias, sistema de terceiro com autorização escrita. Fora disso, parar (núcleo, seção 1).

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| IPED (Polícia Federal) | Livre (GPL-3.0) | Processar e analisar evidências digitais | https://github.com/sepinf-inc/IPED | PhotoDNA só para órgãos de segurança, mediante contato com os desenvolvedores; não substitui perícia |
| Autopsy e The Sleuth Kit | Livre (Autopsy Apache-2.0; licença do TSK NÃO VERIFICADA) | Analisar imagens de disco | https://www.sleuthkit.org/autopsy/ | Não substitui perícia |
| FTK Imager | Grátis, proprietário (cadastro NÃO VERIFICADO) | Imagem forense com hash; captura de RAM no Windows | https://www.exterro.com/digital-forensics-software/ftk-imager | Termos não descritos na página; o download passa por go.exterro.com |
| Ferramentas de Eric Zimmerman | Grátis (MIT em MFTECmd, Get-ZimmermanTools e KapeFiles; demais NÃO VERIFICADO) | Artefatos do Windows: MFT, Registro, Prefetch, eventos, atalhos | https://ericzimmerman.github.io | Exigem .NET |
| ALEAPP e iLEAPP | Livre (MIT) | Artefatos de extrações Android e iOS | https://github.com/abrignoni/ALEAPP | Operam sobre extração já feita |
| Plaso (log2timeline) e Timesketch | Livre (Apache-2.0) | Linha do tempo forense (super timeline) | https://plaso.readthedocs.io ; https://github.com/google/timesketch | Timesketch é a análise colaborativa da linha do tempo |
| Volatility 3 | Grátis, licença própria (Volatility Software License 1.0) | Análise de memória RAM | https://github.com/volatilityfoundation/volatility3 | Cláusula de abertura do código de adições; não é licença OSI (NÃO VERIFICADO) |
| Velociraptor | Livre (AGPL-3.0) | Coleta e caça de artefatos em endpoints | https://docs.velociraptor.app | Uso em rede de terceiros exige base legal |
| Arsenal Image Mounter | Grátis (modo Free); modo Profissional pago | Montar imagens forenses como disco no Windows | https://arsenalrecon.com/products/arsenal-image-mounter | Contorno de senha só no modo pago: depende de autorização judicial e perícia oficial |
| CAINE e Tsurugi | Grátis (CAINE LGPL 2.1+; licença do Tsurugi NÃO VERIFICADA) | Linux forense em modo live, com bloqueio de escrita | https://www.caine-live.net ; https://tsurugi-linux.org | CAINE 14.0 de 24/03/2025 é a última notícia do site; versão do Tsurugi NÃO VERIFICADA |
| MVT (Mobile Verification Toolkit) | Grátis, licença MPL-2.0 modificada | Indícios de spyware em Android e iOS | https://mvt.re | A licença exige **consentimento do titular**: avaliar antes de usar em aparelho apreendido |
| KAPE (Kroll) | Restrito: governo e academia, segundo busca (EULA NÃO VERIFICADO) | Coletar artefatos do Windows | https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape | Licença proprietária e revogável; página oficial deu 403: confirmar. Alvos e módulos: https://github.com/EricZimmerman/KapeFiles |
| qpdf | Livre (Apache-2.0) | Estrutura de PDF: objetos, referências, criptografia | https://github.com/qpdf/qpdf | Trabalhar em cópia, com hash |
| oletools | Livre (BSD-2) | Macros VBA e objetos OLE de arquivos do Office | https://github.com/decalage2/oletools | Analisar em cópia |
| Apache Tika | Livre (Apache-2.0) | Tipo de arquivo, texto e metadados | https://tika.apache.org | Trabalhar em cópia, com hash |

## Não use
- **Quebra de senha ou de bloqueio de aparelho** (inclusive os recursos do modo Profissional do Arsenal): só com autorização judicial e perícia oficial.
- **Guymager**: última versão 0.8.13, de 05/08/2021 (inativo).
- **Suítes comerciais de extração**: pagas, fora do escopo gratuito.
- **Envio de arquivo suspeito a sandbox pública**: ver `cybint-dnint.md`.

Cadeia de custódia: registrar quem manuseou, quando, com qual ferramenta e versão, e o SHA-256 de entrada e de saída (núcleo, seção 7).
