---
id: proc-765679-svg-upload
tags:
  - file-upload
  - svg-payload
  - xss
type: procedure
tools:
  - '[[tools/Notepad]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.708Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Craft-and-Upload-Malicious-SVG-to-Inbox

## Summary

This procedure creates a malicious SVG file with an XSS payload, disguises it as an image, and uploads it to an Outpost Inbox conversation for storage and later execution.

## Description

Exploit the lack of file validation by renaming SVG files containing JavaScript (via onload attribute) to .png, .gif, or .bmp extensions. Upload via the web interface to a new conversation targeted at the victim. This stores the payload server-side, leading to execution when rendered in the browser.

## Requirements

1. Authenticated attacker session in Outpost
2. Text editor like [[tools/Notepad]] for payload creation
3. Victim email for conversation targeting

## Defense

Defensive measures and detection strategies:

- Validate file content (not just extension) using MIME type checking
- Sanitize SVG files by removing scriptable attributes like onload
- Scan uploads for JavaScript patterns

## Objectives

1. Bypass superficial format checks
2. Store XSS payload in attachments
3. Deliver to victim via conversation

## Instructions

### Step 1: Craft SVG Payload

**Context**: Create the malicious SVG using a text editor.

Open [[tools/Notepad]] and enter: `<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="2560.000000pt" height="1600.000000pt" viewBox="0 0 2560.000000 1600.000000" preserveAspectRatio="xMidYMid meet" onload="alert(document.cookie)">`. Save as Payload.png (repeat for .gif and .bmp).

> File saved with disguised extension; verify content shows onload alert.

### Step 2: Create Conversation and Upload

**Context**: Use the Inbox to send the payload.

In the authenticated session, create a new conversation, add victim email (seq1@seq1.teamoutpost.com), attach the three files, and send.

> Attachments uploaded; conversation sent without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Notepad]]

## Tags

- [[file-upload]]
- [[svg-payload]]
- [[xss]]
