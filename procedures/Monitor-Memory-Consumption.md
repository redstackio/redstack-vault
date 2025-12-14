---
tags:
  - memory-monitoring
  - dos-validation
type: procedure
tools:
  - '[[tools/top]]'
  - '[[tools/Task-Manager]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/monitor-with-top]]'
  - '[[commands/monitor-with-task-manager]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:28:28.297Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: b0b2e176-4232-4ff1-9607-8f9d302810ed
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Monitor-Memory-Consumption

## Summary

This procedure uses system monitoring tools to observe the increasing memory usage during PoC execution, validating the leak's impact on resource exhaustion and potential DoS.

## Description

While the PoC runs, tools like top on Linux or Task Manager on Windows track the process's resident set size (RSS), expecting growth from initial low KB to tens of thousands due to unfreed allocations. This confirms the vulnerability's exploitability in Hyperledger Fabric chaincode environments.

## Requirements

1. Running PoC process
2. Access to system monitoring tools
3. Basic familiarity with process IDs

## Defense

Defensive measures and detection strategies:

- Set memory limits on applications using cgroups (Linux) or Job Objects (Windows)
- Alert on anomalous memory growth via monitoring dashboards
- Regular code audits for leak patterns

## Objectives

1. Visualize memory leak in real-time
2. Quantify exhaustion for impact assessment
3. Identify signs of integer overflow if buffer issues occur

## Instructions

### Step 1: Monitor on Linux with Top

**Context**: Track the PoC process memory usage interactively.

**Command** ([[commands/monitor-with-top]]):
```bash
top -p $(pgrep memory_leak_poc)
```

> Displays real-time stats; look for RSS column increasing steadily. Expected: Growth to >32,000 KB.

### Step 2: Monitor on Windows with Task Manager

**Context**: Use GUI to watch memory for the executable process.

**Command** ([[commands/monitor-with-task-manager]]):
```bash
# Launch via GUI: Ctrl+Shift+Esc > Processes tab > Sort by Memory
```

> No CLI command; observe 'memory_leak_poc.exe' memory column rising. Expected: Similar growth pattern.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/monitor-with-top]]
- [[commands/monitor-with-task-manager]]

## Tools Used

- [[tools/top]]
- [[tools/Task-Manager]]

## Tags

- memory-monitoring
- dos-validation
