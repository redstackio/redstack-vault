---
id: proc-uuid-1
tags:
  - xss
  - file-upload
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Filename-in-Nextcloud

## Summary

This procedure involves uploading or renaming a file in Nextcloud with a malicious JavaScript payload embedded in the filename, setting the stage for a reflected XSS attack when the file is later renamed by a victim.

## Description

In the context of Nextcloud's file management, filenames are not sufficiently sanitized during certain operations. By creating a file named with an XSS payload like `<img src=x onerror=prompt(1)>.jpg`, an attacker positions the vulnerability. When a victim attempts to rename this file, the error handling reflects the payload. This requires authenticated access to upload files and assumes a shared environment where victims can interact with attacker-created files. Expected outcomes include payload reflection without immediate execution, pending trigger.

## Requirements

1. Authenticated access to Nextcloud web interface
2. Permissions to create or upload files in a shared directory
3. Web browser for interaction

## Defense

Defensive measures and detection strategies:

- Implement strict filename sanitization on upload and display
- Enforce CSP headers to block inline JavaScript execution
- Monitor file creation logs for suspicious filenames containing script tags

## Objectives

1. Inject XSS payload into a persistent filename
2. Position file for victim interaction
3. Prepare for reflection in error messages

## Instructions

### Step 1: Log In and Navigate to File Area

**Context**: Gain access to the file management section to prepare for file creation.

Log in to Nextcloud and navigate to the files app or a shared folder.

### Step 2: Upload or Create File with Malicious Name

**Context**: Set the filename to include the XSS payload to embed the script.

Use the upload interface or new file creation: Name the file `<img src=x onerror=prompt(1)>.jpg` and save or upload a dummy content file.

> This embeds the payload in the filename, which will be stored and displayed without sanitization in error contexts.

**Expected Output**: File listed in the directory with the exact malicious name.

### Step 3: Verify File Accessibility

**Context**: Ensure the file is visible to potential victims.

Share the folder if needed and confirm the filename displays correctly for other users.

> Success confirms the payload is persisted.

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
- nextcloud
