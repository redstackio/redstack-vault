---
tags:
  - file-upload
  - payload-delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:22.510Z'
sub_techniques: []
id: 34563e01-93c7-4dd2-b1fa-ed707eb04e91
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Zip-Payload

## Summary

Upload a crafted zip file containing a modified App.php to the Nextcloud root folder, setting up the payload for extraction exploitation.

## Description

The zip (nextcloud-shell.zip) includes a tampered version of apps/files/App.php that enables command execution via a URL parameter (poc_cmd). Uploading to the root as a low-priv user bypasses initial checks, positioning the payload for traversal during extraction.

## Requirements

1. Authenticated session as low-priv user
2. Prepared zip file with modified App.php
3. Web access to files interface

## Defense

Defensive measures and detection strategies:

- Scan uploads for malicious zips (e.g., content validation)
- Limit file types and sizes
- Log all uploads and monitor for suspicious patterns

## Objectives

1. Deliver payload without triggering alerts
2. Position file for extraction
3. Maintain stealth in file operations

## Instructions

### Step 1: Prepare Payload Zip

**Context**: Ensure the zip contains the exploit code.

Craft nextcloud-shell.zip with the modified App.php that parses poc_cmd for system execution.

### Step 2: Upload to Root Folder

**Context**: Place the zip in an accessible location.

In the files app, navigate to root (/), click upload, select nextcloud-shell.zip.

**Expected Output**: File listed in root with upload confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- payload-delivery
