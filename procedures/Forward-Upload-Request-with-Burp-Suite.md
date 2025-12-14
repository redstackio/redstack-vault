---
tags:
  - proxy
  - request-forward
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.617Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e03ec3e0-9f8b-4124-b161-7ddb80397f97
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Upload-Request-with-Burp-Suite

## Summary

This procedure forwards the intercepted upload request in Burp Suite, allowing the server to process and extract the malicious SCORM ZIP without validation.

## Description

The POST request contains the ZIP as multipart form data. Forwarding triggers extraction to /CServer/Courseware/, deploying the ASPX shell due to absent file type checks.

## Requirements

1. Intercepted request in Burp Repeater
2. Valid session in proxy
3. Target endpoint responsive

## Defense

Defensive measures and detection strategies:

- Validate ZIP contents pre-extraction
- Block executable file deployment
- Monitor file system changes in course directories

## Objectives

1. Submit request for processing
2. Confirm extraction success
3. Transition to metadata step

## Instructions

### Step 1: Review Intercepted Request

**Context**: Inspect the POST to ensure ZIP payload is intact.

In Burp Repeater, verify multipart/form-data with file.

> Expected output: Request body shows ZIP upload.

### Step 2: Forward Request

**Context**: Release the request to the server.

Click 'Forward' in Burp to send the POST.

> Expected output: Server 200 OK or redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy
- request-forward
