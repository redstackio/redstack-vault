---
tags:
  - http-request-smuggling
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-start-http-server]]'
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 99290a95-811a-4fbf-8bb6-11eafac10323
created_at: '2025-12-13T09:01:17.449Z'
updated_at: '2025-12-13T09:01:17.449Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Node.js Testing HTTP Server

## Summary

This procedure sets up a basic HTTP server in Node.js to test and observe request parsing behavior, particularly for demonstrating vulnerabilities like HTTP Request Smuggling.

## Description

The server is created using Node.js's http module and listens on port 80. It processes incoming requests by reading headers and body, then responds with a JSON object containing the parsed data. This is essential for replicating the environment where the llhttp parser's flaw in handling multi-line headers can be tested.

## Requirements

1. Node.js installed (version 17.6.0 recommended for vulnerability replication)
2. A script file named server.js with the HTTP server code
3. Local access to run the server on port 80

## Defense

Defensive measures and detection strategies:

- Update Node.js to a patched version that correctly handles header folding per RFC7230
- Monitor server logs for unusual header formats or desynchronization indicators

## Objectives

1. Establish a controlled environment for vulnerability testing
2. Enable observation of request parsing
3. Prepare for sending crafted exploits

## Instructions

### Step 1: Prepare and Run Server Script

**Context**: Start the Node.js HTTP server to begin listening for requests.

**Command** ([[commands/node-start-http-server]]):

```bash
node server.js
```

> This command executes the server.js script, which creates an HTTP server that parses incoming requests and responds with JSON-formatted details of headers and body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/node-start-http-server]]

## Tools Used

- [[tools/Node-js]]

## Tags

- [[http-request-smuggling]]
- [[node-js]]
