---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - self-xss
  - shopify
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
updated_at: '2025-12-14T00:11:16.093Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-Filename-for-Self-XSS

## Summary

This procedure exploits a self-XSS vulnerability by uploading an invalid CSV file with a JavaScript payload embedded in the filename, which is reflected unsanitized in the error message, executing code only in the attacker's browser.

## Description

The Shopify import feature fails to sanitize uploaded filenames, allowing payloads like "><img src=xx onerror=alert(document.domain)> to break out of HTML context and execute on error display. This is limited to self-XSS, affecting only the uploader, with low impact but demonstrating a reflection flaw. Prerequisites include admin access and an invalid file (e.g., non-CSV content).

## Requirements

1. Access to import page in Shopify admin
2. An invalid CSV file (e.g., text file renamed)
3. JavaScript payload knowledge for testing

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all reflected user inputs, including filenames
- Validate file extensions and content before processing
- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous error messages with script tags

## Objectives

1. Trigger filename reflection in error output
2. Execute JavaScript payload in browser
3. Confirm self-XSS without cross-user impact

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a file that will fail validation but carry the payload.

Rename an empty text file to "><img src=xx onerror=alert(document.domain)>.csv" or similar payload.

> Ensure the file is invalid (e.g., no proper CSV headers) to trigger error reflection.

### Step 2: Upload the File

**Context**: Submit via the import form to invoke the vulnerable reflection.

In the import page, select the prepared file and click 'Upload' or equivalent.

> The system processes the upload, detects invalidity, and displays an error echoing the filename, executing the onerror handler.

### Step 3: Verify Execution

**Context**: Observe the payload trigger.

Watch for an alert dialog showing the domain (e.g., 'yourstore.myshopify.com').

> Alert confirms successful self-XSS; inspect page source for reflected payload if needed.

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
- [[self-xss]]
- [[shopify]]
- [[file-upload]]
