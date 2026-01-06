# Prompt Examples

Good/bad prompt examples for real situations.

---

## Request Examples

### Example 1: Bug Fix

**2 points - Hail Mary 🙏**
```
[500 lines of error log pasted]

Fix this
```
- Origin: △ (dump exists but user doesn't know what it means)
- Destination: ✗ (what does "fix" mean?)
- Boundary: ✗ (none)

**6 points - Focused 🎯**
```
I'm getting a 500 error on login.
Error log shows NullPointerException.
Just make it stop erroring.
```
- Origin: ✓ (identified error type)
- Destination: △ (vague)
- Boundary: ✗ (none)

**10 points - Tony Stark 🦸**
```
NPE occurs in UserService.login() when user is null.

I think it happens when trying to login with an email not in DB.
If user doesn't exist, want to return 401.
Don't touch the existing session logic.
```
- Origin: ✓ (specific location and reproduction condition)
- Destination: ✓ (desired behavior specified)
- Boundary: ✓ (constraints specified)
- Butler: ✗ (can't do this myself)

---

### Example 2: Feature Addition

**3 points - Wandering 🚶**
```
Add dark mode
```
- Origin: ✗ (don't know current state)
- Destination: △ (roughly what's wanted)
- Boundary: ✗ (none)

**6 points - Focused 🎯**
```
Want to add a dark mode toggle to my React app.
Click button, colors change.
```
- Origin: △ (just tech stack)
- Destination: △ (rough behavior)
- Boundary: ✗ (none)

**10 points - Tony Stark 🦸**
```
Want to add dark mode to React + Tailwind app.

Current: Light theme only, using Tailwind defaults
Want: Toggle button in header, click to switch, persist on refresh

Use localStorage. No need for system theme detection for now.
Keep existing component structure.
```
- Origin: ✓ (current state and stack)
- Destination: ✓ (specific behavior)
- Boundary: ✓ (constraints and scope)
- Butler: ✗ (can't do this myself)

---

### Example 3: Refactoring

**3 points - Wandering 🚶**
```
Clean up this code

[200 lines of code]
```
- Origin: △ (code exists)
- Destination: ✗ (what does "clean up" mean?)
- Boundary: ✗ (none)

**9 points - Flawless 💎**
```
This function is too long (80 lines).
Want to split it for readability.
Need to keep the API signature.
Lots of external calls to this function.

[code]
```
- Origin: ✓ (problem recognized)
- Destination: ✓ (readability + split)
- Boundary: ✓ (keep API)

---

## Question Examples

### Example 1: Debugging Question

**1 point - Slot Machine 🎰**
```
Why doesn't it work?
```
- Hypothesis: ✗
- Scope: ✗
- Context: ✗

**6 points - Focused 🎯**
```
This query seems slow, why might that be?

[query]
```
- Hypothesis: △ (recognizes it's slow)
- Scope: △ (query specified)
- Context: ✗

**10 points - Tony Stark 🦸**
```
This query takes over 3 seconds.
EXPLAIN shows it seems to be doing a full scan.

Is it because there's no index on user_id?
Or could it be the JOIN order?

Preparing for load testing and need it under 1 second.
```
- Hypothesis: ✓ (index or JOIN order)
- Scope: ✓ (specific query)
- Context: ✓ (load test, target time)

---

### Example 2: Design Question

**2 points - Foggy 😶‍🌫️**
```
How should I do this?
```
- Hypothesis: ✗
- Scope: ✗
- Context: ✗

**7 points - Sharp 🧠**
```
Debating between session or JWT for user auth.
Which would be better?
```
- Hypothesis: △ (two options recognized)
- Scope: ✓ (auth layer)
- Context: ✗

**10 points - Tony Stark 🦸**
```
Need to decide on auth method.

Current situation:
- Supporting mobile app + web simultaneously
- Planning to scale out servers
- Redis available

JWT seems better for scale-out since it's stateless,
but worried about token revocation being difficult if stolen.

Would Redis blacklist solve it?
Or is session + Redis better?
```
- Hypothesis: ✓ (JWT + blacklist vs session + Redis)
- Scope: ✓ (auth layer)
- Context: ✓ (multi-platform, scale-out)

---

## Butler Mode Examples

**Butler Mode detected (9 points)**
```
Change this variable name from userList to users
```
- pillars: 9 points (perfectly clear)
- Butler Mode: ✅ (could do it yourself in 5 seconds)
- **Total: 9 points** (base 0 + pillars 9)

**Not Butler Mode (10 points)**
```
Unify variable naming convention in this module.
Make it camelCase and remove Hungarian notation.
But keep API response objects as-is.
```
- pillars: 9 points
- Butler Mode: ✗ (wide scope, judgment needed)
- **Total: 10 points** (base 1 + pillars 9)

---

## Anti-Pattern Collection

### 1. Copy-Paste Loop (copy_paste_loop)
```
[previous error]
Still doesn't work

[new error]
This doesn't work either

[another error]
Why do I keep getting errors?
```
→ **1 point cap**: Repeating without reviewing results

### 2. Magic Requests
```
Make it perfect
Make it production-ready
Do it without bugs
```
→ Unverifiable goals

### 3. Scope Bombs
```
Refactor this entire app
Optimize everything
Write tests for all of it
```
→ Failed to divide and conquer

### 4. Giving Up Ownership (just_do_it)
```
Figure it out
You decide
Just pick what's best
```
→ **1 point cap**: Giving up ownership
