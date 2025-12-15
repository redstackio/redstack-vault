---
id: proc-uuid-002
tags:
  - file-upload
  - data-tampering
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:09.922Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Arbitrary-Files-to-Server

## Summary

This procedure allows uploading arbitrary files to the server via the exposed debug page, potentially introducing malicious payloads or overwriting existing files.

## Description

Once on the debug page, the upload functionality lacks validation, enabling attackers to send any file type. Files are stored on the server and listed for further actions, risking server compromise if executable files are uploaded.

## Requirements

1. Access to the debug page (from prior procedure)
2. Local file to upload (e.g., JSON test file)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Validate and sanitize file uploads with type restrictions and size limits
- Store uploads outside the web root and scan for malware
- Log all upload attempts and alert on suspicious file types

## Objectives

1. Transfer files to the server without authentication
2. Verify upload success via the file list
3. Enable subsequent read or delete operations

## Instructions

### Step 1: Select File

**Context**: Choose a local file to upload to the server.

Click the 'Choose File' button on the debug page and select a file from your local system, or manually enter the file path in the location field.

> The file path field accepts standard formats; ensure the file is accessible.

### Step 2: Submit Upload

**Context**: Execute the upload to store the file on the server.

Click the 'Upload Files' button to submit.

> The file should appear in the list on the page upon success, confirming storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[data-tampering]]
