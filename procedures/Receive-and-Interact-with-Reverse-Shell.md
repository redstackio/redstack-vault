---
id: receive-reverse-shell-001
tags:
  - reverse-shell
  - post-exploitation
  - rce
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T03:46:09.293Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Receive-and-Interact-with-Reverse-Shell

## Summary

This procedure handles the reception and interaction with the reverse shell spawned by the loaded JVM agent on the Kafka Connect server, enabling full control for further exploitation.

## Description

Upon successful agent load via Jolokia, the embedded payload executes system commands to connect back to the netcat listener on the VPS port 4446, providing a bind shell. This grants access to the JVM process context on the target, allowing file access, process enumeration, and persistence.

## Requirements

1. Active netcat listener from prior step
2. VPS with stable connection to target
3. Knowledge of target environment (e.g., Java/Kafka paths)

## Defense

Defensive measures and detection strategies:

- Monitor JVM processes for unauthorized agent loads (e.g., via jcmd or logs)
- Implement application whitelisting to block unsigned JAR execution
- Network segmentation to prevent outbound connections from Connect servers
- Alert on unexpected TCP connections to external high ports

## Objectives

1. Confirm reverse shell establishment
2. Execute post-exploitation commands on target
3. Maintain access for data exfiltration or lateral movement

## Instructions

### Step 1: Monitor Netcat for Connection

**Context**: Observe the listener for the incoming shell from the exploited agent.

No specific command; interact directly in the netcat terminal.

> Expected output: Connection message followed by target shell prompt (e.g., "$" or "#"). Test with basic commands like `whoami` or `id` to verify access.

### Step 2: Interact with Shell

**Context**: Use the shell for reconnaissance and actions.

**Command** (Example Unix Shell):
```bash
whoami; uname -a; pwd
```

> Run commands to gather info. Expected output: User (likely kafka-connect), kernel details, current directory (e.g., /opt/kafka).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Netcat]]

## Tags

- reverse-shell
- post-exploitation
- rce
