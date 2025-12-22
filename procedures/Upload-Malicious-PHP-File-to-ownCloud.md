---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - file-upload
  - payload-delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:32.355Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-File-to-ownCloud

## Summary

This procedure uploads a malicious PHP file to the ownCloud Files section, placing it on the server filesystem for later execution via the exploited AV path.

## Description

Using the datadirectory path from the config report, the uploaded file's full server path can be determined. The PHP code (e.g., a web shell) is embedded in the file, with extension irrelevant as execution is forced via shell. This step delivers the payload in ownCloud 10.4.1.3 before AV scanning is misconfigured.

## Requirements

1. Admin or user access to Files interface
2. Malicious PHP payload file prepared (e.g., shell.php with <?php system($_GET['cmd']); ?>)
3. Datadirectory path from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enable file type validation and scanning on uploads
- Monitor upload logs for suspicious file contents
- Restrict executable file uploads via .htaccess or app config

## Objectives

1. Place PHP shell on server filesystem
2. Determine exact full path for AV chaining
3. Avoid immediate scanning by configuring AV post-upload

## Instructions

### Step 1: Navigate to Files Section

**Context**: Access the upload interface.

From the dashboard, click Files and select the upload button.

> Browse and select the malicious PHP file. Expected output: Upload progress bar completes.

### Step 2: Confirm Path and Contents

**Context**: Verify placement using datadirectory.

Note the filename in Files list; construct full path as datadirectory + /files/filename.php.

> Example: /var/www/owncloud/data/files/shell.php. Access the file URL to confirm upload if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- payload-delivery
