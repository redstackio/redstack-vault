---
id: proc-upload-arbitrary-file
tags:
  - arbitrary-file-upload
  - web
  - php
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-file-upload]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.124Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Arbitrary-File

## Summary

This procedure exploits an unauthenticated file upload endpoint to store arbitrary files on the server without validation, enabling the placement of potentially malicious content like scripts for XSS or RCE.

## Description

Targeting PHP-based web applications with insecure upload handlers, this procedure submits files via a multipart form to an endpoint like /upload.php. The lack of authentication and file type checks allows any file to be uploaded and stored in a publicly accessible directory. In the DoD website scenario, a test file upload succeeds, confirming the vulnerability. Outcomes include file persistence, which can be leveraged for further attacks. Requires prior confirmation of endpoint accessibility.

## Requirements

1. Access to the upload form (from previous reconnaissance)
2. A test file (e.g., text file with benign content)
3. curl tool for automated testing or browser for manual

## Defense

Defensive measures and detection strategies:

- Validate file types, sizes, and contents server-side (e.g., MIME type checks, virus scanning)
- Store uploads outside the web root or with restricted permissions
- Monitor server logs for upload attempts and anomalous file patterns (e.g., .php shells)

## Objectives

1. Successfully store an arbitrary file on the target server
2. Receive confirmation of upload without errors
3. Prepare for public access testing

## Instructions

### Step 1: Prepare Test File

**Context**: Create a simple file to test upload without triggering immediate alerts.

Create a file named 'delete.me' with content 'test file' using a text editor.

> Expected output: File ready for upload.

### Step 2: Submit Upload via Browser or Curl

**Context**: Use the form or HTTP POST to send the file to the endpoint.

**Command** ([[commands/curl-file-upload]]):
```bash
curl -X POST -F "file=@delete.me" https://█████████/upload.php
```

> This sends a multipart form-data request. Expected output: Server response with success message, e.g., "File uploaded successfully." If using browser, select file and submit form; look for similar confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/curl-file-upload]]

## Tools Used

- [[tools/curl]]

## Tags

- [[arbitrary-file-upload]]
- [[web]]
- [[php]]
