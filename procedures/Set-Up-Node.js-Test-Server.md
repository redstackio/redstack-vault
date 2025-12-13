---
tags:
  - node.js
  - setup
  - http-server
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-server]]'
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: eaaadd31-a65a-48cd-a80c-b1ada2e9073c
created_at: '2025-12-13T09:01:21.684Z'
updated_at: '2025-12-13T09:01:21.684Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set Up Node.js Test Server

## Summary

This procedure sets up a basic Node.js HTTP server to demonstrate vulnerabilities in the llhttp parser, specifically for testing HTTP Request Smuggling scenarios.

## Description

The procedure involves creating and running a simple server script that listens on port 5000 and processes incoming HTTP requests, logging body length and content. This targets the Node.js http module and is used in controlled environments to replicate the vulnerability.

## Requirements

1. Node.js installed (version 16.3.0 or similar vulnerable version)
2. Local access to run scripts
3. Port 5000 available

## Defense

Defensive measures and detection strategies:

- Update Node.js to patched versions that enforce strict header parsing
- Monitor server logs for anomalous header formats

## Objectives

1. Establish a test environment for vulnerability demonstration
2. Confirm server processes requests correctly
3. Prepare for exploitation testing

## Instructions

### Step 1: Run the Server Script

**Context**: Execute the Node.js script to start the HTTP server.

**Command** ([[commands/node-run-server]]):

```bash
node app.js
```

> This command runs the app.js script, which creates an HTTP server listening on port 5000 and logs request body details.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/node-run-server]]

## Tools Used

- [[tools/node]]

## Tags

- [[node.js]]
- [[http-server]]
