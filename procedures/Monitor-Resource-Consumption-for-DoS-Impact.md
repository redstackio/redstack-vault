---
tags:
  - dos
  - monitoring
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0e23b58d-2944-4de5-9cb8-42e3585f42fa
created_at: '2025-12-14T17:26:30.110Z'
updated_at: '2025-12-14T17:26:30.110Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Monitor-Resource-Consumption-for-DoS-Impact

## Summary

This procedure monitors CPU, memory, and network resource usage on the target server and client machine during the curl globbing exploit to validate the denial of service impact from the request flood.

## Description

After initiating the curl exploit, resource monitoring reveals the effects of the massive URL expansion, including high CPU from parsing and network I/O from request generation. Tools like top, htop, or netstat can be used on Linux to track metrics. This step confirms the vulnerability's severity, showing potential for service crashes due to overload. It assumes the local HTTP server and curl are running.

## Requirements

1. Access to system monitoring tools (e.g., top, ps)
2. Ongoing exploit execution
3. Permissions to view system processes and network stats

## Defense

Defensive measures and detection strategies:

- Implement resource quotas and alerts for CPU/network spikes
- Log analysis for patterns of globbing-like request floods
- Rate limiting on servers to mitigate DoS

## Objectives

1. Quantify resource exhaustion from exploit
2. Identify DoS symptoms like high load
3. Validate attack success

## Instructions

### Step 1: Observe System Metrics

**Context**: Use built-in Linux tools to track resource usage in real-time as the curl requests flood the server.

**Command** (No specific command; use top or similar):
```bash
top
```

> Run top to monitor processes; look for high CPU in curl and server processes, along with elevated network activity. Expected output: Process list showing %CPU near 100% for affected binaries, increased load average, and potential swap usage.

### Step 2: Check Network Logs

**Context**: Review server logs for request volume to correlate with resource spikes.

**Command** (Tail server output or logs):
```bash
tail -f /path/to/server.log
```

> If the HTTP server logs to stdout or a file, tail it to see the influx of GET requests. Expected output: Thousands of log entries per second for paths /N/, indicating the flood.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[monitoring]]
