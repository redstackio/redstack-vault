---
id: proc-uuid-001
name: Create-Malicious-File-Name-for-XSS
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.554Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - file-creation
  - payload-injection
commands: []
platforms:
  - Linux
  - macOS
  - Node.js
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-Malicious-File-Name-for-XSS

## Summary

This procedure creates a file with a malicious name using the javascript: URI scheme to exploit stored XSS in directory listings that lack sanitization, allowing JS execution when the link is clicked.

## Description

In the context of the simplehttpserver Node.js module, file names are directly inserted into HTML <a> tags without escaping. By naming a file 'javascript:alert('You are pwned!')', the generated listing creates a clickable link that executes the JS payload. This is a stored XSS as the payload persists in the file system and affects any user viewing the directory. Prerequisites include a writable directory and basic file system access. Expected outcome is a harmless alert, but scalable to drive-by downloads or external JS loading via iframes.

## Requirements

1. Access to a local directory writable by the user
2. Node.js environment with simplehttpserver installed (though not used here)
3. Basic command-line knowledge for file creation

## Defense

Defensive measures and detection strategies:

- Sanitize file names on upload/creation to block URI schemes and special characters
- Use HTML entity encoding when rendering file names in listings
- Implement Content Security Policy (CSP) to restrict javascript: URIs and inline scripts
- Monitor file system for suspicious names containing 'javascript:' or script tags

## Objectives

1. Inject a persistent XSS payload via file naming
2. Prepare the environment for server-side rendering of the payload
3. Enable client-side execution without direct code injection

## Instructions

### Step 1: Create the Malicious File

**Context**: Use touch or echo to create an empty file with the exact malicious name, ensuring the javascript: scheme is not escaped.

**Command** (Manual file creation):
No specific command; use filesystem tools.

> Create the file named `javascript:alert('You are pwned!')` using `touch 'javascript:alert(\'You are pwned!\')'` on Unix-like systems. Verify with `ls` to see the name intact. Expected output: File listed with the full malicious string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-creation]]
- [[payload-injection]]
