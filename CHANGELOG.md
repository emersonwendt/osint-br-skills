# Registro de mudanças

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versões seguem [SemVer](https://semver.org/lang/pt-BR/).

## [Não publicado]

## [1.1.0] — 2026-11-15

Contribuição de Alan Douglas Silva (Professor na WB Educação).

### Adicionado
- Skill `osint-identidade-digital` (nome de usuário, e-mail, telefone, perfis públicos e mensageria, nos limites da seção 1 do núcleo).
- Skill `osint-preservacao-evidencias` (captura local, manifesto com SHA-256 e script `manifesto.py` de registro e conferência).
- Skill `ints-outras-disciplinas` (CYBINT/DNINT, forense digital, FININT, GEOINT, IMINT, TECHINT, MASINT, MEDINT/BIOINT, HUMINT e SIGINT abertos), com uma referência por disciplina.
- Agente `analista-osint-br`.
- Plugin do Claude Code (`.claude-plugin/plugin.json`) e marketplace no próprio repositório (`.claude-plugin/marketplace.json`).

### Alterado
- `osint-fontes-abertas`: novas skills no encaminhamento por seletor; preservação sem expor a URL investigada (acionar archive.today ou "Save Page Now" publica a consulta); checagem obrigatória antes de usar ferramenta fora das skills.
- `osint-infraestrutura-digital`: Amass v5 sem `-passive` (conferido no código-fonte), dnsx sem força bruta, arquivos públicos só para o que pode ser exposto.
- `osint-midia-e-ativos`: análise forense local e alerta sobre envio de imagem a buscadores e ao FotoForensics.
- Scripts de instalação copiam também o agente.

## [1.0.0] — 2026-10-30

### Adicionado
- Skill `osint-fontes-abertas` (núcleo: escopo, limites, canais formais, análise, OPSEC, cadeia de custódia, relatório, grafo).
- Skill `osint-infraestrutura-digital` (domínios, DNS, IP/ASN, CT, servidores expostos, arquivos web, pesquisa avançada, Git, roteiro de golpe).
- Skill `osint-midia-e-ativos` (imagens e vídeos, empresas e beneficiário final, criptoativos, aeronaves e embarcações).
- Guia para alunos (`docs/guia-alunos.md`).
- Scripts de empacotamento e instalação.
- Documentos de ética, aviso legal, contribuição, segurança e citação.

### Fontes e normas verificadas nesta versão (30/10/2026)
- RDAP do Registro.br (`rdap.registro.br`).
- Consulta ao RAB da ANAC.
- Resoluções BCB 519, 520 e 521/2025 (em vigor desde 02/02/2026).
- Querido Diário (Open Knowledge Brasil).
