---
name: failure-logging
description: "Use when recording AI workflow failures, reviewing failure patterns, or applying the three-occurrence rule. Provides drift category codes and structured failure capture guidance."
---

## Drift Categories

When recording a failure, classify it using one of these five categories:

| Code | Category | What it means | Diagnostic question |
|------|----------|---------------|-------------------|
| SS | State Staleness | Acted on information that was true when cached but isn't anymore | "Was the data I used still current?" |
| CF | Context Fragmentation | Knowledge from one session never reached another | "Did another session or person already handle this?" |
| ID | Instruction Decay | Rules exist but weren't loaded or were contradicted by newer rules | "Is there a rule for this that I missed or that conflicts?" |
| DF | Discovery Failure | Built something that already existed because it wasn't discoverable | "Does this already exist somewhere I didn't check?" |
| FL | Feedback Loss | Learned from a failure but didn't encode the lesson durably | "Have I seen this before and failed to write it down?" |

## The Three-Occurrence Rule

When the same root cause appears **3 times** in the failure log, it's no longer a one-off mistake — it's a system bug. The system is missing a preventive rule.

At 3 occurrences:
1. Stop treating it as individual failures
2. Write a preventive rule (a CLAUDE.md entry, a hook, a checklist item, or a process change)
3. Record the rule in the failure log's "Preventive rule" column

The rule doesn't need to be perfect. It needs to exist. A rough rule that catches 80% of recurrences is better than no rule that catches none.

## Severity

Each failure entry records blast radius:

| Value | Meaning |
|-------|---------|
| CONTAINED | Caught before affecting external output |
| EXTERNAL | Affected a client, published output, or downstream system |

## Remediation Tracking

Each entry tracks progress from detection to enforcement:

| Status | Meaning |
|--------|---------|
| DETECTED | Failure recorded, no rule written yet |
| RULE WRITTEN | Preventive rule exists but not yet enforced automatically |
| ENFORCED | Rule is enforced via hook, gate, or automated check |

New entries start at DETECTED. Update the status as remediation progresses. The `/nexus-status` command reports unresolved (non-ENFORCED) entries.

## Writing Preventive Rules

Good preventive rules are:
- **Specific**: "Check HubSpot deal status before drafting follow-up email" not "be more careful"
- **Automatable**: Can be turned into a hook, a checklist, or a CLAUDE.md instruction
- **Testable**: You can tell whether the rule was followed or not
- **Proportionate**: The cost of the rule should be less than the cost of the failure recurring
