---
tags:
  - verification
  - file-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-cron-backdoor]]'
  - '[[commands/cat-cron-backdoor]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.474Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7b150726-2bd5-47fc-95d4-766a96a44ebf
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Arbitrary-File-Write-Success

## Summary

This procedure verifies the success of the cURL path traversal exploit by checking the written file's existence, ownership, and contents in the target directory.

## Description

Post-exploitation, use ls and cat to inspect /etc/cron.daily/zzz-backdoor. Target: Linux systems. Ensures the backdoor was placed correctly with root privileges, confirming traversal worked and payload integrity.

## Requirements

1. Root or read access to /etc/cron.daily/
2. Successful prior cURL write

## Defense

Defensive measures and detection strategies:

- Log file creation in sensitive directories (e.g., auditd watches on /etc/)
- Integrity checks on cron files using tripwire or AIDE
- Alert on unexpected file writes to system paths

## Objectives

1. Confirm file creation and permissions
2. Validate payload contents
3. Indicate exploitation success

## Instructions

### Step 1: List File Details

**Context**: Check ownership and permissions.

**Command** ([[commands/ls-cron-backdoor]]):

```bash
ls -l /etc/cron.daily/zzz-backdoor
```

> Shows long format: e.g., "-rw-r--r-- 1 root root 123 May 1 06:30 /etc/cron.daily/zzz-backdoor"

### Step 2: Display Contents

**Context**: Verify script matches hosted payload.

**Command** ([[commands/cat-cron-backdoor]]):

```bash
cat /etc/cron.daily/zzz-backdoor
```

> Outputs backdoor.sh contents, e.g., shell code for reverse shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/ls-cron-backdoor]]
- [[commands/cat-cron-backdoor]]

## Tools Used


## Tags

- verification
- file-discovery
