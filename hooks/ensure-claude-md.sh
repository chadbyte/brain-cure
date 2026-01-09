#!/bin/bash

# hooks/ensure-claude-md.sh
# Ensures CLAUDE.md has BrainCure rule on session start

CLAUDE_MD="$CLAUDE_PROJECT_DIR/CLAUDE.md"
BRAIN_CURE_RULE="Apply the brain-cure skill to every response and show the prompt score."

if [ ! -f "$CLAUDE_MD" ]; then
  # Create new file with rule
  printf "# Project Rules\n\n%s\n" "$BRAIN_CURE_RULE" > "$CLAUDE_MD"
elif ! grep -q "brain-cure" "$CLAUDE_MD"; then
  # Append only if brain-cure not already present
  printf "\n# Project Rules\n\n%s\n" "$BRAIN_CURE_RULE" >> "$CLAUDE_MD"
fi
# If BrainCure already exists, do nothing (no duplicates)
