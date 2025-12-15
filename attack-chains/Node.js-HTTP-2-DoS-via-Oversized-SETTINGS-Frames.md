---
tags:
  - dos
  - http2
  - node-js
  - resource-exhaustion
  - cpu-exhaustion
type: attack_chain
tools:
  - '[[tools/Custom-Node-js-Server-Script]]'
  - '[[tools/Custom-HTTP2-Attack-Script]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Node.js
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Start-Node-js-HTTP2-Server]]'
  - '[[procedures/Establish-Multiple-HTTP2-Connections]]'
  - '[[procedures/Send-Large-SETTINGS-Frames]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.685Z'
description: >-
  A denial-of-service attack exploiting the Node.js HTTP/2 module by sending
  large SETTINGS frames to cause CPU exhaustion and persistent connections.
skill_level: intermediate
impact_level: high
id: 97934169-ae26-4ac8-9273-a5a8c98f2a44
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Node.js HTTP/2 DoS via Oversized SETTINGS Frames

Multi-stage attack chain demonstrating a complete denial-of-service workflow against Node.js HTTP/2 servers by exploiting improper handling of large SETTINGS frames, leading to 100% CPU usage on a single core from a single attacking machine.

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
    A[Setup Server] --> B[Establish Connections]
    B --> C[Send Malicious Frames]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Custom-Node-js-Server-Script]]
- [[tools/Custom-HTTP2-Attack-Script]]

### Target Environment

- Node.js runtime (versions prior to patch, e.g., 10.x-12.x)
- HTTP/2 enabled server
- Open port 443 or 80 for HTTP/2 connections

### Initial Access Requirements

- Network access to the target Node.js HTTP/2 server
- No credentials required; exploits public-facing service
- Attacker machine with Node.js for scripting

## Detailed Attack Procedures

### Step 1: Setup HTTP/2 Server
procedure: [[procedures/Start-Node-js-HTTP2-Server]]

**Objective**: Initialize a vulnerable Node.js HTTP/2 server to simulate the target environment for testing the exploit.

**Instructions**: Use the custom server script to start an HTTP/2 server listening on a specified port. Save the provided Node.js code to a file named `server.js` and execute it using Node.js.

```bash
node server.js
```

**Expected Output**: Server logs indicating "Server listening on port 3000" or similar, confirming HTTP/2 is active.

**Success Indicators**:
- Server process starts without errors
- HTTP/2 endpoint is reachable (e.g., via curl --http2)

### Step 2: Establish Multiple Connections
procedure: [[procedures/Establish-Multiple-HTTP2-Connections]]

**Objective**: Open numerous concurrent HTTP/2 connections to the target server to prepare for frame injection.

**Instructions**: Run the custom attack script to create multiple connections. Configure the script to target the server's IP and port, opening at least 100 connections.

```bash
node attack.js --target localhost:3000 --connections 100
```

**Expected Output**: Script output showing "Connection X established" for each connection.

**Success Indicators**:
- Multiple connections are open and persistent
- No immediate server errors or connection drops

### Step 3: Inject Oversized SETTINGS Frames
procedure: [[procedures/Send-Large-SETTINGS-Frames]]

**Objective**: Transmit large SETTINGS frames over the open connections to trigger CPU exhaustion in the Node.js HTTP/2 module.

**Instructions**: With connections established, use the attack script to send SETTINGS frames with a 14400-byte payload on each connection. This simulates the RFC 10.5 oversized frame attack.

```bash
node attack.js --send-settings --payload-size 14400
```

**Expected Output**: Script confirms frames sent; monitor server CPU usage spiking to 100% on one core.

**Success Indicators**:
- Server CPU utilization reaches 100% on a core
- Connections remain open indefinitely, sustaining the DoS
- Server becomes unresponsive to legitimate requests

## Attack Chain Summary

### Key Achievements

1. Successful setup of a vulnerable HTTP/2 server environment
2. Establishment of persistent multiple connections without detection
3. Induction of resource exhaustion leading to full DoS from a single attacker

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
