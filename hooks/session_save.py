#!/usr/bin/env python3
"""Stop hook — persist session state for next pre-flight.

Writes .nexus/session-state/last-session.json with current branch,
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


def find_nexus_dir():
    toplevel = git(["rev-parse", "--show-toplevel"])
    if toplevel:
        return Path(toplevel) / ".nexus"
    return Path.cwd() / ".nexus"


def main():
    try:
        nexus_dir = find_nexus_dir()
        state_dir = nexus_dir / "session-state"

        if not nexus_dir.exists():
            return

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
