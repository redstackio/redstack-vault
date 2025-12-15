---
id: proc-uuid-2
tags:
  - connections
  - http2
  - dos
type: procedure
tools:
  - '[[tools/Custom-HTTP2-Attack-Script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-attack-connections]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:26:30.678Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Establish-Multiple-HTTP2-Connections

## Summary

This procedure opens multiple concurrent HTTP/2 connections to a Node.js server, setting the stage for injecting oversized SETTINGS frames to exploit the DoS vulnerability.

## Description

By establishing many persistent connections (e.g., 100+), the attacker prepares to flood the server with malicious frames. Node.js fails to limit or close these, allowing sustained resource drain. This targets the HTTP/2 module's connection handling flaws.

## Requirements

1. Running Node.js HTTP/2 server from previous procedure
2. Network access to the server endpoint
3. Custom attack script with connection logic

## Defense

Defensive measures and detection strategies:

- Limit concurrent HTTP/2 connections per IP using rate limiting (e.g., via firewall or application gateway)
- Log and alert on sudden spikes in connection counts
- Use intrusion detection systems to flag anomalous HTTP/2 traffic patterns

## Objectives

1. Create numerous open HTTP/2 connections
2. Ensure connections remain persistent
3. Prepare for frame transmission without disconnection

## Instructions

### Step 1: Run Connection Script

**Context**: Execute the attack script to initiate multiple connections to the target.

**Command** ([[commands/node-attack-connections]]):
```bash
node attack.js --target localhost:3000 --connections 100
```

> This opens 100 connections. Expected output: Logs of each connection success, no server-side rejection.

### Step 2: Monitor Connections

**Context**: Verify connections are active using netstat or similar.

**Command** ([[commands/netstat-connections]]):
```bash
netstat -an | grep :3000 | wc -l
```

> Counts connections to port 3000. Successful output: Number matching or exceeding 100.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Standard Application Layer Protocol]]

### Sub-Techniques


## Commands Used

- [[commands/node-attack-connections]]
- [[commands/netstat-connections]]

## Tools Used

- [[tools/Custom-HTTP2-Attack-Script]]

## Tags

- [[connections]]
- [[http2]]
- [[dos]]
