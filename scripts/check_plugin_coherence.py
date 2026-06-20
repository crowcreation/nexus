#!/usr/bin/env python3
"""Coherence check for the Nexus plugin.

Loads nexus.structure.json (the single source of structural truth) and asserts
that every consumer in the repo agrees with it. The plugin restates its own
structure in many places: markdown commands describe paths in prose, hooks
hardcode them in Python, docs reference them in links. Nothing imports the JSON,
so the JSON is only canonical because this check makes deviation fail.

Why it exists: the 0.5.0 to 0.6.0 reconciliation happened because two state
models (a `.nexus/` directory and the KB-root structure) had been living in one
plugin for weeks without anyone noticing. This check is the rule written so that
class of silent drift cannot happen a third time.

Zero dependencies. Standard library only — no network, no third-party packages,
matching the hooks' design. Run it directly:

    python scripts/check_plugin_coherence.py

Exits 0 when every consumer agrees with nexus.structure.json. Exits 1 with a
precise diff when something has drifted. Advisory findings (the scaffolder PARA
check) print as warnings and never change the exit code.
"""

import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
STRUCTURE_FILE = REPO_ROOT / "nexus.structure.json"

# ---------------------------------------------------------------------------
# Consumer allowlists. These are the files Phase A reconciled (the 9 functional
# files) plus the failure-log referencers (~13). They are listed explicitly so a
# reviewer can see exactly what the check covers, and so a NEW consumer that
# forgets to agree with the structure is a visible omission, not a silent gap.
# ---------------------------------------------------------------------------

# Files whose drift state-paths matter. ROADMAP.md is deliberately excluded from
# the `.nexus/` ban: it carries the single permitted historical mention in its
# "Retired commands" note. The check script itself lives under scripts/ and is
# pruned from the walk (it necessarily contains the string it searches for).
NEXUS_BAN_EXCLUDE_DIRS = {".git", "scripts", "images", ".obsidian", "node_modules"}
NEXUS_BAN_EXCLUDE_FILES = {"ROADMAP.md", "nexus.structure.json"}
NEXUS_BAN_EXTS = {".md", ".py", ".json"}

# The three hooks must each anchor session state at the declared session_state_dir.
HOOK_FILES = [
    "hooks/session_preflight.py",
    "hooks/branch_verify.py",
    "hooks/session_save.py",
]

# The scaffolders that emit the PARA skeleton (advisory check only — the
# setup-prompt is LLM prose, so we can flag a missing folder name but cannot
# prove the scaffold actually emits it).
SCAFFOLDER_FILES = [
    "setup-prompt.md",
    "commands/nexus-init.md",
]

# Files that state the drift-category vocabulary. Per the category decision,
# categories are an OPTIONAL, emergent vocabulary — never imposed on a day-one
# log. Where the vocabulary is stated, it must be the same seven codes. The seed
# template (templates/failure-log.md) lists them only in an explicitly-optional
# pointer; it is checked here for vocabulary agreement AND, separately, asserted
# to keep a category-free entry format.
DRIFT_VOCAB_FILES = [
    "skills/failure-logging/SKILL.md",
    "templates/CLAUDE-lite.md",
    "commands/failure.md",
    "templates/failure-log.md",
]

# Directory prefixes allowed in front of `failure-log.md`. The empty prefix is
# the canonical root state path. The rest are legitimate documentation links
# pointing at the repo's own template and pattern files.
ALLOWED_LOG_PREFIXES = {
    "",
    "./",
    "templates/",
    "../templates/",
    "patterns/",
    "../patterns/",
}

_LOG_PATH_RE = re.compile(r"((?:[\w.@~-]+/)*)failure-log\.md")
_NEXUS_RE = re.compile(r"\.nexus/")

# Drift-code extraction patterns (see extract_drift_codes).
_TABLE_CELL_RE = re.compile(r"(?m)^\|\s*([A-Z]{2})\s*\|")
_PAREN_LIST_RE = re.compile(r"\(([A-Z]{2}(?:,\s*[A-Z]{2}){2,})\)")
_PIPE_LIST_RE = re.compile(r"([A-Z]{2}(?:\|[A-Z]{2}){2,})")


class Result:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.checks_run = 0

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def ok(self):
        self.checks_run += 1


