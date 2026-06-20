---
description: "Bootstrap the KB-root Nexus foundations in this repo — a CLAUDE.md of operating rules, root failure-log.md, the KB/ PARA skeleton, and day-one hygiene files. Idempotent: ensures what's missing, never overwrites."
allowed-tools: ["Write", "Read", "Bash", "Glob"]
---

Scaffold the same KB-root foundations the setup-prompt emits, in one command. Use this when you want the structure without pasting the full setup-prompt interview. It is **idempotent** — it ensures each piece exists and leaves anything already present untouched. There is no dedicated state directory in this model; state lives at the repo root (`failure-log.md`, `universe.md`) and under `.claude/session-state/`.

## Pre-flight checks

Before scaffolding, verify dependencies:

1. Run `python3 --version` (or `python --version` on Windows). If neither works, tell the user: "Python 3.8+ is required for Nexus hooks. Install it from python.org before continuing."
2. Run `git --version`. If it fails, tell the user: "Git is required for session pre-flight and branch verification."
3. Confirm the current directory is a git repo (`git rev-parse --show-toplevel`). If not, suggest `git init`.

Report any missing dependencies before proceeding. All three are required.

## Steps

For each item below, check whether it already exists. If it does, leave it as-is and report "ensured (already present)". Only create what's missing. Never overwrite an existing file.

1. **Root `failure-log.md`** — if absent, create it from the plugin's `templates/failure-log.md`. This is the append-only failure record. `/done` and `/failure` both write here.

2. **`KB/` PARA skeleton** — ensure these folders exist, each with a one-line `README.md` explaining what lives there (only write the README if the folder or README is missing):
   - `KB/Projects/` — time-bounded initiatives with a start and an end.
   - `KB/Areas/` — ongoing responsibilities with no end date.
   - `KB/Knowledge/` — reusable, evergreen reference. Fills through use, never pre-filled.
   - `KB/Goals/` — the outcomes you're working towards.
   - `KB/Daily/` — daily notes; `/done` appends here.
   - `KB/Archive/` — completed or retired material.
   - `KB/_Admin/` — governance, indexes, and house-keeping.

3. **`.gitignore`** — if absent, create it with these entries:

   ```
   .env
   .env.*
   !.env.example
   .auth/
   state/
   .claude/session-state/
   .claude/worktrees/
   __pycache__/
   *.pyc
   .obsidian/workspace*
   .DS_Store
   .tmp/
   ```

   If a `.gitignore` already exists, ensure `.claude/session-state/` is among its entries (append it if missing) and leave the rest alone.

4. **`.env.example`** — if absent, create it with placeholder keys only (NEVER a committed `.env`):

   ```
   ANTHROPIC_API_KEY=
   OPENAI_API_KEY=
   HF_TOKEN=
   GITHUB_TOKEN=
   ```

   with a comment noting these are filled when wiring real tools, not on day one.

5. **`CLAUDE.md`** — if absent, create it from the plugin's `templates/CLAUDE-lite.md`. This holds your operating rules: the five disciplines and the session ritual. (The setup-prompt writes a fuller `CLAUDE.md`; this is the lean starter so the quick path is not rule-less.)

6. **Summary** — print what was created versus what was already present:

   ```
   Nexus KB-root foundations ensured:
     failure-log.md    — append-only failure record (committable)   [created | already present]
     CLAUDE.md         — operating rules (the disciplines)          [created | already present]
     KB/ (PARA)        — Projects/Areas/Knowledge/Goals/Daily/Archive/_Admin  [created | already present]
     .gitignore        — day-one hygiene                             [created | ensured | already present]
     .env.example      — placeholder keys                            [created | already present]

   Next: failures are recorded with /failure (and at session close with /done).
   Pre-flight runs automatically at session start and reads .claude/session-state/.
   ```

7. If the user has an expected working branch, offer to write it to `.claude/session-state/expected-branch.txt` so branch verification activates. Create the `.claude/session-state/` directory if needed.
