---
id: proc-nc-listener-001
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
  - '[[commands/nc-listen-reverse-shell]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Asymmetric Cryptography]]'
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:24:08.287Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Asymmetric Cryptography]]'
  - '[[Connection Proxy]]'
---
# Set-Up-Netcat-Listener-for-Reverse-Shell

## Summary

This procedure configures netcat (nc) on the attacker's host to listen on a specified port, ready to receive an incoming reverse shell connection from the target.

## Description

Netcat is used as a simple TCP listener to catch the reverse shell payload. This step is performed on the attacker's controlled machine, assuming port 1337 is available and not firewalled. It complements RCE exploits by providing the endpoint for shell interaction.

## Requirements

1. Netcat installed on attacker's host
2. Port 1337 available (or adjust as needed)
3. Network path from target to attacker

## Defense

Defensive measures and detection strategies:

- Block inbound connections on high ports via firewall
- Monitor for nc processes and unusual TCP listeners
- Use IDS to detect reverse shell patterns

## Objectives

1. Bind to port for incoming connections
2. Receive shell payload
3. Enable interactive access

## Instructions

### Step 1: Run Netcat Listener

**Context**: Start nc in listen mode with no DNS, verbose output, and port specification.

**Command** ([[commands/nc-listen-reverse-shell]]):
```bash
nc -nvlp 1337
```

> Flags: -n (no DNS), -v (verbose), -l (listen), -p 1337 (port). Output shows listening status; keep terminal open.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Asymmetric Cryptography]] Encrypted Code Execution
- [[Connection Proxy]] Proxy

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-reverse-shell]]

## Tools Used

- [[tools/nc]]

## Tags

- listener
- nc
