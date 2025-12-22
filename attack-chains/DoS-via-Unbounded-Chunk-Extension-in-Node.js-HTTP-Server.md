---
id: ac-nodejs-unbounded-chunk-dos
tags:
  - dos
  - node-js
  - http
  - chunked-encoding
  - resource-exhaustion
type: attack_chain
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-Chunked-HTTP-Request]]'
  - '[[procedures/Send-Request-to-Node.js-Server]]'
  - '[[procedures/Monitor-Resource-Exhaustion]]'
step_count: 3
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.986Z'
description: >-
  Multi-stage attack exploiting a vulnerability in Node.js HTTP servers to cause
  denial of service through unbounded reading of chunk extensions, leading to
  CPU and network exhaustion.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# DoS via Unbounded Chunk Extension in Node.js HTTP Server

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of limits on chunk extension bytes in Node.js HTTP parsing, allowing an attacker to exhaust server resources without sending actual data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Request] --> B[Send Request to Server]
    B --> C[Monitor Resource Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Netcat]]

### Target Environment

- Node.js HTTP server (versions 18.x, 20.x, 21.x)
- Required services/ports: HTTP on port 80 or 3000
- Network access requirements: Direct TCP connectivity to the server

### Initial Access Requirements

- No credentials required
- Attacker must have network reachability to the target HTTP endpoint
- No prior access needed

## Detailed Attack Procedures

### Step 1: Craft Malicious Request
procedure: [[procedures/Craft-Malicious-Chunked-HTTP-Request]]

**Objective**: Create a specially crafted HTTP request using chunked transfer encoding with an unbounded chunk extension to trick the server into reading unlimited bytes.

**Instructions**: Prepare the request headers and body with a chunk extension that specifies a large or unbounded read without providing data. The extension abuses the parsing logic to initiate continuous reading.

**Expected Output**: A raw HTTP request string ready for transmission.

**Success Indicators**:
- Request string validates against HTTP chunked encoding specs with malicious extension
- No syntax errors in the crafted payload

### Step 2: Send Request to Server
procedure: [[procedures/Send-Request-to-Node.js-Server]]

**Objective**: Transmit the crafted request over a single TCP connection to the Node.js HTTP server endpoint.

**Instructions**: Use [[commands/nc-send-chunked-request]] to connect to the server and pipe the malicious request:

```bash
cat malicious_request.txt | nc target-server 3000
```

**Expected Output**: The connection hangs as the server attempts to read unbounded data, without closing.

**Success Indicators**:
- TCP connection established and request sent
- Server does not respond or close the connection promptly

### Step 3: Monitor Resource Exhaustion
procedure: [[procedures/Monitor-Resource-Exhaustion]]

**Objective**: Observe the server's CPU and network bandwidth consumption due to the unbounded reading attempt.

**Instructions**: While the request is active, use [[commands/top-monitor-cpu]] on the server (if accessible) or network tools to watch metrics:

```bash
top -p $(pgrep node)
```

Monitor for spiking CPU usage in the Node.js process and sustained network activity on the connection.

**Expected Output**: High CPU utilization (near 100%) and continuous inbound traffic without request completion.

**Success Indicators**:
- Node.js process CPU usage exceeds 50%
- Network interface shows elevated bandwidth usage from the single connection
- Server becomes unresponsive to new requests

## Attack Chain Summary

### Key Achievements

1. Bypassed standard HTTP protections like timeouts and body size limits
2. Caused denial of service on all active Node.js versions (18.x, 20.x, 21.x)
3. Demonstrated resource exhaustion via a single, low-bandwidth connection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2024-10-01T00:00:00Z*
