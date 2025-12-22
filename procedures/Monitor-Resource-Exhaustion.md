---
id: proc-monitor-exhaustion
tags:
  - dos
  - monitoring
  - cpu
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/top-monitor-cpu]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.979Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Monitor-Resource-Exhaustion

## Summary

This procedure observes the impact of the DoS attack on the Node.js server, confirming CPU and network bandwidth exhaustion from the unbounded chunk reading.

## Description

After sending the malicious request, monitor server metrics to validate the exploit's success. The Node.js process will spike in CPU due to continuous parsing attempts, and the network connection will consume bandwidth without progress. This bypasses standard limits, leading to service denial. Access to server monitoring tools is ideal, but network-side observation works if server access is unavailable.

## Requirements

1. Access to server for process monitoring or network tools
2. Tools like top or htop installed
3. Knowledge of Node.js process ID

## Defense

Defensive measures and detection strategies:

- Set resource usage alerts (e.g., CPU >80% for web processes)
- Implement anomaly detection for single connections causing high load
- Regularly patch Node.js to versions addressing this vuln (post-2024)

## Objectives

1. Confirm elevated CPU and network usage
2. Validate DoS impact on server responsiveness
3. Measure attack effectiveness

## Instructions

### Step 1: Identify Node.js Process

**Context**: Locate the HTTP server process.

Run:

```bash
pgrep -f node
```

> Gets PID for monitoring.

### Step 2: Monitor CPU Usage

**Context**: Watch real-time resource consumption.

Execute [[commands/top-monitor-cpu]]:

```bash
top -p $(pgrep -f node)
```

> Observe %CPU column for spikes.

### Step 3: Check Network Activity

**Context**: Verify sustained connection.

Use netstat or ss:

```bash
ss -tuln | grep :3000
```

**Expected Output**: High CPU (e.g., 90%+), active ESTABLISHED connection with low throughput.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/top-monitor-cpu]]

## Tools Used


## Tags

- resource-monitoring
- dos-validation
