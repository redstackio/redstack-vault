---
tags:
  - upload
  - burp-suite
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
updated_at: '2025-12-14T17:29:44.622Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 32fb208e-95c7-48bd-a94a-c16deb809602
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-SCORM-Package-Upload

## Summary

This procedure starts the upload of the malicious SCORM ZIP to the vulnerable endpoint, using Burp Suite to intercept the request for controlled submission.

## Description

The endpoint at https://████████/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004uploadcourse.aspx lacks authorization checks, allowing any authenticated user to upload. Interception ensures the request is forwarded only when ready, preventing premature execution.

## Requirements

1. Active authenticated session
2. Malicious SCORM ZIP prepared
3. Burp Suite configured as proxy

## Defense

Defensive measures and detection strategies:

- Require admin roles for uploads
- Implement file size/type limits
- Log and alert on upload attempts

## Objectives

1. Select and submit ZIP via form
2. Capture POST in Burp Repeater
3. Prepare for forwarding

## Instructions

### Step 1: Navigate to Upload Page

**Context**: Access the SCORM upload interface.

Go to https://████████/Kview/CustomCodeBehind/base/courseware/scorm/management/scorm2004uploadcourse.aspx.

> Expected output: Upload form visible.

### Step 2: Select File and Intercept

**Context**: Choose the malicious ZIP and enable Burp interception.

Select the ZIP file and click upload, with Burp Repeater active.

> Expected output: POST request intercepted in Burp.

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

- upload
- burp-suite
