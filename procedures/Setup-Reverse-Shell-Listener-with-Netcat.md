---
id: proc-003
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
  - '[[commands/nc-listen-reverse-shell]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:23:49.750Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Setup-Reverse-Shell-Listener-with-Netcat

## Summary

This procedure sets up a netcat listener to receive an incoming reverse TCP shell from the exploited DNN server.

## Description

Netcat is used in listen mode on port 7575 to catch the PowerShell reverse connection initiated by the RCE payload. This provides an interactive shell on the target Windows server. Run before sending the RCE trigger.

## Requirements

1. Netcat installed on attacker's machine
2. Port 7575 open and not firewalled
3. Attacker's IP accessible from target (e.g., via port forwarding)

## Defense

Defensive measures and detection strategies:

- Monitor inbound connections on non-standard ports
- Use host-based firewalls to block unauthorized listeners
- Log PowerShell executions for reverse connect attempts

## Objectives

1. Establish listening socket for reverse connection
2. Receive shell upon target execution
3. Interact with target system

## Instructions

### Step 1: Start Netcat Listener

**Context**: Initiate listening on specified port in verbose mode.

**Command** ([[commands/nc-listen-reverse-shell]]):
```bash
nc -nlvp 7575
```

> Outputs listening confirmation. Success when target connects, showing remote IP and shell prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-reverse-shell]]

## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- listener
- post-exploitation
