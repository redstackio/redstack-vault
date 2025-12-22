---
id: proc-uuid-004
tags:
  - file-delete
  - data-loss
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.915Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Delete-Files-from-Server

## Summary

This procedure removes files from the server via the debug page, causing potential data loss or cleanup after exploitation.

## Description

The delete function targets exposed application files without confirmation or restrictions, allowing attackers to erase evidence or disrupt operations.

## Requirements

1. Access to the debug page with target files listed
2. Web browser
3. Specific file selected for deletion

## Defense

Defensive measures and detection strategies:

- Require multi-factor confirmation for deletes
- Implement audit logs for all file operations
- Backup critical files and monitor for mass deletions

## Objectives

1. Eliminate files to cause impact or hide actions
2. Verify deletion success
3. Demonstrate full control over file system

## Instructions

### Step 1: Select File

**Context**: Choose the file to remove from the server.

From the file list, select the target file.

> Multiple selections may be possible depending on the interface.

### Step 2: Execute Delete

**Context**: Trigger the deletion without authentication.

Click the 'Delete ENC Files' button.

> The file should be removed from the list immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-delete]]
- [[data-loss]]
