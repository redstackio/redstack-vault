---
id: proc-spray-bucket-addresses
tags:
  - apache
  - spray
  - oob
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/gdb-print-process-score-parent-0]]'
  - '[[commands/gdb-print-process-score-parent-1]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:30:47.276Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Dynamic-link Library Injection]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Process Injection]]'
---
# Spray Fake Bucket Addresses by Modifying process_score Buckets

## Summary

This procedure modifies multiple process_score->bucket indexes in Apache SHM using the UAF primitive to spray fake structure addresses, ensuring OOB access hits the controlled bucket post-restart despite all_buckets relocation.

## Description

Change bucket values across process_score entries (spaced e.g., 0x24 bytes) to point to the fake prefork_child_bucket. Use negative offsets and spraying to cover possible memory shifts during graceful restart. Builds on prior fake structure crafting.

## Requirements

1. UAF write access to SHM process_score array
2. Known spacing (e.g., &parent[1] - &parent[0] = 0x24)
3. Fake structure address ready

## Defense

Defensive measures and detection strategies:

- Validate bucket indexes in make_child()
- Monitor SHM modifications via kernel hooks
- Limit worker process lifetimes

## Objectives

1. Update multiple bucket indexes to fake addresses
2. Spray for relocation robustness
3. Prepare for OOB read in restart

## Instructions

### Step 1: Modify process_score Buckets

**Context**: Use UAF to set process_score->bucket to fake structure addresses across entries.

No direct command; PHP UAF writes to offsets like 0x7f4a9323e020 + (index * 0x24) + bucket_offset.

> Spray values with negative offsets to cover regions.

### Step 2: Verify Modifications

**Context**: Inspect updated process_score in GDB.

**Command** ([[commands/gdb-print-process-score-parent-0]]):
```bash
(gdb) p ap_scoreboard_image->parent[0]
```

> Outputs: { ... bucket = <fake_address> }

**Command** ([[commands/gdb-print-process-score-parent-1]]):
```bash
(gdb) p ap_scoreboard_image->parent[1]
```

> Confirm spacing and multiple updates.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Process Injection]] Process Injection

### Sub-Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

## Commands Used

- [[commands/gdb-print-process-score-parent-0]]
- [[commands/gdb-print-process-score-parent-1]]

## Tools Used

- [[tools/GDB]]

## Tags

- bucket-spray
- shm-modify
