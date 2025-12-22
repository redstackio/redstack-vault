---
id: proc-uuid-004
tags:
  - file-upload
  - s3-abuse
  - arbitrary-upload
type: procedure
tools:
  - '[[tools/aws-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-to-s3-with-aws-py]]'
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.923Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Arbitrary-Files-to-S3-Bucket

## Summary

This procedure uses presigned S3 POST credentials from the BCM API to upload arbitrary files of any type and size (up to 64MB) to the 'bcm-hk' bucket, resulting in publicly accessible storage.

## Description

Leveraging the generated presigned data, a multipart/form-data POST is sent to https://bcm-hk.s3.ap-east-1.amazonaws.com/ with fields like key, Policy, X-Amz-Signature, and the file (base64-encoded if needed). The bucket lacks restrictions, allowing abuse for free storage, malware hosting, or DoS via large files. Uploaded files are public, e.g., https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/randomkey/filename.

## Requirements

1. Presigned JSON from prior API call
2. Python 3 with requests, json, base64, mimetypes, sys libraries
3. Target file to upload (any size/type)
4. Custom script [[tools/aws-py]] or equivalent

## Defense

Defensive measures and detection strategies:

- Add bucket policies to restrict public access and require signed requests
- Validate file content/type server-side before upload
- Enable S3 event notifications and CloudWatch alarms for unusual upload patterns

## Objectives

1. Transfer arbitrary files to S3 without auth
2. Obtain public download URL for persistence/sharing
3. Demonstrate resource abuse potential

## Instructions

### Step 1: Prepare Presigned Data

**Context**: Load the JSON credentials into the upload script.

Ensure presigned.json is available with postUrl, key, Policy, etc.

### Step 2: Execute Upload

**Context**: Run the custom Python script to perform the multipart POST.

Use [[commands/upload-to-s3-with-aws-py]]:

```bash
python aws.py /path/to/filename
```

> The script reads presigned.json (or args), encodes the file, constructs the POST with fields (key, X-Amz-Algorithm=AWS4-HMAC-SHA256, Policy, X-Amz-Credential, X-Amz-Date, X-Amz-Signature, file=(filename, base64data, mimetype)), and sends to postUrl. Handles any size up to policy limit.

**Expected Output**: HTTP 204 No Content from S3; log shows URL like https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/14HXhz8Aef9NnH1Ubvwb5gEXUebzZjtEem/23a3ca622f9d4e52bc69387451580ae8.

### Step 3: Verify Upload

**Context**: Access the public URL to confirm file availability.

```bash
curl -I https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/.../filename
```

**Expected Output**: 200 OK with Content-Type matching file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/upload-to-s3-with-aws-py]]

## Tools Used

- [[tools/aws-py]]

## Tags

- arbitrary-file-upload
- cloud-storage-abuse
- ingress-tool-transfer
