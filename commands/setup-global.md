---
description: "Add BrainCure rule to global ~/.claude/CLAUDE.md (applies to all projects)"
allowed-tools: Read, Write, Glob
---

# /setup-global

Add BrainCure rule to your global `~/.claude/CLAUDE.md`. This applies to ALL projects.

## What to Add

```markdown
# Project Rules

Apply the brain-cure skill to every response and show the prompt score.
```

## Steps

1. Check if `~/.claude/CLAUDE.md` exists
2. If exists, check if "brain-cure" already mentioned
3. If not present: append the rule
4. If file doesn't exist: create it with the rule
5. If already configured: inform user

## Output

**Success (new file):**
```
✅ Created ~/.claude/CLAUDE.md with BrainCure rule (global)
```

**Success (appended):**
```
✅ Added BrainCure rule to ~/.claude/CLAUDE.md (global)
```

**Already configured:**
```
ℹ️ BrainCure rule already present in ~/.claude/CLAUDE.md
```
