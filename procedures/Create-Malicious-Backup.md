---
id: proc-003
tags:
  - backup
  - ownbackup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:33.056Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Backup

## Summary

This procedure uses the OwnBackup interface to create a backup that incorporates the previously uploaded malicious files, embedding the deserialization payload for later exploitation.

## Description

After uploading the crafted files, the OwnBackup app's backup feature archives them, including the malicious `data.dump`. This step ensures the payload is preserved and selectable for restoration, where deserialization can be triggered. Admin access is required, and the process simulates legitimate backup operations to evade detection.

## Requirements

1. Installed OwnBackup app
2. Malicious files uploaded to Files section
3. Admin privileges

## Defense

Defensive measures and detection strategies:

- Audit backup operations for inclusion of user-uploaded files
- Limit backup scopes to exclude arbitrary files
- Log and review backup creation events

## Objectives

1. Archive malicious files in a backup
2. Make the backup available for restoration
3. Maintain stealth in operations

## Instructions

### Step 1: Navigate to OwnBackup Settings

**Context**: Access the backup interface.

No command; go to admin > Settings > Additional > OwnBackup.

> Interface loads with backup options.

### Step 2: Initiate Backup

**Context**: Create the backup including uploaded files.

No specific command; click Create Backup and wait for completion.

> Backup listed in the interface upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[backup]]
- [[ownbackup]]
