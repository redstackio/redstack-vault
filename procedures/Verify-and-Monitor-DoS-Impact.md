---
id: proc-verify-dos-impact-001
tags:
  - monitoring
  - verification
  - logs
type: procedure
tools:
  - '[[tools/netstat]]'
  - '[[tools/nginx]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/jobs-check-pending]]'
  - '[[commands/netstat-connection-count]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:26:48.937Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Verify-and-Monitor-DoS-Impact

## Summary

This procedure monitors the DoS effectiveness by checking pending curl jobs, counting established connections, and reviewing nginx logs for long response times and large byte transfers.

## Description

After launching requests, verify proxy exhaustion: jobs show pending curls, netstat counts connections to attacker IP, and nginx access.log reveals 500 status, high bytes (1GB), and times (1500s+ for slow, 50s for big).

## Requirements

1. Ongoing DoS launch ([[procedures/Launch-Slow-and-Large-DoS-via-Proxy]])
2. Access to launch machine and attacker server

## Defense

Defensive measures and detection strategies:

- Log analysis for anomalous long connections
- Alerts on high connection counts to single IPs
- Real-time monitoring of proxy resource usage

## Objectives

1. Confirm resource exhaustion on proxy
2. Measure impact (connections, bandwidth, time)
3. Identify successful attack parameters

## Instructions

### Step 1: Check Pending Jobs

**Context**: Verify curls are still running on launch machine.

Execute [[commands/jobs-check-pending]]:

```bash
jobs
```

> Expected output: List like [1] Running time curl ... (multiple jobs).

### Step 2: Count Connections

**Context**: On attacker server, count ESTABLISHED TCP to proxy IP.

Execute [[commands/netstat-connection-count]]:

```bash
netstat -nt | grep ESTABLISHED | grep -c ████32
```

> Expected output: Number e.g., 20 connections.

### Step 3: Review Nginx Logs

**Context**: Inspect access.log for details.

tail -f /var/log/nginx/access.log | grep slow.php

> Expected output: Lines with GET /slow.php 500, bytes ~640kB, time 1500s+; for big.php ~1GB in 50s.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Service Scanning (adapted for monitoring)

### Sub-Techniques


## Commands Used

- [[commands/jobs-check-pending]]
- [[commands/netstat-connection-count]]

## Tools Used

- [[tools/netstat]]
- [[tools/nginx]]

## Tags

- monitoring
- verification
