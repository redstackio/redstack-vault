---
tags:
  - xss
  - self-xss
  - file-upload
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.534Z'
sub_techniques: []
id: 43454f30-6d18-44fd-bda7-59324649dad5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-Attachment-Filename

## Summary

This procedure exploits insufficient filename sanitization by uploading a file with an XSS payload in its name, triggering self-execution when the attachment is viewed in an iframe.

## Description

In the Acronis support case interface, attachments are rendered without proper escaping of user-supplied filenames, allowing JavaScript injection. The payload executes in an iframe context on www.acronis.com, alerting the document domain only for the uploader. Target environment is the web upload form. Expected outcome is payload execution upon viewing, confirming the self-XSS. Impact is low as it affects only the user.

## Requirements

1. Open support case from previous step
2. Benign file to upload (e.g., empty PNG)
3. Payload: `"><img src=\"x\" onerror=\"alert(document.domain)\">.png`

## Defense

Defensive measures and detection strategies:

- Sanitize and escape filenames during rendering, stripping script tags and quotes
- Render attachments in isolated contexts or use Content Security Policy (CSP) to block inline scripts
- Monitor for unusual filename patterns in logs

## Objectives

1. Inject XSS payload via filename
2. Trigger execution on view
3. Verify self-XSS with domain alert

## Instructions

### Step 1: Prepare Malicious File

**Context**: Rename a harmless file with the XSS payload to bypass basic checks.

No command required; create or rename a file (e.g., using file explorer) to `"><img src=\"x\" onerror=\"alert(document.domain)\">.png`.

> Ensure the file is a valid image or document to avoid upload rejection.

### Step 2: Upload in Support Case

**Context**: Attach the file to the case, injecting the payload.

No command required; in the case details, expand attachments, add a comment if prompted, select the file, and upload.

> Upload succeeds; the filename appears in the list without immediate execution.

### Step 3: View Attachment to Trigger

**Context**: Access the attachment to execute the payload in the iframe.

No command required; click to view the attachment.

> An alert box displays 'www.acronis.com' or similar, confirming execution. Only visible to the uploader.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- self-xss
- file-upload
