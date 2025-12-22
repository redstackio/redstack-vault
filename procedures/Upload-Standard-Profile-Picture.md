---
id: proc-713407-upload-standard
tags:
  - upload
  - file
  - profile
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
updated_at: '2025-12-14T17:26:56.306Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques:
  - '[[T1105.003]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Standard-Profile-Picture

## Summary

This procedure performs a baseline profile picture upload on HackerOne to capture the normal request structure, enabling subsequent modification for exploitation.

## Description

Targeting the profile update form, this step uploads a standard image to understand the HTTP request payload. It uses the web form at https://hackerone.com/profile/edit and assumes proxy interception is configured. Outcome: Successful upload or captured request for alteration.

## Requirements

1. Access to profile edit page
2. Standard image file (e.g., JPG under 5MB)
3. Proxy tool like Burp Suite configured for interception

## Defense

Defensive measures and detection strategies:

- Validate file types and sizes on upload
- Log all file upload attempts

## Objectives

1. Submit a normal upload to baseline the request
2. Capture the multipart form data for modification
3. Confirm upload endpoint behavior

## Instructions

### Step 1: Select Image File

**Context**: Choose a valid file to initiate the upload process.

No command required; in the browser form, select an image file via the file input.

> File is attached to the form; preview may appear.

### Step 2: Submit Update Profile

**Context**: Trigger the HTTP POST request.

No command required; click the 'Update Profile' button.

> Request is intercepted if proxy is active; otherwise, profile updates successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- [[T1105.003]] Alternative API

## Commands Used


## Tools Used


## Tags

- upload
- file
- profile
