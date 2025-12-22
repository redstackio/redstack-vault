---
tags:
  - file-upload
  - malicious-payload
  - unrestricted-upload
type: procedure
tools:
  - '[[tools/Malicious-HTML-Payload-for-XSS-and-PHP-Shell]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:46:37.450Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 37b0c321-acb9-409f-8e07-5879032e6d8c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-Payload

## Summary

This procedure uploads a specially crafted HTML file containing XSS JavaScript and embedded PHP shell code to the request form, exploiting the lack of file type validation to introduce malicious content into the application.

## Description

Targeting web applications with unrestricted file uploads, such as those using XPages, this procedure selects the malicious HTML file via the form's browse button. The file includes JavaScript for stored XSS (e.g., <script>alert('XSS')</script>) and PHP code like <?php system($_GET['cmd']); ?> for a basic shell. Upon upload, the file is stored server-side without sanitization, enabling later exploitation. Prerequisites include having the payload file ready and being on the upload-enabled form page.

## Requirements

1. Prepared malicious HTML file with XSS and PHP code
2. Access to the form's file upload field
3. Browser supporting file selection

## Defense

Defensive measures and detection strategies:

- Enforce file type whitelisting (e.g., only PDF, DOC) and MIME type validation
- Scan uploads for embedded scripts using antivirus or WAF
- Store uploads outside web root and serve via sanitized viewer

## Objectives

1. Successfully attach and prepare the malicious file for submission
2. Bypass any client-side checks on file extension
3. Ensure file is queued for server-side storage

## Instructions

### Step 1: Locate Upload Field

**Context**: Identify the file attachment option on the form.

Scroll to the bottom of the form page where the 'browse' button for file upload is located.

> Upload field is visible and clickable.

### Step 2: Select Malicious File

**Context**: Choose the payload using the provided tool.

Click 'browse' and navigate to select the HTML file (e.g., unsure1.html) created with [[tools/Malicious-HTML-Payload-for-XSS-and-PHP-Shell]].

> File name appears in the upload field, ready for submission.

### Step 3: Verify File Selection

**Context**: Confirm no immediate rejection.

Check that the form accepts the .html extension without errors.

> No validation alerts; file is accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Malicious-HTML-Payload-for-XSS-and-PHP-Shell]]

## Tags

- [[file-upload]]
- [[malicious-payload]]
