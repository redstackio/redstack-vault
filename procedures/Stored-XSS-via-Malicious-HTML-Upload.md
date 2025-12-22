---
tags:
  - xss
  - stored-xss
  - file-upload
  - node-js
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-create-malicious-html]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 34c992f0-1a13-49d7-a7ce-79530528cff5
created_at: '2025-12-14T03:15:10.416Z'
updated_at: '2025-12-14T03:15:10.416Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored-XSS-via-Malicious-HTML-Upload

## Summary

This procedure exploits the tianma-static module's improper content-type handling by uploading an HTML file with embedded JavaScript, which is served as `text/html` without sanitization, enabling stored XSS execution when accessed by users.

## Description

In the tianma-static Node.js module, uploaded files with `.html` extensions are automatically served with `text/html` content-type. Attackers can upload HTML containing `<script>` tags, and when victims access the file URL (e.g., via the static server on port 8080), the browser executes the script. This requires file upload functionality in the target application. The vulnerability stems from lack of content validation or sanitization during serving.

## Requirements

1. Access to file upload endpoint in the Node.js application using tianma-static.
2. Network connectivity to the web server on port 8080.
3. Shell environment to create the malicious file locally before upload.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file contents, rejecting or stripping script tags.
- Serve uploaded files with `application/octet-stream` content-type instead of inferring from extension.
- Implement Content Security Policy (CSP) to block inline scripts.
- Monitor for anomalous file uploads and access patterns.

## Objectives

1. Store malicious script on the server via upload.
2. Execute JavaScript in accessing users' browsers.
3. Potential data exfiltration or session hijacking.

## Instructions

### Step 1: Create Malicious HTML File

**Context**: Generate an HTML file with an XSS payload to upload.

**Command** ([[commands/echo-create-malicious-html]]):
```bash
echo "<script>alert(1);</script>" > ex.html
```

> This command creates `ex.html` with a script that alerts '1'. Expected output: File created successfully. Verify with `cat ex.html`.

### Step 2: Upload the File

**Context**: Submit the file to the target's upload endpoint (e.g., via POST request or form).

**Instructions**: Use a tool like curl to upload: `curl -F "file=@ex.html" http://target:8080/upload`. No specific command linked; adapt based on endpoint.

> Expected output: Upload success response. The file is now stored and servable.

### Step 3: Access to Trigger XSS

**Context**: Request the uploaded file to execute the payload.

**Instructions**: Navigate to `http://target:8080/ex.html` in a browser.

> Expected output: Alert '1' pops up, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/echo-create-malicious-html]]

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[file-upload]]
