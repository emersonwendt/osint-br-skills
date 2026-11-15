# IMINT — forense de imagem local e verificação

Referência da skill **ints-outras-disciplinas**. Vale o núcleo (osint-fontes-abertas). Verificado em 15/11/2026. Complementa **osint-midia-e-ativos**, parte A (metadados com exiftool e ffprobe, origem, autenticidade, geolocalização). Aqui entram as ferramentas e suas condições.

**Regras.**
1. **Detector de IA ou de deepfake não é prova.** O resultado é probabilístico, varia entre execuções e pode errar por grupo demográfico.
2. **Ampliação por IA inventa detalhe.** Serve só como pista, nunca como prova, e não substitui perícia.
3. **Caso sigiloso: só ferramenta local.** Calcular o hash antes de qualquer análise. Serviço marcado "envia" recebe o arquivo.
4. Trabalhar em cópia e registrar cada operação aplicada. Não reconhecer rosto (núcleo e midia-e-ativos).

| Ferramenta | Gratuidade | Para quê | Link | Cuidado |
|---|---|---|---|---|
| Sherloq | Livre (GPL-3.0) | Bancada local: ELA, PRNU, copy-move, JPEG ghost | https://github.com/GuidoBartoli/sherloq | Não é detector automático; sem releases; último commit 16/07/2026 |
| FFmpeg / ffprobe | Livre (LGPL 2.1+; partes GPL) | Quadros, fluxos e metadados de vídeo; hash de quadros | https://ffmpeg.org | Extrair quadros-chave para busca reversa |
| MediaInfo | Livre (estilo BSD) | Codecs, contêiner e marcas de tempo | https://mediaarea.net/en/MediaInfo | Usar a versão instalada, **não o MediaInfoOnline** (tratamento do arquivo não verificado) |
| c2patool | Livre (Apache-2.0 ou MIT) | Validar manifesto C2PA | https://github.com/contentauth/c2patool | Ausência de manifesto não prova adulteração nem autenticidade |
| ImageMagick (`identify`) | Livre (licença ImageMagick) | Formato, perfis, compressão | https://imagemagick.org | Local |
| OpenCV img_hash | Livre (Apache-2.0) | Hash perceptual para comparar imagens | https://github.com/opencv/opencv_contrib/tree/master/modules/img_hash | **Não usar em rostos** |
| TruFor (GRIP-UNINA) | Só não comercial e sem fins lucrativos | Localizar falsificação em imagem | https://github.com/grip-unina/TruFor | Local (Docker, PyTorch); LICENSE.txt não lido: confirmar; último commit 29/05/2025 |
| InVID-WeVerify | Livre (MIT) | Plugin de verificação de vídeo e imagem | https://github.com/AFP-Medialab/verification-plugin | Envio de dados a terceiros não registrado na pesquisa: conferir antes de usar com material de caso |
| TinEye | Só não comercial (100 buscas/dia) | Busca reversa; ordena pela mais antiga | https://tineye.com | Não guarda a imagem enviada, segundo a página; ainda é envio a terceiro |
| Google Lens, Bing Visual, Yandex | Grátis | Busca reversa | https://support.google.com/websearch/answer/1325808 | **Envia a terceiro**; sem rostos |
| Search by Image (extensão) | Livre (GPL-3.0) | Mais de 30 buscadores reversos em um clique | https://github.com/dessant/search-by-image | Envia imagem ou URL aos buscadores escolhidos; v8.5.4 de 16/06/2026 |
| RevEye (extensão) | Livre (GPL-3.0) | Abre a imagem em Google, Bing, Yandex e TinEye | https://github.com/steven2358/reveye | Baixa atividade (agosto de 2024); repassa a URL a terceiros; sem Baidu |
| Baidu Images | Grátis (conta NÃO VERIFICADO) | Busca reversa de conteúdo chinês | https://graph.baidu.com/pcpage/index?tpl_from=pc | Interface em chinês; botão de envio NÃO VERIFICADO; envia a terceiro (China) |
| Frame By Frame (extensão) | Livre (MIT) | Vídeo quadro a quadro | https://addons.mozilla.org/addon/frame-by-frame/ | Pede acesso a dados de todos os sites; sem atualização desde 17/08/2022 |
| GIMP | Livre (GPL) | Recorte, curvas e nitidez | https://www.gimp.org | Sempre em cópia |
| darktable | Livre (GPL-3.0) | RAW, edição não destrutiva com histórico | https://www.darktable.org | A função "neural restore" (IA) inventa detalhe |
| Upscayl, Real-ESRGAN, Video2X | Livre (AGPL-3.0; BSD-3-Clause; AGPL-3.0) | Ampliação de imagem e vídeo por IA | https://github.com/upscayl/upscayl ; https://github.com/xinntao/Real-ESRGAN ; https://github.com/k4yt3x/video2x | **A IA cria detalhe inexistente.** Executáveis locais; versão Cloud e demos online enviam o arquivo; Real-ESRGAN praticamente parado |
| Content Credentials Verify | Grátis | Procedência C2PA | https://verify.contentauthenticity.org | Envio e retenção NÃO VERIFICADOS: presumir envio a terceiro |
| DeepFake-o-Meter | Grátis, sem fins lucrativos (cadastro) | Vários detectores de deepfake | https://zinc.cse.buffalo.edu/ubmdfl/deep-o-meter/ | **Envia o arquivo** (EUA); resultado inconsistente, sem valor conclusivo |
| Hive AI Detector | Demonstração e extensão grátis; API paga | Estimar se é gerado por IA | https://hivemoderation.com/ai-generated-content-detection | **Envia o arquivo**; limites e política de dados NÃO VERIFICADOS |
| Picarta | Freemium (coordenada exata exige conta e plano) | Estimar o local da foto por IA | https://picarta.ai | **Envia a imagem**; estimativa, não prova |

## Não use
- **PimEyes e FaceCheck.ID**: reconhecimento facial; dado biométrico é sensível (LGPD, art. 5º, II: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm, acesso em 15/11/2026).
- **FotoForensics**: envios públicos e veda uso jurídico.
- **Parados ou encerrados**: JPEGsnoop (2018), Ghiro (2016), TrueMedia.org (serviço encerrado), Watch Frame by Frame e Amnesty YouTube DataViewer (descontinuados).
- **GeoSpy/Raven**: não é gratuito; só órgãos governamentais e empresas, mediante licença.
- **Sensity**: comercial.
