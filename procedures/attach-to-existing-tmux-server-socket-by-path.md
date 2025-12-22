---
id: a05a198e-b1bb-48d1-bd75-3ebe970659cd
name: attach-to-existing-tmux-server-socket-by-path
type: procedure
verified: true
submitted: false
created_at: '2019-11-25T21:35:19.654137+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism/T1548.003|T1548.003 - Access
    Token Manipulation]]
platforms:
  - Linux
tags:
  - Misconfiguration
commands:
  - '[[commands/ps-list-all-running-processes]]'
  - '[[commands/tmux-attach-to-socket]]'
tools:
  - '[[tools/tmux]]'
validated: true
---

# Attach to Existing Tmux Server Socket by Path

## Summary

Exploit a misconfigured tmux socket with permissive permissions to attach to an existing session, inheriting the privileges of the session owner (e.g., root) for escalation in a Linux CTF.

## Description

Tmux sockets can be created in custom paths like /tmp/tmux-1000/sock. If world-readable/writable, low-priv users can attach via -S flag, gaining the session's context without auth.

## Requirements

1. Shell access and tmux installed
2. Readable socket path from ps output
3. Target tmux session running

## Defense

Set strict socket permissions (700), use unique socket names, and avoid custom paths in shared environments.

## Objectives

1. Locate exploitable tmux sockets
2. Attach to gain elevated access
3. Execute commands in privileged context

## Instructions

### Step 1: Identify Tmux Processes and Sockets

**Context**: List processes to find tmux server PIDs and associated socket files, why: to target misconfigured ones.

**Command** ([[commands/ps-list-all-running-processes]]):
```bash
ps aux | grep tmux
```

> Expected output shows tmux commands with socket args like -S /tmp/tmux/sock. Note the path.

### Step 2: Attach to Socket

**Context**: Use -S to specify the socket path; if permissions allow, you'll join the session.

**Command** ([[commands/tmux-attach-to-socket]]):
```bash
tmux -S $_SOCKET_PATH attach
```

> Expected output is the session prompt, often root@. If detached, use attach-session; detach with Ctrl-b d.
