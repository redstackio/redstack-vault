---
id: proc-uuid-2
tags:
  - file-upload
  - testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.122Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Test Upload Limits with Large File

## Summary

This procedure tests the file upload endpoint by submitting an excessively large file (e.g., 2.52 GB) to evaluate server-side handling and detect lack of size enforcement, often resulting in connection issues.

## Description

Targeting the 'upload picture' feature on user profile pages, this step uploads a large .7z archive via the web form. Without proper checks, the server processes the file despite PHP limits, causing slowdowns or failures, indicating vulnerability to DoS.

## Requirements

1. Large test file prepared (e.g., 2.52 GB .7z archive)
2. Active browser session on the target site
3. Access to the upload form at /user/{id}/edit

## Defense

Defensive measures and detection strategies:

- Set and enforce upload_max_filesize in application code
- Use rate limiting on upload endpoints
- Monitor server logs for large POST requests

## Objectives

1. Probe for size limit bypass
2. Observe server response to oversized uploads
3. Confirm potential for resource strain

## Instructions

### Step 1: Prepare and Initiate Upload

**Context**: Select the large file and submit via the web interface.

No command; in browser, go to https://staging.uzbey.com/user/406/edit, click 'upload picture', select 2.52 GB .7z file, and submit.

> Expected: No 413 Payload Too Large error; upload starts, page hangs or slows.

### Step 2: Monitor Response

**Context**: Watch for errors or performance degradation.

Observe browser and server; connection may timeout without rejection.

> Success: Slowdown without size warning, indicating unenforced limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[testing]]
