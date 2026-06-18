#!/usr/bin/env python3
"""PreToolUse hook — soft-warn on branch mismatch before git commit.

Checks whether the current git branch matches the expected branch
(from .claude/session-state/expected-branch.txt). If they differ,
emits a stderr warning. Does NOT block — exit 0 always.

The expected-branch file is opt-in. If it doesn't exist, the hook
does nothing. Users set it via /nexus-init or manually.
"""

import json
import re
import subprocess
import sys
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
        data = json.loads(sys.stdin.read())
        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})

        if tool_name != "Bash":
            return

        command = tool_input.get("command", "")
        if not re.search(r"git\s+commit", command):
            return

        state_dir = find_state_dir()
        expected_file = state_dir / "expected-branch.txt"

        if not expected_file.exists():
            return

        expected = expected_file.read_text(encoding="utf-8").strip()
        if not expected:
            return

        current = git(["rev-parse", "--abbrev-ref", "HEAD"])
        if not current:
            return

        if current.lower() != expected.lower():
            print(
                f"[nexus] Branch mismatch: expected '{expected}', "
                f"currently on '{current}'. If intentional, update: "
                f"echo '{current}' > .claude/session-state/expected-branch.txt",
                file=sys.stderr,
            )
    except Exception:
        pass


if __name__ == "__main__":
    main()
    sys.exit(0)
