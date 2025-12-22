---
tags:
  - xss
  - payload
  - javascript
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
updated_at: '2025-12-14T03:16:37.212Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fa4041b4-2c7b-4807-8302-8dfe9e6d4db6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-File-for-Iframe

## Summary

This procedure generates the HTML file loaded by the injected iframe, containing JavaScript for arbitrary code execution, such as an alert demonstrating the XSS.

## Description

The iframe src points to this local file, which includes a <script> tag executing JavaScript in the browser context. This achieves reflected XSS in the directory listing, potentially leading to session hijacking or data exfiltration.

## Requirements

1. Text editor for HTML creation
2. Same directory as the server files
3. Basic HTML and JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Scan uploaded or created files for malicious scripts
- Disable directory listings or use secure templating engines
- Employ content security policy (CSP) to block inline scripts and iframes

## Objectives

1. Load executable JavaScript via iframe
2. Demonstrate arbitrary code execution
3. Simulate real-world payload like keylogging or phishing

## Instructions

### Step 1: Create the HTML File

**Context**: Write the HTML with embedded script to alert on load.

**Command**:
```bash
cat > malware_frame.html << EOF
<html><head><meta charset="utf8"/><title>Frame embeded with malware :P</title></head><body><p>iframe element with malicious code</p><script>alert('Uh oh, I am bad, bad malware!!!')</script></body></html>
EOF
```

> This creates the file with the payload. Expected output: File saved, verifiable by cat malware_frame.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
