---
id: proc-004
tags:
  - monitoring
  - memory-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:36.734Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Monitor-Server-Memory-Consumption

## Summary

This procedure uses system tools to watch the Node.js server's memory usage, detecting leaks from unreleased buffers during unknownProtocol events.

## Description

Focus on RSS (Resident Set Size) and VMS (Virtual Memory Size) metrics to identify gradual memory depletion leading to OOM if FD limits are not hit first.

## Requirements

1. Linux with tools like top or htop
2. Access to run monitoring commands
3. Running Node.js process

## Defense

Defensive measures and detection strategies:

- Enable Node.js heap dumps on high memory
- Use container limits for memory
- Monitor with tools like Node Clinic

## Objectives

1. Baseline memory usage
2. Detect increases from leaks
3. Confirm DoS via OOM

## Instructions

### Step 1: Baseline Monitoring

**Context**: Observe pre-attack memory.

**Command**:
```bash
top -p {PID}
```

> Replace {PID}; focus on %MEM and RES columns. Expected output: Stable memory values.

### Step 2: Continuous Watch

**Context**: Track during attack.

**Command**:
```bash
htop --filter=node
```

> Or use top with watch. Expected output: Rising RES indicating leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- monitoring
- memory-leak
