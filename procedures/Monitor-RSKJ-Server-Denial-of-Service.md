---
id: proc-uuid-4
tags:
  - monitoring
  - dos-impact
  - oom-crash
type: procedure
tools:
  - '[[tools/Java]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.327Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Monitor-RSKJ-Server-Denial-of-Service

## Summary

This procedure observes the effects of the malicious UDP packet on the RSKJ server, confirming the infinite loop in RLP decoding leads to blocked traffic handling and an out-of-memory crash, validating the denial-of-service impact.

## Description

Post-packet transmission, the server's UDPServer thread hangs indefinitely on the single packet due to the loop in decode2 (no position advance despite length=0). Other packets are dropped, and after minutes, heap exhaustion causes OOM. Monitor via logs and tools like top; affects other entry points using decode2. Linux/Java environment; expected outcome: Server unresponsive and crashed.

## Requirements

1. Access to server console/logs
2. Resource monitoring tools (e.g., top, jstack)
3. Running RSKJ server from prior steps

## Defense

Defensive measures and detection strategies:

- Enable Java heap dumps on OOM for root cause analysis
- Set up alerts for high CPU/memory on Java processes
- Isolate UDP handlers in separate threads with timeouts

## Objectives

1. Confirm server hang and traffic blockage
2. Observe progression to out-of-memory crash
3. Validate full denial-of-service effect

## Instructions

### Step 1: Monitor Server Logs and Resources

**Context**: Watch for infinite loop indicators in RLP.java processing.

Use tail on logs:

```bash
tail -f rskj.log
```

> Look for repeated decode2 calls or stalled threads. Use top to see Java process CPU at 100%.

### Step 2: Test Traffic Blockage

**Context**: Send benign UDP packets to verify they are ignored.

Attempt peer discovery packets; expected: No response, confirming DoS.

> After ~5 minutes, expect OOM error: "java.lang.OutOfMemoryError".

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Java]]

## Tags

- [[monitoring]]
- [[dos-impact]]
- [[oom-crash]]
