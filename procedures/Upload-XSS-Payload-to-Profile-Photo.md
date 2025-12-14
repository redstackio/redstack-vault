---
tags:
  - xss
  - file-upload
  - airbnb
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.050Z'
sub_techniques: []
id: 61cafdcb-1372-4b5a-9bd3-cefe0085e904
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-XSS-Payload-to-Profile-Photo

## Summary

This procedure uploads a file with a malicious filename to the profile photo feature on airbnb.es, triggering XSS execution when the filename is processed or displayed without sanitization.

## Description

The Airbnb.es profile photo upload mishandles filenames by reflecting them directly into HTML without escaping, allowing injected JavaScript to run in the context of the authenticated user. Upon upload, viewing the profile or processing the image executes the payload, enabling cookie theft and session hijacking. This requires an active user session and targets web-based upload endpoints.

## Requirements

1. Authenticated account on airbnb.es
2. Web browser with upload capabilities
3. Pre-crafted file with XSS filename from prior procedure

## Defense

Defensive measures and detection strategies:

- Enforce filename sanitization: remove or escape quotes, angle brackets, and script tags
- Validate file extensions and MIME types server-side
- Use HTTP-only and Secure flags on cookies to mitigate theft
- Log and alert on suspicious upload patterns or JavaScript errors

## Objectives

1. Deliver the XSS payload via legitimate upload feature
2. Achieve code execution in the browser context
3. Collect sensitive data like session cookies

## Instructions

### Step 1: Access Upload Feature

**Context**: Navigate to the profile section to reach the photo upload interface.

Log in to airbnb.es and go to account settings > profile > photo upload.

> Expected output: Upload dialog or form appears, ready for file selection.

### Step 2: Perform the Upload

**Context**: Select and submit the malicious file to trigger processing.

Choose the file named "><img src='x' onerror=alert(document.cookie)>.txt (or image file with same name) and complete the upload.

> Upon success, view the profile or trigger processing; the payload executes, alerting cookies. Modify payload (e.g., to send cookies to attacker server) for real exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
- [[airbnb]]
