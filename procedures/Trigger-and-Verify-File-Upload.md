---
id: proc-uuid-3
tags:
  - file-upload
  - xss
  - verification
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:10.144Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Trigger and Verify File Upload

## Summary

This procedure submits the avatar form to trigger the server's download of the external file and verifies successful storage and execution of the payload, such as JavaScript in an SVG.

## Description

Upon form submission, ExpressionEngine fetches the file from the provided URL and saves it to /images/avatars/ with the original extension. No validation occurs, allowing malicious content. Verification involves accessing the uploaded file directly or via proxy interception. Assumes prior URL input and admin context.

## Requirements

1. Form populated with malicious URL
2. HTTP proxy tool for traffic monitoring
3. Browser for payload execution testing

## Defense

Defensive measures and detection strategies:

- Scan downloaded files for malicious content using antivirus
- Log and alert on external file downloads in web apps

## Objectives

1. Force server-side file download and storage
2. Confirm payload integrity and executability
3. Observe impact like client-side alerts

## Instructions

### Step 1: Submit the Form

**Context**: Initiate the download process.

No specific command; click 'Save' or submit the profile settings form.

> Page redirects, and server processes the URL.

### Step 2: Monitor and Access Uploaded File

**Context**: Intercept or directly request the stored file to verify.

Use [[tools/HTTP-Proxy]] to capture the request to http://[HOST]/images/avatars/test_1.svg, or open the URL in a browser.

> If SVG contains <script>alert('XSS')</script>, an alert box appears, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[file-upload]]
- [[xss]]
- [[verification]]
