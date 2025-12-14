---
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.301Z'
sub_techniques: []
id: c4029278-33ad-4281-9427-083583090299
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Filename-for-XSS

## Summary

This procedure creates a file with a filename containing a stored XSS payload, exploiting the lack of sanitization in http-file-server's directory listing to inject JavaScript that executes on client-side interaction.

## Description

Filenames in the server's HTML output are not HTML-encoded, allowing injection of attributes like onmouseover with alert(1). The payload '" onmouseover=alert(1) "' closes a quote in the HTML and adds the event handler. This is performed in a test directory like ~/Desktop/ to simulate a shared folder scenario.

## Requirements

1. Access to a writable directory (e.g., ~/Desktop/)
2. Shell access on Linux
3. Basic file creation tools like touch

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs like filenames before rendering in HTML
- Implement Content Security Policy (CSP) to block inline scripts
- Scan shared directories for suspicious filenames with script tags or event handlers

## Objectives

1. Store the XSS payload persistently in the filename
2. Prepare for server exposure leading to client execution
3. Demonstrate injection without direct HTML modification

## Instructions

### Step 1: Create the Malicious File

**Context**: Use touch to create an empty file with the payload in its name, ensuring special characters are handled properly.

**Command**:
```bash
touch '~/Desktop/" onmouseover=alert(1) "'
```

> The single quotes around the filename handle the embedded double quotes. Expected output is no error, and the file appears in ls listing. Verify with ls -la to see the filename intact.

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
- payload-injection
