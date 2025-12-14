---
id: proc-005
tags:
  - suid
  - root-access
  - escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ls-check-tmp-suid]]'
  - '[[commands/execute-suid-bash]]'
  - '[[commands/id-verify-root]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Setuid and Setgid]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:07.218Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Setuid and Setgid]]'
  - '[[Unix Shell]]'
---
# Execute-SUID-Bash-for-Root-Access

## Summary

This procedure runs the SUID bash binary created by the payload to obtain a root shell, verifying the privilege escalation success.

## Description

Post-reboot, the /tmp/evilbash file is an SUID copy of bash. Executing it with -p preserves the effective UID, spawning a shell running as root (euid=0) while maintaining the original uid. This grants full root capabilities to the unprivileged user. Requires the payload to have executed successfully.

## Requirements

1. SUID bash binary present in /tmp
2. Unprivileged user access
3. Bash version 5.0 or compatible

## Defense

Defensive measures and detection strategies:

- Scan for SUID binaries regularly: find /tmp -perm -4000
- Remove world-writable /tmp or use sticky bit enforcement
- Use grsecurity or PaX to limit SUID abuse
- Monitor process execution with ps or auditd for unexpected root shells

## Objectives

1. Spawn root shell via SUID execution
2. Verify escalation with identity check
3. Achieve persistent local root access

## Instructions

### Step 1: Check for SUID Binary

**Context**: List /tmp to confirm the evilbash file exists with SUID bit.

**Command** ([[commands/ls-check-tmp-suid]]):
```bash
ls -l /tmp
```

> Shows -rwsr-xr-x /tmp/evilbash.

### Step 2: Execute SUID Bash

**Context**: Run the binary with -p to preserve environment and gain root shell.

**Command** ([[commands/execute-suid-bash]]):
```bash
/tmp/evilbash -p
```

> Drops to root shell (prompt: evilbash-5.0#).

### Step 3: Verify Root Privileges

**Context**: Inside the shell, check user IDs to confirm euid=0.

**Command** ([[commands/id-verify-root]]):
```bash
id
```

> Output: uid=1000(user) gid=1000(user) euid=0(root) groups=1000(user),998(nordvpn).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Setuid and Setgid]] Setuid and Setgid Binaries
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques

-

## Commands Used

- [[commands/ls-check-tmp-suid]]
- [[commands/execute-suid-bash]]
- [[commands/id-verify-root]]

## Tools Used

-

## Tags

- [[suid]]
- [[root-access]]
- [[escalation]]
