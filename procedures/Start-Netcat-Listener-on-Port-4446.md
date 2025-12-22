---
id: start-nc-listener-001
tags:
  - listener
  - reverse-shell
  - netcat
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nc-listen-port-4446]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Device CLI]]'
updated_at: '2025-12-14T03:46:09.298Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Network Device CLI]]'
---
# Start-Netcat-Listener-on-Port-4446

## Summary

This procedure deploys a netcat listener on a VPS to capture incoming reverse shell connections, essential for post-exploitation interaction in the Kafka Connect RCE chain.

## Description

Netcat serves as a simple TCP listener, binding to port 4446 on all interfaces. In the exploit scenario, the JVM agent loaded via Jolokia spawns a reverse shell to this endpoint, allowing command execution on the target Kafka Connect server. The verbose and no-DNS flags ensure clear logging without resolution delays.

## Requirements

1. Netcat installed on the VPS (common on Linux distributions)
2. Port 4446 open in VPS firewall (e.g., ufw allow 4446/tcp)
3. Root or sufficient privileges to bind ports

## Defense

Defensive measures and detection strategies:

- Monitor for netcat processes (ps aux | grep nc) and unusual port bindings
- Use host-based firewalls to block inbound connections on high ports
- Log network connections and alert on external listener setups

## Objectives

1. Bind a TCP listener for reverse shell reception
2. Maintain session for interactive shell access
3. Validate connectivity before exploit execution

## Instructions

### Step 1: Launch Netcat Listener

**Context**: Start the listener in a dedicated terminal or background process to await the reverse connection from the exploited agent.

**Command** ([[commands/nc-listen-port-4446]]):
```bash
nc -nlvp 4446
```

> The -n flag skips DNS, -l listens, -v provides verbose output, and -p specifies port 4446. Expected output: "Listening on [0.0.0.0] (family 0, port 4446)". Upon successful exploit, a connection appears with the target's shell prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution (listener for payload execution)

### Techniques

- [[Network Device CLI]] Network Connection (netcat for C2)

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-port-4446]]

## Tools Used

- [[tools/Netcat]]

## Tags

- listener
- reverse-shell
- netcat
