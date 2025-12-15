---
tags:
  - rce
  - php-payload
type: procedure
tools:
  - '[[tools/RCE-Tester-py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:24:08.063Z'
sub_techniques: []
id: 434b43e9-87f9-4d94-9adb-464064d55399
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Attempt-RCE-with-Crafted-Image-Payload

## Summary

Attempt remote code execution by uploading crafted image content via the 'image' parameter, which is processed with imagecreatefromstring() and saved as PHP if traversal is used, potentially executing embedded code.

## Description

The endpoint treats 'image' data as an image stream but saves it without sanitization. If saved as .php via traversal, it may execute PHP code. The procedure uses a Python script to test payloads, though full RCE was not demonstrated; it could expose Twitter user auth tokens stored in the app.

## Requirements

1. Python environment for scripting
2. Crafted payload including PHP code (e.g., system('id'))
3. Access to vulnerable endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize image data before processing (e.g., validate as valid image)
- Disable PHP execution in upload directories (.htaccess)
- Scan uploads for malicious code signatures

## Objectives

1. Embed and execute PHP code via image stream
2. Gain shell or command execution on server
3. Access sensitive data like auth tokens

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create image data with embedded PHP using [[tools/RCE-Tester-py]].

No command; edit script to include payload like GD image header + '<?php system("id"); ?>'.

> Expected: Binary data mimicking image but with code.

### Step 2: Upload and Test Execution

**Context**: Send via traversal and access file.

Use script or curl with base64-encoded payload:

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<base64_malicious>&filename=/../../shell&extension=php"
```

Access https://reverb.twitter.com/view/data/shell.php to trigger.

> If RCE works, outputs command result; else, treats as image.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Command and Scripting Interpreter: PHP

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/RCE-Tester-py]]

## Tags

- [[rce]]
- [[payload-craft]]
