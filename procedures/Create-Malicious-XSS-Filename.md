---
id: proc-398285-create-xss-file
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
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.933Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-XSS-Filename

## Summary

This procedure creates a file with a filename embedding an XSS payload, such as an img tag with onerror handler, to inject and store malicious JavaScript that executes when the directory listing is viewed via the serve module.

## Description

The serve module's directory listing (in serve-handler's directory.js) inserts filenames directly into <a> tags without HTML escaping, allowing attackers to close the tag and inject scripts. This stored XSS persists in the file system and triggers on any user accessing the listing, potentially stealing cookies or redirecting to phishing sites. Target environment is a local directory on a Node.js system.

## Requirements

1. Write access to the target directory
2. Basic shell access for file creation
3. Knowledge of XSS payloads compatible with HTML context

## Defense

Defensive measures and detection strategies:

- Sanitize filenames on upload or creation in web apps
- Disable directory listings in web servers
- Scan for suspicious filenames with scripts or tools like ClamAV

## Objectives

1. Store XSS payload in filename for persistence
2. Break out of HTML attribute context in directory rendering
3. Enable arbitrary JS execution on listing view

## Instructions

### Step 1: Craft and Create Payload File

**Context**: Design a filename that closes the <a> tag and injects a script, then create an empty file with that name.

**Command** (bash):
```bash
touch '<img src=x onerror="alert(\"XSS\")">.txt'
```

> The touch command creates the file without content. The payload uses double quotes escaped for shell, injecting <img src=x onerror=alert('XSS')> to execute on error. Expected output: No output if successful; verify with ls.

### Step 2: Verify File Creation

**Context**: Confirm the malicious filename exists without triggering execution.

**Command** (bash):
```bash
ls -la
```

> Lists files, showing the injected name. Expected output: File listed with the payload string as name.

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
