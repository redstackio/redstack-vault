---
id: ee1cf37e-c22b-44b0-93a5-99d6e2015434
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T21:24:57.127217+00:00'
updated_at: '2023-05-25T20:12:30.688031+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Setuid and Setgid|T1548.001 - Setuid and Setgid]]'
sub_techniques: []
platforms:
  - Linux
tags:
  - Linux
  - vulnerability
commands:
  - '[[commands/find-setuid-files]]'
  - '[[commands/getcap-list-capabilities]]'
tools: []
validated: true
---

# Find-Linux-Files-with-Elevated-Privileges

## Summary

Scan a Linux system for setuid/setgid binaries and file capabilities that could enable privilege escalation by allowing execution as root or bypassing permissions.

## Description

Setuid files run as the owner (often root), while capabilities grant specific privileges like net_raw. This procedure enumerates them to identify misconfigurations or vulnerabilities, such as exploitable SUID nmap.

## Requirements

- Shell access to target (e.g., reverse shell)
- Find and getcap commands available
- Root or user permissions for scanning

## Defense

- Audit and remove unnecessary SUID bits
- Use minimal capabilities instead of full SUID
- Regularly scan for privilege escalation vectors with tools like LinPEAS

## Objectives

1. List all setuid/setgid executables
2. Identify files with extended capabilities
3. Pinpoint potential escalation targets like SUID nmap

## Instructions

### Step 1: Search for Setuid Files

**Context**: Use find to locate files with u+s permission (4000), listing details to check ownership.

**Command** ([[commands/find-setuid-files]]):
```bash
find / -perm -4000 -ls 2>/dev/null
```

> Output shows paths like /usr/bin/nmap with rwsr-xr-x; focus on non-system ones.

### Step 2: Enumerate Capabilities

**Context**: Getcap recursively lists files with capabilities, revealing granular privileges.

**Command** ([[commands/getcap-list-capabilities]]):
```bash
getcap -r / 2>/dev/null
```

> Look for cap_setuid or cap_net_bind_service; cross-reference with setuid findings for exploits.
