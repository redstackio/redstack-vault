---
tags:
  - ssrf
  - file-upload
  - ios
  - nextcloud
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:40.123Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 91d123da-5e17-40c7-9b54-7030f9143710
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Proof-of-Concept-File-to-Nextcloud-iOS

## Summary

This procedure uploads a simple text file to the local storage of the Nextcloud iOS app to verify upload functionality and establish a target file for later SSRF exploitation in a vulnerability assessment.

## Description

In the context of testing the Nextcloud iOS app's local storage feature, this step involves creating and uploading a proof-of-concept text file named 'ssrfpoc.txt' with content 'test ssrf'. This file acts as a benign target that can be referenced in subsequent SSRF payloads to demonstrate local file disclosure without alerting defenses. The procedure exploits the app's lack of strict content validation during upload, setting the stage for more advanced manipulations. Expected outcomes include successful file persistence in the app's local directory, accessible via the file viewer.

## Requirements

1. Nextcloud iOS app installed and authenticated on an iOS device
2. Access to the local storage upload interface within the app
3. A text editor on the device or another app to create the proof file

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning on upload to block suspicious files
- Monitor app logs for unusual file access patterns or JavaScript execution attempts
- Use app sandboxing to restrict file:// protocol access from web views

## Objectives

1. Verify the ability to upload files to local storage
2. Create a reference file for SSRF testing
3. Confirm no immediate content restrictions

## Instructions

### Step 1: Create the Proof File

**Context**: Prepare a simple text file to serve as the target for SSRF disclosure.

Create a new text file named 'ssrfpoc.txt' with the exact content 'test ssrf' using any text editor on the iOS device.

### Step 2: Upload the File

**Context**: Use the Nextcloud app to store the file locally, confirming upload success.

Open the Nextcloud iOS app, navigate to the local storage or files section, and select the upload option. Choose 'ssrfpoc.txt' from your device's files and complete the upload process.

**Expected Output**: The file appears in the app's file list, and viewing it displays 'test ssrf'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[file-upload]]
- [[ios]]
- [[nextcloud]]
