---
tags:
  - file-upload
  - rce
  - php
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
updated_at: '2025-12-14T17:23:27.926Z'
sub_techniques: []
id: a4895e18-5d52-42c2-8278-cc0338792140
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-PHP-File-as-Profile-Photo

## Summary

This procedure exploits the lack of file type validation in the profile photo upload to place a malicious PHP script on the server, enabling subsequent code execution.

## Description

The MTN Careers site's upload feature accepts any file type without checking extensions or content, storing files in a web-accessible directory. A simple PHP webshell (e.g., <?php phpinfo(); ?> or system command executor) can be uploaded, leading to RCE when accessed.

## Requirements

1. Authenticated session
2. Malicious PHP file prepared (e.g., shell.php with executable code)
3. Access to profile upload form

## Defense

Defensive measures and detection strategies:

- Validate and sanitize file types/mime on upload (e.g., allow only images)
- Store uploads outside web root or rename with safe extensions
- Scan uploads for malicious content using AV or static analysis

## Objectives

1. Bypass upload restrictions
2. Place executable file on server
3. Confirm storage in accessible location

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a PHP payload for execution.

Use a text editor to make a file like shell.php: <?php system($_GET['cmd']); ?>

### Step 2: Select and Upload File

**Context**: Submit the file via the profile photo input.

In the upload section, choose the PHP file and click 'Upload' or 'Save'.

### Step 3: Verify Upload Success

**Context**: Check for acceptance without errors.

Look for success message; the file is now stored server-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- rce
