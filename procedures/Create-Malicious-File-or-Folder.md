---
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
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.473Z'
sub_techniques: []
id: 0c6eeb37-4baf-4b6d-bb58-a3abff78893f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-File-or-Folder

## Summary

This procedure creates a file or folder with a name containing a malicious HTML/JavaScript payload, exploiting the lack of sanitization in dy-server2's directory listing to store and later execute XSS code when served.

## Description

By naming a file or folder with embedded JavaScript like `<img src=x onerror=alert(1)>`, the payload is stored in the file system. When dy-server2 serves the directory, it renders the name without escaping, allowing the script to execute in the victim's browser. This targets local development environments using dy-server2 for previews. Prerequisites include file system write access in the target directory.

## Requirements

1. Write permissions in the current working directory
2. Basic shell access for mkdir or touch commands
3. dy-server2 installed (from prior procedure)

## Defense

Defensive measures and detection strategies:

- Implement file name validation to block HTML/JS characters in naming
- Use servers with automatic HTML escaping for listings (e.g., nginx with proper config)
- Scan directories for suspicious names containing script tags

## Objectives

1. Inject persistent XSS payload into file system metadata
2. Prepare content for serving without detection
3. Enable client-side execution upon directory access

## Instructions

### Step 1: Create Malicious Folder

**Context**: Use shell commands to create a folder with the XSS payload in its name, ensuring the script embeds directly.

**Command** (Standard bash mkdir):
```bash
mkdir '<img src=x onerror=alert(1)>'
```

> The single quotes preserve the special characters in the name. Expected output: No output if successful; use 'ls' to verify the folder exists with the exact name.

### Step 2: Verify Creation

**Context**: Confirm the malicious name is intact for serving.

**Command** (Standard bash ls):
```bash
ls
```

> Lists directory contents, showing the payload-laden name. Expected output: The folder appears as '<img src=x onerror=alert(1)>'.

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
