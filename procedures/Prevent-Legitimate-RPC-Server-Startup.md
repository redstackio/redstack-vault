---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - defense-evasion
  - port-hijack
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:29:10.119Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Prevent-Legitimate-RPC-Server-Startup

## Summary

This procedure blocks the victim's legitimate monero-wallet-rpc from starting by occupying the RPC port, causing a silent failure if auto-started.

## Description

With the fake server bound, the monero-wallet-rpc executable attempts to bind to the same port and fails with an error. On systems without GUI feedback (e.g., headless or service-based startup), the victim remains unaware, allowing the fake server to handle all traffic.

## Requirements

1. Fake server already running on the RPC port
2. Victim configured to start monero-wallet-rpc manually or via service
3. No port ownership checks in the application

## Defense

Defensive measures and detection strategies:

- Implement startup checks for port availability and alert on bind failures
- Use privileged ports (<1024) or capabilities like CAP_NET_BIND_SERVICE
- Log service startup errors and monitor for RPC connection issues

## Objectives

1. Force failure of legitimate server
2. Maintain control of the port
3. Avoid victim detection

## Instructions

### Step 1: Monitor for Victim Startup Attempt

**Context**: Wait for the victim to launch monero-wallet-rpc.

Victim command (intercepted failure):
```bash
monero-wallet-rpc --rpc-bind-port 18081 --rpc-bind-ip 127.0.0.1 --wallet-file /path/to/wallet --password pass
```

> Error: "Failed to bind to 127.0.0.1:18081 - bind: Address already in use"

### Step 2: Verify Port Occupation

**Context**: Confirm the legitimate process cannot bind.

On Linux/macOS:
```bash
netstat -tuln | grep 18081
# Should show fake process PID
lsof -i :18081
```
On Windows:
```cmd
netstat -ano | findstr 18081
tasklist | findstr PID
```

> Port listed as occupied by attacker's process.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- defense-evasion
- port-hijack
