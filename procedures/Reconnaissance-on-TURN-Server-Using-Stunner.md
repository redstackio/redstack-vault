---
tags:
  - turn-recon
  - stunner
  - open-relay
type: procedure
tools:
  - '[[tools/Stunner]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/stunner-recon-turn-server]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:44.168Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ced17104-cd64-4536-a92e-2e138d6b4f7f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
---

# Reconnaissance-on-TURN-Server-Using-Stunner

## Summary

This procedure uses the stunner tool to probe a TURN server for misconfigurations, such as open relays allowing internal peer IPs, confirming vulnerability to abuse for internal network pivoting.

## Description

Stunner is a specialized tool for testing TURN/STUN servers. With extracted credentials, it authenticates and runs reconnaissance to check relay permissions, peer IP allowances (e.g., 127.0.0.1, 169.254.169.254), and protocol support (TCP/UDP). This reveals lack of denied-peer-ip config in coturn, enabling firewall bypass. Targets are public TURN servers on TLS port 443.

## Requirements

1. TURN credentials (username) from prior extraction
2. Stunner tool installed on Linux/macOS
3. Network access to TURN server port 443/TLS

## Defense

Defensive measures and detection strategies:

- Configure coturn with denied-peer-ip to block internal ranges
- Log and monitor TURN authentication attempts and relay allocations
- Use rate limiting on TURN endpoints to detect scanning

## Objectives

1. Confirm open relay status and peer restrictions
2. Identify supported protocols and ports for exploitation
3. Gather config details for targeted abuse

## Instructions

### Step 1: Authenticate and Recon

**Context**: Run stunner recon to probe server configuration and relay behavior.

**Command** ([[commands/stunner-recon-turn-server]]):
```bash
stunner recon tls://turn.example.com:443 -u extracted_username
```

> This command authenticates with the username and outputs relay details, including allowed peers (e.g., any IP), open relay confirmation, and UDP/TCP support. Look for absence of peer validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/stunner-recon-turn-server]]

## Tools Used

- [[tools/Stunner]]

## Tags

- [[turn-recon]]
- [[tools/Stunner]]
- [[open-relay]]

---
