---
tags:
  - file-upload
  - vulnerability-testing
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-upload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: da47206c-8fe8-46d6-a8cb-0ef4df3a0324
created_at: '2025-12-14T05:32:13.797Z'
updated_at: '2025-12-14T05:32:13.797Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Unrestricted-File-Upload

## Summary

This procedure tests the .ashx endpoint on mobile.starbucks.com.sg by attempting to upload non-image files, verifying the lack of file type validation and confirming the unrestricted upload vulnerability.

## Description

The endpoint, designed for image files, does not enforce MIME type or extension checks, allowing arbitrary files like .txt or .aspx to be uploaded. This test uses a harmless file to probe without causing damage, observing server responses to determine if uploads succeed and files are stored accessibly. In an ASP.NET environment, this can lead to file persistence in a web-accessible directory.

## Requirements

1. Access to the target endpoint
2. A test file (e.g., test.txt with benign content)
3. Curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Validate file types server-side using extension and content checks
- Scan uploads for malicious patterns with antivirus
- Log and alert on unexpected file extensions

## Objectives

1. Confirm acceptance of non-image files
2. Identify upload success indicators
3. Assess potential for malicious exploitation

## Instructions

### Step 1: Prepare Test File

**Context**: Create a simple text file to test restrictions.

**Command** (No command; manual):

> echo "test" > test.txt

### Step 2: Upload Test File

**Context**: Send the file via POST to check for rejection.

**Command** ([[commands/curl-test-upload]]):
```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@test.txt" -v
```

> The -F flag sends multipart form data. Expected output: 200 OK without type errors, possibly a file ID or path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-upload]]

## Tools Used


## Tags

- [[file-upload]]
- [[vulnerability-testing]]
