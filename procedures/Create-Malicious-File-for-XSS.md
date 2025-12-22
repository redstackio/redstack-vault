---
id: proc-uuid-2
tags:
  - xss
  - payload-injection
  - file-system
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.972Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-File-for-XSS

## Summary

This procedure creates a file with a malicious name containing a Stored XSS payload, which will be rendered unsafely in the Glance directory listing, allowing JavaScript execution upon clicking.

## Description

By naming a file with payloads like 'javascript:alert("you are pwned!")' or '1"><iframe src="malicious_frame.html">', the vulnerability is triggered because Glance inserts file names directly into HTML without escaping. This is a stored attack as the payload persists in the file system and affects any viewer of the listing. Prerequisites include a writable directory.

## Requirements

1. Write access to the target directory
2. Basic shell or file explorer for file creation
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Sanitize file names on upload/creation to remove special characters and scripts
- Disable directory listings or use templated HTML with escaping
- Monitor file system for suspicious names containing script tags

## Objectives

1. Inject XSS payload into file name
2. Ensure payload is valid for HTML/JS execution
3. Prepare for server exposure

## Instructions

### Step 1: Create File with Payload

**Context**: Manually create an empty file with a name that embeds the XSS payload to exploit the lack of sanitization.

**Command** (Manual):
```bash
touch 'javascript:alert("you are pwned!")'
```

> Use touch or any file creation method to name the file with the javascript: URI. Alternatively, for HTML injection: touch '1"><iframe src=\"malicious_frame.html\">'. Expected output: File created; verify with ls to see the name intact.

### Step 2: Verify File Creation

**Context**: Confirm the malicious name is set correctly.

**Command** (Manual):
```bash
ls -la
```

> Lists files; look for the payload in the name. Success if no truncation or errors.

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
- stored-xss
- file-injection
