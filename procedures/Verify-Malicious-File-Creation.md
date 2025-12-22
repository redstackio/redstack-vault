---
tags:
  - verification
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-list-files]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:53.429Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4c2313fd-6608-438e-9ccd-44b5b6e354c3
validated: true
mitre_tactics:
  - '[[Discovery]]'
---
# Verify-Malicious-File-Creation

## Summary

This procedure lists directory contents to confirm the creation of a file with an embedded XSS payload, ensuring it's ready for RDoc processing.

## Description

After creating a malicious file, verification prevents errors in subsequent steps. In a Ruby project, this checks that the filename includes the unescaped HTML/JS payload, which RDoc will later embed into index.html as a vulnerable link.

## Requirements

1. Shell access to the project directory
2. The malicious file already created

## Defense

Defensive measures and detection strategies:

- Implement file naming policies to block special characters
- Use automated scans for suspicious filenames in repositories
- Log file creation events for anomaly detection

## Objectives

1. Confirm file existence and payload integrity
2. Identify any creation issues early
3. Prepare for documentation generation

## Instructions

### Step 1: List Directory Files

**Context**: Use ls to display all files, verifying the malicious name is intact.

**Command** ([[commands/ls-list-files]]):
```bash
ls
```

> This outputs the full filename, showing the payload like '"><object src=1 onerror="javascript:alert(1);">Controlling what is documented here'. Success if no truncation or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- None

### Sub-Techniques

- None

## Commands Used

- [[commands/ls-list-files]]

## Tools Used

- None

## Tags

- [[verification]]
