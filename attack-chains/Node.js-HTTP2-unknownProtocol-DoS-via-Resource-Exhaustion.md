---
tags:
  - dos
  - node-js
  - http2
  - resource-exhaustion
  - vulnerability
type: attack_chain
tools:
  - '[[tools/openssl]]'
  - '[[tools/Node.js]]'
  - '[[tools/OpenVAS]]'
  - '[[tools/Greenbone-Vulnerability-Manager]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Client-Script-for-HTTP2-DoS]]'
  - '[[procedures/Setup-Vulnerable-Node.js-HTTP2-Server]]'
  - '[[procedures/Monitor-Server-File-Descriptors]]'
  - '[[procedures/Monitor-Server-Memory-Consumption]]'
  - '[[procedures/Initiate-DoS-Attack-with-OpenSSL-Client]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.756Z'
description: >-
  A denial-of-service attack exploiting the Node.js HTTP2 server's improper
  handling of the unknownProtocol event, leading to file descriptor and memory
  leaks through malformed connections.
id: 4183d414-7140-4db9-9e26-e00e16541186
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Node.js HTTP2 unknownProtocol DoS via Resource Exhaustion

Multi-stage attack chain demonstrating a complete denial-of-service workflow against a Node.js HTTP2 server by triggering resource leaks via malformed protocol connections.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable Server] --> B[Prepare Malicious Client]
    B --> C[Monitor Resources]
    C --> D[Initiate Flood Attack]
    D --> E[Observe DoS Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]
- [[tools/openssl]]
- [[tools/OpenVAS]]
- [[tools/Greenbone-Vulnerability-Manager]]

### Target Environment

- Linux OS
- Node.js runtime (version 12.19.0 or similar vulnerable versions)
- HTTP2 server listening on port 50000 with SSL certificates
- File descriptor limits configured (optional, but impacts exhaustion type)

### Initial Access Requirements

- Local or network access to the target server
- Ability to run Node.js scripts and monitor processes
- No credentials needed for unauthenticated DoS

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Server
procedure: [[procedures/Setup-Vulnerable-Node.js-HTTP2-Server]]

**Objective**: Deploy a Node.js HTTP2 server vulnerable to the unknownProtocol event mishandling.

**Instructions**: Create and run the server script using [[tools/Node.js]] to listen on port 50000 with provided SSL key and certificate files.

**Expected Output**: Server starts without errors, listening on 127.0.0.1:50000.

**Success Indicators**:
- Node.js process PID obtainable
- Server logs confirm HTTP2 session readiness

### Step 2: Create Malicious Client Script
procedure: [[procedures/Create-Malicious-Client-Script-for-HTTP2-DoS]]

**Objective**: Prepare a bash script to generate malformed HTTP/1.1 requests over SSL, triggering the unknownProtocol event.

**Instructions**: Write the client.sh file with a loop that spawns background openssl processes to send invalid requests.

**Expected Output**: Script file created and executable.

**Success Indicators**:
- Script runs without syntax errors
- Background processes can be spawned manually

### Step 3: Monitor File Descriptors
procedure: [[procedures/Monitor-Server-File-Descriptors]]

**Objective**: Baseline and track file descriptor leaks in the Node.js process.

**Instructions**: Use [[commands/monitor-file-descriptors]] to count open FDs and mapped files before the attack:

```bash
ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l
```

Replace {PID} with the Node.js process ID.

**Expected Output**: Two numbers representing FD count and map files count (e.g., 10 and 5).

**Success Indicators**:
- Baseline counts recorded
- Command executes without permission errors

### Step 4: Monitor Memory Consumption
procedure: [[procedures/Monitor-Server-Memory-Consumption]]

**Objective**: Track memory usage to detect leaks during the attack.

**Instructions**: Use system tools like `top` or `htop` to watch the Node.js process RSS and VMS memory.

**Expected Output**: Real-time memory stats showing gradual increase.

**Success Indicators**:
- Memory usage visible and stable pre-attack
- Tools accessible without installation

### Step 5: Initiate DoS Attack
procedure: [[procedures/Initiate-DoS-Attack-with-OpenSSL-Client]]

**Objective**: Flood the server with connections to exhaust resources.

**Instructions**: Execute the client script using [[commands/send-malformed-http-request]] in a loop:

```bash
echo $request | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &
```

Where $request is "GET / HTTP/1.1\r\nHost: Anything\r\n\r\n".

**Expected Output**: No visible output; server logs show unknownProtocol events repeatedly.

**Success Indicators**:
- File descriptors or memory increase rapidly
- New connections fail after exhaustion

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of the Node.js HTTP2 vulnerability
2. Demonstration of file descriptor and memory leaks
3. Achievement of DoS impacting HTTP2 services like gRPC

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
