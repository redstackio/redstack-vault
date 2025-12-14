---
tags:
  - file-upload
  - bypass
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
updated_at: '2025-12-14T05:32:13.341Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4669ce60-23e9-4b5e-b125-c711a2a47512
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-File-as-Profile-Picture

## Summary

This procedure uploads the prepared malicious MVG payload as a profile picture through the web application's edit endpoint, bypassing basic file type checks by using a .gif extension.

## Description

The target application at /settings/profile/edit allows users to upload profile pictures without verifying file contents, only relying on extensions. By naming the ASCII MVG file x.gif, it passes initial checks and gets stored for processing, setting up the RCE.

## Requirements

1. Valid user session in the web application
2. Access to /settings/profile/edit endpoint
3. Prepared x.gif file from previous procedure

## Defense

Defensive measures and detection strategies:

- Enforce MIME type validation on upload
- Scan files for non-image content
- Log and monitor upload attempts

## Objectives

1. Successfully submit the file to the server
2. Ensure the file is queued for ImageMagick processing
3. Avoid triggering upload errors

## Instructions

### Step 1: Access Upload Endpoint

**Context**: Log in and navigate to the profile edit page to locate the upload form.

Use browser or curl to POST the file:

```bash
curl -X POST -F "profile_picture=@x.gif" https://target.com/settings/profile/edit -b "session=your_cookie"
```

> Expected output: HTTP 200 or redirect confirming upload success.

### Step 2: Confirm Upload

**Context**: Check if the profile picture is updated or if any error occurs.

Refresh the profile page or check response for success message.

> Expected output: Profile picture set, no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
