---
tags:
  - xss
  - bypass
  - upload
type: procedure
tools:
  - '[[tools/TamperData]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bbec6334-8e56-40c6-bc31-7ce5c67967c9
created_at: '2025-12-13T23:56:03.289Z'
updated_at: '2025-12-13T23:56:03.289Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-File-Upload-Validation

## Summary

This procedure intercepts and modifies POST requests during WordPress file uploads to bypass client-side JavaScript validation, allowing malicious content like embedded scripts to be submitted.

## Description

In WordPress, client-side checks prevent non-image content in uploads, but these can be bypassed by tampering with the HTTP request. Using a proxy tool, alter the request body to remove validation triggers, enabling upload of files with JavaScript payloads disguised as images. This targets the media upload endpoint and requires upload privileges.

## Requirements

1. Firefox browser with [[tools/TamperData]] extension installed
2. Valid WordPress login with media upload access
3. Network access to the target WordPress instance

## Defense

Defensive measures and detection strategies:

- Implement server-side content-type validation beyond client-side checks
- Monitor upload logs for unusual request modifications via WAF rules
- Use file scanning tools to detect embedded scripts in uploads

## Objectives

1. Allow submission of malicious file content
2. Evade browser-based upload restrictions
3. Prepare for server-side exploitation

## Instructions

### Step 1: Activate TamperData

**Context**: Start the interception tool to capture upload requests.

Install and launch [[tools/TamperData]] in Firefox. Enable it to proxy all POST requests to `/wp-admin/async-upload.php` or similar endpoints.

### Step 2: Initiate Upload and Intercept

**Context**: Trigger the upload to capture the request for modification.

Navigate to the upload interface, select a file, and submit. When TamperData prompts, edit the request: remove or alter JavaScript validation fields (e.g., set content-type to image/png while allowing script inclusion).

### Step 3: Forward Modified Request

**Context**: Send the tampered request to the server.

Approve the modified POST in TamperData and monitor the response for successful upload acknowledgment.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/TamperData]]

## Tags

- [[xss]]
- [[bypass]]
- [[upload]]
