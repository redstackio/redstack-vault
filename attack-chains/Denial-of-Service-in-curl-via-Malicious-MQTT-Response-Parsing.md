---
tags:
  - dos
  - curl
  - mqtt
  - resource-exhaustion
  - cpu-consumption
type: attack_chain
tools:
  - '[[tools/socat]]'
  - '[[tools/curl]]'
  - '[[tools/top]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-MQTT-Server-with-socat]]'
  - '[[procedures/Trigger-curl-DoS-with-MQTT-URL]]'
  - '[[procedures/Observe-Resource-Consumption-with-top]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.693Z'
description: >-
  A multi-step attack demonstrating a DoS vulnerability in curl's MQTT protocol
  handler, where a crafted 5-byte response causes an infinite loop and high CPU
  consumption.
skill_level: intermediate
impact_level: high
id: 2d16268c-ae45-4ab9-84ef-527a83d70282
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Denial of Service in curl via Malicious MQTT Response Parsing

Multi-stage attack chain demonstrating a complete DoS workflow exploiting a vulnerability in curl's MQTT protocol handling, leading to uncontrolled CPU consumption.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Malicious Server] --> B[Trigger curl Connection]
    B --> C[Observe DoS Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/socat]]
- [[tools/curl]]
- [[tools/top]]

### Target Environment

- Linux platform
- MQTT service simulation on port 12345
- curl built with MQTT support

### Initial Access Requirements

- Local network access to set up server
- No credentials required
- Administrative privileges not needed for basic reproduction

## Detailed Attack Procedures

### Step 1: Setup Malicious Server
procedure: [[procedures/Set-Up-Malicious-MQTT-Server-with-socat]]

**Objective**: Create a local TCP server that serves a 5-byte malicious MQTT response to trigger the vulnerability.

**Instructions**: Prepare a 'poc' file with the binary content (MQTT header: 0x10 0x18 0x00 0x04 'MQTT' version 4, keepalive 60, partial client ID). Then execute [[commands/socat-mqtt-server-setup]] to start the server:

```bash
socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork
```

**Expected Output**: Server listens on port 12345, forking for connections and serving the poc file content unidirectionally.

**Success Indicators**:
- Server process running without errors
- Port 12345 bound and listening (verifiable with netstat or ss)

### Step 2: Trigger curl Connection
procedure: [[procedures/Trigger-curl-DoS-with-MQTT-URL]]

**Objective**: Connect curl to the malicious server using an MQTT URL, causing it to enter an infinite parsing loop upon connection closure.

**Instructions**: With the server running, execute [[commands/curl-mqtt-dos-trigger]] to initiate the connection:

```bash
curl mqtt://localhost:12345
```

For testing with mitigation, use [[commands/curl-mqtt-with-timeout]]:

```bash
curl -m3 mqtt://localhost:12345
```

**Expected Output**: curl enters a busy loop, printing repeated 'mqtt_doing: state [0]' messages and consuming high CPU; with timeout, it exits after 3 seconds.

**Success Indicators**:
- curl process shows high CPU usage
- No immediate completion; requires interruption or timeout

### Step 3: Observe DoS Impact
procedure: [[procedures/Observe-Resource-Consumption-with-top]]

**Objective**: Monitor the curl process to confirm the DoS effect through resource exhaustion.

**Instructions**: While the curl command is running, execute [[commands/top-monitor-processes]] in another terminal:

```bash
top
```

**Expected Output**: curl process listed with ~100% CPU usage on one core due to the infinite loop in lib/mqtt.c.

**Success Indicators**:
- CPU utilization near 100% for curl
- Process stuck in 'mqtt_doing' state

## Attack Chain Summary

### Key Achievements

1. Simulated a malicious MQTT server with minimal effort (5-byte payload)
2. Triggered remote DoS on curl-based applications via protocol parsing flaw
3. Demonstrated high-impact resource consumption affecting automated tools like web crawlers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2023-10-01T00:00:00Z*
