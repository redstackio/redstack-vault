---
id: proc-verify-repeat-001
tags:
  - verification
  - iteration
  - vote-inflation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.890Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify and Repeat Vote Manipulation

## Summary

This procedure refreshes the definition page to observe the effects of parallel votes and iterates the process (reset and parallel execution) to achieve desired vote inflation or negative counts.

## Description

After parallel execution, the page must be reloaded to display updated counts, which may show multiples or negatives if over-voting opposite directions. Repeat by removing votes (via UI) and re-executing. Target: Browser and terminal. Outcomes: Confirmed manipulation, scalable to arbitrary values.

## Requirements

1. Browser for verification
2. Ability to repeat prior steps
3. Patience for iteration

## Defense

Defensive measures and detection strategies:

- Audit vote counts for anomalies (e.g., negatives)
- Implement vote reconciliation jobs
- Alert on rapid count changes

## Objectives

1. Validate race condition success
2. Scale manipulation through repetition
3. Achieve target vote values

## Instructions

### Step 1: Refresh and Observe

**Context**: Reload to see changes from parallel votes.

In browser:

```bash
# Reload the definition page (Ctrl+R or F5)
```

> Check up/down counts; expect inflation beyond limits, possibly negatives.

### Step 2: Remove Vote and Repeat

**Context**: If needed, reset via UI removal, then re-run parallel curl.

Click the remove vote option if available, then execute Step 4 again.

> Iterate 5-10 times for significant inflation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- iteration
- vote-inflation
