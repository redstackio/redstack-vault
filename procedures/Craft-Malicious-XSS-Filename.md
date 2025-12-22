---
tags:
  - xss
  - payload-crafting
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
updated_at: '2025-12-14T03:15:53.054Z'
sub_techniques: []
id: 186c8bd7-babe-48af-8f89-61f7ea5711da
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-XSS-Filename

## Summary

This procedure involves creating a filename for an uploaded file that contains an XSS payload, exploiting applications that fail to sanitize filenames before reflecting them in HTML contexts.

## Description

In scenarios like file uploads where filenames are displayed or processed without proper escaping, attackers can inject JavaScript payloads into the filename. For the Airbnb.es vulnerability, a payload such as "><img src='x' onerror=alert(document.cookie)> breaks out of HTML attributes and executes code to steal cookies. This targets web applications handling user uploads, requiring only basic knowledge of HTML and JavaScript injection.

## Requirements

1. Access to a text editor or file explorer to rename files
2. Understanding of XSS payload syntax
3. A target file (e.g., empty .txt) to apply the name to

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all uploaded filenames, stripping special characters and quotes
- Use secure file naming (e.g., UUIDs) instead of user-provided names
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or cookie access in logs

## Objectives

1. Generate a functional XSS payload embedded in a filename
2. Ensure payload executes in an HTML context
3. Prepare file for upload to trigger the exploit

## Instructions

### Step 1: Design the XSS Payload

**Context**: Construct a payload that closes any surrounding HTML tags or attributes and injects executable JavaScript.

No specific command; use a text editor to create the string: "><img src='x' onerror=alert(document.cookie)>

> This payload assumes reflection in an <img src="filename"> context. Test locally by saving an HTML file with <img src="><img src='x' onerror=alert(1)>.txt"> and opening it in a browser to verify alert(1) fires.

### Step 2: Apply to Filename

**Context**: Rename a dummy file with the payload to simulate upload.

Use file explorer or command line (e.g., mv dummy.txt "><img src='x' onerror=alert(document.cookie)>.txt on Linux/Mac).

> Expected output: File renamed successfully. Verify by checking file properties.

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
- [[payload-crafting]]
