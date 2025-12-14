---
id: proc-setup-nc-listener
tags:
  - reverse-shell
  - listener
  - netcat
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nc-reverse-shell-listener]]'
verified: false
platforms:
  - Linux
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:48.424Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Setup-Netcat-Reverse-Shell-Listener

## Summary

This procedure sets up a netcat listener to receive an incoming reverse shell connection from the exploited Apache Flink server, enabling command execution post-RCE.

## Description

Netcat is used in listen mode on a specified port (8888) to catch the reverse shell payload delivered via the JavaScript gadget in the Flink RCE. This is a standard preparation for outbound connections from the target. Run on the attacker's machine with open firewall on the port. Expected outcome: Active listener ready for shell reception.

## Requirements

1. Netcat installed on attacker's system
2. Open outbound port 8888 on attacker's firewall
3. Knowledge of target listener IP for PoC configuration

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound connections from Flink servers to external IPs on high ports
- Use network segmentation to block Flink instances from initiating external connections
- Implement endpoint detection rules for netcat-like tools on internal networks

## Objectives

1. Establish a listener for reverse shell
2. Prepare for RCE payload reception
3. Enable interactive command execution

## Instructions

### Step 1: Start Netcat Listener

**Context**: Initiate listening mode to await the reverse shell.

**Command** ([[commands/nc-reverse-shell-listener]]):
```bash
nc -n -lvp 8888
```

> This command listens without DNS (-n), in listen mode (-l), verbose (-v), on port 8888 (-p). Expected output: 'Listening on [0.0.0.0] (family 0, port 8888)'. Keep terminal open.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/nc-reverse-shell-listener]]

## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- listener
- netcat
