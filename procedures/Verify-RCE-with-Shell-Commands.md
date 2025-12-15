---
tags:
  - rce-verification
  - shell
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/whoami]]'
  - '[[commands/id]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:20.428Z'
sub_techniques: []
id: 6a77a57e-4db8-4e31-8261-9f9174617104
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Verify-RCE-with-Shell-Commands

## Summary

This procedure confirms successful RCE by executing basic identity commands in the server shell, verifying execution context and privileges.

## Description

Using the webhook-provided interactive shell, run 'whoami' and 'id' to confirm running as 'rocketchat' user (uid 65533), indicating full server compromise without root but with DB and config access.

## Requirements

1. Active RCE shell via webhook
2. Basic Unix commands
3. Output capture in script

## Defense

- Isolate app user with minimal privileges
- Monitor for shell executions from app processes
- Use containerization with seccomp

## Objectives

1. Confirm user context
2. Assess privileges
3. Validate full control

## Instructions

### Step 1: Run Whoami

**Context**: Identify current user.

**Command** ([[commands/whoami]]):
```bash
whoami
```

> Expected: rocketchat

### Step 2: Run Id

**Context**: Get detailed UID/GID.

**Command** ([[commands/id]]):
```bash
id
```

> Expected: uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/whoami]]
- [[commands/id]]

## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- verification
