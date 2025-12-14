---
id: proc-hangersteak-script-001
tags:
  - directory-traversal
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/nodejs]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.549Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Hangersteak-Server-Script

## Summary

This procedure creates a basic Node.js server script using the hangersteak module to serve static files, exposing the directory traversal vulnerability on port 3006.

## Description

The script uses Node's http module to create a server and passes requests to hangersteak without path validation. This setup listens on all interfaces (0.0.0.0), making it accessible externally. Prerequisites include the installed hangersteak module. The outcome is a running server vulnerable to path traversal via '../' in URLs.

## Requirements

1. hangersteak module installed
2. Text editor (e.g., vim, nano)
3. Node.js environment
4. Project directory with index.js writable

## Defense

Defensive measures and detection strategies:

- Review server scripts for unsanitized module usage
- Use path validation libraries like path.normalize
- Scan code for http.createServer patterns with third-party handlers

## Objectives

1. Generate a minimal server script
2. Ensure vulnerability exposure
3. Prepare for server execution

## Instructions

### Step 1: Write the Server Script

**Context**: Create index.js to require modules and start the server on port 3006.

**Command** (Manual file creation):
```javascript
const http = require('http');
const hangersteak = require('hangersteak');
http.createServer(hangersteak).listen(3006);
console.log('Server running on port 3006');
```

> Save this as index.js. No command execution here; verify by running node -c index.js for syntax check. Expected output: No errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nodejs]]

## Tags

- [[directory-traversal]]
- [[node-js]]
