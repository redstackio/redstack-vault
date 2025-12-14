---
tags:
  - shell-access
  - verification
type: procedure
tools:
  - '[[tools/pre_auth_nosqli.py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/whoami-verify-user]]'
  - '[[commands/id-check-privileges]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:30.561Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Unix Shell]]'
id: 4534aade-041e-40a3-95bf-b64437cc21f4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Interact-with-RCE-Shell-to-Verify-Access

## Summary

This procedure uses the RCE shell from the webhook to execute commands confirming execution context and privileges.

## Description

In the reverse shell or webhook-triggered session, run basic commands to verify running as rocketchat user with expected UID/GID. This validates full compromise and allows further exploration like DB access.

## Requirements

1. Established RCE shell
2. Netcat or similar listener on attacker side
3. Basic Linux command knowledge

## Defense

Defensive measures and detection strategies:

- Isolate rocketchat user (no shell access)
- Monitor process executions from app user
- Use containerization with seccomp

## Objectives

1. Confirm user context
2. Validate RCE success
3. Enable further exploitation

## Instructions

### Step 1: Check Current User

**Context**: Execute whoami to identify running user.

**Command** ([[commands/whoami-verify-user]]):
```bash
whoami
```

> In shell: Outputs "rocketchat". Confirms non-root but app user access.

### Step 2: Check Privileges

**Context**: Use id to get UID/GID/groups.

**Command** ([[commands/id-check-privileges]]):
```bash
id
```

> Outputs "uid=65533(rocketchat) gid=65533(rocketchat) groups=65533(rocketchat)". Verifies isolation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/whoami-verify-user]]
- [[commands/id-check-privileges]]

## Tools Used

- [[tools/pre_auth_nosqli.py]]

## Tags

- shell-access
- verification
