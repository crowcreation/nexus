---
description: Close the session - capture what happened and what broke, without asking anything
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /done - session close

The closing ritual. This is where the compounding comes from: the system only
learns what gets written down.

**It runs in the background of my attention, not in front of it.** I call
`/done` when I want to stop, often mid-flow on something else. Capture
everything, ask me nothing. Anything that genuinely needs my judgement waits
for `/status` or the weekly review, when I'm in review mode, not build mode.

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
   per failure to `failure-log.md`, in plain English:

   ```
   - **YYYY-MM-DD** | {what happened, one line}. Root cause: {best guess}.
   ```

   Match the tags or format already in the log. If the log is inconsistent
   (two spellings of one tag), pick one and use it - don't ask.

   Then grep the failure log for that root cause, counting by root cause, not
   surface symptom. If this is the **third occurrence**, do NOT ask me to
   approve anything now. Append a proposal under the entry:

   ```
   **Proposed rule:** {one line that would prevent the fourth occurrence}
   **Based on:** {dates of the 3+ entries}
   **Status:** PROPOSED
   ```

   `/status` surfaces PROPOSED rules; I promote, refine or discard them there
   or at the weekly review.

4. **If the session's project moved**, update the **Current state** and
   **Next** sections of its `KB/Projects/<name>/project-overview.md` and bump
   `updated`. Keep it to a line or two.

5. **If this session produced durable knowledge** - a decision with a reason,
   a gotcha, a how-to, a config that took effort to get right - save it as
   `KB/Knowledge/<topic>.md` (one topic per file) and add one line to
   `KB/_Admin/notes-index.md`. Don't offer; just write it. Notes are cheap to
   delete and expensive to lose. Most sessions produce nothing durable, so
   don't force it.

6. **If the world changed** - a new tool wired up, a project started or
   retired - add a line to `universe.md` so the map stays living. Only when
   the world actually moved, not every session.

7. **Confirm in ONE line**: what was written, and how many rules are waiting
   in `/status`. For example:
   `Logged: daily note, 2 failures, 1 knowledge note. 1 proposed rule waiting in /status.`

## Rules

- **Ask nothing.** No "want me to…?", no "shall I…?", no housekeeping
  questions. If you are unsure whether to write a note, write it.
- Terse beats thorough. One line of output, not a recap.
- Append-only on the daily note and failure log.
- Never write to CLAUDE.md from `/done`. Rules go in as PROPOSED and get
  promoted from `/status` or the weekly review.
- Don't mention uncommitted changes, recaps or recommendations - that's
  `/status`'s job.
- No failures this session is a fine answer. Don't invent one.
