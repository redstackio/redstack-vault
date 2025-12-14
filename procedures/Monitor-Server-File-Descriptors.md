---
id: proc-003
tags:
  - monitoring
  - file-descriptors
  - resource-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/monitor-file-descriptors]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:36.747Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Monitor-Server-File-Descriptors

## Summary

This procedure queries and monitors the number of open file descriptors and mapped files for the Node.js server process to detect leaks during the DoS attack.

## Description

Using /proc filesystem on Linux, count FDs and map_files for the target PID before and after attack initiation to observe exhaustion.

## Requirements

1. Linux with /proc access
2. Root or same-user access to process
3. Known PID of Node.js server

## Defense

Defensive measures and detection strategies:

- Set low ulimits to fail fast on leaks
- Use monitoring tools like Prometheus for FD metrics
- Alert on FD count thresholds

## Objectives

1. Baseline resource usage
2. Track increases during attack
3. Validate leak exploitation

## Instructions

### Step 1: Get Baseline Count

**Context**: Run before attack to record initial values.

**Command** ([[commands/monitor-file-descriptors]]):
```bash
ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l
```

> Replace {PID} with actual process ID (e.g., from `ps aux | grep node`). Expected output: Two integers, e.g., '15' and '8'.

### Step 2: Monitor During Attack

**Context**: Re-run periodically to observe growth.

**Command** ([[commands/monitor-file-descriptors]]):
```bash
watch -n 5 'ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l'
```

> Uses watch for 5-second intervals. Expected output: Increasing numbers indicating leaks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/monitor-file-descriptors]]

## Tools Used


## Tags

- monitoring
- file-descriptors
- resource-leak
