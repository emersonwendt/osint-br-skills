#!/usr/bin/env bash
# Gera em dist/ um .zip por skill (para upload no Claude web/desktop)
# e um .zip com todas as skills (para o Claude Code).
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$RAIZ/dist"
rm -rf "$DIST"; mkdir -p "$DIST"
cd "$RAIZ/skills"
for d in */; do
  nome="${d%/}"
  [[ -f "$nome/SKILL.md" ]] || { echo "ERRO: $nome sem SKILL.md" >&2; exit 1; }
  zip -qr "$DIST/$nome.zip" "$nome" -x '*.DS_Store'
  echo "  $nome.zip"
done
zip -qr "$DIST/skills-osint-br-claude-code.zip" . -x '*.DS_Store'
echo "  skills-osint-br-claude-code.zip"
echo "Pacotes em: $DIST"
