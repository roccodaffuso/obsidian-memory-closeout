#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_NAME="obsidian-memory-closeout"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
TARGET_DIR="$CLAUDE_HOME/skills/$SKILL_NAME"

mkdir -p "$(dirname "$TARGET_DIR")"
rm -rf "$TARGET_DIR"
cp -R "$REPO_ROOT/skill/$SKILL_NAME" "$TARGET_DIR"

echo "Installed $SKILL_NAME to $TARGET_DIR"
