---
id: proc-netcat-listener
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
  - '[[commands/netcat-listener]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:57.745Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
---
# Set-Up-Netcat-Listener

## Summary

This procedure sets up a netcat listener on the attacker's machine to catch the incoming reverse shell from the exploited LGTM build container.

## Description

Netcat serves as a simple TCP listener to receive the shell connection initiated by the RCE payload. This provides interactive access to the sandboxed container, allowing exploration of internal network and services like the Docker Registry at 172.17.0.1:5000.

## Requirements

1. Netcat installed on attacker's machine
2. Open port (e.g., 4444) not blocked by firewall
3. Static IP or accessible host for the target container

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected inbound connections on high ports
- Use IDS to detect netcat usage patterns
- Restrict outbound connections from sandboxes to known endpoints

## Objectives

1. Receive reverse shell for container access
2. Maintain session for subsequent commands
3. Validate RCE success

## Instructions

### Step 1: Launch Netcat Listener

**Context**: Start listening on the specified port to await the shell connection.

**Command** ([[commands/netcat-listener]]):
```bash
nc -vlp ATTACKER_PORT
```

> This enters listen mode (-l), verbose (-v), on port ATTACKER_PORT (e.g., 4444). Expected output: 'Listening on [0.0.0.0] (family 0, port 4444)'. Upon connection: shell prompt from container.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/netcat-listener]]

## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- listener

---
