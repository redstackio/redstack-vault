---
id: proc-restore-malicious-backup
tags:
  - restore
  - discourse
  - username-injection
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
updated_at: '2025-12-14T17:30:07.561Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Restore-Malicious-Backup-and-Login

## Summary

This procedure uploads and restores a tampered Discourse backup to apply the malicious username to the database, followed by logging into the modified account to set up for export triggering.

## Description

The backup restore feature in Discourse applies changes from the archive to the live database, including user details. By uploading a modified backup, the injected username persists. Login uses email to avoid issues with special characters. This assumes admin privileges and targets web-based Ruby on Rails apps. Expected outcome: Malicious username active in the system.

## Requirements

1. Admin access to upload backups
2. Prepared malicious archive from prior procedure
3. Valid email for the target account
4. Web access to admin/restore endpoint

## Defense

Defensive measures and detection strategies:

- Scan uploads for anomalies like shell characters in user fields
- Require confirmation for restores and log all activities
- Implement rate limiting on backup operations
- Audit database changes post-restore for suspicious usernames

## Objectives

1. Apply injected username to live database
2. Gain access to the modified account
3. Position for export-based exploitation

## Instructions

### Step 1: Upload Modified Archive

**Context**: Use admin panel to upload the tampered backup.

**Instructions**: Navigate to admin/backups and select upload option.

No command; web UI action.

> Expected: Archive accepted and queued for restore.

### Step 2: Initiate Restore

**Context**: Trigger the restore process to update the database.

**Instructions**: Confirm and start restore in the admin interface.

> Expected: Restore completes, applying username changes.

### Step 3: Login to Modified Account

**Context**: Access the account using email to bypass username issues.

**Instructions**: Use login form with the account's email and password.

> Expected: Successful session for the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- restore
- discourse
- username-injection
