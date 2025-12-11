---
tags:
  - archive-trigger
  - file-overwrite
type: procedure
tools:
  - '[[tools/tree]]'
  - '[[tools/git]]'
  - '[[tools/docker]]'
  - '[[tools/cat]]'
  - '[[tools/ssh]]'
  - '[[tools/whoami]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/tree-display]]'
  - '[[commands/git-archive-injected]]'
  - '[[commands/docker-exec-bash]]'
  - '[[commands/cat-file]]'
  - '[[commands/ssh-connect]]'
  - '[[commands/whoami-user]]'
  - '[[commands/gitlab-rake-env]]'
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4e9afc17-24d1-4366-b816-679c851a0e6e
created_at: '2025-12-11T06:10:22.643Z'
updated_at: '2025-12-11T06:10:22.643Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Trigger Git Archive Download

## Summary

This procedure triggers the download of a malicious directory as a tar archive in GitLab, exploiting the command injection to overwrite server files.

## Description

By requesting the archive of the crafted path, Gitaly executes the git archive command with injected options, writing to the specified file instead of returning the archive.

## Requirements

1. Malicious repository uploaded to GitLab.
2. Access to GitLab's download feature.
3. Vulnerable GitLab version (11.11).

## Defense

Defensive measures and detection strategies:

- Patch GitLab to sanitize path parameters.
- Log and alert on git archive commands with unusual options.

## Objectives

1. Execute injected git command.
2. Overwrite target file.
3. Prepare for RCE.

## Instructions

### Step 1: Initiate Download

**Context**: Use GitLab interface to download the malicious directory as tar.

This triggers the server-side execution of [[commands/git-archive-injected]]:

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

> Writes the tar content to the authorized_keys file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/git-archive-injected]]

## Tools Used

- [[tools/git]]

## Tags

- [[archive-trigger]]
- [[commands/cat-file]]
