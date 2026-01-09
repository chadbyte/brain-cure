---
description: "View prompt score session statistics"
---

# /score

Shows prompt score session statistics.

## Behavior

1. Read `/memories/prompt_scores.json`
2. Output session average, trend, recent scores

## Output

```
📊 BrainCure Session Stats

Average: 7.2/10
Trend: 📈 improving
Prompts: 12

Recent 5: 🦸 10 → 🦾 8 → 🧠 7 → 🦾 8 → 🧠 7
```

## Related Commands

- `/reset` - Reset session scores
- `/help` - Explain scoring system
- `/setup-global` - Add BrainCure rule globally
- `/setup-local` - Add BrainCure rule to this project
- `/savage` - Enable savage mode (drill sergeant)
