---
id: proc-verify-truncation
tags:
  - verification
  - file-system
  - dos
type: procedure
tools:
  - '[[tools/ls]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-verify-file-truncation]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:08.795Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-File-Truncation-with-Ls

## Summary

This procedure checks the server file system to confirm the injected Git command created and truncated the target file to zero bytes.

## Description

After API injection, git log writes commits to the file, but rev-list truncates it, demonstrating the DoS potential. Performed on the GitLab server (Linux/Docker) with git user permissions.

## Requirements

1. Server access (e.g., via SSH or container)
2. Target file path known (/tmp/written)
3. ls command available

## Defense

Defensive measures and detection strategies:

- Audit file creation in /tmp and sensitive dirs
- Alert on unexpected zero-byte files

## Objectives

1. Validate injection success
2. Confirm truncation effect
3. Identify DoS impact

## Instructions

### Step 1: List File Details

**Context**: Examine the file's size and metadata post-injection.

**Command** ([[commands/ls-verify-file-truncation]]):
```bash
ls -asl /tmp/written
```

> -a shows all, -s size, -l long format; expects size 0 indicating truncation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/ls-verify-file-truncation]]

## Tools Used

- [[tools/ls]]

## Tags

- [[verification]]
- [[dos]]
