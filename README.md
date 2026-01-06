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
- **Zero Config** - Works immediately after installation

## 📦 Installation

### From Marketplace

```bash
claude plugin add brain-cure
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

#### Development Setup

```bash
# Symlink for instant updates during development
ln -s /path/to/brain-cure/skills/brain-cure ~/.claude/skills/brain-cure

# Changes apply after restarting Claude Code
```

## 🚀 Usage

Once installed, BrainCure automatically evaluates every prompt:

```
⏺ 📊 BrainCure: 8/10 🦾 Commander
  ⎿ Session avg: 7.2
⏺ 📝 Nice!
```

### Commands

| Command | Description |
|---------|-------------|
| `/score` | View session statistics |
| `/score reset` | Reset session tracking |
| `/score help` | Explain the scoring system |
| `/score setup` | Add BrainCure rule to CLAUDE.md |

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

1. **Context** - Did you provide enough background?
2. **Constraints** - Did you set clear boundaries?
3. **Ownership** - Are you directing, or just delegating?

The plugin automatically adds its evaluation rule to your project's CLAUDE.md on session start.

## 🤝 Contributing

Contributions are welcome! See the source repository for development guidelines.

### Project Structure

```
brain-cure/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── hooks/
│   ├── hooks.json           # SessionStart hook config
│   └── ensure-claude-md.sh  # Auto-setup script
├── skills/
│   └── brain-cure/
│       ├── SKILL.md         # Main instructions
│       ├── FRAMEWORK.md     # Evaluation criteria
│       ├── EXAMPLES.md      # Example prompts
│       └── scripts/
│           └── score.py     # Score calculation
├── commands/
│   └── score.md             # /score slash command
└── README.md
```

## 📄 License

MIT
