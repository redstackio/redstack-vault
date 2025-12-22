---
id: proc-uuid-3
tags:
  - dos
  - settings-frames
  - cpu-exhaustion
type: procedure
tools:
  - '[[tools/Custom-HTTP2-Attack-Script]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/node-send-settings]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.675Z'
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Send-Large-SETTINGS-Frames

## Summary

This procedure sends oversized HTTP/2 SETTINGS frames with 14400-byte payloads over multiple connections to a Node.js server, causing uncontrolled CPU consumption and denial of service.

## Description

Exploiting the lack of limits on SETTINGS frame size and number in Node.js HTTP/2, this injects frames violating RFC 7540 section 10.5. The server processes them excessively without closing connections, pinning one CPU core at 100% usage indefinitely.

## Requirements

1. Multiple established HTTP/2 connections from prior procedure
2. Custom script capable of crafting HTTP/2 frames
3. Monitoring tools for CPU usage (e.g., top or htop)

## Defense

Defensive measures and detection strategies:

- Update Node.js to mitigate the frame handling flaw
- Enforce strict HTTP/2 frame size validation at the edge (e.g., using h2o or Envoy proxy)
- Detect via CPU anomaly monitoring and HTTP/2 log analysis for large SETTINGS frames

## Objectives

1. Transmit oversized SETTINGS frames to trigger processing loop
2. Achieve sustained CPU exhaustion on target
3. Confirm DoS by server unresponsiveness

## Instructions

### Step 1: Execute Frame Injection

**Context**: Use the attack script to send large frames on all open connections.

**Command** ([[commands/node-send-settings]]):
```bash
node attack.js --send-settings --payload-size 14400
```

> Sends frames with many settings entries totaling 14400 bytes. Expected output: Confirmation of transmission; server CPU spikes observable.

### Step 2: Validate DoS Impact

**Context**: Monitor server resources to confirm exploitation success.

**Command** ([[commands/top-cpu-monitor]]):
```bash
watch -n 1 'top -p $(pgrep node)'
```

> Watches Node.js process CPU. Successful output: One core at 100% usage persistently.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/node-send-settings]]
- [[commands/top-cpu-monitor]]

## Tools Used

- [[tools/Custom-HTTP2-Attack-Script]]

## Tags

- [[dos]]
- [[settings-frames]]
- [[cpu-exhaustion]]
