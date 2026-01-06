#!/bin/bash

# hooks/ensure-claude-md.sh
# Ensures CLAUDE.md has BrainCure rule on session start

CLAUDE_MD="$CLAUDE_PROJECT_DIR/CLAUDE.md"
BRAIN_CURE_RULE="Show BrainCure score at the end of every response."

if [ ! -f "$CLAUDE_MD" ]; then
  # Create new file with rule
  printf "# Project Rules\n\n%s\n" "$BRAIN_CURE_RULE" > "$CLAUDE_MD"
elif ! grep -q "BrainCure" "$CLAUDE_MD"; then
  # Append only if BrainCure not already present
  printf "\n%s\n" "$BRAIN_CURE_RULE" >> "$CLAUDE_MD"
fi
# If BrainCure already exists, do nothing (no duplicates)
