---
tags:
  - http-request-smuggling
  - node-js
  - vulnerability-demonstration
type: attack_chain
tools:
  - '[[tools/Node-js]]'
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/node-start-http-server]]'
  - '[[commands/printf-nc-send-crafted-request]]'
platforms:
  - Node.js
  - Web
complexity: medium
procedures:
  - '[[procedures/Setup-Node-js-Testing-HTTP-Server]]'
  - '[[procedures/Send-Crafted-HTTP-Request-with-Multi-line-Transfer-Encoding]]'
  - '[[procedures/Observe-and-Confirm-Incorrect-Parsing-in-Node-js]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage demonstration of HTTP Request Smuggling vulnerability in Node.js
  due to incorrect parsing of multi-line Transfer-Encoding headers, leading to
  potential desynchronization with proxies.
skill_level: intermediate
impact_level: high
id: a1986ed4-9fa7-416a-92da-22b70a6647e7
created_at: '2025-12-13T09:01:17.454Z'
updated_at: '2025-12-13T09:01:17.454Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Node.js HTTP Request Smuggling via Multi-line Transfer-Encoding

## Overview

This attack chain demonstrates a vulnerability in Node.js where the llhttp parser mishandles multi-line Transfer-Encoding headers, interpreting them as 'chunked' instead of 'chunked, identity' per RFC7230. This can cause desynchronization with upstream proxies, enabling attacks like cache poisoning, security bypass, and credential theft. The chain involves setting up a test server, sending a crafted request, and observing the parsing behavior.

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Server] --> B[Send Crafted Request]
    B --> C[Observe Response]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node-js]]
- [[tools/printf]]
- [[tools/nc]]

### Target Environment

- Node.js version 17.6.0 with http module and llhttp parser
- HTTP server running on port 80
- Localhost access for testing

### Initial Access Requirements

- Local machine with Node.js installed
- Ability to run commands on the local system
- No prior credentials needed for this demonstration

## Detailed Attack Procedures

### Step 1: Setup Testing HTTP Server
procedure: [[procedures/Setup-Node-js-Testing-HTTP-Server]]

**Objective**: Create a simple Node.js HTTP server to observe how incoming requests are parsed.

**Instructions**: Use [[commands/node-start-http-server]] to start the server:

```bash
node server.js
```

This sets up an HTTP server listening on port 80 that reads request headers and body, responding with JSON output.

**Expected Output**: Server starts listening with no direct output, ready for connections.

**Success Indicators**:
- Server is running and accessible on localhost:80
- No errors in console

### Step 2: Send Crafted HTTP Request
procedure: [[procedures/Send-Crafted-HTTP-Request-with-Multi-line-Transfer-Encoding]]

**Objective**: Send a request with a multi-line Transfer-Encoding header to trigger the parsing vulnerability.

**Instructions**: Execute [[commands/printf-nc-send-crafted-request]] to send the payload:

```bash
printf "GET / HTTP/1.1\r\nTransfer-Encoding: chunked\r\n , identity\r\n\r\n1\r\na\r\n0\r\n\r\n" | nc localhost 80
```

This crafts a GET request with folded Transfer-Encoding and a chunked body.

**Expected Output**: Server processes the request and responds with HTTP/1.1 200 OK and JSON showing the headers and body.

**Success Indicators**:
- Request is sent without errors
- Server receives and processes the request

### Step 3: Observe Server Response
procedure: [[procedures/Observe-and-Confirm-Incorrect-Parsing-in-Node-js]]

**Objective**: Verify that Node.js incorrectly parses the header as 'chunked' instead of 'chunked, identity'.

**Instructions**: Check the server's JSON output, which should show Transfer-Encoding as 'chunked , identity' and body length 1 with content 'a', confirming the vulnerability.

**Expected Output**: JSON response indicating improper header folding and chunked body processing.

**Success Indicators**:
- Output shows multi-line header not properly replaced with spaces
- Body is parsed as chunked, demonstrating desynchronization potential

## Attack Chain Summary

### Key Achievements

1. Established a test environment to replicate the vulnerability
2. Triggered incorrect parsing with a crafted request
3. Confirmed exploitation potential for request smuggling attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
