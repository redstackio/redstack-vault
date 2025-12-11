---
tags:
  - ssh
  - rce
  - verification
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 86fbdfe2-6e61-42dd-a090-0c7ad3803de4
created_at: '2025-12-11T03:47:47.576Z'
updated_at: '2025-12-11T03:47:47.576Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Establish SSH Access and Verify

## Summary

This procedure establishes SSH connection using the injected key and verifies access.

## Description

After key injection, connect as git user and run commands to confirm RCE.

## Requirements

1. Private key file
2. SSH access to server

## Defense

Defensive measures and detection strategies:

- SSH login monitoring
- Anomalous access detection

## Objectives

1. Gain remote shell
2. Verify user privileges
3. Confirm key presence

## Instructions

### Step 1: SSH Connection

**Context**: Connect using private key.

**Command** ([[commands/ssh-connect-with-key]]):
```bash
ssh git@gitlab-vm.local -i gitlab
```

> Gains shell access.

### Step 2: Verify User ID

**Context**: Check current user.

**Command** ([[commands/id-verify-user]]):
```bash
id
```

> Shows git user details.

### Step 3: Check Authorized Keys

**Context**: Verify injected key.

**Command** ([[commands/cat-authorized-keys]]):
```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

> Displays key content.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/ssh-connect-with-key]]
- [[commands/id-verify-user]]
- [[commands/cat-authorized-keys]]

## Tools Used

- [[tools/ssh]]

## Tags

- [[tools/ssh]]
- #rce
- #verification
