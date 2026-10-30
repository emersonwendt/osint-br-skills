#!/usr/bin/env bash
# Copia as skills deste repositório para ~/.claude/skills (Claude Code).
# Uso: ./scripts/instalar-claude-code.sh [--link]
#   --link  cria links simbólicos (git pull atualiza as skills sem reinstalar)
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DESTINO="${HOME}/.claude/skills"
MODO="copia"; [[ "${1:-}" == "--link" ]] && MODO="link"
mkdir -p "$DESTINO"
for d in "$RAIZ"/skills/*/; do
  nome="$(basename "$d")"
  rm -rf "${DESTINO:?}/$nome"
  if [[ "$MODO" == "link" ]]; then ln -s "$d" "$DESTINO/$nome"; else cp -R "$d" "$DESTINO/$nome"; fi
  echo "  instalada: $nome"
done
echo "Pronto. Reabra o Claude Code para carregar as skills."
