---
tags:
  - dos
  - infinite-loop
  - rlp-decoding
  - rskj
  - udp-exploit
  - uncontrolled-resource-consumption
type: attack_chain
tools:
  - '[[tools/Java]]'
  - '[[tools/Python-3]]'
  - '[[tools/pysha3]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Java
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Vulnerable-RSKJ-Software]]'
  - '[[procedures/Launch-Vulnerable-RSKJ-Node]]'
  - '[[procedures/Craft-and-Send-Malicious-UDP-Packet]]'
  - '[[procedures/Monitor-RSKJ-Server-Denial-of-Service]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.354Z'
description: >-
  A multi-stage attack exploiting an uncontrolled resource consumption
  vulnerability in the RSKJ server's RLP decoding, leading to an infinite loop
  and eventual out-of-memory crash via a crafted UDP packet.
skill_level: intermediate
impact_level: high
id: c0b272e3-a7b8-405a-88e2-9d6fc73ddf2d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Denial-of-Service Attack on RSKJ Server via Malformed RLP Decoding

Multi-stage attack chain demonstrating exploitation of a denial-of-service vulnerability in the RSKJ (Rootstock Java) server through malformed Recursive Length Prefix (RLP) data in a UDP packet, causing an infinite loop in the decoding function and leading to server hang and out-of-memory crash.

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
    A[Obtain Vulnerable Software] --> B[Launch RSKJ Server]
    B --> C[Send Crafted UDP Packet]
    C --> D[Observe Server Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Java]]
- [[tools/Python-3]]
- [[tools/pysha3]]

### Target Environment

- Java-based RSKJ node (version 5.0.0-FINGERROOT)
- Linux OS
- UDPv6 port 5050 open for peer communications

### Initial Access Requirements

- Network access to the target's UDPv6 port 5050
- No credentials required; exploits public-facing UDP listener
- Attacker positioned to send UDP packets to the server

## Detailed Attack Procedures

### Step 1: Obtain Vulnerable Software
procedure: [[procedures/Obtain-Vulnerable-RSKJ-Software]]

**Objective**: Download the vulnerable RSKJ JAR file to set up the target environment for exploitation.

**Instructions**: Access the GitHub releases page and download the specific vulnerable version of the RSKJ core JAR file.

**Expected Output**: rskj-core-5.0.0-FINGERROOT-all.jar file obtained and ready for server launch.

**Success Indicators**:
- JAR file downloaded successfully
- File integrity verified (e.g., via checksum if available)

### Step 2: Launch Vulnerable RSKJ Node
procedure: [[procedures/Launch-Vulnerable-RSKJ-Node]]

**Objective**: Start the RSKJ server to expose the vulnerable UDPv6 listener on port 5050.

**Instructions**: Use [[commands/start-rskj-server]] to initiate the node with the downloaded JAR:

```bash
java -classpath rskj-core-5.0.0-FINGERROOT-all.jar -Drpc.providers.web.cors=* -Drpc.providers.web.ws.enabled=true co.rsk.Start
```

**Expected Output**: Server starts and logs indicate listening on UDPv6 port 5050 for peer communications.

**Success Indicators**:
- Server process running without errors
- UDPv6 port 5050 confirmed open via netstat or similar

### Step 3: Craft and Send Malicious UDP Packet
procedure: [[procedures/Craft-and-Send-Malicious-UDP-Packet]]

**Objective**: Prepare the Python environment and execute a PoC script to send a crafted UDP packet triggering the RLP decoding infinite loop.

**Instructions**: First, install the required library using [[commands/install-pysha3]]:

```bash
pip install pysha3
```

Then, download the poc.py script, modify the HOST variable to the target's IP, and run the script to send the malformed packet to UDPv6 port 5050.

**Expected Output**: Script executes without errors, packet sent to target.

**Success Indicators**:
- pysha3 library installed
- PoC script runs and confirms packet transmission

### Step 4: Monitor RSKJ Server Denial of Service
procedure: [[procedures/Monitor-RSKJ-Server-Denial-of-Service]]

**Objective**: Observe the server's response to the malicious packet, confirming the hang and eventual crash.

**Instructions**: Monitor server logs and resource usage while sending additional benign traffic; the server should process only the malicious packet indefinitely.

**Expected Output**: Server hangs on the packet, blocks further UDP traffic, and crashes with out-of-memory error after several minutes.

**Success Indicators**:
- Server stops responding to new UDP packets
- Logs show infinite loop in RLP.java decode2 function
- Out-of-memory exception after ~5 minutes

## Attack Chain Summary

### Key Achievements

1. Successfully launched vulnerable RSKJ node exposing UDPv6 port 5050
2. Crafted and sent UDP packet with malformed RLP data causing infinite loop in bytesToLength method
3. Induced server denial-of-service, preventing peer communications and leading to crash

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
