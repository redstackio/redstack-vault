---
tags:
  - xss
  - node-js
  - execution
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-app]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.831Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 688f7fbb-6b5a-4622-958e-b4068fb7925a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Vulnerable-Node-js-Server

## Summary

This procedure runs the Node.js application to start an HTTP server that serves the parsed XLSX content, setting the stage for XSS triggering upon browser access.

## Description

Executing app.js launches the server on port 8080, where the unescaped HTML from exceljs is available at http://localhost:8080. This simulates a production web app displaying user-uploaded spreadsheets. Prerequisites: app.js and testsheet.xlsx ready. Expected outcome: Server logs confirm listening, ready for client access.

## Requirements

1. Node.js installed and in PATH
2. app.js script developed with exceljs integration
3. XLSX file in the same directory

## Defense

Defensive measures and detection strategies:

- Run applications in isolated environments (e.g., Docker) to limit exposure
- Monitor server logs for unusual file parsing or error patterns indicating malicious inputs
- Use web application firewalls (WAF) to detect and block requests serving unescaped content

## Objectives

1. Start the HTTP server hosting vulnerable content
2. Verify XLSX parsing occurs without errors
3. Prepare for browser-based payload execution

## Instructions

### Step 1: Run the Script

**Context**: Launch the Node.js runtime to execute the server code.

**Command** ([[commands/node-run-app]]):
```bash
node app.js
```

> This starts the server and parses the XLSX on load. Expected output: 'server is listening on 8080' in console; no crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-app]]

## Tools Used

- [[tools/Node-js]]

## Tags

- xss
- node-js
- execution
