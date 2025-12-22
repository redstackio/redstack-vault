---
id: 202a1ee6-2b22-4586-98ad-ea2f02c122da
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:05.902Z'
updated_at: '2025-12-11T03:48:05.902Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - exfiltration
  - file-read
commands: []
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
skill_level: beginner
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1083]]'
---

# Access and Download Exfiltrated Files

## Summary

This procedure accesses the exfiltrated files by following the symlinks in the imported group's milestone and modifying URLs to download additional files.

## Description

After import, the milestone in the new group contains links that resolve to the symlinked server files. Clicking the 'passwd' link downloads /etc/passwd, and modifying the URL allows downloading secrets.yml, achieving arbitrary file read.

## Requirements

1. Imported group accessible
2. Web browser
3. Knowledge of symlinked file names

## Defense

Defensive measures and detection strategies:

- Restrict file access permissions for git user
- Audit access to sensitive files

## Objectives

1. Download symlinked passwd file
2. Access additional secrets via URL modification
3. Confirm successful exfiltration

## Instructions

### Step 1: View Milestone and Download passwd

**Context**: Download the file, which resolves the symlink to /etc/passwd.

Navigate to the milestone in the imported group and click the 'passwd' link.

> File downloaded containing /etc/passwd contents.

### Step 2: Modify URL for secrets.yml

**Context**: Change the filename in the upload URL to download the symlinked secrets file.

Modify the URL by replacing 'passwd' with 'secrets.yml' and access it.

> Secrets.yml downloaded.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Exfiltration]]
- #file-read
