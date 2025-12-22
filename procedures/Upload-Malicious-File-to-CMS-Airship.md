---
id: proc-uuid-002
name: Upload-Malicious-File-to-CMS-Airship
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.832Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Remote File Copy]]'
tags:
  - file-upload
  - cms-airship
commands:
  - '[[commands/curl-upload-file]]'
platforms:
  - Web
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---

# Upload-Malicious-File-to-CMS-Airship

## Summary

This procedure uploads a crafted malicious file to CMS Airship's file upload feature as an authenticated user, storing it for later serving without security headers, setting up stored XSS exploitation.

## Description

CMS Airship's upload endpoint in PublicFiles.php allows authenticated users to store files, but serves them without preventive headers, enabling content sniffing attacks. The uploaded file's URL can then be shared to trigger execution in vulnerable browsers.

## Requirements

1. Valid authenticated session in CMS Airship
2. Crafted malicious file (e.g., xss.zip)
3. Network access to the upload endpoint

## Defense

Defensive measures and detection strategies:

- Enforce file type validation and magic byte checks
- Add X-Download-Options: noopen and Content-Disposition: attachment
- Log and review all file uploads for suspicious patterns

## Objectives

1. Store the malicious file on the server
2. Obtain a publicly accessible URL
3. Ensure serving without MIME enforcement

## Instructions

### Step 1: Authenticate and Upload

**Context**: Use the CMS login to gain upload permissions, then POST the file.

**Command** ([[commands/curl-upload-file]]):
```bash
curl -X POST -F "file=@xss.zip" -H "Cookie: session=your_auth_cookie" -H "Content-Type: multipart/form-data" https://target.com/admin/upload
```

> Submits the file via multipart form. Replace session cookie with actual value from browser. Expected output: JSON response with upload success and file URL, e.g., {"status":"success","url":"/files/xss.zip"}.

### Step 2: Retrieve and Verify URL

**Context**: Access the uploaded file to confirm it's served raw.

**Command** ([[commands/curl-fetch-file]]):
```bash
curl -I https://target.com/files/xss.zip
```

> HEAD request to check headers. Expected output: No X-Content-Type-Options header, Content-Type: application/zip or unknown.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-file]]
- [[commands/curl-fetch-file]]

## Tools Used


## Tags

- [[file-upload]]
- [[cms-airship]]
