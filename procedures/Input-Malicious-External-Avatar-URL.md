---
id: proc-uuid-2
tags:
  - arbitrary-file-upload
  - external-url
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.147Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Input Malicious External Avatar URL

## Summary

This procedure involves selecting the external link option in the avatar settings and providing a URL to a malicious file, exploiting the lack of URL or content validation in ExpressionEngine.

## Description

ExpressionEngine's avatar feature allows linking to external images, but it downloads and saves the file without checking MIME types, content, or extensions, using the original filename. This enables uploading payloads like malicious SVGs. Requires admin access and the profile settings page loaded.

## Requirements

1. Access to the 'Change avatar' section
2. Control over an external server hosting the malicious file
3. Browser or proxy for form interaction

## Defense

Defensive measures and detection strategies:

- Validate and sanitize external URLs in file download functions
- Restrict avatar sources to whitelisted domains

## Objectives

1. Deliver malicious file URL to the server
2. Bypass local upload restrictions
3. Set stage for automatic download

## Instructions

### Step 1: Select Link Option

**Context**: Choose the external linking method to avoid direct uploads.

No specific command; in the form, select 'Link to avatar' radio button or dropdown.

> The URL input field becomes active.

### Step 2: Enter Malicious URL

**Context**: Provide a URL to a file with exploitable content, such as SVG with embedded JavaScript.

No specific command; input http://strukt.tk/test.svg (or your controlled URL) into the field.

> Form accepts the input without errors, ready for submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[arbitrary-file-upload]]
- [[external-url]]
