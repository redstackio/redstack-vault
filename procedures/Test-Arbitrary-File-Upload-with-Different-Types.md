---
id: proc-uuid-4
tags:
  - arbitrary-file-upload
  - zip
  - extension-bypass
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
updated_at: '2025-12-14T05:32:10.142Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Test Arbitrary File Upload with Different Types

## Summary

This procedure repeats the upload process with a non-image file like a ZIP to prove the vulnerability allows arbitrary extensions, potentially leading to server-side exploitation beyond client-side attacks.

## Description

By reusing the avatar link feature with a ZIP URL, the system saves the archive in the uploads folder without checks, demonstrating full arbitrary upload capability. This could enable further attacks like extracting to execute commands. Builds on prior steps in an admin session.

## Requirements

1. Successful prior upload confirmation
2. External host with ZIP file (e.g., server wizard archive)
3. Access to verify file in avatars directory

## Defense

Defensive measures and detection strategies:

- Enforce file type whitelisting and MIME validation on downloads
- Restrict writable directories like uploads/ from executing files

## Objectives

1. Upload non-standard file types
2. Confirm lack of extension or content restrictions
3. Highlight potential for RCE via uploaded executables

## Instructions

### Step 1: Repeat Upload Process

**Context**: Use the same form to input a new URL.

No specific command; return to avatar settings, select 'Link to avatar', and enter https://ellislab.com/asset/file/ee_server_wizard.zip.

> Form accepts the ZIP URL.

### Step 2: Submit and Verify

**Context**: Trigger download and check storage.

No specific command; submit the form and access http://[HOST]/images/avatars/ee_server_wizard_1.zip.

> The ZIP file is downloadable, confirming arbitrary storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[arbitrary-file-upload]]
- [[zip]]
- [[extension-bypass]]
