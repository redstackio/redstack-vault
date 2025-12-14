---
id: proc-request-s3-url-001
tags:
  - upload
  - s3
  - pre-signed
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
updated_at: '2025-12-14T05:32:10.568Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Request-Pre-Signed-S3-URL-for-SVG

## Summary

This procedure requests a pre-signed S3 upload URL for an SVG file by specifying the image/svg+xml MIME type, bypassing potential restrictions on XML-based uploads in avatar features.

## Description

In applications using S3 for file storage, avatar upload endpoints often generate pre-signed URLs without strict MIME validation. By requesting with image/svg+xml, attackers can prepare for XXE injection. This targets APIs like TopCoder's /photoUploadUrl, returning a URL and token for subsequent uploads. Prerequisites include authenticated access to the user profile API.

## Requirements

1. Valid API authentication token for the target user
2. Network access to the API endpoint (e.g., https://api.topcoder.com/v3)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Validate and restrict MIME types to non-XML images (e.g., JPEG, PNG only)
- Implement server-side content inspection for uploads
- Monitor for unusual MIME requests in API logs

## Objectives

1. Obtain S3 pre-signed URL and token for SVG upload
2. Confirm lack of MIME validation
3. Prepare for malicious payload delivery

## Instructions

### Step 1: Send POST Request for URL

**Context**: Initiate the request to get the pre-signed URL.

**Command** (curl-post-photo-upload):
```bash
curl -X POST https://api.topcoder.com/v3/members/{username}/photoUploadUrl \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"contentType": "image/svg+xml"}'
```

> This sends a JSON payload specifying the SVG MIME type. Expected output is JSON with "preSignedURL" and "token" fields. Success if no rejection on MIME.

### Step 2: Extract Response Values

**Context**: Parse the response for use in later steps.

No command needed; manually extract preSignedURL and token from JSON response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload
- s3
