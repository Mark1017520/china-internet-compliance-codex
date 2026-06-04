#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${HOME}/.agents/skills"
REQUIRED_SKILLS=(
  china-internet-compliance
  china-product-compliance
  china-data-privacy-compliance
  china-ai-algorithm-compliance
  china-content-governance
  china-advertising-marketing
  china-platform-transaction
  china-game-virtual-assets
  china-payment-fintech-adjacent
  china-ip-open-source
  china-vendor-contract
  china-regulatory-response
)

missing=0

echo "Checking global Codex skill installation in ${TARGET_DIR}"

for skill in "${REQUIRED_SKILLS[@]}"; do
  if [[ -f "${TARGET_DIR}/${skill}/SKILL.md" ]]; then
    echo "[OK] ${skill}"
  else
    echo "[MISSING] ${skill}"
    missing=1
  fi
done

if [[ "${missing}" -ne 0 ]]; then
  echo "Some skills are missing. Run ./scripts/install-global.sh from the repository root." >&2
  exit 1
fi

echo "All china-* skills are installed."
