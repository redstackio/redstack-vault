---
id: proc-uuid-2
name: Create Malicious XSS File
tags:
  - xss
  - payload-creation
type: procedure
tools:
  - '[[tools/touch]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/touch-xss-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.377Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Create Malicious XSS File

## Summary

This procedure creates an empty file with a name containing a stored XSS payload, which will be rendered unsanitized in the flsaba directory listing, leading to JavaScript execution.

## Description

By naming a file with HTML-breaking and script-injecting content like '><img src=x onerror=javascript:alert("xss")>', the payload closes an open HTML tag in the server's listing and injects an onerror event. When served by flsaba and viewed in a browser, it executes arbitrary JS, such as alerting "xss".

## Requirements

1. Write permissions in the current directory
2. Unix-like shell (Linux)
3. No prior malicious files to avoid conflicts

## Defense

Defensive measures and detection strategies:

- Sanitize file names on creation (e.g., restrict special characters)
- Monitor filesystem for suspicious file names with script tags
- Use antivirus or EDR to flag anomalous file creations

## Objectives

1. Store XSS payload in file metadata
2. Prepare for server exposure
3. Ensure payload survives filesystem operations

## Instructions

### Step 1: Create File with Payload

**Context**: Use touch to generate the file; the name itself is the vector.

**Command** ([[commands/touch-xss-file]]):
```bash
touch '><img src=x onerror=javascript:alert("xss")>'
```

> Quotes escape the special characters. Expected output: No output if successful; use `ls` to confirm file existence with exact name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/touch-xss-file]]

## Tools Used

- [[tools/touch]]

## Tags

- xss
- payload-creation

