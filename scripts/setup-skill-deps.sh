#!/usr/bin/env bash
#
# Installs the runtime dependencies the bundled skills need.
#
# Only a handful of the skills in .claude/skills ship executable code; the rest
# are prose-only and need nothing. This script covers the ones that do.
#
# Usage: scripts/setup-skill-deps.sh
set -euo pipefail

echo "==> System packages"
# poppler-utils  -> pdftoppm/pdftotext, used by pdf/ and pptx/thumbnail.py
# libreoffice-*  -> docx/pptx/xlsx conversion. libreoffice-core alone cannot
#                   load Writer/Impress documents, so the modules are required.
if command -v apt-get >/dev/null 2>&1; then
  apt-get update -qq
  apt-get install -y -qq \
    poppler-utils \
    libreoffice-writer libreoffice-impress libreoffice-calc
else
  echo "    apt-get not available - install poppler-utils and LibreOffice manually"
fi

echo "==> Python packages"
# playwright is pinned to match the Chromium build already on the image
# (node playwright 1.56.x -> chromium-1194). A different version makes
# p.chromium.launch() fail with "please run playwright install".
PLAYWRIGHT_PIN="playwright==1.56.0"
if [ -d /opt/pw-browsers ]; then
  echo "    pinning $PLAYWRIGHT_PIN to match /opt/pw-browsers"
else
  PLAYWRIGHT_PIN="playwright"
fi

pip3 install --no-input \
  python-docx python-pptx openpyxl \
  pypdf pdfplumber pymupdf pdf2image reportlab \
  pillow imageio imageio-ffmpeg numpy \
  lxml defusedxml beautifulsoup4 pyyaml fonttools \
  anthropic "mcp>=1.1.0,<2" \
  "$PLAYWRIGHT_PIN"

echo "==> Node packages (remembering-conversations tool, optional)"
TOOL_DIR="$(dirname "$0")/../.claude/skills/remembering-conversations/tool"
if [ -f "$TOOL_DIR/package.json" ] && command -v npm >/dev/null 2>&1; then
  (cd "$TOOL_DIR" && npm install --no-audit --no-fund)
else
  echo "    skipped"
fi

echo "==> Done"
