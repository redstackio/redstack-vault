---
id: 123e4567-e89b-12d3-a456-426614174002
name: Verify-No-HACKED-File
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.206Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - verification
  - pre-exploitation
commands: []
platforms:
  - Linux
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---

# Verify-No-HACKED-File

## Summary

This procedure checks the test directory to ensure no 'HACKED' file exists prior to exploitation, providing a baseline for confirming the success of the RCE attack.

## Description

Before executing the malicious clone command, verify the absence of the indicator file 'HACKED' by listing directory contents. This step is crucial for validating that any subsequent file creation is due to the vulnerability exploitation and not pre-existing artifacts.

## Requirements

1. Access to the test directory created in prior steps
2. Basic shell access for listing files

## Defense

Defensive measures and detection strategies:

- Implement file integrity monitoring to detect unexpected file creations
- Use read-only filesystems for sensitive directories during testing

## Objectives

1. Confirm clean pre-exploitation state
2. Establish verification criteria for attack success

## Instructions

### Step 1: Check Directory Contents

**Context**: Manually inspect the test directory to ensure 'HACKED' is absent.

**Command** (Manual ls):
```bash
ls -la
```

> List all files; expected output should not include 'HACKED'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[pre-exploitation]]
