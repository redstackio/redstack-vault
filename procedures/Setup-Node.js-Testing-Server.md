---
tags:
  - node.js
  - http-server
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Initial Access]]'
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
id: 54578515-d969-4d4e-abd1-e9d551cb504e
created_at: '2025-12-13T09:01:17.195Z'
updated_at: '2025-12-13T09:01:17.195Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Node.js Testing Server

## Summary

This procedure sets up a simple HTTP server using Node.js to test for vulnerabilities by echoing back request headers, body length, and content as JSON.

## Description

The server is created to listen on port 80 and handle incoming requests, making it ideal for reproducing parsing issues like HTTP Request Smuggling. It requires a server.js script that implements the HTTP server logic using the Node.js http module.

## Requirements

1. Node.js installed (versions v16.16.0 or v18.7.0)
2. server.js script prepared with HTTP server code
3. Access to run commands on the local machine

## Defense

Defensive measures and detection strategies:

- Use updated Node.js versions with fixes for CVE-2022-32215
- Monitor server logs for unusual request parsing

## Objectives

1. Establish a test environment for vulnerability reproduction
2. Ensure server echoes request details accurately
3. Prepare for payload testing

## Instructions

### Step 1: Run the Server Script

**Context**: Starts the Node.js HTTP server to listen for requests.

**Command** ([[commands/node-run-server]]):

```bash
node server.js
```

> This command executes the server.js script, starting an HTTP server on port 80 that echoes request details as JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/node-run-server]]

## Tools Used

- [[tools/Node.js]]

## Tags

- [[tools/Node.js]]
- [[http-server]]
