---
tags:
  - http-smuggling
  - node-js
  - haproxy
  - access-bypass
type: attack_chain
tools:
  - '[[tools/HAProxy]]'
  - '[[tools/Express]]'
  - '[[tools/Node-js]]'
  - '[[tools/npm]]'
  - '[[tools/body-parser]]'
  - '[[tools/wget]]'
  - '[[tools/tar]]'
  - '[[tools/make]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/wget-download-haproxy]]'
  - '[[commands/tar-extract-haproxy]]'
  - '[[commands/cd-change-to-haproxy-dir]]'
  - '[[commands/make-compile-haproxy]]'
  - '[[commands/haproxy-run-with-config]]'
  - '[[commands/npm-install-express]]'
  - '[[commands/node-run-express-app]]'
platforms:
  - Linux
  - Web
complexity: medium
procedures:
  - '[[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]'
  - '[[procedures/Setup-Node-js-Express-Backend-Server]]'
  - '[[procedures/Send-Crafted-HTTP-Request-for-Smuggling]]'
  - '[[procedures/Reproduce-Vulnerability-with-Node-js-Script]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits a vulnerability in Node.js HTTP parsing allowing duplicate
  Transfer-Encoding headers to smuggle requests past frontend proxies like
  HAProxy, bypassing access controls.
skill_level: intermediate
impact_level: high
id: f307326d-d372-43d3-a652-34af3eac6157
created_at: '2025-12-13T09:01:22.141Z'
updated_at: '2025-12-13T09:01:22.141Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via Duplicate Transfer-Encoding Headers

Multi-stage attack chain demonstrating HTTP request smuggling in Node.js by exploiting duplicate Transfer-Encoding headers, leading to desynchronization with frontend proxies like HAProxy and bypassing access controls to restricted endpoints.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Proxy] --> B[Setup Backend]
    B --> C[Send Smuggled Request]
    C --> D[Verify Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HAProxy]]
- [[tools/Node-js]]
- [[tools/Express]]
- [[tools/npm]]
- [[tools/wget]]
- [[tools/tar]]
- [[tools/make]]

### Target Environment

- Linux platform
- Open ports: 80, 8080
- Services: HTTP server (Express on Node.js), Proxy (HAProxy)
- Tech stack: Node.js, Express, HAProxy

### Initial Access Requirements

- Local machine access for setup
- No prior credentials needed
- Network access to localhost for testing

## Detailed Attack Procedures

### Step 1: Compile and Setup HAProxy Frontend Proxy
procedure: [[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]

**Objective**: Set up a vulnerable HAProxy instance as the frontend proxy configured to restrict access to certain URIs like /flag.

**Instructions**: Download the HAProxy source using [[commands/wget-download-haproxy]]:

```bash
wget https://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz
```

Extract the tarball with [[commands/tar-extract-haproxy]]:

```bash
tar zxvf haproxy-1.5.3.tar.gz
```

Change directory using [[commands/cd-change-to-haproxy-dir]]:

```bash
cd haproxy-1.5.3
```

Compile HAProxy with [[commands/make-compile-haproxy]]:

```bash
make TARGET=linux2628
```

Run HAProxy with the configuration file using [[commands/haproxy-run-with-config]]:

```bash
./haproxy -f haproxy.cfg -d
```

**Expected Output**: HAProxy running in debug mode, listening on port 80, with ACL denying /flag paths and proxying to backend on 127.0.0.1:8080.

**Success Indicators**:
- HAProxy binary compiled successfully
- Proxy server starts without errors and binds to port 80

### Step 2: Setup Node.js Express Backend Server
procedure: [[procedures/Setup-Node-js-Express-Backend-Server]]

**Objective**: Configure and run a Node.js Express application as the backend server vulnerable to HTTP request smuggling.

**Instructions**: Install Express using [[commands/npm-install-express]]:

```bash
npm install express
```

Run the Express app with debug logging using [[commands/node-run-express-app]]:

```bash
DEBUG=express:* node app.js
```

**Expected Output**: Express server listening on port 8080 with debug output, exposing GET /, GET /flag, and POST / endpoints.

**Success Indicators**:
- Express installed in node_modules
- Server starts and listens on port 8080

### Step 3: Send Crafted HTTP Request for Smuggling
procedure: [[procedures/Send-Crafted-HTTP-Request-for-Smuggling]]

**Objective**: Craft and send an HTTP request with duplicate Transfer-Encoding headers to smuggle a GET /flag request past the proxy.

**Instructions**: Manually craft a POST request with duplicate Transfer-Encoding: chunked and chunked-false headers, embedding a smuggled GET /flag in the body chunks. Send it to the HAProxy frontend on port 80.

**Expected Output**: The smuggled GET /flag request is processed by the backend, returning the restricted content while bypassing the proxy's ACL.

**Success Indicators**:
- Response includes content from /flag endpoint
- No denial from HAProxy ACL

### Step 4: Reproduce Vulnerability with Node.js Script
procedure: [[procedures/Reproduce-Vulnerability-with-Node-js-Script]]

**Objective**: Confirm the vulnerability using a Node.js script to simulate the smuggling without full proxy setup.

**Instructions**: Create and run a Node.js script using http and net modules to send a smuggled request to a local HTTP server, verifying the desynchronization in header processing.

**Expected Output**: Script confirms Node.js processes only the first Transfer-Encoding header, allowing smuggling.

**Success Indicators**:
- Script executes and demonstrates smuggling
- Vulnerability reproduced in isolation

## Attack Chain Summary

### Key Achievements

1. Bypassed proxy access controls
2. Accessed restricted resources
3. Demonstrated potential for service disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Lateral Movement]]

*Last updated: 2023-10-01*
