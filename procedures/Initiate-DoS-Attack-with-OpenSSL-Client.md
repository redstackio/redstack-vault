---
id: proc-005
tags:
  - dos
  - openssl
  - flood-attack
type: procedure
tools:
  - '[[tools/openssl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-malformed-http-request]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.726Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Initiate-DoS-Attack-with-OpenSSL-Client

## Summary

This procedure runs the client script to flood the Node.js HTTP2 server with malformed SSL connections, exploiting the unknownProtocol event for resource exhaustion.

## Description

The attack sends HTTP/1.1 requests over SSL, causing the server to emit unknownProtocol, close the socket with an error, but wait for a non-existent client response, leaking FDs and memory.

## Requirements

1. client.sh script prepared
2. openssl installed
3. Target server running on 127.0.0.1:50000

## Defense

Defensive measures and detection strategies:

- Patch Node.js to handle unknownProtocol with timeouts
- Firewall rules to limit connection rates
- Intrusion detection for anomalous SSL traffic

## Objectives

1. Trigger multiple unknownProtocol events
2. Exhaust server resources
3. Achieve DoS on new connections

## Instructions

### Step 1: Start the Attack Script

**Context**: Launch the infinite loop of connections.

**Command** ([[commands/send-malformed-http-request]]):
```bash
./client.sh
```

> Executes the loop spawning openssl processes. Expected output: No console output; check server logs for events.

### Step 2: Validate Impact

**Context**: Confirm resource exhaustion.

**Command**:
```bash
# Run in another terminal: monitor-file-descriptors
ls -l /proc/{PID}/fd | wc -l
```

> Expected output: Rapidly increasing FD count until limit hit.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion

### Sub-Techniques


## Commands Used

- [[commands/send-malformed-http-request]]

## Tools Used

- [[tools/openssl]]

## Tags

- dos
- openssl
- flood-attack
