---
tags:
  - gitlab
  - archive-download
  - command-injection
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9115eb5f-e588-4756-a7a5-8584113c5254
created_at: '2025-12-11T03:47:40.137Z'
updated_at: '2025-12-11T03:47:40.137Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Trigger Git Archive Download in GitLab

## Summary

This procedure triggers the download of a malicious directory as a tar archive in GitLab, exploiting the Gitaly vulnerability to overwrite server files via misinterpreted command options.

## Description

By initiating the 'download directory as tar' feature, the crafted path is passed to git archive without escaping, allowing injection of '--output=' to redirect the archive to authorized_keys. Targets vulnerable GitLab versions.

## Requirements

1. Malicious repository already created
2. Access to GitLab UI
3. Vulnerable Gitaly component

## Defense

- Validate and escape paths in git commands
- Monitor archive download logs for anomalies

## Objectives

1. Execute vulnerable git archive command
2. Overwrite target file on server
3. Prepare for SSH exploitation

## Instructions

### Step 1: Initiate Download

**Context**: Use GitLab interface to download the crafted directory.

Click 'download directory as tar', triggering [[commands/git-archive-overwrite]]:

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

> Misinterprets path as options, writing to specified file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

- [[commands/git-archive-overwrite]]

## Tools Used

- #gitlab-rake
- [[tools/Gitaly]]

## Tags

- #command-injection
- #archive-download
