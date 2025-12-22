---
id: proc-002
tags:
  - payload-creation
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:13.076Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Prepare-Malicious-JavaScript-File

## Summary

This procedure involves creating a malicious JavaScript file to upload as a payload, targeting Node.js execution for RCE in express-cart.

## Description

The vulnerability allows uploading any file without validation, so prepare a .js file that can overwrite app.js or act as a web shell. In a Node.js environment, this enables command execution via child_process. Prerequisites include a local development setup; outcomes include a ready-to-upload file that leads to server-side execution upon inclusion or restart.

## Requirements

1. Text editor or IDE for writing JavaScript
2. Knowledge of Node.js APIs like child_process
3. Local file system access

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all uploaded file contents and extensions
- Scan uploads for malicious code using antivirus or static analysis
- Restrict file writes to isolated directories

## Objectives

1. Create executable JavaScript payload for RCE
2. Ensure compatibility with Node.js runtime
3. Test payload locally if possible

## Instructions

### Step 1: Write the Payload Code

**Context**: Develop JavaScript that executes system commands.

**Command** (Create File):
Use echo or a text editor:

```bash
echo "const { exec } = require('child_process'); exec('id', (err, stdout) => console.log(stdout)); module.exports = {};" > malicious.js
```

> This creates malicious.js with basic command execution. Expected output: File saved with payload.

### Step 2: Verify Payload

**Context**: Test the code snippet in a safe environment.

**Command** (Node Test):
Run node on the file:

```bash
node malicious.js
```

> Expected output: Execution of 'id' command, printing user info, confirming functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-creation
- javascript

