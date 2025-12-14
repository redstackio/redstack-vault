---
tags:
  - file-delete
  - disruption
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T05:32:10.279Z'
sub_techniques: []
id: db484a6d-f017-4c1b-99e6-7267edee76e4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Delete Files using Debug Functionality

## Summary

This procedure removes files from the server via the unprotected debug page, enabling disruption or cleanup.

## Description

The 'Delete ENC Files' button on the debug page allows permanent deletion of selected files without confirmation or auth, risking loss of critical application data in a DoD context.

## Requirements

1. File present in the debug list
2. Access to the debug page
3. Intent to disrupt or remove evidence

## Defense

Defensive measures and detection strategies:

- Protect delete operations with multi-factor auth
- Backup critical files and audit deletions
- Use immutable storage for important data

## Objectives

1. Disrupt application functionality
2. Erase traces of prior actions
3. Delete sensitive files

## Instructions

### Step 1: Select File for Deletion

**Context**: Target the file to remove.

Click on the file in the list.

> File is highlighted for action.

### Step 2: Execute Deletion

**Context**: Permanently remove the file.

Click the 'Delete ENC Files' button.

> File vanishes from the list.

**Expected Output**: Confirmation via absent file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-delete]]
- [[disruption]]
