---
tags:
  - upload
  - file-upload
  - tus
type: procedure
tools:
  - '[[tools/tusd]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Node.js
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 19abb345-a9ae-433c-ba67-900ac4c3f1fe
created_at: '2025-12-14T03:16:14.081Z'
updated_at: '2025-12-14T03:16:14.081Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Crafted-SVG-via-Uppy-Dashboard

## Summary

This procedure uses the Uppy dashboard to upload the malicious SVG file, leveraging the TUS protocol via tusd server, which stores the file without content validation, setting up for XSS execution.

## Description

The Uppy dashboard provides a web interface for file selection and upload. The backend tusd server handles resumable uploads but serves files directly to browsers without sanitizing SVG contents, allowing embedded scripts to persist and execute later.

## Requirements

1. Running Uppy dev server on port 3452
2. Crafted SVG file prepared
3. Browser access to localhost:3452

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning on upload
- Log and monitor upload endpoints for anomalous file types
- Rate-limit uploads to prevent abuse

## Objectives

1. Successfully store the malicious file in the system
2. Generate a viewable link for the uploaded file
3. Confirm no upload rejection due to content

## Instructions

### Step 1: Access Dashboard

**Context**: Navigate to the Uppy interface.

Open http://localhost:3452 in a browser.

> Loads the file upload dashboard. Expected output: Interface with file selection option.

### Step 2: Select and Upload File

**Context**: Choose the SVG and initiate upload.

Click 'Select files', choose `malicious.svg`, and click upload.

> Uses tusd for transfer. Expected output: Progress bar completes, file listed with link.

### Step 3: Verify Upload

**Context**: Check that the file is stored and accessible.

Inspect the dashboard list for the file entry.

> Confirms persistence. Expected output: File name visible, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/tusd]]

## Tags

- upload
- file-upload
- tus
