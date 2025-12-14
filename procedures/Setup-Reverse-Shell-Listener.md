---
tags:
  - listener-setup
  - reverse-shell
  - network
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nc-tcp-listener]]'
platforms:
  - Linux
techniques:
  - '[[Encrypted Channel]]'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
id: 10d48b9e-f905-42f7-bc0e-021541fd3617
created_at: '2025-12-14T17:24:08.466Z'
updated_at: '2025-12-14T17:24:08.466Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Encrypted Channel]]'
---
# Setup-Reverse-Shell-Listener

## Summary

This procedure configures a netcat listener on the attacker's machine to receive the incoming reverse shell connection from the executed PHP payload.

## Description

Netcat acts as a simple TCP server, binding to a specified port and waiting for connections. When the PHP shell executes, it initiates a reverse connection, handing over a shell session. This is a common C2 mechanism in pentesting and attacks.

## Requirements

1. Netcat installed on attacker's machine
2. Chosen port (e.g., 1234) available and not firewalled
3. Attacker's IP reachable from the target server

## Defense

Defensive measures and detection strategies:

- Block inbound connections on non-standard ports via firewalls
- Monitor for netcat processes or unusual listening sockets (e.g., via netstat or ss)
- Use IDS/IPS to detect reverse shell traffic patterns

## Objectives

1. Bind listener to target port
2. Prepare for incoming connection
3. Enable interactive shell upon callback

## Instructions

### Step 1: Start Netcat Listener

**Context**: Initiate TCP listening mode.

**Command** ([[commands/nc-tcp-listener]]):
```bash
nc -nlvp 1234
```

> Command starts verbose listener on port 1234; displays 'listening on [any] 1234'. Expected output waits for connections.

### Step 2: Monitor for Connection

**Context**: Keep the session open until payload triggers.

Leave the terminal running; it will show incoming connection details.

> Upon success, connection established message appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Encrypted Channel]]

### Sub-Techniques


## Commands Used

- [[commands/nc-tcp-listener]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[listener-setup]]
- [[reverse-shell]]
- [[network]]
