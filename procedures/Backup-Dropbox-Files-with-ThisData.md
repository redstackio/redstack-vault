---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - backup
  - thisdata
  - sync
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.944Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Backup-Dropbox-Files-with-ThisData

## Summary

This procedure syncs Dropbox files into ThisData's backup system, transferring the malicious file name payload for subsequent exploitation in the rendering interface.

## Description

ThisData integrates with Dropbox to backup files, pulling metadata like names without sanitization. By initiating a backup, the attacker's maliciously named file is ingested, setting up the XSS trigger. This step assumes authenticated access to both services and focuses on the sync mechanism as the delivery vector.

## Requirements

1. ThisData account with Dropbox integration enabled
2. Permissions to initiate backups
3. Malicious file already present in Dropbox

## Defense

Defensive measures and detection strategies:

- Validate and escape file metadata during import
- Log and review backup syncs for suspicious file names
- Use API rate limiting to detect anomalous activity

## Objectives

1. Transfer the malicious file to ThisData's storage
2. Preserve the payload in file metadata
3. Enable access to the backup interface

## Instructions

### Step 1: Access ThisData Backup Feature

**Context**: Navigate to the integration settings.

Log into ThisData and go to the backup or sync section, ensuring Dropbox is connected.

### Step 2: Initiate Sync

**Context**: Pull files from Dropbox into ThisData.

Select the Dropbox folder containing the malicious file and trigger the backup/sync operation.

> This process copies file names and contents; the payload relies on the name field.

### Step 3: Confirm Backup Completion

**Context**: Verify the malicious file is now in ThisData.

Check the backup logs or file list to see the synced files, including the one with the payload name.

**Expected Output**: Sync succeeds, file visible in ThisData.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[backup]]
- [[thisdata]]
- [[sync]]
