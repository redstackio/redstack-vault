---
id: proc-uuid-1
tags:
  - setup
  - http2
  - node-js
type: procedure
tools:
  - '[[tools/Custom-Node-js-Server-Script]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-run-server]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:26:30.682Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Start-Node-js-HTTP2-Server

## Summary

This procedure initializes a Node.js HTTP/2 server using a custom script to create a vulnerable target environment for testing the large SETTINGS frame DoS exploit, as described in the HackerOne report.

## Description

The procedure sets up an HTTP/2 server in Node.js, which improperly handles large SETTINGS frames per RFC 7540 section 10.5. This server will process oversized frames without limits, leading to CPU exhaustion when exploited. It requires Node.js installed and simulates a public-facing web server. Expected outcome is a running server ready for connection establishment.

## Requirements

1. Node.js version 10.x or later (vulnerable versions pre-patch)
2. Local or remote network access to run the server
3. Basic knowledge of Node.js scripting

## Defense

Defensive measures and detection strategies:

- Patch Node.js to version 12.4.0 or later where this vulnerability is fixed
- Implement HTTP/2 frame size limits and connection throttling at the proxy level (e.g., NGINX)
- Monitor for unusual HTTP/2 SETTINGS frame traffic and high CPU on single cores

## Objectives

1. Deploy a functional HTTP/2 server for exploit testing
2. Verify server readiness for incoming connections
3. Ensure HTTP/2 protocol is enabled without errors

## Instructions

### Step 1: Prepare Server Script

**Context**: Create the server file using the provided code from the report, which sets up an HTTP/2 server with TLS or plain HTTP/2.

**Command** ([[commands/node-run-server]]):
```bash
node server.js
```

> This command executes the server script, binding to port 3000 (configurable). Expected output includes server startup logs and confirmation of HTTP/2 support.

### Step 2: Verify Server Status

**Context**: Confirm the server is listening and HTTP/2 is active by testing connectivity.

**Command** ([[commands/curl-http2-test]]):
```bash
curl --http2 https://localhost:3000 -I
```

> This sends a HEAD request over HTTP/2. Successful output shows HTTP/2 response headers without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/node-run-server]]
- [[commands/curl-http2-test]]

## Tools Used

- [[tools/Custom-Node-js-Server-Script]]

## Tags

- [[setup]]
- [[http2]]
- [[node-js]]
