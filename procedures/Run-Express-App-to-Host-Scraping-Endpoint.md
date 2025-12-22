---
id: proc-run-express-app
tags:
  - node-execution
  - server-start
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-express-app]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.495Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Express-App-to-Host-Scraping-Endpoint

## Summary

This procedure starts the Node.js Express application, hosting the /scrap endpoint that performs the vulnerable metascraper extraction and serves the XSS-prone HTML.

## Description

Execute app.js to launch the server on port 8888. The app will scrape on demand when /scrap is hit. Expected outcome: Server ready, logging metadata on access. Prerequisites: app.js created and dependencies installed.

## Requirements

1. app.js file present
2. Node.js runtime
3. Port 8888 free

## Defense

Defensive measures and detection strategies:

- Run apps in containers with network isolation
- Monitor Node.js processes for scraping libraries
- Implement rate limiting on scraping endpoints

## Objectives

1. Start the vulnerable server
2. Confirm listening on port 8888
3. Prepare for browser trigger

## Instructions

### Step 1: Execute the Node.js Script

**Context**: Run the app to initialize the Express server.

**Command** ([[commands/node-run-express-app]]):
```bash
node app.js
```

> Starts the server; expected output: 'Example app listening on port 8888!' and any scrape logs on access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-run-express-app]]

## Tools Used

- [[tools/node]]

## Tags

- [[node-execution]]
- [[server-start]]
