#!/usr/bin/env python3
"""Stop hook — persist session state for next pre-flight.

Writes .claude/session-state/last-session.json with current branch,
HEAD SHA, timestamp, and session ID. The next session's pre-flight
reads this to detect what changed between sessions.

Always exits 0. All errors swallowed.
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


def find_state_dir():
    toplevel = git(["rev-parse", "--show-toplevel"])
    if toplevel:
        return Path(toplevel) / ".claude" / "session-state"
    return Path.cwd() / ".claude" / "session-state"


def main():
    try:
        # Only persist state inside a git repo — outside one there is no
        # stable toplevel to anchor .claude/session-state/ to.
        toplevel = git(["rev-parse", "--show-toplevel"])
        if not toplevel:
            return

        state_dir = find_state_dir()
        state_dir.mkdir(parents=True, exist_ok=True)

        branch = git(["rev-parse", "--abbrev-ref", "HEAD"])
        head_sha = git(["rev-parse", "HEAD"])
        session_id = os.environ.get("CLAUDE_CODE_SESSION_ID", "")

        state = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "branch": branch,
            "head_sha": head_sha,
            "session_id": session_id,
        }

        state_file = state_dir / "last-session.json"
        state_file.write_text(
            json.dumps(state, indent=2) + "\n",
            encoding="utf-8",
        )
    except Exception:
        pass


if __name__ == "__main__":
    main()
    sys.exit(0)
