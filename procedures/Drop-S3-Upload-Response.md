---
id: proc-uuid-3
tags:
  - response-drop
  - s3
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:27:43.194Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Drop-S3-Upload-Response

## Summary

Intercept and drop the S3 upload response to prevent import in the attacker's account while extracting the redirect URL parameters for CSRF.

## Description

The S3 response is a 303 See Other with Location: https://app.taxjar.com/csv_imports/upload_complete?bucket=taxjar-prod-bucket&key=uploads%2F{uuid}%2F{filename}&etag=%22{etag}%22. Dropping it keeps the file in S3 accessible but unprocessed, allowing reuse via CSRF.

## Requirements

1. Intercepted upload request from previous procedure
2. Burp Suite active

## Defense

Defensive measures and detection strategies:

- Validate all S3 completions server-side with tokens
- Detect dropped responses via upload logs

## Objectives

1. Extract bucket, key, etag
2. Prevent attacker-side import
3. Preserve S3 object for CSRF

## Instructions

### Step 1: Capture Response in Burp

**Context**: Monitor for the 303 response after request forward.

Forward the POST request in Burp to S3, then intercept the incoming response.

### Step 2: Drop and Extract

**Context**: Manually note parameters before dropping.

Copy the Location header values (bucket, key, etag), then drop the response to abort the redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[response-manipulation]]
