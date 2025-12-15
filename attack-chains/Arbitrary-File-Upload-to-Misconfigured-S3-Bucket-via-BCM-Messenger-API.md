---
id: ac-uuid-001
tags:
  - s3-misconfig
  - file-upload
  - aws
  - android
  - ssl-pinning-bypass
  - access-control
type: attack_chain
tools:
  - '[[tools/Frida]]'
  - '[[tools/aws-py]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Android
  - AWS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-SSL-Pinning-in-Android-App-with-Frida]]'
  - '[[procedures/Identify-Unprotected-S3-Upload-Endpoint]]'
  - '[[procedures/Generate-Presigned-S3-Upload-Credentials]]'
  - '[[procedures/Upload-Arbitrary-Files-to-S3-Bucket]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:32:20.929Z'
description: >-
  Multi-stage attack exploiting a misconfigured API in the BCM Messenger Android
  app to bypass SSL pinning, discover an unprotected S3 upload endpoint,
  generate presigned credentials, and upload arbitrary files to the 'bcm-hk'
  bucket for potential abuse as free storage.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Arbitrary File Upload to Misconfigured S3 Bucket via BCM Messenger API

Multi-stage attack chain demonstrating exploitation of a misconfigured Amazon S3 bucket in the BCM Messenger Android app, allowing arbitrary file uploads without authentication. The attack begins by bypassing SSL pinning to intercept traffic, identifies an open API endpoint, generates presigned POST URLs, and uploads files to the 'bcm-hk' bucket, which can be abused for free storage, malicious content sharing, or resource exhaustion.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Bypass SSL Pinning] --> B[Identify Upload Endpoint]
    B --> C[Generate Presigned Credentials]
    C --> D[Upload Arbitrary File]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Frida]]
- [[tools/aws-py]]

### Target Environment

- Android device or emulator with BCM Messenger app (com.bcm.messenger) installed
- Network access to API endpoint at http://47.52.75.65:8080
- AWS S3 bucket 'bcm-hk' in ap-east-1 region (publicly accessible post-upload)
- Ports: 8080 (API)

### Initial Access Requirements

- Installed BCM Messenger app (unrestricted registration, no email/phone verification needed)
- Rooted Android device or emulator for Frida injection
- Python 3 environment for custom script

## Detailed Attack Procedures

### Step 1: Bypass SSL Pinning
procedure: [[procedures/Bypass-SSL-Pinning-in-Android-App-with-Frida]]

**Objective**: Disable SSL certificate validation in the BCM Messenger app to intercept unencrypted HTTP traffic and reveal API endpoints.

**Instructions**: Install and run Frida on a rooted Android device or emulator. Hook into the app's SSL validation functions to bypass pinning, allowing traffic tracing with tools like mitmproxy or Wireshark.

**Expected Output**: Intercepted HTTP requests from the app, including API calls without encryption.

**Success Indicators**:
- SSL errors resolved in traffic logs
- Cleartext API endpoints visible in traces

### Step 2: Identify Upload Endpoint
procedure: [[procedures/Identify-Unprotected-S3-Upload-Endpoint]]

**Objective**: Trace app traffic to discover the unprotected API endpoint for S3 profile image uploads.

**Instructions**: With SSL bypassed, simulate app actions like profile setup to trigger API calls. Monitor traffic for requests to http://47.52.75.65:8080//v1/attachments/s3/upload_certification, which returns presigned S3 data.

**Expected Output**: JSON response with S3 bucket details, access key (e.g., AKIA3NG2JXZC3SY2WNXE), policy, and signature.

**Success Indicators**:
- Endpoint responds without authentication
- Presigned POST data extracted

### Step 3: Generate Presigned Credentials
procedure: [[procedures/Generate-Presigned-S3-Upload-Credentials]]

**Objective**: Call the API directly to obtain presigned POST URLs for S3 uploads without app mediation.

**Instructions**: Send a POST request to the upload endpoint using curl or similar to receive JSON with postUrl (https://bcm-hk.s3.ap-east-1.amazonaws.com/), key, credentials, policy (base64-encoded with conditions for content length 1-67108864 bytes), and signature.

**Expected Output**: JSON object containing all fields needed for S3 multipart POST upload.

**Success Indicators**:
- Valid presigned data received
- Policy allows uploads to 'bcm-hk' bucket

### Step 4: Upload Arbitrary File
procedure: [[procedures/Upload-Arbitrary-Files-to-S3-Bucket]]

**Objective**: Use presigned credentials to upload any file to the S3 bucket, resulting in a public URL.

**Instructions**: Parse the presigned JSON and execute [[commands/upload-to-s3-with-aws-py]] with the target filename. The script handles base64 encoding and multipart POST to S3.

```bash
python aws.py filename
```

**Expected Output**: File uploaded successfully, accessible via public URL like https://bcm-hk.s3.ap-east-1.amazonaws.com/profile/.../....

**Success Indicators**:
- HTTP 204 or success response from S3
- File downloadable from generated URL

## Attack Chain Summary

### Key Achievements

1. Bypassed app security to expose internal API
2. Discovered and exploited unauthenticated S3 upload mechanism
3. Achieved arbitrary file storage in AWS bucket without restrictions
4. Demonstrated potential for abuse including malware hosting and resource drain

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
