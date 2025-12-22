---
id: 3d95e3e3-2dfe-4e78-823d-dab696da1025
name: list-running-processes
type: procedure
verified: true
submitted: true
created_at: '2019-11-25T19:44:10.853039+00:00'
updated_at: '2023-05-26T00:43:25.588182+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Process Discovery|T1057 - Process Discovery]]'
sub_techniques: []
platforms:
  - Linux
tags:
  - Enumeration
commands:
  - '[[commands/ps-list-all-running-processes]]'
tools: []
validated: true
---

# List Running Processes

## Summary

Enumerate all running processes on a Linux system using ps to identify potential escalation vectors like tmux sessions or vulnerable services post-SSH access in a CTF.

## Description

The ps command lists process details including PID, user, and command line. This procedure uses aux flags for full output, helping spot misconfigurations like world-readable tmux sockets.

## Requirements

1. Shell access to target
2. No special privileges (runs as current user)
3. Basic Linux environment

## Defense

Use process monitoring tools like auditd, restrict socket permissions, and limit process visibility with namespaces.

## Objectives

1. Identify running services and users
2. Locate tmux or other session managers
3. Spot privilege escalation opportunities

## Instructions

### Step 1: Run Full Process List

**Context**: Execute ps aux to get a comprehensive view; grep for specific terms like tmux to narrow down.

**Command** ([[commands/ps-list-all-running-processes]]):
```bash
ps aux
```

> Expected output is a table with USER, PID, %CPU, COMMAND. Look for tmux entries with socket paths in /tmp. If needed, pipe to grep: ps aux | grep tmux.
