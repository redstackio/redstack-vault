---
tags:
  - nodejs
  - server-execution
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-scrap-js]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.707Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 292bffaf-a36e-41e6-83f5-b4576a3ba23e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-the-Vulnerable-Node-js-Application

## Summary

This procedure launches the Express application using Node.js, starting the server on port 8080 to await requests that will trigger the metadata scraping and XSS.

## Description

In a local Node.js environment, this executes the vulnerable script, making the /scrap endpoint available. The scenario assumes prior code development; outcome is a running server ready for browser interaction to execute the payload.

## Requirements

1. scrap.js file present
2. Node.js installed
3. Port 8080 free

## Defense

Defensive measures and detection strategies:

- Run apps in containers with network restrictions
- Log and monitor server startups
- Use process managers like PM2 with security configs

## Objectives

1. Start the Express server
2. Enable scraping on request
3. Prepare for XSS trigger

## Instructions

### Step 1: Execute the Script

**Context**: Run the Node.js file to initiate the server.

**Command** ([[commands/node-run-scrap-js]]):
```bash
node scrap.js
```

> Terminal shows server listening; keep running for access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-scrap-js]]

## Tools Used

- [[tools/node]]

## Tags

- nodejs
- server-execution
