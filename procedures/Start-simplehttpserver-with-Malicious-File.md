---
id: proc-uuid-002
name: Start-simplehttpserver-with-Malicious-File
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.549Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - server-start
  - xss-trigger
  - node.js
commands:
  - '[[commands/start-simplehttpserver]]'
platforms:
  - Node.js
  - Linux
  - macOS
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Start-simplehttpserver-with-Malicious-File

## Summary

This procedure launches the simplehttpserver Node.js module to serve a directory containing a maliciously named file, generating an HTML listing that embeds the XSS payload without sanitization.

## Description

The simplehttpserver module, when started via its CLI, serves the current directory on port 8000 and outputs file names directly into HTML via string concatenation in simplehttpserver.js (lines 106-117). With a malicious file present, this renders exploitable <a> tags. Target environment is a local Node.js setup with the module installed via npm. Outcomes include a running server ready for access, exposing the stored XSS to browsers.

## Requirements

1. simplehttpserver installed: `npm install simplehttpserver`
2. Current directory contains the malicious file from prior procedure
3. Port 8000 free on localhost

## Defense

Defensive measures and detection strategies:

- Patch or replace vulnerable modules with sanitized alternatives (e.g., using escape-html)
- Run servers in isolated environments or containers to limit exposure
- Log server starts and monitor for unusual file names in served directories
- Use web application firewalls (WAF) to block javascript: schemes in responses

## Objectives

1. Activate the vulnerable server to render the payload
2. Expose the directory listing for client access
3. Enable the chain toward JS execution

## Instructions

### Step 1: Execute Server CLI

**Context**: From the directory with the malicious file, run the CLI to start serving on 0.0.0.0:8000.

**Command** ([[commands/start-simplehttpserver]]):
```bash
./node_modules/simplehttpserver/cli.js
```

> This command initiates the HTTP server, binding to all interfaces on port 8000 and setting the web root to the current directory. Expected output: "Listening 0.0.0.0:8000 web root dir /path/to/dir". The server runs until stopped with Ctrl+C.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/start-simplehttpserver]]

## Tools Used


## Tags

- [[server-start]]
- [[xss-trigger]]
- [[node.js]]
