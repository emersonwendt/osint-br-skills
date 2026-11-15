# OSINT-BR — Skills de investigação em fontes abertas para o Claude

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23808035.svg)](https://doi.org/10.5281/zenodo.23808035)

Biblioteca de *skills* (instruções estruturadas para assistentes de IA) para investigação em fontes abertas (OSINT), adaptada às fontes, à legislação e à prática investigativa brasileiras. Funciona no **Claude** (web e desktop) e no **Claude Code**.

> [!IMPORTANT]
> **Leia antes de usar:** [ETICA.md](ETICA.md) (limites de uso) e [AVISO-LEGAL.md](AVISO-LEGAL.md) (isenção de responsabilidade). O uso deste material implica concordância com ambos.

Organização: **Prof. Dr. Emerson Wendt** — PPGD Universidade La Salle. Material didático e de pesquisa para os alunos de todos os cursos do autor: WB Educação, Faculdade Brasileira de Inovação (FABIN) e cursos de formação e capacitação das Polícias e do Ministério Público.

## As skills

| Skill | Para quê | Principais conteúdos |
| --- | --- | --- |
| [`osint-fontes-abertas`](skills/osint-fontes-abertas/SKILL.md) | Núcleo: método | Escopo autorizado, limites, canais formais (Marco Civil, Lei 12.850/2013), ciclo de inteligência, Sistema Almirantado, hipóteses concorrentes, escala de probabilidade, OPSEC, cadeia de custódia (CPP, arts. 158-A a 158-F), relatório, grafo de vínculos |
| [`osint-infraestrutura-digital`](skills/osint-infraestrutura-digital/SKILL.md) | Domínios, sites, servidores | RDAP do Registro.br, DNS, IP/ASN, Certificate Transparency, Shodan/Censys, Wayback e WARC, pesquisa avançada, histórico Git, roteiro de site de golpe |
| [`osint-midia-e-ativos`](skills/osint-midia-e-ativos/SKILL.md) | Imagens, empresas, cripto, veículos | Metadados, busca reversa, autenticidade, geolocalização com pistas brasileiras, CNPJ e beneficiário final, criptoativos (Res. BCB 519–521/2025), aeronaves (RAB/ANAC) e embarcações |
| [`osint-identidade-digital`](skills/osint-identidade-digital/SKILL.md) | Nome de usuário, e-mail, telefone, perfis públicos | Roteiro priorizado por seletor, validação de acertos de enumeração, plataformas e mensageria, ferramentas a evitar |
| [`osint-preservacao-evidencias`](skills/osint-preservacao-evidencias/SKILL.md) | Evidência que não pode se perder | Captura local (SingleFile, WARC, WACZ), sigilo dos arquivos públicos, manifesto com SHA-256 e script de registro e conferência |
| [`ints-outras-disciplinas`](skills/ints-outras-disciplinas/SKILL.md) | Demais disciplinas de inteligência | CYBINT/DNINT, forense digital, FININT, GEOINT, IMINT, TECHINT, MASINT, MEDINT/BIOINT, apoio a HUMINT e SIGINT em transmissões abertas, com o que exige canal formal |

A skill-núcleo vale sempre e encaminha o trabalho para as técnicas conforme o seletor inicial (domínio, imagem, CNPJ, carteira, matrícula de aeronave, nome de usuário).

O agente [`analista-osint-br`](agents/analista-osint-br.md) conduz a investigação do escopo ao relatório, aplicando as skills com coleta passiva, manifesto de evidências e rótulos calibrados (disponível no Claude Code).

## Instalação rápida

**Claude (web e desktop)** — planos Pro, Max, Team e Enterprise:

1. Baixe os seis arquivos `.zip` das skills na página **Releases** deste repositório (ou gere-os com `scripts/empacotar.sh`).
2. No Claude, abra **Settings > Capabilities** e confirme que *Code execution and file creation* está ativo.
3. Em **Skills**, clique em **Upload skill** e envie cada `.zip`.

**Claude Code como plugin** (recomendado; instala as skills e o agente):

```text
/plugin marketplace add emersonwendt/osint-br-skills
/plugin install osint-br@osint-br-skills
```

Use o plugin **ou** a instalação solta abaixo, não as duas: as mesmas skills apareceriam duas vezes.

**Claude Code, instalação solta** (macOS/Linux):

```bash
git clone https://github.com/emersonwendt/osint-br-skills.git
cd osint-br-skills
./scripts/instalar-claude-code.sh
```

No Windows (PowerShell): `.\scripts\instalar-claude-code.ps1`.

Passo a passo completo, testes e exercícios: [docs/guia-alunos.md](docs/guia-alunos.md).

## Estrutura

```
skills/                 as skills (uma pasta por skill, com SKILL.md e, se preciso, referencias/ e scripts/)
agents/                 agente analista (Claude Code)
.claude-plugin/         manifesto do plugin e do marketplace
docs/guia-alunos.md     guia de instalação, uso e aprimoramento
scripts/                empacotamento (zips para o Claude) e instalação no Claude Code
ETICA.md                limites de uso
AVISO-LEGAL.md          isenção de responsabilidade
CONTRIBUTING.md         como propor melhorias
THIRD_PARTY_NOTICES.md  licença do material de terceiros (UseOSINT)
CITATION.cff            como citar
```

## Contribuições

- **Alan Douglas Silva**, Professor na WB Educação (15/11/2026): skills `osint-identidade-digital`, `osint-preservacao-evidencias` e `ints-outras-disciplinas`; agente `analista-osint-br`; empacotamento como plugin do Claude Code; ajustes de sigilo e de ferramentas nas skills existentes. Ferramentas conferidas em página oficial ou repositório na data indicada.

## Contribuir

Melhorias são bem-vindas — especialmente fontes estaduais, correções de fontes desatualizadas e casos de teste fictícios. Veja [CONTRIBUTING.md](CONTRIBUTING.md). Toda contribuição deve respeitar [ETICA.md](ETICA.md).

## Como citar

WENDT, Emerson. **OSINT-BR: skills de investigação em fontes abertas para o Claude**. Versão 1.0.0. Zenodo, 2026. DOI: 10.5281/zenodo.23808036. Disponível em: https://doi.org/10.5281/zenodo.23808036.

Para citar sempre a versão mais recente, use o DOI 10.5281/zenodo.23808035 (https://doi.org/10.5281/zenodo.23808035).

Metadados completos em [CITATION.cff](CITATION.cff).

## Licença e créditos

Distribuído sob a [licença MIT](LICENSE). Parte do conteúdo técnico foi traduzida e adaptada de [UseOSINT/Skills](https://github.com/UseOSINT/Skills) (MIT, © 2026 osint-skills contributors) — aviso integral em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

"Claude" e "Claude Code" são marcas da Anthropic. Este projeto é independente e não tem afiliação, patrocínio ou endosso da Anthropic, da UseOSINT, da Polícia Civil do Rio Grande do Sul ou de qualquer órgão público.
