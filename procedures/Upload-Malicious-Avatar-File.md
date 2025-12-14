---
id: proc-upload-avatar-964550
tags:
  - file-upload
  - unrestricted-upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:52:49.264Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Avatar-File

## Summary

This procedure submits the modified multipart/form-data request to upload the malicious PNG as an avatar, exploiting lack of Content-Type validation to store it on Shopify CDN.

## Description

The upload targets https://accounts.shopify.com/accounts/<ID> with specific form fields. After MIME manipulation, the server accepts the file without checking content, storing it as an avatar asset. This enables later XSS when accessed. Assumes prior interception and authenticated session.

## Requirements

1. Modified request ready in Burp Suite
2. Valid authenticity_token from the form
3. Account ID for the endpoint

## Defense

Defensive measures and detection strategies:

- Implement server-side file type whitelisting and content scanning (e.g., libmagic for true MIME)
- Reject uploads with non-image Content-Types
- Quarantine and scan new avatar files before CDN serving

## Objectives

1. Successfully submit the upload request
2. Receive confirmation of avatar update
3. Verify file storage on CDN

## Instructions

### Step 1: Prepare Form Data

**Context**: Ensure all required fields are present in the request.

Include utf8=%E2%9C%93, _method=patch, authenticity_token=<token>, account[avatar]=@malicious.png with modified Content-Type.

### Step 2: Submit Request

**Context**: Forward or send the request via Burp Repeater.

In Burp, use the Intercept or Repeater tab to submit the POST to https://accounts.shopify.com/accounts/<ID>.

> Expected: 200 OK with JSON or HTML confirming avatar set; response may include CDN URL.

### Step 3: Verify Upload

**Context**: Check for storage location.

Inspect response for avatar URL like shopify-assets.shopifycdn.com/.../avatar.png.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- shopify
- avatar-upload
