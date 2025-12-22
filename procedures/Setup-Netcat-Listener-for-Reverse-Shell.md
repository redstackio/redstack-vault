---
id: proc-uuid-002
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
  - '[[commands/nc-listen-on-port-4444]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:54.873Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Setup-Netcat-Listener-for-Reverse-Shell

## Summary

This procedure sets up a netcat listener on the attacker's server to catch the incoming reverse shell from the exploited Grafana instance, enabling interactive command execution on the target.

## Description

Netcat is used as a simple TCP listener to receive the bash reverse shell payload injected via the grafana-image-renderer configuration. The listener must be running on a publicly accessible port before triggering the exploit to ensure the connection is established immediately upon renderer invocation.

## Requirements

1. Netcat installed on attacker machine (common on Linux/Unix systems)
2. Public IP address or port forwarding for the listener port
3. No firewall blocking inbound TCP on port 4444

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected inbound connections on high ports
- Use network segmentation to limit reverse shell callbacks
- Implement host-based firewalls to block unauthorized listeners

## Objectives

1. Establish a TCP listener for reverse shell reception
2. Verify connectivity from the target environment
3. Gain interactive shell access post-exploitation

## Instructions

### Step 1: Verify Netcat Availability

**Context**: Ensure netcat is installed and functional.

Run `nc --version` to check installation.

**Expected Output**: Version information confirming netcat presence.

### Step 2: Start Listener

**Context**: Launch the listener on port 4444 to await the reverse shell.

Execute [[commands/nc-listen-on-port-4444]]:

```bash
nc -n -lvp 4444
```

> This command listens (-l) on port 4444 (-p 4444) without DNS resolution (-n) in verbose mode (-v), displaying connection attempts.

**Expected Output**: Output like "listening on [any] 4444 ..." followed by connection details upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-on-port-4444]]

## Tools Used

- [[tools/netcat]]

## Tags

- reverse-shell
- listener
- netcat
