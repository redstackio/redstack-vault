---
id: proc-send-chunked-request
tags:
  - dos
  - network
  - tcp
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/nc-send-chunked-request]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.981Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Send-Request-to-Node.js-Server

## Summary

This procedure transmits the crafted malicious HTTP request to a Node.js HTTP server over a single TCP connection, initiating the resource exhaustion by leveraging the unbounded chunk extension vulnerability.

## Description

Using a raw TCP tool like netcat, the procedure sends the prepared request to the server's HTTP endpoint (typically port 3000 or 80). The server, upon receiving the chunked request with the malicious extension, begins attempting to read unlimited bytes from the connection, leading to DoS. This exploits the lack of bounds in the http module's parsing logic, affecting active Node.js lines. Expected outcome is a hung connection consuming server resources.

## Requirements

1. Crafted request payload from prior procedure
2. Netcat (nc) installed on attacker's machine
3. Network access to target's HTTP port

## Defense

Defensive measures and detection strategies:

- Enforce connection timeouts (e.g., 30s idle)
- Log and alert on chunked requests with unusual extensions
- Use WAF rules to inspect and block malformed chunked encodings

## Objectives

1. Establish TCP connection and send payload
2. Trigger server's unbounded read behavior
3. Maintain connection to sustain exhaustion

## Instructions

### Step 1: Prepare Connection

**Context**: Identify target host and port.

Set variables:

```bash
export TARGET_HOST="target-server"
export TARGET_PORT=3000
```

> Ensures correct endpoint for transmission.

### Step 2: Transmit Request

**Context**: Pipe the malicious request to netcat for sending.

Execute [[commands/nc-send-chunked-request]]:

```bash
cat malicious_request.txt | nc $TARGET_HOST $TARGET_PORT
```

> Netcat connects via TCP and sends the raw HTTP data. The connection should not close immediately.

### Step 3: Verify Transmission

**Context**: Check if the request was accepted without error.

Monitor local output for connection success; no response expected from server.

**Expected Output**: No errors from nc, connection remains open.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/nc-send-chunked-request]]

## Tools Used

- [[tools/Netcat]]

## Tags

- dos
- tcp-injection
