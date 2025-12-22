---
id: p-upload-executable-contact
tags:
  - file-upload
  - malware-upload
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.202Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Arbitrary-Executable-as-Contact-Image

## Summary

This procedure exploits the lack of file type validation in the Nextcloud Contacts app's image upload feature to upload arbitrary executables, such as malware, disguised as contact photos.

## Description

The upload handler in the Contacts app accepts any file without MIME type or extension checks, allowing executables to be stored in the instance. This can lead to malware persistence accessible to users viewing contacts. The attack targets the web interface in a logged-in session, with outcomes including successful storage of harmful files.

## Requirements

1. Active Nextcloud session (e.g., via demo)
2. Access to Contacts app
3. Local executable file (e.g., SimpleCrackMe.exe) for testing

## Defense

Defensive measures and detection strategies:

- Enforce MIME type validation and file extension whitelisting on uploads
- Scan uploaded files with antivirus
- Log and monitor upload attempts for anomalous file types

## Objectives

1. Bypass upload restrictions to store executables
2. Demonstrate potential for malware distribution
3. Highlight storage of harmful content in user data

## Instructions

### Step 1: Create or Edit a Contact

**Context**: Prepare a contact entry to access the image upload functionality.

**Instructions**: In the Contacts app, create a new contact or edit an existing one, then click the image/photo field to open the upload popup.

> The popup appears as a standard file selector dialog.

### Step 2: Select and Upload Executable

**Context**: Choose and submit the arbitrary file to test validation bypass.

**Instructions**: In the upload popup, browse to and select 'SimpleCrackMe.exe' (or similar), then confirm the upload.

> The file is processed and saved without rejection, appearing as the contact's image.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[nextcloud]]
