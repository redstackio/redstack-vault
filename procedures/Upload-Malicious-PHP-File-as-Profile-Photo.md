---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
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
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.296Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-File-as-Profile-Photo

## Summary

This procedure exploits the lack of file type validation in the profile photo upload feature on the MTN Careers website to upload a malicious PHP file, which is stored in a web-accessible directory without sanitization.

## Description

Once authenticated, the profile update section includes a file upload field for profile photos with no restrictions on file extensions or MIME types. Attackers can upload a PHP file containing executable code (e.g., a webshell like `<?php system($_GET['cmd']); ?>`) disguised as an image. The file is saved directly to /en/user/images/users/ with a timestamped name, making it immediately executable via the web server. This leads to potential RCE, server compromise, or site defacement.

## Requirements

1. Active authenticated session from prior registration/login
2. Prepared malicious PHP file (e.g., payload.php)
3. Access to the profile update page on https://careers.mtn.cm/

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded files by checking MIME types, extensions, and scanning for executable content
- Store uploads outside the web root or rename with safe extensions (e.g., .jpg)
- Implement web application firewall (WAF) rules to block suspicious uploads and monitor file access logs for anomalous patterns

## Objectives

1. Bypass file upload restrictions to place executable code on the server
2. Ensure the file is stored in an executable directory
3. Prepare for direct access to trigger execution

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a simple PHP payload to test or exploit RCE.

Use a text editor to create payload.php with content like `<?php echo 'RCE Success'; system($_GET['cmd']); ?>`. Save it locally.

### Step 2: Navigate to Profile Update

**Context**: Access the upload interface within the authenticated profile section.

Log in if needed, then go to the profile editing area and locate the 'Upload Profile Photo' or similar field.

### Step 3: Upload the File

**Context**: Submit the malicious file through the upload form without triggering any validation errors.

Select the payload.php file in the upload dialog and submit. Observe for success indicators like 'Upload complete' without rejection.

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
- [[rce]]
- [[php]]
