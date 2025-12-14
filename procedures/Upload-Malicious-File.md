---
tags:
  - malicious-upload
  - rce-potential
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
updated_at: '2025-12-14T05:32:10.263Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2bf9f702-7717-4c38-8a17-c9b098685bf7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload Malicious File

## Summary

This procedure exploits the unrestricted file upload by attaching dangerous files like .exe or .php to the DoD request, bypassing all type checks.

## Description

The upload feature in `███SubmitRequest/Index.cfm?fwa=wizardform` accepts any file under 5MB without extension or MIME validation. Testing with Visual Studio .exe installer and PHP webshell confirms acceptance. Uploaded files attach to support tickets, risking RCE if opened by staff or served via web.

## Requirements

1. Access to upload tab
2. Malicious file prepared (<5MB, e.g., .exe or .php shell)
3. Browser supporting file uploads

## Defense

Defensive measures and detection strategies:

- Enforce server-side file type whitelisting (e.g., only .pdf, .doc)
- Scan uploads with antivirus/malware detection
- Store uploads outside web root and sanitize filenames

## Objectives

1. Successfully attach unrestricted file
2. Demonstrate lack of validation
3. Position file for potential execution

## Instructions

### Step 1: Select and Upload File

**Context**: Choose a test malicious file to verify vulnerability.

Click 'Select File' and choose a .exe (e.g., installer) or .php script (<5MB).

> Expected output: File uploads and attaches without rejection.

### Step 2: Verify Attachment

**Context**: Confirm the file is linked to the request.

Check the attachment list in the form.

> Expected output: File name displayed, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[rce]]
