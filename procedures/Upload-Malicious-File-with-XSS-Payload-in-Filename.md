---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Upload-Malicious-File-with-XSS-Payload-in-Filename
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.480Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - file-upload
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Upload-Malicious-File-with-XSS-Payload-in-Filename

## Summary

This procedure exploits the file upload feature in Concrete CMS 5.7.2.1 to inject a stored XSS payload into the filename, allowing malicious JavaScript to be stored and later executed when other users interact with the file in the manager.

## Description

In Concrete CMS 5.7.2.1, the file upload functionality lacks comprehensive sanitization for filenames, enabling attackers with upload permissions to embed JavaScript payloads. This builds on a partial fix from version 5.7.0.4 (issue #30019) that was incomplete. The payload persists in the filename and executes client-side when rendered on pages like delete or properties views, potentially leading to cookie theft or phishing attacks against other authenticated users.

## Requirements

1. Authenticated access to Concrete CMS with file upload permissions
2. A web browser to perform the upload
3. A benign file to upload (e.g., empty .txt file)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation for all user-supplied filenames, stripping HTML/JS tags
- Use Content Security Policy (CSP) to restrict script execution
- Monitor file uploads for suspicious patterns like angle brackets or script tags in metadata

## Objectives

1. Store an XSS payload in a file's filename without triggering immediate execution
2. Ensure the payload is viewable and executable by other users
3. Demonstrate persistence across sessions

## Instructions

### Step 1: Prepare the Malicious Filename

**Context**: Craft a filename that breaks out of any quoting and injects executable JavaScript, such as an img tag with an onerror handler to exfiltrate cookies.

No command required; manually enter the filename during upload.

> Use a payload like `'><img src=0 onerror=confirm(document.cookie)>.txt` to test execution via a cookie-confirming alert.

### Step 2: Perform the Upload

**Context**: Access the file upload interface and submit the file with the malicious name.

Navigate to the CMS dashboard > File Manager > Upload Files. Select your file and set the name to the payload before submitting.

> Upon successful upload, verify in the file manager that the filename displays the injected content without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[file-upload]]
