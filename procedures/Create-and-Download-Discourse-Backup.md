---
tags:
  - backup-creation
  - discourse
  - download
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
updated_at: '2025-12-14T17:30:18.620Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d78edd64-07bd-4f01-94ee-b8f96565ea8e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Download-Discourse-Backup

## Summary

This procedure covers generating a legitimate backup in Discourse, including database and files, then downloading it for local modification to insert symlinks.

## Description

Discourse's backup feature creates a tar.gz archive with SQL dump and /public/uploads/* contents. This is exploited by downloading, modifying, and reuploading. Prerequisites include admin access. Expected outcome: Local copy of backup ready for tampering, enabling symlink insertion for arbitrary file read post-restore.

## Requirements

1. Admin access to /admin/backups/
2. Local storage space for the downloaded archive (typically several MB to GB)
3. Tar utility for extraction (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Disable or monitor backup creation frequency
- Validate backup contents on upload for anomalies like symlinks
- Log all backup operations with IP and user details

## Objectives

1. Obtain a base backup structure including uploads
2. Download without errors for offline editing
3. Ensure compatibility for reupload and restore

## Instructions

### Step 1: Initiate Backup Creation

**Context**: Generate the archive via admin interface.

In /admin/backups/, click 'Create Backup' and ensure 'Include files' is selected.

> Expected: Progress indicator; backup ready after ~1-5 minutes depending on size.

### Step 2: Download the Backup

**Context**: Retrieve the tar.gz file locally.

Click the download link for the new backup.

> Expected: File saves to local machine, e.g., discourse_backup_2023-10-01.tar.gz.

### Step 3: Extract Locally

**Context**: Unpack to access internal structure.

Use terminal:

```bash
tar -xzf discourse_backup_2023-10-01.tar.gz
```

> Expected: Directory with db.sql and uploads/ folder extracted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- backup-download
- tar-extraction
