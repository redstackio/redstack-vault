---
tags:
  - file-verification
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Discovery]]'
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
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8dfb635a-81ca-4161-ad3e-3f86762e3bb5
created_at: '2025-12-11T06:10:29.862Z'
updated_at: '2025-12-11T06:10:29.862Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Verify File Overwrite

## Summary

This procedure checks the contents of an overwritten file to confirm successful exploitation and content control.

## Description

After injecting Git flags to overwrite a file, use cat to read and verify that the file contains the expected git log output with the controlled commit message.

## Requirements

1. Shell access to the target system (post-exploitation)
2. Path to the overwritten file

## Defense

Defensive measures and detection strategies:

- Monitor file system changes in sensitive directories
- Use file integrity monitoring tools

## Objectives

1. Confirm file overwrite success
2. Validate controlled content insertion
3. Proceed to next exploitation steps

## Instructions

### Step 1: Read File Contents

**Context**: Use cat to display the file.

**Command** ([[commands/cat-file-contents]]):
```bash
cat /tmp/file
```

> Expected to show commit details including 'controlled content'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/cat-file-contents]]

## Tools Used

- [[tools/cat]]

## Tags

- [[file-verification]]
