---
tags:
  - metadata
  - intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.612Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b78d3264-f4db-42cc-a065-f4914db0e539
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Process-Metadata-Edit-Request

## Summary

This procedure intercepts the automatic metadata edit request following upload, forwarding it to obtain the response containing the course ID.

## Description

After upload, the app issues a POST to /Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004editmetadata.aspx. Intercepting the response allows extraction of the generated course ID needed for shell access.

## Requirements

1. Burp Suite in intercept mode
2. Upload completed successfully
3. Response interception enabled

## Defense

Defensive measures and detection strategies:

- Sanitize metadata responses to avoid ID leaks
- Rate-limit sequential requests post-upload
- Audit metadata edits for anomalies

## Objectives

1. Capture metadata POST
2. Forward and intercept response
3. Preserve HTML for ID parsing

## Instructions

### Step 1: Enable Response Intercept

**Context**: Prepare Burp for the follow-up request.

Right-click in Burp and select 'Do intercept > response to this request'.

> Expected output: Intercept option active.

### Step 2: Forward Requests

**Context**: Process the metadata cycle.

Intercept the POST, forward it, then intercept and forward the response.

> Expected output: Full HTML response received.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- metadata
- intercept
