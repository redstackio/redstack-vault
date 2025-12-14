---
tags:
  - dos
  - monitoring
  - cpu-exhaustion
type: procedure
tools:
  - '[[tools/top]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/top-monitor-processes]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:36.672Z'
sub_techniques: []
id: 71db9bfb-a51c-4001-8127-4f4ce2da9ee1
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-Resource-Consumption-with-top

## Summary

This procedure monitors system processes in real-time to confirm the DoS impact, specifically high CPU usage from the curl process stuck in the MQTT parsing loop.

## Description

During the attack, curl consumes nearly 100% CPU on one core due to repeated failed reads in the busy loop. The target environment is Linux with the top utility available. This step validates the vulnerability's effect post-trigger. Expected outcome: Visual confirmation of resource exhaustion, highlighting the DoS severity for applications auto-fetching MQTT URLs.

## Requirements

1. Linux system with top installed (standard on most distros)
2. Running curl process from the trigger procedure
3. Terminal access for monitoring

## Defense

Defensive measures and detection strategies:

- Implement process monitoring tools like Prometheus for CPU alerts
- Use resource limits (ulimit) on curl invocations
- Scan for vulnerable curl versions and update promptly

## Objectives

1. Verify CPU consumption from the exploit
2. Quantify impact for severity assessment
3. Identify stuck processes for cleanup

## Instructions

### Step 1: Monitor Processes

**Context**: Launch top to view real-time CPU and memory usage, focusing on the curl process.

**Command** ([[commands/top-monitor-processes]]):
```bash
top
```

> This displays a dynamic list sorted by CPU. Expected output: curl at top with %CPU ~100, state 'D' or running, confirming the loop.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/top-monitor-processes]]

## Tools Used

- [[tools/top]]

## Tags

- [[dos]]
- [[monitoring]]
