---
description: "Add BrainCure rule to project's CLAUDE.md (this project only)"
allowed-tools: Read, Write, Glob
---

# /setup-local

Add BrainCure rule to the current project's `CLAUDE.md`. This applies to this project only.

## What to Add

```markdown
# Project Rules

Apply the brain-cure skill to every response and show the prompt score.
```

## Steps

1. Check if `CLAUDE.md` exists in project root
2. If exists, check if "brain-cure" already mentioned
3. If not present: append the rule
4. If file doesn't exist: create it with the rule
5. If already configured: inform user

## Output

**Success (new file):**
```
✅ Created CLAUDE.md with BrainCure rule (local)
```

**Success (appended):**
```
✅ Added BrainCure rule to CLAUDE.md (local)
```

**Already configured:**
```
ℹ️ BrainCure rule already present in CLAUDE.md
```
