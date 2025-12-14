---
tags:
  - ssrf
  - upload
  - nextcloud
  - ios
type: procedure
tools: []
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.553Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f3ee1761-97cd-475c-a633-78f4c99a6f76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Test-File-to-Verify-Local-Storage

## Summary

This procedure verifies the basic upload functionality in the Nextcloud iOS app's local storage feature by uploading a simple text file, setting the stage for more advanced manipulations in an SSRF attack.

## Description

In the context of exploiting SSRF in the Nextcloud iOS app, this initial step confirms that files can be uploaded to local storage without immediate restrictions. It uses a benign text file to test the feature, ensuring the app accepts uploads before proceeding to malicious content. The target environment is an iOS device with the vulnerable Nextcloud app installed. Expected outcomes include successful file listing and access, indicating lack of basic validation.

## Requirements

1. Nextcloud iOS app installed and accessible on an iOS device
2. Permissions to use the local storage upload feature
3. A test file prepared with simple text content like 'test ssrf'

## Defense

Defensive measures and detection strategies:

- Implement file type and content validation on upload
- Monitor for unusual file uploads in app logs
- Use sandboxing to restrict app access to local file system

## Objectives

1. Confirm upload capability to local storage
2. Establish baseline for file handling behavior
3. Identify any immediate upload restrictions

## Instructions

### Step 1: Prepare and Upload Test File

**Context**: Create a simple text file to test the upload process without triggering any security alerts.

Navigate to the local storage section in the Nextcloud iOS app and select the upload option. Choose the prepared text file containing 'test ssrf' and complete the upload.

> The file should upload without errors, appearing in the local storage list.

### Step 2: Verify Upload Success

**Context**: Check that the file is accessible post-upload to confirm functionality.

Browse to the uploaded file in the app and open it to view the content.

> Expected output: The text 'test ssrf' is displayed, confirming successful upload and access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[upload]]
- [[nextcloud]]
- [[ios]]
