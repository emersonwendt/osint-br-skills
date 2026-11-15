# TECHINT — equipamentos, patentes, homologação e engenharia reversa

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026.

**Certificado, patente e FCC ID provam o registro do modelo**, não a autenticidade nem a origem do exemplar examinado. **Exame de aparelho apreendido é perícia oficial.** A análise de firmware faz-se em cópia, com hash, cadeia de custódia e autorização cabível. Marcas e titulares de patente no Brasil já aparecem em **osint-midia-e-ativos** (parte B, INPI); aqui entram as buscas técnicas.

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| Anatel, Certifica | Grátis (exige conta gov.br) | Produto de telecomunicações homologado, por número, modelo ou fabricante | https://apps.anatel.gov.br/Certifica/ConsultaPublica.aspx | Substituiu o SCH; se o número estiver nas duas bases, vale o Certifica. Guia que cita só o Mosaico/SCH está desatualizado |
| FCC ID Search e fccid.io | Grátis | Fotos internas, manuais e relatórios de teste de rádio | https://www.fcc.gov/oet/ea/fccid ; https://fccid.io | Página da FCC deu 403 (NÃO VERIFICADA); fccid.io é terceiro sem operador identificado: conferir na FCC. Só mostra o que o fabricante não pediu sigilo |
| INPI, pePI | Grátis; busca anônima pelo botão "Continuar" | Patentes, desenhos industriais e marcas no Brasil | https://busca.inpi.gov.br/pePI/ | Se o acesso anônimo cobre marcas e patentes: NÃO VERIFICADO |
| Google Patents | Grátis (login NÃO VERIFICADO) | Texto integral, com tradução automática | https://patents.google.com | Texto integral menos completo que o bibliográfico; sem garantia de completude |
| Espacenet (EPO) | Grátis (conta NÃO VERIFICADO) | Patentes mundiais, famílias, situação legal INPADOC | https://worldwide.espacenet.com | Página inicial deu 403; gratuidade confirmada em notícia do EPO |
| WIPO PATENTSCOPE | NÃO VERIFICADO (gratuito segundo resumo de busca) | Pedidos PCT e coleções nacionais | https://patentscope.wipo.int | Página de busca deu 403 |
| Lens.org | Grátis só para uso pessoal não comercial | Patentes e literatura científica | https://www.lens.org | Anônimo exporta até 1.000 registros; raspagem e download em massa restritos |
| iFixit | Grátis (CC BY-NC-SA 3.0, NÃO VERIFICADO em página aberta) | Desmontagens com fotos internas de aparelhos | https://www.ifixit.com | Páginas abriram vazias na verificação; uso comercial exige permissão |
| Ghidra (NSA) | Livre (Apache-2.0) | Desmontar e decompilar binários e firmware | https://github.com/NationalSecurityAgency/ghidra | Requer Java; release 12.2 de 22/10/2026 |
| binwalk | Livre (MIT) | Extrair arquivos e sistemas de arquivos embutidos em firmware | https://github.com/ReFirmLabs/binwalk | Última release v3.1.0 (31/10/2024); atividade recente só em commits |
| radare2 e Cutter | Livre (radare2: licença composta; Cutter GPL-3.0) | Engenharia reversa por linha de comando e interface gráfica | https://github.com/radareorg/radare2 ; https://github.com/rizinorg/cutter | Cutter usa o Rizin, não o radare2; curva de aprendizado alta |
| FACT (Fraunhofer FKIE) | Livre (GPL-3.0) | Analisar e comparar imagens de firmware | https://github.com/fkie-cad/FACT_core | Docker e vários serviços: exige infraestrutura |

## Não use
- **Ferramenta feita sobretudo para contornar proteção técnica de dispositivo alheio**: fora do catálogo.
- **Sem confirmação em página aberta, não adotar**: alldatasheet.com e Octopart (403), ODIN/TRADOC (conexão recusada), iTrace/Conflict Armament Research (portal não abriu).
- **Exame de equipamento apreendido por conta própria**: é perícia oficial.
