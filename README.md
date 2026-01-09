![BrainCure](brain-cure.jpg)

# 🧠 BrainCure

**Stop outsourcing your thinking to AI.** BrainCure is a Claude Code plugin that scores your prompts and helps you stay in the driver's seat of your projects.

> "AI is a tool, not a replacement for your brain."

## 🤔 Why BrainCure?

When you let AI do all the thinking, you lose:
- Deep understanding of your own codebase
- Problem-solving skills that make you valuable
- The ability to debug when AI gets it wrong

BrainCure gives you real-time feedback on your prompt quality, encouraging you to think first, delegate wisely.

## ✨ Features

- **Automatic Scoring** - Every prompt gets a 0-10 score
- **Session Tracking** - Monitor your average across a session
- **Actionable Feedback** - Know exactly how to improve
- **Drill Sergeant Mode** - Forrest Gump style feedback 🎖️
- **Zero Config** - Works immediately after installation

## 📦 Installation

### From Claude Code

```bash
/plugin marketplace add chadbyte/lab
/plugin install brain-cure
```

### Setup

After installation, add BrainCure to your projects:

```bash
# For all projects (global)
/brain-cure:setup-global

# For current project only
/brain-cure:setup-local
```

### From Source

For contributors or those who want the latest development version:

```bash
# Clone the repository
git clone https://github.com/chadleeshaw/brain-cure.git

# Install as plugin
claude plugin install ./brain-cure

# Verify installation
claude plugin list
```

## 🚀 Usage

Once installed, BrainCure automatically evaluates every prompt:

```
⏺ 📊 BrainCure: 8/10 🦾 Commander
  Session avg: 7.2

⏺ 📝 Nice!
```

### Commands

All commands use the `/brain-cure:` prefix:

| Command | Description |
|---------|-------------|
| `/brain-cure:score` | View session statistics |
| `/brain-cure:reset` | Reset session tracking |
| `/brain-cure:help` | Explain the scoring system |
| `/brain-cure:setup-global` | Add BrainCure to ~/.claude/CLAUDE.md (all projects) |
| `/brain-cure:setup-local` | Add BrainCure to project's CLAUDE.md |
| `/brain-cure:savage` | Enable savage mode (drill sergeant) 🎖️ |

## 📊 Scoring System

```
Base 1 point + pillars (0-9) = max 10 points
Butler Mode: base 0 points → max 9 points
```

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

## 🔍 How It Works

BrainCure evaluates prompts on three pillars:

**For Requests (tasks):**
| Pillar | Question |
|--------|----------|
| Origin | Do you know what the problem is? |
| Destination | Do you know what you want? |
| Boundary | Do you have success/failure criteria? |

**For Questions (exploration):**
| Pillar | Question |
|--------|----------|
| Hypothesis | Do you have your own theory? |
| Scope | Where are you looking? |
| Context | Why are you curious about this? |

### Butler Mode 🛎️

When you ask AI to do something you could easily do yourself (rename a variable, add an import), Butler Mode activates and caps your base score at 0.

## 🎖️ Drill Sergeant Mode

Want feedback from a Marine Corps drill instructor? Enable drill sergeant mode:

```
/brain-cure:savage
```

Scoring stays fair. But feedback comes Forrest Gump style:

**Good prompt (8/10):**
```
⏺ 📊 BrainCure: 8/10 🦾 Commander
  Session avg: 7.2

⏺ 📝 OUTSTANDING, PRIVATE! That's the finest prompt I've seen all day!
```

**Bad prompt (2/10):**
```
⏺ 📊 BrainCure: 2/10 😶‍🌫️ Foggy
  Session avg: 5.2

⏺ 📝 WHAT IS THIS, PRIVATE?! You call this a prompt?! WHERE'S YOUR CONTEXT?!
```

## 🤝 Contributing

Contributions are welcome! See the source repository for development guidelines.

### Project Structure

```
brain-cure/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── hooks/
│   ├── hooks.json            # SessionStart hook config
│   └── ensure-claude-md.sh   # Auto-setup script
├── skills/
│   └── brain-cure/
│       ├── SKILL.md          # Main instructions
│       ├── FRAMEWORK.md      # Evaluation criteria
│       ├── EXAMPLES.md       # Example prompts
│       └── scripts/
│           └── score.py      # Score calculation
├── commands/
│   ├── score.md              # /score command
│   ├── reset.md              # /reset command
│   ├── help.md               # /help command
│   ├── setup-global.md       # /setup-global command
│   ├── setup-local.md        # /setup-local command
│   └── roast.md              # /roast command
└── README.md
```

## 📄 License

MIT
