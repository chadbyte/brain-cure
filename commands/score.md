---
description: "View prompt score session statistics"
---

# /score

Shows prompt score session statistics.

## Usage

```
/score          View session stats
/score reset    Reset session
/score help     Explain scoring system
/score setup    Add BrainCure rule to CLAUDE.md
```

## Behavior

### /score (default)

1. Read `/memories/prompt_scores.json`
2. Output session average, trend, recent scores

**Output example:**
```
📊 BrainCure Session Stats

Average: 7.2/10
Trend: 📈 improving
Prompts: 12

Recent 5: 🦸 10 → 🦾 8 → 🧠 7 → 🦾 8 → 🧠 7
```

### /score reset

Reset session scores. Deletes `/memories/prompt_scores.json`.

```
✅ Session scores have been reset.
```

### /score help

Brief scoring system explanation:

```
📖 BrainCure Scoring System

base 1 point + pillars (0-9) = max 10 points
Butler Mode: base 0 points → max 9 points

| Score | Title |
|-------|-------|
| 10 | 🦸 Tony Stark |
| 9 | 💎 Flawless |
| 8 | 🦾 Commander |
| 7 | 🧠 Sharp |
| 6 | 🎯 Focused |
| 5 | 🧭 On Track |
| 4 | 🤔 Getting There |
| 3 | 🚶 Wandering |
| 2 | 😶‍🌫️ Foggy |
| 1 | 🎰 Slot Machine |
| 0 | 🙏 Hail Mary |

Details: See FRAMEWORK.md
```

### /score setup

Add BrainCure rule to project's `CLAUDE.md`. Creates file if it doesn't exist.

```
✅ BrainCure rule added to CLAUDE.md
```
