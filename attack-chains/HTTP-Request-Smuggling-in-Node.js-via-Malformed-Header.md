---
tags:
  - http-request-smuggling
  - node.js
  - vulnerability
  - web
type: attack_chain
tools:
  - '[[tools/node]]'
  - '[[tools/echo]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/node-run-server]]'
  - '[[commands/echo-nc-send-request]]'
platforms:
  - Node.js
  - Web
complexity: medium
procedures:
  - '[[procedures/Set-Up-Node.js-Test-Server]]'
  - '[[procedures/Send-Malformed-HTTP-Request]]'
  - '[[procedures/Verify-Request-Smuggling-Vulnerability]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of Node.js llhttp parser vulnerability allowing HTTP Request
  Smuggling through malformed headers
skill_level: intermediate
impact_level: high
id: 75e484b5-6182-4010-9fd9-676acca07d0e
created_at: '2025-12-13T09:01:21.692Z'
updated_at: '2025-12-13T09:01:21.692Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via Malformed Header

Multi-stage attack chain demonstrating HTTP Request Smuggling in Node.js by exploiting a vulnerability in the llhttp parser that accepts spaces before colons in header fields, leading to desynchronization with proxies and potential attacks like cache poisoning or credential theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Server] --> B[Send Malformed Request]
    B --> C[Verify Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/node]]
- [[tools/echo]]
- [[tools/nc]]

### Target Environment

- Node.js platform (version 16.3.0 or vulnerable)
- HTTP server running on port 5000
- Local network access for testing

### Initial Access Requirements

- Localhost access
- Ability to run Node.js scripts
- No credentials required for demonstration

## Detailed Attack Procedures

### Step 1: Setup Test Server
procedure: [[procedures/Set-Up-Node.js-Test-Server]]

**Objective**: Establish a sample Node.js HTTP server to test the vulnerability in the llhttp parser.

**Instructions**: Create and run a basic HTTP server script using [[commands/node-run-server]]:

```bash
node app.js
```

This starts the server listening on port 5000, which logs received body length and content.

**Expected Output**: Server starts and listens for incoming requests.

**Success Indicators**:
- Server running on port 5000
- No startup errors

### Step 2: Send Malformed Request
procedure: [[procedures/Send-Malformed-HTTP-Request]]

**Objective**: Craft and send an HTTP request with a space before the colon in the Content-Length header to exploit the parser vulnerability.

**Instructions**: Use [[commands/echo-nc-send-request]] to send the crafted request:

```bash
echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello" | nc localhost 5000
```

This sends a GET request with the malformed 'Content-Length : 5' header and a 5-byte body.

**Expected Output**: The server processes the request and responds with body details.

**Success Indicators**:
- Request accepted by Node.js
- Body interpreted as per malformed header

### Step 3: Verify Exploitation
procedure: [[procedures/Verify-Request-Smuggling-Vulnerability]]

**Objective**: Observe and confirm that Node.js accepts the malformed header, leading to potential request smuggling.

**Instructions**: Check the server logs or response for confirmation of body processing. The server should output 'Body length: 5 Body: hello', indicating acceptance of the invalid header format.

**Expected Output**: Server logs show correct interpretation of the malformed request.

**Success Indicators**:
- Malformed header processed without rejection
- Desynchronization potential confirmed for proxy setups

## Attack Chain Summary

### Key Achievements

1. Demonstrated acceptance of invalid HTTP headers in Node.js
2. Highlighted risk of HTTP Request Smuggling
3. Potential for real-world attacks like cache poisoning or bypassing security

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
