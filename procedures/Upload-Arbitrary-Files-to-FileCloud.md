---
id: proc-upload-files-filecloud
tags:
  - file-upload
  - arbitrary-upload
  - malware-hosting
  - filecloud
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
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.213Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Arbitrary-Files-to-FileCloud

## Summary

This procedure uploads arbitrary files, including images and executables, to the unauthenticated FileCloud shared directory via the UI, bypassing file type validation.

## Description

In public mode, the upload functionality lacks restrictions, allowing any file type (e.g., .jpg, .exe) to be stored in shared paths. This enables hosting of malware on trusted domains like .mil for social engineering. Post-remediation, uploads may fail due to backend checks, but the procedure highlights the initial vulnerability.

## Requirements

1. Access to the public mode UI and a created subdirectory
2. Local files prepared for upload (e.g., test.jpg, putty.exe)
3. Active browser session

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning (e.g., antivirus) on uploads
- Block executables and scripts in shared/public folders
- Rate-limit uploads and monitor for bulk or anomalous file types via SIEM
- Partial fixes like upload blocking should be extended to read access

## Objectives

1. Transfer arbitrary files to the server without authentication
2. Host potentially malicious content publicly
3. Demonstrate execution potential via uploaded binaries

## Instructions

### Step 1: Initiate Upload

**Context**: Select the upload feature in the UI for the target directory.

No command required.

Click the 'Upload' or folder icon in the FileCloud explorer.

> Expected output: File selection dialog opens.

### Step 2: Select and Upload Files

**Context**: Choose files and confirm upload to the subdirectory.

No command required.

Select files (e.g., image.jpg, putty.exe) and click 'Upload'.

> Files process and appear in the directory. Success if no type or auth errors; note failures post-remediation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- arbitrary-upload
- malware-hosting
- filecloud
