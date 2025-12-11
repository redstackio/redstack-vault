---
tags:
  - ssh
  - rce
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[tools/ssh]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1e92f2cf-f019-45c1-82e2-bf2581351f5a
created_at: '2025-12-11T03:47:40.101Z'
updated_at: '2025-12-11T03:47:40.101Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1021.004]]'
---
# Establish SSH Connection for RCE

## Summary

This procedure establishes an SSH connection to the GitLab server using the injected public key, achieving remote code execution as the git user.

## Description

After overwriting authorized_keys, use the private key to SSH in and confirm access with whoami, enabling arbitrary command execution.

## Requirements

1. Private SSH key matching the injected public key
2. Network access to GitLab server on SSH port

## Defense

- Use key-based authentication restrictions
- Monitor SSH login attempts

## Objectives

1. Gain shell access as git user
2. Confirm RCE capability

## Instructions

### Step 1: SSH Connection

**Context**: Connect to the server as git user.

Execute [[commands/ssh-connect-git]]:

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

> Establishes SSH session.

### Step 2: Verify User

**Context**: Confirm the current user.

Execute [[commands/whoami-check]]:

```bash
whoami
```

> Outputs 'git'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[tools/ssh]]

### Sub-Techniques

## Commands Used

- [[commands/ssh-connect-git]]
- [[commands/whoami-check]]

## Tools Used

- [[tools/ssh]]
- #whoami

## Tags

- #rce
- [[tools/ssh]]
