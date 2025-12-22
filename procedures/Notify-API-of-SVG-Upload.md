---
id: proc-notify-upload-001
tags:
  - api
  - notify
  - upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.559Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Notify-API-of-SVG-Upload

## Summary

This procedure registers the SVG upload with the application API using the token from the pre-signed URL request, ensuring the file is associated with the user profile.

## Description

After obtaining the pre-signed URL, notify the API via a PUT request to /photo endpoint. This step confirms the upload intent and links the token to the user's avatar. Lack of validation here allows progression to XXE exploitation. Targets environments like TopCoder where SVG is accepted without scrutiny.

## Requirements

1. Token from previous pre-signed URL request
2. Authenticated API access
3. HTTP client

## Defense

Defensive measures and detection strategies:

- Reject SVG or XML MIME types in upload notifications
- Log and alert on token usage with non-image types
- Enforce client-side and server-side MIME whitelisting

## Objectives

1. Register the upload to enable S3 persistence
2. Verify API acceptance of SVG
3. Set up for payload processing

## Instructions

### Step 1: Send PUT Notification

**Context**: Use the token to inform the API of the incoming upload.

**Command** (curl-put-photo-notify):
```bash
curl -X PUT https://api.topcoder.com/v3/members/{username}/photo \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"token": "{extracted_token}", "contentType": "image/svg+xml"}'
```

> Expected output: 200 OK or success JSON. This registers the file without fetching it yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api
- notify
