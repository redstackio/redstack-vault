---
id: proc-uuid-3
tags:
  - ssh
  - key-generation
  - gitlab
type: procedure
tools:
  - '[[tools/ssh]]'
  - '[[tools/git]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:15.344Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Generate-and-Inject-SSH-Key

## Summary

This procedure generates an RSA SSH key pair and embeds the public key into a GitLab wiki commit message, preparing it as payload for authorized_keys overwrite.

## Description

To achieve persistence via SSH, an attacker generates a key pair locally and uses the public key as a commit message in a new wiki page. This ensures the key is available in git log output during injection. Requires local SSH tools and GitLab access; targets Linux environments with GitLab.

## Requirements

1. Local access to ssh-keygen or equivalent
2. GitLab project with wiki
3. API token for page creation

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous commit messages containing base64-like strings (SSH keys)
- Rotate SSH keys periodically
- Audit wiki changes for sensitive data

## Objectives

1. Create attacker-controlled SSH public key
2. Embed key in commit for payload reuse
3. Enable backdoor via key injection

## Instructions

### Step 1: Generate Key Pair

**Context**: Create an RSA key pair for SSH access.

**Command** (using ssh-keygen, inferred from context):
```bash
ssh-keygen -t rsa -b 2048 -f gitlab -N ''
```

> Generates private key 'gitlab' and public 'gitlab.pub'. Expected output: Key files created.

### Step 2: Create Wiki Page with Key

**Context**: Commit a new wiki page using the public key content as the message.

**Command** (via GitLab UI or API with [[tools/curl]]):
```bash
curl --request POST --header "PRIVATE-TOKEN: $TOKEN" --header "Content-Type: text/markdown" --data "# Key Page" 'http://gitlab-vm.local/api/v4/projects/5/wikis/pages?page=key.md' --header 'X-Gitlab-Wiki-Commit-Message: $(cat gitlab.pub)'
```

> Note: Commit message set to public key content. Expected output: Page created with key in commit log.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ssh]]
- [[tools/git]]

## Tags

- ssh
- key-generation
- gitlab
