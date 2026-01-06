# Evaluation Framework

## Background: Why This Framework?

### Problem: The "Hail Mary" Trap

```
Error occurs → Copy-paste dump → Throw at AI → Doesn't work → Throw more → ...
     ↓
Context grows, problem unsolved
     ↓
git reset
     ↓
Project no longer matches my mental map
     ↓
🧠 Brain Rot
```

**Root cause**: When users request without thinking, they can't verify the results either.

### Solution: Tony Stark vs Hail Mary

| Hail Mary | Tony Stark |
|-----------|------------|
| "Fix it" | "I want to solve this problem this way" |
| AI decides | User decides, AI executes |
| Can't verify results | Verify against my own criteria |

**Key**: Tony delegates execution to Jarvis, not thinking.

---

## Scoring System

```
base 1 point + pillars (0-9) = max 10 points
Butler Mode: base 0 points → max 9 points
```

| Score | Title | Meaning |
|-------|-------|---------|
| 10 | 🦸 Tony Stark | Perfect prompt + maintained ownership |
| 9 | 💎 Flawless | Perfect prompt |
| 8 | 🦾 Commander | In command |
| 7 | 🧠 Sharp | Sharp |
| 6 | 🎯 Focused | Focused |
| 5 | 🧭 On Track | On track |
| 4 | 🤔 Getting There | Getting somewhere |
| 3 | 🚶 Wandering | Walking without direction |
| 2 | 😶‍🌫️ Foggy | In the fog |
| 1 | 🎰 Slot Machine | Just pulling the lever |
| 0 | 🙏 Hail Mary | Just praying |

---

## 3 Pillars for Requests

### 1. Origin
> "Do you know what the problem is?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Specific location and symptom | "NullPointerException at UserService.java line 45" |
| 2 | Symptom only | "I get an error when logging in" |
| 1 | Vague mention | "Something's not working" |
| 0 | Nothing | (just dumps error log) |

### 2. Destination
> "Do you know what you want?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Specific result state | "Want to return JWT token on successful login" |
| 2 | Direction only | "Make login work" |
| 1 | Implicit | "Fix it" |
| 0 | Nothing | (just the error) |

### 3. Boundary
> "Do you have success/failure criteria?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Clear constraints and criteria | "Keep existing API spec, tests must pass" |
| 2 | Constraints only | "Don't touch other files" |
| 1 | Implicitly exists | (inferred from conversation context) |
| 0 | Nothing | (thrown without any constraints) |

---

## 3 Pillars for Questions

### 1. Hypothesis
> "Do you have your own theory?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Specific hypothesis | "I think the DB connection pool is exhausted, could it be HikariCP config?" |
| 2 | Direction only | "Seems like a DB issue..." |
| 1 | Vague guess | "Something seems wrong" |
| 0 | Nothing | "Why doesn't it work?" |

### 2. Scope
> "Where are you looking?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Specific file/function/line | "The query in UserRepository.findById() method" |
| 2 | Module/layer level | "In the database layer" |
| 1 | Whole system level | "Somewhere" |
| 0 | Nothing | "I don't know where" |

### 3. Context
> "Why are you curious about this?"

| Score | Criteria | Example |
|-------|----------|---------|
| 3 | Purpose and background stated | "Preparing for load testing, want to check if connection management is the bottleneck" |
| 2 | Purpose only | "Looking at this for performance improvement" |
| 1 | Implicit context | (inferred from conversation flow) |
| 0 | Nothing | (sudden question) |

---

## Butler Mode 🛎️

**Base score 0 when asking AI to do something you could do yourself**

| Situation | Butler Mode |
|-----------|-------------|
| Change a single variable name | ✅ |
| Add one import line | ✅ |
| Move/delete file | ✅ |
| Fix typo | ✅ |
| Complex refactoring | ❌ |
| New feature implementation | ❌ |
| Debugging | ❌ |
| Design decisions | ❌ |

---

## Hail Mary Patterns (Auto Score Cap)

When these patterns are detected, apply score cap:

| Pattern | Cap | Example |
|---------|-----|---------|
| hail_mary | 2 points | Full error dump + "fix it" |
| just_do_it | 1 point | "Just do it", "Figure it out" |
| why_no_context | 1 point | "Why?" with no context |
| copy_paste_loop | 1 point | Consecutive copy-paste (resending previous results as-is) |

---

## Feedback Generation Rules

### Key: Claude Writes It Directly

score.py only provides score and metadata. Claude writes the feedback based on context.

### Approach by Score Range

| Score | Feedback Style |
|-------|----------------|
| 8-10 | **Praise only**. Short like "Nice!" or "On it!" |
| 5-7 | Praise + one light suggestion. Helpful, not nitpicking. |
| 0-4 | Honest feedback + improvement direction. Be specific about what more info is needed. |

### Tone

- Judge ❌ → Coach ✅
- "This is missing" ❌ → "If you tell me this too, I can help more accurately" ✅
- When done well, say it was done well. Don't nitpick every time.

---

## Memory Tool Integration

### File Structure
```
/memories/prompt_scores.json
```

### Schema
```json
{
  "session_id": "uuid",
  "scores": [
    {
      "timestamp": "ISO8601",
      "type": "request|question",
      "pillars": {
        "p1": 2,
        "p2": 3,
        "p3": 1
      },
      "total": 7,
      "butler_mode": false,
      "pattern_detected": "none"
    }
  ],
  "average": 6.7,
  "trend": "improving|stable|declining"
}
```

### Operation
1. Before response: Check `/memories/prompt_scores.json`
2. After evaluation: Add score, recalculate average
3. End of response: Show current score + session average