def read_text(relpath):
    path = REPO_ROOT / relpath
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def extract_drift_codes(text):
    """Collect drift codes stated in a recognised category context.

    Three forms cover every statement in the repo: a markdown table whose first
    cell is the code, a parenthesised comma list `(SS, CF, ...)`, and a
    pipe-delimited list `SS|CF|...`. Plain `CODE (Name)` prose pairs are not
    parsed — they never introduce a code the other forms miss.
    """
    codes = set()
    for m in _TABLE_CELL_RE.finditer(text):
        codes.add(m.group(1))
    for m in _PAREN_LIST_RE.finditer(text):
        codes.update(c.strip() for c in m.group(1).split(","))
    for m in _PIPE_LIST_RE.finditer(text):
        codes.update(m.group(1).split("|"))
    return codes


def check_structure_file(result):
    """The structure file itself must parse and declare every required key."""
    required = [
        "failure_log_path",
        "session_state_dir",
        "universe_path",
        "para_folders",
        "frontmatter_fields",
        "commands",
        "drift_categories",
    ]
    missing = [k for k in required if k not in STRUCTURE]
    if missing:
        result.error(
            f"nexus.structure.json is missing required key(s): {', '.join(missing)}"
        )
    else:
        result.ok()


def check_no_nexus_state(result):
    """(1) No functional `.nexus/<state>` reference remains anywhere."""
    found = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NEXUS_BAN_EXCLUDE_DIRS]
        for name in filenames:
            if Path(name).suffix not in NEXUS_BAN_EXTS:
                continue
            rel = Path(dirpath, name).relative_to(REPO_ROOT).as_posix()
            if rel in NEXUS_BAN_EXCLUDE_FILES:
                continue
            text = (REPO_ROOT / rel).read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                if _NEXUS_RE.search(line):
                    found.append(f"  {rel}:{i}: {line.strip()}")
    if found:
        result.error(
            "Stale `.nexus/` state reference(s) found (the KB-root model uses "
            "root `failure-log.md` / `universe.md` and `.claude/session-state/`):\n"
            + "\n".join(found)
        )
    else:
        result.ok()


def check_failure_log_path(result):
    """(2) The failure-log path string is identical across all consumers."""
    declared = STRUCTURE.get("failure_log_path", "failure-log.md")
    if declared != "failure-log.md":
        result.error(
            f"nexus.structure.json failure_log_path is '{declared}', expected the "
            "root 'failure-log.md' for the KB-root model."
        )
        return
    bad = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in NEXUS_BAN_EXCLUDE_DIRS]
        for name in filenames:
            if Path(name).suffix not in NEXUS_BAN_EXTS:
                continue
            rel = Path(dirpath, name).relative_to(REPO_ROOT).as_posix()
            text = (REPO_ROOT / rel).read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                for m in _LOG_PATH_RE.finditer(line):
                    prefix = m.group(1)
                    if prefix not in ALLOWED_LOG_PREFIXES:
                        bad.append(
                            f"  {rel}:{i}: path '{prefix}failure-log.md' "
                            f"(expected root 'failure-log.md')"
                        )
    if bad:
        result.error(
            "failure-log.md referenced at a non-root path (the log lives at the "
            "repo root under the KB-root model):\n" + "\n".join(bad)
        )
    else:
        result.ok()


def check_commands(result):
    """(3) The command set matches the JSON and the README references."""
    declared = sorted(STRUCTURE.get("commands", []))
    cmd_dir = REPO_ROOT / "commands"
    on_disk = sorted(p.stem for p in cmd_dir.glob("*.md"))
    if on_disk != declared:
        missing = sorted(set(declared) - set(on_disk))
        extra = sorted(set(on_disk) - set(declared))
        parts = []
        if missing:
            parts.append(f"declared but no commands/{{{','.join(missing)}}}.md")
        if extra:
            parts.append(f"commands/*.md present but not declared: {', '.join(extra)}")
        result.error("Command set mismatch: " + "; ".join(parts))
    else:
        result.ok()

    readme = read_text("README.md") or ""
    missing_in_readme = [
        c for c in declared
        if f"/{c}" not in readme and f"nexus:{c}" not in readme
    ]
    if missing_in_readme:
        result.error(
            "Command(s) declared in nexus.structure.json but not referenced in "
            f"README.md: {', '.join(missing_in_readme)}"
        )
    else:
        result.ok()


