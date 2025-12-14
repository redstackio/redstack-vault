---
id: proc-uuid-2
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-malicious-directory]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.823Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Directory-for-XSS

## Summary

This procedure creates a directory with a malicious filename containing a JavaScript payload, exploiting the lack of sanitization in html-pages to store XSS for later execution in directory listings.

## Description

By naming a directory with a payload like `"><svg onload=alert(5);>`, the string breaks out of HTML attributes when inserted into the server's directory listing page. This stored XSS executes when any user views the listing, potentially stealing session data or hijacking browsers in a shared development environment.

## Requirements

1. html-pages module installed
2. Shell access with mkdir command
3. Working directory writable

## Defense

Defensive measures and detection strategies:

- Sanitize all filesystem inputs in web apps
- Use HTML entity encoding for user-controlled data in outputs
- Scan directories for suspicious names with scripts

## Objectives

1. Inject stored XSS payload via filesystem
2. Prepare for reflection in HTML output
3. Enable client-side execution on access

## Instructions

### Step 1: Create the Directory

**Context**: Use mkdir to create a directory with the XSS payload as its name, ensuring special characters are handled by quoting.

**Command** ([[commands/mkdir-malicious-directory]]):
```bash
mkdir "><svg onload=alert(5);>
```

> The command creates the directory; verify with `ls` showing the name. The payload targets <svg> onload for cross-browser execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-malicious-directory]]

## Tools Used


## Tags

- xss
- injection
