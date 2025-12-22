---
tags:
  - verification
  - file-check
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
  - Docker
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6c6c3ef1-3284-4db9-a337-f33edd6e4a7d
created_at: '2025-12-11T03:47:40.113Z'
updated_at: '2025-12-11T03:47:40.113Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Verify Authorized Keys Overwrite

## Summary

This procedure verifies that the authorized_keys file on the GitLab server has been successfully overwritten with the attacker's public key.

## Description

Access the server environment (via Docker in PoC) and inspect the target file to confirm the exploit's success, showing tar headers and the injected key.

## Requirements

1. Docker access to GitLab container
2. Overwrite already triggered

## Defense

- Restrict file permissions on sensitive paths
- Log file modifications in .ssh directory

## Objectives

1. Confirm file overwrite
2. Validate exploit effectiveness

## Instructions

### Step 1: Access Container

**Context**: Enter the Docker container shell.

Execute [[commands/docker-exec-bash]]:

```bash
docker exec -ti e1a bash
```

> Opens bash prompt inside the container.

### Step 2: Check File Contents

**Context**: Display the overwritten file.

Execute [[commands/cat-file-contents]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

> Shows tar headers and public key.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques

## Commands Used

- [[commands/docker-exec-bash]]
- [[commands/cat-file-contents]]

## Tools Used

- #docker
- #cat

## Tags

- #verification
