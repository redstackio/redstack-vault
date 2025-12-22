---
tags:
  - server-start
  - node-red
  - web-ui
type: procedure
tools:
  - '[[tools/node]]'
  - '[[tools/Firefox]]'
  - '[[tools/Chromium]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-red-start-server]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:16:20.444Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 64e1604c-36bc-4728-9166-cbc9341ad27e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Start-Node-RED-Server

## Summary

This procedure launches the Node-RED server, exposing the vulnerable web UI on port 1880 for subsequent XSS payload injection.

## Description

After installation, running Node-RED starts a Node.js process that serves the flow editor UI. The UI at http://localhost:1880 allows editing nodes and flows where the XSS vulnerability resides. This step requires the server to be running locally and a browser to access it. Expected outcomes include the server binding to port 1880 without conflicts.

## Requirements

1. Node-RED installed globally
2. Port 1880 free on localhost
3. Web browser (Firefox or Chromium) available

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict port 1880 access to trusted networks
- Monitor for unexpected Node.js processes on port 1880
- Use WAF to inspect traffic to Node-RED endpoints

## Objectives

1. Initiate the vulnerable Node-RED runtime
2. Access the web-based editor for exploitation
3. Confirm UI loads correctly

## Instructions

### Step 1: Launch Server

**Context**: Start the Node-RED application using the Node.js runtime to host the web UI.

**Command** ([[commands/node-red-start-server]]):
```bash
node-red
```

> This spawns the server, logging startup messages including 'Server now running at http://127.0.0.1:1880/'. Keep the terminal open to maintain the session.

### Step 2: Access UI

**Context**: Use a browser to navigate to the local endpoint and verify the editor interface.

**Instructions**: Open Firefox or Chromium and go to http://localhost:1880. The palette, workspace, and deploy button should be visible.

> No command needed; expected output is the fully rendered Node-RED dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/node-red-start-server]]

## Tools Used

- [[tools/node]]
- [[tools/Firefox]]
- [[tools/Chromium]]

## Tags

- server-start
- node-red
- web-ui
