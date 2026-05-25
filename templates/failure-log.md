# Failure Log

Append-only record of AI workflow failures. Review weekly for patterns.

## Category codes

| Code | Category | Description |
|------|----------|-------------|
| SS | State Staleness | Acted on information that was true when cached but isn't anymore |
| CF | Context Fragmentation | Knowledge from one session never reached another |
| ID | Instruction Decay | Rules exist but weren't loaded or were contradicted by newer rules |
| IDUP | Infrastructure Duplication | Built something that already existed because it wasn't discoverable |
| FL | Feedback Loss | Learned from a failure but didn't encode the lesson durably |

## Log

| Date | What happened | Root cause | Category | Occurrences | Preventive rule |
|------|---------------|------------|----------|-------------|-----------------|
| | | | | | |

## Weekly review notes

<!-- Each week, scan the log for clusters. When the same root cause appears
     3 times, it's a system bug - write a preventive rule. -->

### Week of YYYY-MM-DD

- Clusters found:
- Rules written:
- Open questions:
