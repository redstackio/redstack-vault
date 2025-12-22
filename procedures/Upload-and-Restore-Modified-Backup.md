---
tags:
  - upload
  - restore
  - discourse
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
updated_at: '2025-12-14T17:30:18.612Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5f32ec15-f3ea-47de-a830-a209e8e4b37b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-and-Restore-Modified-Backup

## Summary

This procedure handles uploading the symlink-modified tar backup to Discourse and initiating the restore, which extracts and resolves the symlink to enable file read.

## Description

The restore process in /admin/backups/ extracts the tar without checking symlinks, placing the resolved file in /public/uploads/. This allows subsequent URL access. More severe in multisite due to predictable paths. Assumes admin access and restore enabled.

## Requirements

1. Admin session active
2. Modified tar.gz file ready
3. Site setting 'restore enabled' toggled on

## Defense

Defensive measures and detection strategies:

- Validate tar contents on upload (e.g., check for symlinks with pax or custom parser)
- Run restores in sandboxed environment
- Alert on rapid backup create/upload/restore cycles

## Objectives

1. Successfully upload without rejection
2. Complete restore to trigger extraction
3. Confirm no errors in process

## Instructions

### Step 1: Upload the Backup

**Context**: Transfer modified archive to server.

In /admin/backups/, use upload button to select modified.tar.gz.

> Expected: File uploads; listed in backups.

### Step 2: Enable Restore if Needed

**Context**: Ensure functionality allowed.

Go to /admin/site_settings/, search for 'restore', enable if off.

> Expected: Setting saved; restore option appears.

### Step 3: Initiate Restore

**Context**: Extract the backup on server.

Select uploaded backup and click 'Restore'.

> Expected: Process runs; site may restart; success confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- backup-upload
- restore-exploitation
