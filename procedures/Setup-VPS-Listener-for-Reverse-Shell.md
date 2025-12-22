---
id: setup-vps-listener-001
tags:
  - setup
  - vps
  - reverse-shell
type: procedure
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssh-login-to-vps]]'
verified: false
platforms:
  - Cloud
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T03:46:09.301Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Setup-VPS-Listener-for-Reverse-Shell

## Summary

This procedure establishes access to a VPS instance controlled by the attacker, preparing it as a listener endpoint for receiving reverse shell connections from exploited targets like Aiven Kafka Connect servers.

## Description

In the context of the Kafka Connect RCE exploit, a VPS provides an external anchor for command and control. SSH access allows setup of listeners without exposing the attacker's local machine. This step ensures the environment is ready before triggering the payload, which spawns a reverse shell back to the VPS on port 4446.

## Requirements

1. SSH key or credentials for the VPS instance
2. VPS with public IP and open outbound/inbound TCP on port 4446
3. Basic Linux knowledge for shell navigation

## Defense

Defensive measures and detection strategies:

- Monitor SSH logs for unusual access patterns from known attacker IPs
- Use firewall rules to restrict SSH to trusted IPs
- Implement multi-factor authentication (MFA) on VPS management

## Objectives

1. Gain shell access to the VPS for listener deployment
2. Verify network connectivity for reverse connections
3. Prepare for netcat listener without local exposure

## Instructions

### Step 1: SSH Login to VPS

**Context**: Connect to the VPS to access its shell for subsequent listener setup.

**Command** ([[commands/ssh-login-to-vps]]):
```bash
ssh ████
```

> This command initiates an SSH session to the redacted VPS hostname or IP (████ represents the target). Expected output is an interactive bash shell prompt on the VPS, confirming access. If prompted, enter credentials or use key-based auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery (environment setup)

### Techniques

- [[Web Protocols]] Application Layer Protocol (SSH for C2 setup)

### Sub-Techniques


## Commands Used

- [[commands/ssh-login-to-vps]]

## Tools Used


## Tags

- setup
- vps
- reverse-shell
