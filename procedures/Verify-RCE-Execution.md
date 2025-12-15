---
tags:
  - rce
  - verification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/check-rce-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:49.385Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 6d7c9074-dd92-4298-8410-9dcafa03c87f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Verify-RCE-Execution

## Summary

Confirms RCE by checking for the side-effect file created by the payload.

## Description

The payload executes `touch /tmp/rce`; listing it verifies command ran on server.

## Requirements

1. Exploitation performed
2. Shell access to server

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files
- Use immutable file systems
- Log all file creations

## Objectives

1. Validate payload success
2. Confirm deserialization led to execution

## Instructions

### Step 1: Check for Created File

**Context**: List the RCE indicator file.

**Command** ([[commands/check-rce-file]]):
```bash
ls /tmp/rce
```

> Lists file. Expected: /tmp/rce (exists post-exploit); before: No such file.

Optional cleanup: rm /tmp/rce

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/check-rce-file]]

## Tools Used


## Tags

- rce
- verification
