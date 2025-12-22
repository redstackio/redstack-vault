---
id: proc-fanfootage-rename-payload
tags:
  - xss
  - payload-injection
  - filename-manipulation
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.312Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Rename-Image-with-XSS-Payload

## Summary

This procedure details crafting a malicious image filename containing an XSS payload for upload in FanFootage, exploiting the lack of sanitization in Paperclip to inject executable HTML/JavaScript.

## Description

The vulnerability stems from Paperclip reflecting the original filename directly into the profile page HTML without encoding, allowing payloads like closing tags followed by script elements. This step focuses on local file preparation and upload submission. In the attack scenario, it enables injection that triggers on profile view, leading to JavaScript execution for data theft. Prerequisites: Access to the upload form from the prior procedure.

## Requirements

1. Local image file (e.g., a small JPG)
2. File system access to rename files
3. Knowledge of XSS payloads compatible with HTML context

## Defense

Defensive measures and detection strategies:

- Sanitize or strip special characters from filenames on upload
- Encode filenames with HTML entities (e.g., via Rails' h() helper)
- Validate file extensions and scan for embedded scripts

## Objectives

1. Create a filename that breaks out of HTML context and injects executable code
2. Upload the file without server rejection
3. Ensure payload survives storage and reflection

## Instructions

### Step 1: Prepare Local File

**Context**: Rename a benign image to embed the XSS payload.

Select an image file, e.g., test.jpg, and rename it to `'><svg onload=alert(1)>.jpg`. The payload closes a parent tag (e.g., <img src="...">) and injects an SVG that loads JavaScript.

> Expected: File renamed successfully; verify by opening in text editor to see payload in name.

### Step 2: Submit Upload

**Context**: Use the renamed file in the web form to transmit the payload.

In the browser's upload dialog, select the renamed file and submit the form. Monitor network requests for the filename in POST data.

> Expected: Server accepts upload; no immediate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
