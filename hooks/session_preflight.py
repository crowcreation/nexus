#!/usr/bin/env python3
"""SessionStart hook — pre-flight context verification.

Checks three things at session start:
1. Current git branch
2. What changed since last session (commits, branch switches)
3. Whether the last session was recent enough to trust its context

Outputs context via hookSpecificOutput.additionalContext so Claude
reads it as part of the session. Never blocks — always exits 0.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def git(args):
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True, text=True, timeout=5, check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return ""


def find_nexus_dir():
    toplevel = git(["rev-parse", "--show-toplevel"])
    if toplevel:
        return Path(toplevel) / ".nexus"
    return Path.cwd() / ".nexus"


def load_last_session(nexus_dir):
    state_file = nexus_dir / "session-state" / "last-session.json"
    if state_file.exists():
        try:
            return json.loads(state_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    return None


def main():
    try:
        nexus_dir = find_nexus_dir()
        lines = []

        branch = git(["rev-parse", "--abbrev-ref", "HEAD"])
        head = git(["rev-parse", "--short", "HEAD"])

        if not branch:
            print(json.dumps({}))
            return

        lines.append(f"Branch: {branch} ({head})")

        last = load_last_session(nexus_dir)

        if last:
            last_branch = last.get("branch", "")
            last_head = last.get("head_sha", "")[:7]
            last_time = last.get("timestamp", "")

            if last_branch and last_branch != branch:
                lines.append(
                    f"Branch changed: was '{last_branch}', now '{branch}'"
                )

            if last_head and last_head != head:
                log = git([
                    "log", "--oneline",
                    f"{last_head}..HEAD",
                ])
                if log:
                    commit_count = len(log.strip().splitlines())
                    lines.append(
                        f"{commit_count} commit(s) since last session"
                    )
                else:
                    lines.append("HEAD changed since last session")

            if last_time:
                try:
                    ts = datetime.fromisoformat(
                        last_time.replace("Z", "+00:00")
                    )
                    age_hours = (
                        datetime.now(timezone.utc) - ts
                    ).total_seconds() / 3600
                    if age_hours > 24:
                        lines.append(
                            f"Last session was {age_hours:.0f}h ago "
                            "— assumptions may be stale"
                        )
                except Exception:
                    pass

            expected_branch_file = (
                nexus_dir / "session-state" / "expected-branch.txt"
            )
            if expected_branch_file.exists():
                expected = expected_branch_file.read_text(
                    encoding="utf-8"
                ).strip()
                if expected and expected != branch:
                    lines.append(
                        f"Expected branch '{expected}', currently on "
                        f"'{branch}' — verify before committing"
                    )
        elif not nexus_dir.exists():
            lines.append(
                "No .nexus/ directory found. Run /nexus-init to set up "
                "failure logging and session tracking."
            )
        else:
            lines.append("First session with Nexus tracking.")

        recent_log = git(["log", "--oneline", "-5"])
        if recent_log:
            lines.append(f"Recent commits:\n{recent_log}")

        context = "[nexus pre-flight] " + " | ".join(
            l for l in lines if "\n" not in l
        )
        if recent_log:
            context += f"\nRecent commits:\n{recent_log}"

        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": context,
            }
        }
        print(json.dumps(output))

    except Exception:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
            }
        }))


if __name__ == "__main__":
    main()
    sys.exit(0)
