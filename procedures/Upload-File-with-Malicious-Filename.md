---
tags:
  - file-upload
  - xss-injection
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.629Z'
sub_techniques: []
id: 3e6d4fc0-530b-40e8-8a75-adff32829466
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-File-with-Malicious-Filename

## Summary

This procedure describes injecting an XSS payload into a file's filename during an upload attempt in the Shopify live chat to exploit the lack of sanitization in error responses.

## Description

The Shopify live chat file upload feature rejects non-image files but echoes the filename in an error message without HTML escaping. By crafting a filename with JavaScript, such as <img src="c" onerror=alert(1)>, the payload executes when the error renders. This targets the authenticated browser context, potentially leading to session hijacking.

## Requirements

1. Active authenticated session in Shopify live chat
2. A local file (e.g., .txt) to upload
3. Knowledge of disallowed file types (non-jpg/jpeg/gif/png)

## Defense

Defensive measures and detection strategies:

- Sanitize all user-supplied inputs, including filenames, with HTML entity encoding
- Validate file types server-side before generating error messages
- Implement Content Security Policy (CSP) to restrict inline script execution

## Objectives

1. Submit a file with an embedded XSS payload in the filename
2. Trigger the error response that reflects the payload
3. Set up conditions for JavaScript execution

## Instructions

### Step 1: Prepare Malicious Filename

**Context**: Create a filename containing the XSS payload to bypass sanitization.

Rename a local file to `<img src="c" onerror=alert(1)>` or `<svg onload="alert('xx')>"`. Ensure the extension is not an allowed image type.

> This payload uses common XSS vectors; test in a safe environment first.

### Step 2: Initiate Upload in Chat

**Context**: Use the chat's file upload UI to submit the prepared file.

In the live chat interface, click the file attachment icon, select the renamed file, and send it.

> The upload will fail due to type restrictions, generating the vulnerable error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- xss-injection
