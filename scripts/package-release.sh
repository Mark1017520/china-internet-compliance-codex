#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
VERSION="${1:-V1.0.0}"
DIST_DIR="${REPO_ROOT}/dist"
PACKAGE_NAME="china-internet-compliance-codex-${VERSION}"
PACKAGE_PATH="${DIST_DIR}/${PACKAGE_NAME}.zip"

mkdir -p "${DIST_DIR}"
rm -f "${PACKAGE_PATH}"

cd "${REPO_ROOT}"

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Warning: uncommitted changes are not included because this package is built from HEAD." >&2
fi

git archive \
  --format=zip \
  --output="${PACKAGE_PATH}" \
  --prefix="${PACKAGE_NAME}/" \
  HEAD

echo "Created ${PACKAGE_PATH}"
