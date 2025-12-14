---
tags:
  - file-upload
  - malicious-payload
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:42.988Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f7f76fda-b076-4629-b663-702b39d85fcc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Library-to-Evernote-Note

## Summary

This procedure involves preparing a malicious native library file and uploading it as an attachment to an Evernote note, setting the stage for path traversal exploitation in the Android app.

## Description

In the context of exploiting the Evernote Android app, the attacker first creates or obtains a malicious `libjnigraphics.so` library compiled for ARM64 architecture. This library contains code to establish a reverse shell connection upon loading. The file is then attached to a note within the Evernote app. This step requires an attacker-controlled Evernote account and focuses on ingress of the payload without immediate execution.

## Requirements

1. Evernote Android app installed on attacker's device
2. Malicious `libjnigraphics.so` file (ARM64, with reverse shell payload targeting port 6666)
3. Attacker's Evernote account credentials

## Defense

Defensive measures and detection strategies:

- Implement file type validation and scanning for uploaded attachments in note-taking apps
- Monitor for unusual file uploads in mobile apps via endpoint detection tools
- Educate users on risks of opening shared notes from untrusted sources

## Objectives

1. Deliver the malicious payload into the app's ecosystem
2. Position the file for subsequent renaming and sharing
3. Ensure compatibility with victim's device architecture

## Instructions

### Step 1: Prepare the Malicious Library

**Context**: Compile or acquire the payload library that will execute a reverse shell to localhost:6666 when loaded.

No command required; use development tools like Android NDK to build the .so file with embedded shellcode.

### Step 2: Create and Upload to Note

**Context**: Attach the file to a new note in Evernote to make it shareable.

Open the Evernote app, create a new note, tap the attachment icon, and select the `libjnigraphics.so` file from the device storage.

> The file uploads with a default name; verify it's listed in the note.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- android
- payload-delivery
