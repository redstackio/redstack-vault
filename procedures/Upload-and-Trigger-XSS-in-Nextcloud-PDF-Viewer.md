---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - file-upload
  - pdf-trigger
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:21.091Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Upload-and-Trigger-XSS-in-Nextcloud-PDF-Viewer

## Summary

This procedure uploads a malicious PDF exploiting CVE-2018-5158 to Nextcloud and opens it in the PDF viewer, triggering XSS via JavaScript execution in the victim's browser.

## Description

Nextcloud's PDF viewer relies on vulnerable PDF.js, allowing embedded JS in PDFs to run in the browser context upon rendering. Uploading the POC PDF and viewing it executes the payload, potentially stealing cookies or exfiltrating data. This targets web sessions in browsers like Safari 13.0.5 and Firefox 74.0, with impacts including account takeover if combined with further payloads.

## Requirements

1. Authenticated access to Nextcloud for file uploads.
2. Malicious POC PDF prepared from CVE resources.
3. Target browser supporting the exploit (avoid Chrome for testing).

## Defense

Defensive measures and detection strategies:

- Enforce PDF sanitization on upload to strip JavaScript.
- Use updated PDF viewers or disable JS in rendering engines.
- Log and alert on PDF views with anomalous browser behavior.

## Objectives

1. Deliver the payload via file upload to the target.
2. Activate the exploit through viewer interaction.
3. Achieve JS execution in the browser for impact assessment.

## Instructions

### Step 1: Log In to Nextcloud

**Context**: Gain access to the file management interface.

Open the Nextcloud web app in your browser and authenticate with valid credentials.

> Ensures permission to upload and view files.

### Step 2: Upload the Malicious PDF

**Context**: Transfer the POC file to the server for later triggering.

Navigate to the 'Files' app, click 'Upload', and select the POC PDF from your local machine. Wait for the upload to complete.

> Expected output: File appears in the directory listing, e.g., 'poc.pdf'.

### Step 3: Open PDF in Viewer

**Context**: Render the PDF using the integrated vulnerable viewer to execute JS.

Click on the uploaded PDF file and select 'Open' or preview it directly. The PDF.js viewer loads and processes the embedded JavaScript.

> Success: PDF displays, and exploit triggers (monitor console for confirmation).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[drive-by-compromise]]

