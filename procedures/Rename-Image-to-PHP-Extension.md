---
id: proc-rename-to-php
tags:
  - file-upload
  - php-shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mv-rename-file]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T05:32:13.417Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Rename-Image-to-PHP-Extension

## Summary

This simple procedure renames a modified image file to a .php extension, enabling the server to interpret and execute the embedded PHP code as a script rather than an image.

## Description

Following metadata injection, renaming tricks the vulnerable upload handler into saving and serving the file as executable PHP. This exploits servers that check extensions but not content, as in the Monero forum case. No special tools needed beyond basic file operations.

## Requirements

1. Access to a file system (local machine)
2. The prepared image file from previous procedure
3. Basic command-line or GUI file management

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type checking on uploads
- Reject or quarantine files with suspicious extension mismatches
- Log and alert on uploads with executable extensions

## Objectives

1. Alter file extension to trigger PHP parsing
2. Preserve embedded malicious content
3. Prepare for upload without altering functionality

## Instructions

### Step 1: Rename the File

**Context**: Change the extension to .php to enable execution.

**Command** ([[commands/mv-rename-file]]):
```bash
mv picture.png picture.php
```

> This renames the file; expected output is no console message, but verify with `ls -la picture.php` showing the new name. The file should still display as an image in viewers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/mv-rename-file]]

## Tools Used


## Tags

- file-upload
- extension-bypass
