---
id: proc-uuid-004
name: Start-Netcat-Listener-in-Container
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.882Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - netcat
  - listener
  - ssrf
  - docker
commands:
  - '[[commands/nc-listen-12345]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/Netcat]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Start-Netcat-Listener-in-Container

## Summary

This procedure starts a netcat TCP listener on port 12345 inside the GitLab container to capture and verify incoming SSRF requests from the FogBugz import feature.

## Description

Netcat is configured in listen mode with verbose output to monitor connections. Port 12345 is chosen as an arbitrary internal port; the listener confirms the SSRF by detecting requests to localhost. This runs in the container shell and blocks until a connection arrives.

## Requirements

1. Netcat installed in the GitLab container
2. Available port 12345 (not in use)
3. Shell session in the container

## Defense

Defensive measures and detection strategies:

- Firewall rules to block unexpected internal port listening (e.g., iptables in container)
- Container network policies to isolate internal communications
- Log netstat or ss outputs for anomalous listeners

## Objectives

1. Establish a listener for internal SSRF traffic
2. Provide verbose logging for connection confirmation
3. Enable detection of unauthorized internal requests

## Instructions

### Step 1: Launch Netcat Listener

**Context**: Bind netcat to port 12345 in listening mode to await SSRF-triggered connections.

**Command** ([[commands/nc-listen-12345]]):
```bash
nc -llvp 12345
```

> Flags: -l for listen, -v for verbose, -p for port. Expected output: "Listening on [0.0.0.0] (family 0, port 12345)". Upon connection, it will display source details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-12345]]

## Tools Used

- [[tools/Netcat]]

## Tags

- netcat
- listener
- ssrf
- docker
