---
description: Quick-capture an idea to the idea queue - no triage, just capture
argument-hint: [your idea in a sentence or two]
allowed-tools: Read, Edit, Bash
---

# /idea - capture surface

Capture an idea fast. The discipline is restraint: capture and stop. No
research, no scoring, no project creation - triage happens later.

## Input

The idea is: `$ARGUMENTS`

If that's empty, ask: "What's the idea? One or two sentences." Use the reply.
Max 3 sentences. If I write more, summarise to 3.

## Steps

1. **Do NOT read the whole idea queue.** Append-only discipline - never "read
   the file to add a line".
2. Get today's date: run `date +%Y-%m-%d` (Windows PowerShell:
   `Get-Date -Format 'yyyy-MM-dd'`).
3. Ensure `KB/_Admin/idea-queue.md` exists with a `## Active Ideas` header.
   Run `grep -n "## Active Ideas" KB/_Admin/idea-queue.md`. If the file or
   header is missing, create the file containing:
   `# Idea Queue` then a blank line then `## Active Ideas`.
4. Insert the new bullet immediately after the `## Active Ideas` line (newest
   first) with an Edit that adds ONE line. Do not rewrite the file.
   Format: `- **[YYYY-MM-DD]** {the idea text}`
5. Confirm in ONE line: "Captured."

## Rules

- Capture only. Don't suggest next steps, research, score, or create a project.
- Only ever append one bullet under `## Active Ideas`. Touch nothing else.
