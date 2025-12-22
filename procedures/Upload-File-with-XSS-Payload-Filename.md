---
id: proc-uuid-1
name: Upload-File-with-XSS-Payload-Filename
tags:
  - xss
  - stored-xss
  - file-upload
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.845Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-File-with-XSS-Payload-Filename

## Summary

This procedure exploits the lack of filename sanitization in a web application's file upload feature to store an XSS payload, setting up a stored XSS attack that can be triggered later.

## Description

In the context of the partners.line.me platform, the file upload functionality allows users to upload files with arbitrary filenames. The server fails to escape or sanitize special characters and script tags in filenames, leading to the payload being stored as-is. This stored payload can then be retrieved and embedded in HTML responses, causing DOM-based XSS. The attack requires access to the upload interface and relies on the file being temporarily retained on the server.

## Requirements

1. Web browser with developer tools for inspection
2. Access to https://partners.line.me/ and its file upload feature (may require login)
3. A benign file to upload (e.g., empty .txt file)

## Defense

Defensive measures and detection strategies:

- Implement strict filename sanitization: Remove or escape special characters, scripts, and HTML tags
- Use content security policy (CSP) to block inline scripts
- Monitor upload logs for suspicious filenames containing script tags
- Limit file retention period and scan uploads for malicious content

## Objectives

1. Store an unescaped XSS payload in the filename on the server
2. Prepare for subsequent triggering of DOM-based XSS
3. Achieve JavaScript execution in the victim's browser

## Instructions

### Step 1: Prepare Malicious Filename

**Context**: Craft a filename that includes an XSS payload to inject script when embedded in HTML.

Navigate to the file upload page on https://partners.line.me/. Create or rename a file to include a payload like "test'><script>alert(document.domain)</script>.txt".

### Step 2: Perform the Upload

**Context**: Submit the file to the server, exploiting the lack of sanitization.

Use the site's upload button or form to select and upload the prepared file. Submit the form.

> The server processes the upload without validating the filename, storing it with the payload intact.

**Expected Output**: Success message indicating the file was uploaded, possibly with a link to the file path.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[file-upload]]
