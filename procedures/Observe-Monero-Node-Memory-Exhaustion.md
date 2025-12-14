---
id: a2c136aa-78f1-4091-95d0-de87bbecaa72
name: Observe-Monero-Node-Memory-Exhaustion
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.799Z'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - dos
  - monitoring
  - monero
  - memory-exhaustion
commands: []
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---

# Observe-Monero-Node-Memory-Exhaustion

## Summary

This procedure monitors the target Monero node for signs of denial of service, confirming memory exhaustion and unresponsiveness following the malicious request.

## Description

Post-exploitation, the node's core (in m_core.handle_get_objects) allocates memory per ID without bounds, leading to OOM killer activation, crashes, or hangs. Observation can be remote via P2P probes or local if access allows. This validates the DoS impact, where the node fails to process legitimate blockchain requests.

## Requirements

1. Network access for probing the target
2. Monitoring tools like netstat or custom P2P pinger
3. Optional: SSH access for local resource checks

## Defense

Defensive measures and detection strategies:

- Alert on high memory usage in monerod process
- Implement watchdog to restart daemon on hangs
- Log P2P message sizes and handler errors

## Objectives

1. Confirm resource exhaustion and node impairment
2. Measure DoS duration and recovery time
3. Validate attack success for reporting

## Instructions

### Step 1: Probe Node Responsiveness

**Context**: Send follow-up P2P messages (e.g., PING or GET_INFO) to check if the node responds.

Implement a simple probe script:

```cpp
// Send p2p::PING over the connection
// Timeout after 10s
if (no response) { log "Unresponsive"; }
```

> Expected output: Timeouts or errors indicate DoS success.

### Step 2: Monitor Resource Usage

**Context**: If local access, use system tools to watch memory; remotely, infer from unresponsiveness.

For local observation:

```bash
watch -n 1 'free -h | grep Mem'  # Or top -p $(pgrep monerod)
```

> Look for memory nearing 100% or OOM logs in dmesg. Expected output: Escalating usage leading to crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[watch]]
- [[free]]
- [[top]]

## Tools Used


## Tags

- [[dos]]
- [[monitoring]]
- [[monero]]
