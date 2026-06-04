#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET_DIR="${HOME}/.agents/skills"

if [[ ! -d "${REPO_ROOT}/.agents/skills" ]]; then
  echo "Cannot find ${REPO_ROOT}/.agents/skills" >&2
  echo "Run this script from a full clone of china-internet-compliance-codex-skills." >&2
  exit 1
fi

mkdir -p "${TARGET_DIR}"
cp -R "${REPO_ROOT}/.agents/skills/." "${TARGET_DIR}/"

echo "Installed china-* skills to ${TARGET_DIR}"
echo "You can now start Codex from any project and call:"
echo '  $china-internet-compliance'
