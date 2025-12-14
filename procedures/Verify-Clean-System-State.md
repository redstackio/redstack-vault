---
id: proc-002
tags:
  - verification
  - clean-state
  - tmp
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-list-tmp-files]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:30:07.239Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Clean-System-State

## Summary

This procedure checks the /tmp directory for any existing SUID binaries or artifacts to ensure a clean environment before attempting privilege escalation exploitation.

## Description

Before overwriting service files and triggering payloads, verify that /tmp is free of malicious files like SUID bash copies. This step confirms the baseline state on a Linux system, preventing false positives in post-exploitation verification. It uses standard ls command and requires only unprivileged user access.

## Requirements

1. Local unprivileged user access
2. /tmp directory accessible (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Regularly clean /tmp with tmpwatch or systemd-tmpfiles
- Monitor /tmp for unexpected SUID files using cron jobs with find /tmp -perm -4000
- Enable SELinux or AppArmor to restrict SUID binary creation in /tmp

## Objectives

1. Confirm absence of prior exploitation artifacts
2. Establish baseline for success measurement
3. Ensure reliable post-exploit verification

## Instructions

### Step 1: List /tmp Contents

**Context**: Display detailed file listing in /tmp to check for SUID binaries.

**Command** ([[commands/ls-list-tmp-files]]):
```bash
ls -la /tmp
```

> Long listing; expected to show no /tmp/evilbash or files with 's' in permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

-

## Commands Used

- [[commands/ls-list-tmp-files]]

## Tools Used

-

## Tags

- [[verification]]
- [[clean-state]]
- [[tmp]]