def check_drift_vocabulary(result):
    """(4) Drift-category handling is consistent per the category decision."""
    dc = STRUCTURE.get("drift_categories", {})
    canonical = set(dc.get("codes", []))
    if not canonical:
        result.error("nexus.structure.json declares no drift_categories.codes")
        return

    for rel in DRIFT_VOCAB_FILES:
        text = read_text(rel)
        if text is None:
            result.error(f"Drift-vocabulary consumer missing: {rel}")
            continue
        found = extract_drift_codes(text)
        if not found:
            # A consumer that states no codes is fine for the seed template
            # (categories are optional); it just is not asserting a vocabulary.
            result.ok()
            continue
        if found != canonical:
            missing = sorted(canonical - found)
            extra = sorted(found - canonical)
            detail = []
            if missing:
                detail.append(f"missing {', '.join(missing)}")
            if extra:
                detail.append(f"unexpected {', '.join(extra)}")
            result.error(
                f"{rel}: drift codes {sorted(found)} disagree with "
                f"nexus.structure.json {sorted(canonical)} ({'; '.join(detail)})"
            )
        else:
            result.ok()

    # The seed template must keep a category-free ENTRY format: categories are
    # optional, never imposed on a day-one log. (The codes may appear only in an
    # explicitly-optional pointer, which is checked for vocabulary above.)
    seed = read_text("templates/failure-log.md") or ""
    if re.search(r"\*\*Category\*\*|^\s*Category:", seed, re.MULTILINE):
        result.error(
            "templates/failure-log.md imposes a mandatory Category field on the "
            "seed log. The day-one log must stay category-free (categories are an "
            "opt-in vocabulary)."
        )
    else:
        result.ok()


def check_session_state_dir(result):
    """The hooks must anchor session state at the declared directory."""
    declared = STRUCTURE.get("session_state_dir", ".claude/session-state")
    # Hooks build the path from components (Path(top) / ".claude" / "session-state"),
    # so match each path segment rather than the joined string.
    parts = [p for p in declared.split("/") if p]
    for rel in HOOK_FILES:
        text = read_text(rel)
        if text is None:
            result.error(f"Hook missing: {rel}")
        elif not all(p in text for p in parts):
            absent = [p for p in parts if p not in text]
            result.error(
                f"{rel}: does not reference session_state_dir '{declared}' "
                f"(missing segment: {', '.join(absent)})"
            )
        else:
            result.ok()


def check_para_folders_advisory(result):
    """(5) Advisory: scaffolders mention the declared PARA folders.

    The setup-prompt is an LLM prose prompt, not executable, so this flags the
    absence of a folder name; it cannot prove the scaffold emits it. Advisory
    only — never changes the exit code.
    """
    folders = STRUCTURE.get("para_folders", [])
    for rel in SCAFFOLDER_FILES:
        text = read_text(rel)
        if text is None:
            result.warn(f"Scaffolder missing (advisory): {rel}")
            continue
        for folder in folders:
            name = folder.split("/")[-1]
            if folder not in text and name not in text:
                result.warn(
                    f"{rel}: PARA folder '{folder}' not mentioned (advisory)"
                )


def main():
    global STRUCTURE
    if not STRUCTURE_FILE.exists():
        print(f"FAIL: {STRUCTURE_FILE} not found", file=sys.stderr)
        return 1
    try:
        STRUCTURE = json.loads(STRUCTURE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: nexus.structure.json is not valid JSON: {exc}", file=sys.stderr)
        return 1

    result = Result()
    check_structure_file(result)
    check_no_nexus_state(result)
    check_failure_log_path(result)
    check_commands(result)
    check_drift_vocabulary(result)
    check_session_state_dir(result)
    check_para_folders_advisory(result)

    for w in result.warnings:
        print(f"ADVISORY: {w}")

    if result.errors:
        print("")
        print("Nexus plugin coherence check FAILED:")
        print("")
        for e in result.errors:
            print(f"FAIL: {e}")
            print("")
        print(
            f"{len(result.errors)} coherence error(s). Fix the consumer(s) to "
            "agree with nexus.structure.json, or update the structure file if the "
            "shape genuinely changed."
        )
        return 1

    print(
        f"Nexus plugin coherence check passed "
        f"({result.checks_run} assertions, {len(result.warnings)} advisory)."
    )
    return 0


STRUCTURE = {}

if __name__ == "__main__":
    sys.exit(main())
