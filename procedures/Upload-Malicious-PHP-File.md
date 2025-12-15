---
tags:
  - file-upload
  - malware-deployment
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 3b8f708d-5fea-4790-9714-92daaf8bb83a
created_at: '2025-12-14T17:24:08.469Z'
updated_at: '2025-12-14T17:24:08.469Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-File

## Summary

This procedure uploads the generated PHP reverse shell to the Concrete CMS File Manager after enabling PHP as an allowed type, placing the malicious file on the web server.

## Description

With PHP uploads permitted, the File Manager allows drag-and-drop or form-based uploads without extension filtering. The uploaded file is stored in a web-accessible directory, enabling execution via HTTP request. This step exploits the lack of content validation in the admin interface.

## Requirements

1. Admin access to Concrete CMS File Manager
2. Generated shell.php file on local machine
3. PHP uploads enabled via prior configuration

## Defense

Defensive measures and detection strategies:

- Enforce strict file type whitelisting and content scanning (e.g., via ClamAV) on uploads
- Log all file uploads with admin context; review for suspicious extensions
- Isolate upload directories from web execution paths or use no-execute permissions

## Objectives

1. Transfer payload to target server
2. Confirm successful placement in File Manager
3. Obtain URL for triggering execution

## Instructions

### Step 1: Access File Manager

**Context**: Navigate to the upload interface.

From the admin dashboard, select File Manager.

> Interface opens with upload options visible.

### Step 2: Perform Upload

**Context**: Transfer the malicious file.

Drag and drop shell.php into the upload area or use the browse button.

> Progress bar completes with green success indicator; file lists in manager.

### Step 3: Verify Upload

**Context**: Check file properties for access URL.

Click on the uploaded file to view details.

> Properties show file path and URL (e.g., http://target.com/files/shell.php).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[malware-deployment]]
- [[concrete-cms]]
