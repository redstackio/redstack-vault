---
id: proc-uuid-2
name: Create Trigger HTML File
tags:
  - setup
  - file-creation
type: procedure
tools:
  - '[[tools/touch]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-trigger-html-file]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.119Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Trigger HTML File

## Summary

This procedure creates an empty HTML file named after a domain (e.g., 'hackerone.com.html') in the document root, which the hekto server's redirection logic checks for to trigger the open redirect vulnerability.

## Description

The vulnerability in hekto relies on the existence of a file like 'domain.html' when a path like '//domain' is requested. The server appends '.html' to check for the file and, if found, redirects to the protocol-relative URL. This step sets up the trigger file in the current directory, which serves as the document root. Prerequisites include a Unix-like environment. The outcome is the file creation, enabling the flawed logic to activate.

## Requirements

1. Unix-like shell (Linux/macOS)
2. Write permissions in the current directory
3. Post-installation of hekto module

## Defense

Defensive measures and detection strategies:

- Validate filenames to prevent domain-mimicking files in web roots
- Implement file existence checks with sanitization in server logic
- Log unusual file creations in document roots

## Objectives

1. Create the file that fools the server's path handling
2. Prepare for redirection trigger
3. Enable vulnerability exploitation

## Instructions

### Step 1: Create the File

**Context**: Use touch to generate the empty trigger file.

**Command** ([[commands/create-trigger-html-file]]):
```bash
touch hackerone.com.html
```

> This creates an empty file named 'hackerone.com.html'. No output if successful; verify with 'ls' to see the file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-trigger-html-file]]

## Tools Used

- [[tools/touch]]

## Tags

- setup
- file-creation
