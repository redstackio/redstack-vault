---
tags:
  - race-condition
  - symlink-swap
  - toctou
type: procedure
tools:
  - '[[tools/rename-custom]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rename-swap]]'
  - '[[commands/ps-aux]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:19.247Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9e6863ad-874a-4b7d-95bc-a5bf22dc7620
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-Symlink-Swapping-with-Custom-Rename-Tool

## Summary

This procedure runs a custom rename tool to atomically swap a symlink and directory in an infinite loop, creating the TOCTOU race window exploited by libcurl's unsynchronized stat() and fopen() calls.

## Description

The attacker executes the compiled rename program, which uses the renameat2 syscall with RENAME_EXCHANGE flag to swap 'a' (symlink) and 'b' (directory) continuously. This timing attack ensures that during the victim's curl execution, stat('a') sees the directory (skipping regular file checks), but fopen('a', 'w') follows the symlink to 'flag'. The loop runs in the background, enabling the race without immediate detection. Prerequisites: Prepared environment from prior procedure. Expected outcome: Active swap creating vulnerability window for 1-2 seconds or until interrupted.

## Requirements

1. Compiled rename tool available
2. Symlink 'a' and directory 'b' in current directory
3. Permissions to execute renameat2 syscalls
4. Background process capability (nohup or &)

## Defense

Defensive measures and detection strategies:

- Kernel-level race condition mitigations (e.g., disable symlink following with msymlinks=0 mount option)
- Syscall monitoring for repeated renameat2 calls (e.g., via strace or eBPF)
- Filesystem integrity checks with tools like AIDE

## Objectives

1. Initiate continuous atomic file swaps
2. Create TOCTOU window for libcurl exploitation
3. Maintain swap without crashing or alerting
4. Time swap to coincide with victim curl execution

## Instructions

### Step 1: Launch Rename Tool

**Context**: Start the infinite loop swap in background.

**Command** ([[commands/rename-swap]]):
```bash
./rename a b &
```

> Runs rename to exchange 'a' and 'b' using syscall(SYS_renameat2, AT_FDCWD, "a", AT_FDCWD, "b", RENAME_EXCHANGE) in while(1). Expected output: No stdout; process ID returned.

### Step 2: Verify Tool Running

**Context**: Confirm the swap process is active.

**Command** ([[commands/ps-aux]]):
```bash
ps aux | grep rename
```

> Lists processes; expected: ./rename a b running in loop.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/rename-swap]]
- [[commands/ps-aux]]

## Tools Used

- [[tools/rename-custom]]

## Tags

- race-condition
- symlink-swap
- syscall
