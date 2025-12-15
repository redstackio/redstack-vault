---
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
  - '[[commands/nc-listener]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T17:23:41.270Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 6d356b0b-4c2a-4391-af63-0f6c4e7072ee
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Set-Up-Reverse-Shell-Listener

## Summary

This procedure sets up a netcat listener to catch incoming reverse shell connections from the executed payload on the victim's machine.

## Description

After payload delivery, the attacker uses netcat (nc) to listen on a specified port (e.g., 80) for the victim's callback. This provides an interactive shell upon connection. Compatible with macOS/Linux environments. Prerequisites: nc installed and port accessible. Outcome: Ready to receive shell access.

## Requirements

1. Netcat (nc) utility installed
2. Firewall allowing inbound TCP on port 80
3. Public IP or port forwarding if behind NAT

## Defense

Defensive measures and detection strategies:

- Monitor for unusual inbound connections on high ports like 80
- Use host-based firewalls to block unauthorized listeners
- Log nc executions via process monitoring tools like auditd

## Objectives

1. Establish callback endpoint for RCE
2. Provide interactive access post-exploitation
3. Minimize detection during wait

## Instructions

### Step 1: Launch Netcat Listener

**Context**: Bind to port 80 in listen mode without DNS resolution for stealth.

**Command** ([[commands/nc-listener]]):

```bash
nc -nvl 80
```

> Listens verbosely; expect output like 'listening on [any] 80' and connection details upon callback.

### Step 2: Validate Listener

**Context**: Test connectivity from another machine to ensure it's active.

**Command** (Test connection):

```bash
telnet attacker_ip 80
```

> Should connect successfully; disconnect to resume waiting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Web Protocols]] Application Layer Protocol: Web Protocols

### Sub-Techniques

-

## Commands Used

- [[commands/nc-listener]]

## Tools Used

- [[tools/nc]]

## Tags

- [[reverse-shell]]
- [[listener]]
