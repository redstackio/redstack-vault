---
id: proc-upload-profile-image
tags:
  - file-upload
  - rce
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
updated_at: '2025-12-14T05:32:13.412Z'
skill_level: intermediate
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
# Upload-Malicious-Profile-Image

## Summary

This procedure uploads the renamed malicious .php file as a profile image via the forum's upload feature, exploiting lack of validation to place the webshell on the server.

## Description

Targeted at the uploadProfile method in UsersController.php, the upload succeeds despite a 500 error, saving the file to a predictable /uploads/profile/ path. Requires a logged-in account; demonstrates how poor error handling leads to persistence.

## Requirements

1. Valid user account on the target forum
2. Access to profile settings page
3. Prepared malicious .php file

## Defense

Defensive measures and detection strategies:

- Implement comprehensive file validation (content scanning, extension whitelisting)
- Return proper errors without saving invalid files
- Rate-limit uploads and monitor for error patterns

## Objectives

1. Deliver the webshell to the server
2. Obtain save confirmation via error response
3. Enable subsequent access

## Instructions

### Step 1: Log In and Navigate to Profile

**Context**: Gain access to the upload interface.

**Instructions**: Log in to https://forum.getmonero.org, go to user profile, and select image upload option.

**Expected Output**: Upload form visible.

### Step 2: Submit the File

**Context**: Upload the .php file, ignoring validation flaws.

**Instructions**: Select and submit picture.php as the profile image.

**Expected Output**: 500 Internal Server Error, but file saved.

**Success Indicators**:
- Error response contains timestamp
- File persists on server

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

- profile-upload
- validation-bypass
