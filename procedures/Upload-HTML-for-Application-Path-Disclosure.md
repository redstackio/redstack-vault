---
tags:
  - ssrf
  - html-manipulation
  - javascript
  - nextcloud
  - ios
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:39:09.550Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: fdac605a-0e0a-4f83-a682-e9eb66efe7f8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Upload-HTML-for-Application-Path-Disclosure

## Summary

This procedure involves uploading a manipulated HTML file disguised as a common type to the Nextcloud iOS local storage, enabling JavaScript execution to disclose the application path as part of an SSRF attack.

## Description

Targeting the lack of sanitization in the Nextcloud iOS app's local storage, this step uploads an HTML payload using an SVG onload attribute to execute JavaScript that outputs the current document location. The file is manipulated to bypass potential extension checks. In the attack scenario, this reveals the base path needed for subsequent file:// SSRF requests. Prerequisites include verified upload access from prior steps. Outcomes include successful upload and preparation for path revelation.

## Requirements

1. Access to local storage upload in Nextcloud iOS app
2. Prepared HTML payload: <svg/onload=document.write(document.location)>
3. Ability to rename file extension (e.g., to .txt)

## Defense

Defensive measures and detection strategies:

- Sanitize uploaded file contents to strip HTML/JS
- Block SVG and scriptable elements in mobile viewers
- Log and alert on suspicious file content patterns

## Objectives

1. Bypass file type validation for HTML upload
2. Position malicious payload for JavaScript execution
3. Prepare for application path extraction

## Instructions

### Step 1: Prepare Manipulated HTML File

**Context**: Create the payload to execute JavaScript upon loading.

Edit a file to include the content `<svg/onload=document.write(document.location)>` and save it with a common extension like .txt to evade checks.

> This disguises the HTML as a safe text file.

### Step 2: Upload the File

**Context**: Use the app's upload feature to store the payload.

In the Nextcloud iOS app, go to local storage, select upload, and choose the manipulated file.

> Expected output: Upload completes without rejection, file listed in storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[html-manipulation]]
- [[JavaScript]]
- [[nextcloud]]
- [[ios]]
