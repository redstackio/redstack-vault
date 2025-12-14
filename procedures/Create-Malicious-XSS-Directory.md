---
id: proc-uuid-3
name: Create Malicious XSS Directory
tags:
  - xss
  - payload-creation
type: procedure
tools:
  - '[[tools/mkdir]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-xss-directory]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.370Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Create Malicious XSS Directory

## Summary

This procedure creates a directory with a name embedding a stored XSS payload, exploiting the same unsanitization issue in flsaba's HTML output for JavaScript execution.

## Description

Similar to file creation, the directory name '><img src=x onerror=javascript:alert("xss2")>' injects JS via the directory listing's anchor tags (lines 58 and 64 in server.js). This demonstrates the vulnerability affects both files and folders, broadening the attack surface.

## Requirements

1. Write permissions in current directory
2. Unix shell environment
3. Sufficient disk space

## Defense

Defensive measures and detection strategies:

- Enforce file system naming policies to block HTML/JS characters
- Log and alert on directory creations with suspicious patterns
- Integrate with SIEM for filesystem monitoring

## Objectives

1. Embed secondary XSS payload in directory structure
2. Test vulnerability persistence across object types
3. Validate payload for alert "xss2"

## Instructions

### Step 1: Create Directory with Payload

**Context**: Mkdir handles the name directly; quotes prevent shell interpretation.

**Command** ([[commands/mkdir-xss-directory]]):
```bash
mkdir '><img src=x onerror=javascript:alert("xss2")>'
```

> Expected output: Silent success; verify with `ls -d` to see the directory name intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-xss-directory]]

## Tools Used

- [[tools/mkdir]]

## Tags

- xss
- payload-creation

