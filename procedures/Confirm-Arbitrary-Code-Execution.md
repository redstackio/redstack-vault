---
tags:
  - rce
  - privilege-escalation
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/strace]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.769Z'
sub_techniques: []
id: de2f81d4-f430-48cc-8493-c03d1e1b62fc
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Confirm-Arbitrary-Code-Execution

## Summary

This procedure validates the RCE by executing commands in the spawned shell, observing impacts like privilege escalation, data access, or DoS, using tools to trace confirmation.

## Description

Post-exploit, confirm shell spawn and system compromise in Linux curl environment. Outcomes: Proof of arbitrary execution, potential full compromise. Prerequisites: Successful payload execution.

## Requirements

1. Spawned shell from exploit
2. GDB/strace for tracing
3. Access to sensitive commands

## Defense

Defensive measures and detection strategies:

- Behavioral monitoring for shell from non-shell processes
- Privilege separation for curl
- Alert on segfaults or abnormal terminations

## Objectives

1. Execute test commands
2. Check for escalation
3. Document impact (e.g., DoS)

## Instructions

### Step 1: Run Verification Commands

**Context**: In shell, test control.

**Command**:

```bash
id
cat /etc/passwd  # Data access
```

> Expected: User info, file contents if escalated.

### Step 2: Trace with Tools

**Context**: Confirm via debugging.

**Command**:

```bash
strace -f -e execve ./curl -d exploit http://target
(gdb) backtrace  # Post-execution
```

> Output: execve of /bin/sh, confirming spawn.

### Step 3: Check for DoS

**Context**: If crashed, verify impact.

**Command**:

```bash
dmesg | grep segfault  # Kernel log
```

> Shows crash details.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]
- [[tools/strace]]

## Tags

- rce
- privilege-escalation
