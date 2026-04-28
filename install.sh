#!/usr/bin/env bash
set -euo pipefail

target="${1:-all}"
skill_name="xin-sanguo-chat"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_dir="${repo_root}/${skill_name}"

if [[ ! -f "${source_dir}/SKILL.md" ]]; then
  echo "Cannot find ${skill_name}/SKILL.md. Run this installer from the repository root." >&2
  exit 1
fi

install_skill() {
  local root="$1"
  local destination="${root}/${skill_name}"
  mkdir -p "${destination}"
  cp -R "${source_dir}/." "${destination}/"
  echo "Installed ${skill_name} -> ${destination}"
}

case "${target}" in
  all)
    install_skill "${HOME}/.codex/skills"
    install_skill "${HOME}/.claude/skills"
    install_skill "${HOME}/.openclaw/skills"
    install_skill "${HOME}/.hermes/skills"
    ;;
  codex)
    install_skill "${HOME}/.codex/skills"
    ;;
  claude)
    install_skill "${HOME}/.claude/skills"
    ;;
  openclaw)
    install_skill "${HOME}/.openclaw/skills"
    ;;
  hermes)
    install_skill "${HOME}/.hermes/skills"
    ;;
  agents)
    install_skill "${HOME}/.agents/skills"
    ;;
  *)
    echo "Usage: ./install.sh [all|codex|claude|openclaw|hermes|agents]" >&2
    exit 1
    ;;
esac
