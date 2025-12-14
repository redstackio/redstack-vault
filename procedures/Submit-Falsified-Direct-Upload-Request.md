---
id: proc-uuid-2
tags:
  - file-upload
  - bypass
  - rails
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-create-presigned-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.048Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Falsified-Direct-Upload-Request

## Summary

Submit a manipulated request to the Rails DirectUploadsController to obtain a presigned S3 URL with a falsified small byte_size, setting up the bypass for larger uploads.

## Description

The DirectUploadsController processes parameters like filename, content_type, byte_size, and checksum to generate a presigned URL. By setting byte_size to a small value (e.g., 10MB) while planning a larger upload, the attacker tricks the app into creating an unenforced URL. This exploits client-side parameter tampering.

## Requirements

1. Valid app endpoint URL
2. CSRF token if session-based
3. Computed MD5 checksum for a dummy file

## Defense

Defensive measures and detection strategies:

- Server-side re-validation of file size post-upload
- Rate limiting on direct upload requests
- Log and alert on mismatched checksums or sizes

## Objectives

1. Obtain presigned URL without content-length enforcement
2. Prepare for oversized upload
3. Avoid immediate detection

## Instructions

### Step 1: Compute Checksum for Falsified File

**Context**: Generate MD5 base64 for a small dummy file to match the falsified byte_size.

Use Ruby or openssl:

```bash
echo "dummy content" | openssl md5 -binary | base64
```

> Output: Base64 MD5 string for use in request.

### Step 2: Send POST Request to Controller

**Context**: Submit JSON payload with small byte_size to get presigned URL.

Execute [[commands/curl-create-presigned-url]]:

```bash
curl -X POST https://target-app/rails/active_storage/direct_uploads \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: TOKEN_IF_NEEDED" \
  -d '{"filename":"test.txt","content_type":"text/plain","byte_size":10485760,"checksum":"DUMMY_MD5_BASE64"}'
```

> Expected: {"signed_id":"...","direct_upload":{"url":"https://s3...","headers":{...}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-presigned-url]]

## Tools Used

- [[tools/curl]]

## Tags

- file-upload
- bypass
