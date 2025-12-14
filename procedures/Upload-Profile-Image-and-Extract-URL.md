---
tags:
  - upload
  - profile-image
  - url-extraction
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
updated_at: '2025-12-14T17:25:34.402Z'
sub_techniques: []
id: 7f0fcd48-1648-433c-89f7-94930d39dfef
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Profile-Image-and-Extract-URL

## Summary

This procedure covers uploading prepared images as profile pictures in IRCCloud accounts and capturing the resulting direct URLs for subsequent IDOR exploitation.

## Description

Using the IRCCloud web interface, users upload images to set profile pictures, which generates user-specific URLs. These URLs contain parameters directly referencing the uploaded file without proper access controls. This step is performed on multiple accounts to obtain comparable URLs, setting up the IDOR manipulation. Outcomes include accessible image links that can be modified for unauthorized access.

## Requirements

1. Valid IRCCloud account credentials (at least two accounts)
2. Web browser access to IRCCloud interface
3. Prepared JPEG image with EXIF data

## Defense

Defensive measures and detection strategies:

- Enforce authentication checks on all image URLs
- Rate-limit profile image uploads per account
- Log and monitor URL access patterns for anomalies

## Objectives

1. Successfully upload image as profile picture
2. Extract direct URL with identifiable parameters
3. Repeat for multiple accounts to compare structures

## Instructions

### Step 1: Log In and Upload

**Context**: Access the profile settings to upload the image.

No command; via web UI: Navigate to account settings, select profile picture upload, choose the prepared JPEG, and confirm.

> Upload completes, and the image is set as profile picture.

### Step 2: Extract Image URL

**Context**: Obtain the direct link to the uploaded image.

Right-click the profile image or open in new tab to copy URL (e.g., https://www.irccloud.com/image/██████████?user_id=123).

> URL format reveals user-specific parameter like 'user_id' or hash.

### Step 3: Repeat for Second Account

**Context**: Perform identical upload on another account.

Follow Steps 1-2 on the second account to get a second URL (e.g., https://www.irccloud.com/image/█████?user_id=456).

> Ensures parameter differences for IDOR testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload
- profile-image
- url-extraction
