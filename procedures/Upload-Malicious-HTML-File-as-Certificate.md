---
tags:
  - unrestricted-file-upload
  - malicious-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:15:41.705Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 15f6287e-a145-4452-89bf-9b1aeaa7123c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-File-as-Certificate

## Summary

This procedure exploits an unrestricted file upload vulnerability in the certificate upload feature by submitting a malicious HTML file containing JavaScript, which is stored on the server without content-type validation, setting up a stored XSS attack vector.

## Description

The web application's certificate upload endpoint fails to validate uploaded file types, allowing arbitrary files like HTML to be accepted and stored. An attacker creates an HTML file with a script payload (e.g., alert(document.cookie) for cookie theft) and uploads it via the authenticated certification tab. The file is saved and made accessible, enabling later execution when viewed. This targets applications handling user-submitted attachments without MIME-type checks or sanitization.

## Requirements

1. Valid user account and active login session
2. Local HTML file with malicious JavaScript payload
3. Access to the certification tab in the web application

## Defense

Defensive measures and detection strategies:

- Validate and restrict uploaded file types to only allowed extensions (e.g., .crt, .pem) using server-side checks
- Scan uploads for malicious content using antivirus or WAF rules
- Store files outside the web root and serve them with no-execute headers (e.g., Content-Type: application/octet-stream)

## Objectives

1. Bypass file upload restrictions to store arbitrary code on the server
2. Position malicious content for execution in user contexts
3. Enable potential data exfiltration via XSS

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and reach the upload interface.

Log in with your credentials and click on the 'certification' tab to access the upload form.

### Step 2: Prepare and Upload File

**Context**: Create and submit the malicious file to exploit the vulnerability.

Create a file named 'xss.html' with content: `<html><body><script>alert(document.cookie)</script></body></html>`. In the upload field, select this file as the certificate attachment and submit the form.

**Expected Output**: Success message with the file listed in attachments; no rejection for file type.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unrestricted-file-upload]]
- [[malicious-upload]]
