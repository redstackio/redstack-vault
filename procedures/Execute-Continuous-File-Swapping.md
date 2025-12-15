---
tags:
  - swapping
  - renameat2
  - race
type: procedure
tools:
  - '[[tools/rename-custom-swapper]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/run-rename-swap]]'
platforms:
  - Linux
techniques:
  - '[[NTFS File Attributes]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3e19c56e-bb4b-440d-8095-c9f10123f8a3
created_at: '2025-12-14T17:24:22.195Z'
updated_at: '2025-12-14T17:24:22.195Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[NTFS File Attributes]]'
---
# Execute-Continuous-File-Swapping

## Summary

This procedure runs a custom rename tool to atomically swap a symlink and directory in an infinite loop, creating the TOCTOU window for libcurl's stat/fopen race.

## Description

The attacker executes the compiled rename program on 'a' (symlink) and 'b' (directory), using syscall(SYS_renameat2, ..., RENAME_EXCHANGE) to swap names rapidly. This tricks stat() into seeing a directory (!S_ISREG) while fopen() opens the symlink path. Targets Linux with local access; outcomes include successful race hits during victim curl runs, enabling file overwrites.

## Requirements

1. Compiled rename executable present
2. Symlink 'a' and directory 'b' in current directory
3. Local shell access

## Defense

Defensive measures and detection strategies:

- Monitor for high-frequency renameat2 syscalls via strace or eBPF tools
- Restrict unprivileged use of renameat2 with RENAME_EXCHANGE
- Audit logs for rapid file metadata changes

## Objectives

1. Maintain active race window
2. Enable atomic manipulation without detection
3. Prepare for victim interaction

## Instructions

### Step 1: Run Rename Swapper

**Context**: Start infinite loop of atomic swaps between 'a' and 'b'.

**Command** ([[commands/run-rename-swap]]):
```bash
./rename a b
```

> Executes program using renameat2 in while(1) loop. Expected output: No visible output; process runs continuously, swapping files (verify with ls -l in another terminal showing alternating types).

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[NTFS File Attributes]] Hide Artifacts: Parent PID Spoofing (adapted for file hiding via swaps)

### Sub-Techniques


## Commands Used

- [[commands/run-rename-swap]]

## Tools Used

- [[tools/rename-custom-swapper]]

## Tags

- [[swapping]]
- [[renameat2]]
- [[race]]
