---
tags:
  - xss-payload
  - file-creation
type: procedure
tools:
  - '[[tools/touch]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/touch-malicious-filename]]'
platforms:
  - Linux
  - Node.js
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 083fbeef-d772-4407-9db9-01dc107d6d95
created_at: '2025-12-14T03:15:41.884Z'
updated_at: '2025-12-14T03:15:41.884Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Filename-File

## Summary

This procedure creates an empty file with a filename containing a stored XSS payload that injects malicious JavaScript into the serve module's directory listing HTML.

## Description

The payload '"><svg onload=alert(3333333);' closes an HTML attribute (e.g., <a href="filename">) and injects an SVG element with an onload event, executing JavaScript when rendered. This exploits the lack of HTML escaping in serve's directory listing generation. The file must be created in the served directory while the server runs.

## Requirements

1. Unix-like shell (Linux/macOS) or equivalent
2. Write permissions in current directory
3. Serve server running

## Defense

Defensive measures and detection strategies:

- Sanitize filenames on upload/creation
- Escape HTML in directory listings
- Use file naming policies to block special characters

## Objectives

1. Inject persistent XSS payload via filename
2. Store the exploit in the file system
3. Enable execution on directory view

## Instructions

### Step 1: Create File with Payload

**Context**: Use touch to generate the file, escaping the filename properly in the shell.

**Command** ([[commands/touch-malicious-filename]]):
```bash
touch '"><svg onload=alert(3333333);'
```

> Creates an empty file with the exact payload as the name. Expected output: Silent success; verify with ls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/touch-malicious-filename]]

## Tools Used

- [[tools/touch]]

## Tags

- xss-payload
- file-creation
