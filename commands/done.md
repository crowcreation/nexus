---
description: Close the session - two minutes to capture what happened and what broke
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /done - session close

The closing ritual. Two minutes, every session. This is where the compounding
comes from: the system only learns what gets written down.

## Steps

1. **Look back over this session** (the conversation, not the whole repo) and
   answer three things in your head:
   - What did we actually do or decide?
   - Did anything break, confuse, or go wrong, even slightly?
   - Is anything half-finished that future-me needs to know about?

2. **Append a daily note.** Get today's date (`date +%Y-%m-%d`, or PowerShell
   `Get-Date -Format 'yyyy-MM-dd'`). Append to `KB/Daily/YYYY-MM-DD.md`
   (create it if missing) a short block:

   ```
   ## Session close - HH:MM
   - Did: {one or two lines}
   - Open: {anything half-finished, or "nothing"}
   ```

   Append-only. Never rewrite earlier entries in the file.

3. **If anything went wrong this session** - a misunderstanding, a wrong
   assumption, lost context, a tool failure, an AI mistake - append ONE entry
   to `failure-log.md`, in plain English:

   ```
   - **YYYY-MM-DD** | {what happened, one line}. Root cause: {best guess}.
   ```

   Then grep the failure log for that root cause. If this is the **third
   occurrence**, say so loudly and propose a one-line prevention rule for
   CLAUDE.md, but let me approve it before writing.

4. **If the session's project moved**, update the **Current state** and
   **Next** sections of its `KB/Projects/<name>/project-overview.md` and bump
   `updated`. Keep it to a line or two.

5. **If this session produced durable knowledge** - a decision with a reason,
   a gotcha, a how-to, a config that took effort to get right - offer to save
   it as `KB/Knowledge/<topic>.md` (one topic per file) and add one line to
   `KB/_Admin/notes-index.md`. This is how the knowledge base grows: through
   use, never pre-filled. Most sessions produce nothing durable, so don't
   force it.

6. **If the world changed** - a new tool wired up, a project started or
   retired - offer to nudge `universe.md` so the map stays living. Only when
   the world actually moved, not every session.

7. Confirm in two lines max: what was logged, and whether a three-occurrence
   alert fired.

## Rules

- Two minutes of output, not an essay. Terse beats thorough here.
- Append-only on the daily note and failure log.
- Never write a CLAUDE.md rule without my approval.
- No failures this session is a fine answer. Don't invent one.
