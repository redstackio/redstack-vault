---
tags:
  - dos
  - curl
  - globbing
  - resource-exhaustion
type: attack_chain
tools:
  - '[[tools/Python-SimpleHTTPServer]]'
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/python-simplehttpserver-start]]'
  - '[[commands/curl-globbing-dos]]'
platforms:
  - Linux
complexity: medium
procedures:
  - '[[procedures/Set-Up-Local-HTTP-Server-for-Testing]]'
  - '[[procedures/Exploit-curl-Globbing-for-Massive-Requests]]'
  - '[[procedures/Monitor-Resource-Consumption-for-DoS-Impact]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
description: >-
  Demonstrates a denial of service attack by exploiting curl's URL globbing
  feature to generate massive request volumes, leading to resource exhaustion on
  the client or target server.
skill_level: intermediate
impact_level: high
id: 0887cb50-0dd2-4556-bdc2-5091e1226ffc
created_at: '2025-12-14T17:26:30.123Z'
updated_at: '2025-12-14T17:26:30.123Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Denial of Service via curl URL Globbing Expansion

Multi-stage attack chain demonstrating a complete attack workflow exploiting curl's URL globbing to cause denial of service through uncontrolled resource consumption.

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
    A[Setup Local Server] --> B[Execute curl Globbing Exploit]
    B --> C[Monitor Resource Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python-SimpleHTTPServer]]
- [[tools/curl]]

### Target Environment

- Linux platform
- Port 8000 available for local HTTP server
- Local network access for testing

### Initial Access Requirements

- Local machine with Python and curl installed
- No remote credentials needed; local reproduction
- Administrative privileges not required

## Detailed Attack Procedures

### Step 1: Setup Local Server
procedure: [[procedures/Set-Up-Local-HTTP-Server-for-Testing]]

**Objective**: Establish a local HTTP server to receive and log incoming requests, simulating a target for observing the flood from curl's globbing expansion.

**Instructions**: Start the server using [[commands/python-simplehttpserver-start]]:

```bash
python -m SimpleHTTPServer 8000
```

**Expected Output**: Server startup message like 'Serving HTTP on 0.0.0.0 port 8000 ...' and subsequent logs of incoming requests.

**Success Indicators**:
- Server listening on port 8000
- No errors in startup

### Step 2: Execute curl Globbing Exploit
procedure: [[procedures/Exploit-curl-Globbing-for-Massive-Requests]]

**Objective**: Trigger the vulnerability by running curl with an extremely large globbing range in the URL, causing it to expand into billions of potential requests and flood the target.

**Instructions**: Execute the curl command in the background using [[commands/curl-globbing-dos]]:

```bash
nohup ./curl -vv 'http://127.0.0.1:8000/[1-9999999999999999999]/' &
```

**Expected Output**: Verbose logs showing numerous HTTP requests to paths like /1/, /2/, etc., with escalating connection volume leading to high CPU and network usage.

**Success Indicators**:
- Flood of requests observed in server logs
- Increased CPU usage on the machine running curl

### Step 3: Monitor Resource Consumption
procedure: [[procedures/Monitor-Resource-Consumption-for-DoS-Impact]]

**Objective**: Observe the impact of the request flood on server resources to confirm denial of service effects like CPU overload and potential service crashes.

**Instructions**: Use system monitoring tools such as top or htop to track CPU and network metrics during the exploit execution.

**Expected Output**: High CPU utilization (e.g., >90%) and a surge in network requests, potentially leading to server unresponsiveness.

**Success Indicators**:
- Excessive resource consumption detected
- Target server experiences slowdown or crash

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of curl globbing vulnerability using local setup
2. Demonstration of massive URL expansion causing DoS
3. Validation of resource exhaustion impact on client and target

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
