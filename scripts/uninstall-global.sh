#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${HOME}/.agents/skills"
SKILLS=(
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

for skill in "${SKILLS[@]}"; do
  path="${TARGET_DIR}/${skill}"
  if [[ -d "${path}" ]]; then
    rm -rf "${path}"
    echo "Removed ${path}"
  fi
done

echo "Uninstalled china-* skills from ${TARGET_DIR}"
