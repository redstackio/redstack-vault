---
id: proc-uuid-3
tags:
  - xss
  - file-upload
  - javascript-execution
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.849Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-Filename-for-XSS

## Summary

This procedure exploits the reflected XSS vulnerability by uploading a file with an unsanitized malicious filename, causing JavaScript to execute in the attacker's browser session.

## Description

The Digital Downloads App fails to sanitize the 'attachment[filepath]' parameter in the POST request to https://delivery.shopifyapps.com/attachments. By naming a file with an XSS payload like '<svg onload=alert(1)>', the response JSON reflects it unsanitized, triggering execution. This is a self-XSS limited to the uploader's session, potentially enabling session hijacking if combined with social engineering.

## Requirements

1. Configured product with digital attachment option
2. Web browser to handle the upload and execution
3. Test file ready for upload (any small file)

## Defense

Defensive measures and detection strategies:

- Implement server-side sanitization of filenames to strip HTML/JS tags
- Use Content Security Policy (CSP) to block inline scripts
- Monitor upload endpoints for suspicious payloads in logs

## Objectives

1. Trigger arbitrary JavaScript execution
2. Demonstrate reflection in response
3. Assess impact on session

## Instructions

### Step 1: Prepare Malicious Filename

**Context**: Create or rename a test file with the XSS payload as the filename.

No command required; in the file dialog, set filename to '<svg onload=alert(1)>' (any extension).

> Ensure the file is small, e.g., 144 bytes.

### Step 2: Perform Upload

**Context**: Submit the file via the app's upload interface, sending POST to the endpoint.

No command required; click upload and submit.

> The request includes parameters like attachment[filepath]=<svg+onload=alert(1)>, attachment[filesize]=144, etc. Response reflects the filename, executing the onload alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[file-upload]]
