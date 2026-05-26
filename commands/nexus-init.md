---
description: "Initialize the .nexus/ directory with default config, empty failure log, and session state directory."
allowed-tools: ["Write", "Read", "Bash", "Glob"]
---

Set up the Nexus operational discipline directory for this project.

## Pre-flight checks

Before scaffolding, verify dependencies:

1. Run `python3 --version` (or `python --version` on Windows). If neither works, tell the user: "Python 3.8+ is required for Nexus hooks. Install it from python.org before continuing."
2. Run `git --version`. If it fails, tell the user: "Git is required for session pre-flight and branch verification."
3. Confirm the current directory is a git repo (`git rev-parse --show-toplevel`). If not, suggest `git init`.

Report any missing dependencies before proceeding. All three are required.

## Steps

1. Check if `.nexus/` already exists in the project root. If it does, ask the user whether to overwrite or skip.

2. Create the following structure:
   - `.nexus/config.json` — copy from the plugin's `templates/config.json`:

     ```json
     {
       "failure_log_path": ".nexus/failure-log.md",
       "expected_branch_path": ".nexus/session-state/expected-branch.txt",
       "three_occurrence_threshold": 3
     }
     ```

   - `.nexus/failure-log.md` — copy from the plugin's `templates/failure-log.md` (the starter template with category codes table and empty log)
   - `.nexus/session-state/` — create this directory (it will hold ephemeral per-machine state)

3. Suggest adding `.nexus/session-state/` to `.gitignore` (session state is per-machine, not shareable). The config and failure log ARE committable.

4. Print a summary:

   ```
   .nexus/ initialized:
     config.json       — plugin configuration (committable)
     failure-log.md    — append-only failure record (committable)
     session-state/    — ephemeral session tracking (add to .gitignore)

   Next: failures are recorded with /failure. Pre-flight runs automatically at session start.
   Map your tools, repos, and projects with /nexus-onboard.
   ```

5. If the user has an expected working branch, offer to write it to `.nexus/session-state/expected-branch.txt` so branch verification activates.
