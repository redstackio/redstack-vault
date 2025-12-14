---
tags:
  - setup
  - node.js
  - windows
type: procedure
tools: []
tactics: []
commands:
  - '[[commands/node-run-server]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:26:21.794Z'
sub_techniques: []
id: 7d45bab3-eb7a-402a-a634-49390734e2d9
validated: true
---
# Setup Vulnerable Node.js Path Join App

## Summary

This procedure sets up a demo Node.js application on Windows that uses path.join() and path.normalize(), vulnerable to traversal bypass via device names, for testing CVE-2025-23084 exploitation.

## Description

Create a simple HTTP server in Node.js that joins user-provided paths to an 'intended_dir' without additional checks, relying on built-in normalization which fails for device names like CON. This simulates a real-world vulnerable app, such as a file viewer in a web service. Run on Windows to trigger the issue. Expected outcome: Server accepts traversal paths prefixed with device names.

## Requirements

1. Node.js installed on Windows (vulnerable version)
2. Create an 'intended_dir' folder with test files
3. Port 3000 available

## Defense

- Use path validation libraries
- Restrict file access with chroot or permissions

## Objectives

1. Establish a testable vulnerable environment
2. Verify basic path handling

## Instructions

### Step 1: Create Server Script

**Context**: Write the Node.js server code to handle file requests via path.join().

**Command** (Manual file creation):
```bash
# Create server.js with the code provided in attack chain
```

> Save the JavaScript code to server.js. Expected: File created.

### Step 2: Run the Server

**Context**: Start the Node.js server to listen for requests.

**Command** ([[commands/node-run-server]]):
```bash
node server.js
```

> Launches the server. Expected output: 'Server running on port 3000'.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used

- [[commands/node-run-server]]

## Tools Used


## Tags

- setup
- node.js
