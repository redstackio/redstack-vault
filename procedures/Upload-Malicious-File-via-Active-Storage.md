---
tags:
  - upload
  - active-storage
  - mime-bypass
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
updated_at: '2025-12-14T03:16:02.463Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b7682eee-8307-413b-bf17-939c32d2b3e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-File-via-Active-Storage

## Summary

This procedure uploads a malicious .mml file to a Ruby on Rails application using Active Storage, relying on extension-based MIME typing to bypass content validation.

## Description

Active Storage in Rails uses Marcel::MimeType.for to detect file types, falling back to the file extension when magic bytes do not match (common for text-based MathML). The .mml extension triggers application/mathml+xml, allowing the file to be stored and served without sanitization, setting up stored XSS for viewers.

## Requirements

1. Authenticated session in the Rails application
2. Upload endpoint enabled via Active Storage
3. Malicious math.mml file prepared

## Defense

Defensive measures and detection strategies:

- Enforce file extension blacklisting (e.g., block .mml)
- Use content scanning tools like ClamAV on uploads
- Log and monitor unusual MIME types in storage services

## Objectives

1. Successfully store the payload
2. Obtain a direct URL for access
3. Confirm MIME type preservation

## Instructions

### Step 1: Prepare Upload

**Context**: Ensure the file is ready and the app allows uploads.

Verify Active Storage configuration in Rails (e.g., has_one_attached or similar for the model).

> No specific command; use the web form or API endpoint for upload.

### Step 2: Submit the File

**Context**: Perform the upload action.

Use the application's file upload interface to select and submit math.mml. Monitor for errors in Rails logs if accessible.

> Expected: Upload succeeds, file attached to model, URL generated (e.g., /rails/active_storage/blobs/.../math.mml).

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
- active-storage
- mime-bypass
