---
id: proc-uuid-5
tags:
  - ssh
  - rce
  - access
type: procedure
tools:
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:15.340Z'
skill_level: basic
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[External Remote Services]]'
  - '[[Unix Shell]]'
---
# Gain-SSH-Access-as-Git-User

## Summary

This procedure establishes an SSH connection to the GitLab server using the injected public key, verifying access as the git user and enabling RCE.

## Description

After overwriting authorized_keys, connect via SSH with the private key. This provides a shell as uid=998(git), allowing command execution on the server. Targets GitLab's git user on Linux; assumes key injection success.

## Requirements

1. Local private key file (e.g., gitlab)
2. Network access to GitLab SSH port (22)
3. Successful prior key injection

## Defense

Defensive measures and detection strategies:

- Disable passwordless SSH for service accounts
- Monitor SSH logs for unknown keys
- Use fail2ban or anomaly detection on auth attempts

## Objectives

1. Authenticate with injected key
2. Verify git user privileges
3. Confirm key persistence in authorized_keys

## Instructions

### Step 1: SSH Connection

**Context**: Connect to the server as git user.

**Command** ([[commands/ssh-gitlab-access]]):
```bash
ssh git@gitlab-vm.local -i gitlab
```

> Uses private key for auth. Expected output: Shell prompt on Ubuntu 16.04.

### Step 2: Verify User

**Context**: Check current user ID.

**Command** ([[commands/id-user-check]]):
```bash
id
```

> Expected output: uid=998(git) gid=998(git) groups=998(git).

### Step 3: Check Keys

**Context**: Confirm injected key.

**Command** ([[commands/cat-authorized-keys]]):
```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

> Expected output: Commit details followed by the SSH public key.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[External Remote Services]]
- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/ssh-gitlab-access]]
- [[commands/id-user-check]]
- [[commands/cat-authorized-keys]]

## Tools Used

- [[tools/ssh]]
- [[tools/cat]]

## Tags

- ssh
- rce
- access
