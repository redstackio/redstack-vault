---
tags:
  - verification
  - file-access
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 680ba9eb-8cd7-436b-9999-c968a0252483
created_at: '2025-12-11T03:47:47.596Z'
updated_at: '2025-12-11T03:47:47.596Z'
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

This procedure checks the contents of an overwritten file to confirm successful exploitation of the file overwrite vulnerability.

## Description

After injecting a git flag to overwrite a file, use this to verify if the controlled commit message appears in the target file. It assumes shell access or a way to execute commands on the target.

## Requirements

1. Shell access to the target system
2. Path to the overwritten file

## Defense

Defensive measures and detection strategies:

- File integrity monitoring
- Access controls on sensitive files

## Objectives

1. Confirm file contents
2. Validate exploit success

## Instructions

### Step 1: Display File Contents

**Context**: Read the file to check for injected content.

**Command** ([[commands/cat-file-contents]]):
```bash
cat /tmp/file
```

> Expected to show commit details with 'controlled content'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/cat-file-contents]]

## Tools Used

- #cat

## Tags

- #verification
- #file-access
