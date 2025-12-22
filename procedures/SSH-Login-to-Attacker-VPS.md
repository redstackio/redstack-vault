---
id: proc-ssh-vps-login
tags:
  - ssh
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ssh-login-to-vps]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:23:49.661Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# SSH-Login-to-Attacker-VPS

## Summary

This procedure establishes SSH access to an attacker-controlled VPS to prepare the environment for hosting exploit tools like a rogue LDAP server.

## Description

In the context of the Debezium JNDI injection attack, logging into the VPS is the initial step to set up the malicious infrastructure. It requires pre-configured SSH credentials and assumes the VPS is reachable over the internet. Successful login provides a shell for subsequent exploit preparation, enabling the hosting of RogueJndi and netcat listener.

## Requirements

1. SSH client installed on attacker's local machine
2. Valid credentials (hostname and password/key) for the VPS
3. Network connectivity to the VPS IP

## Defense

Defensive measures and detection strategies:

- Monitor SSH logs for unusual login attempts from unknown IPs
- Use key-based authentication and disable password auth
- Implement fail2ban or similar to block brute-force attempts

## Objectives

1. Gain shell access to VPS for exploit setup
2. Prepare environment for rogue server hosting
3. Verify VPS readiness for reverse shell listener

## Instructions

### Step 1: Execute SSH Login

**Context**: Connect to the VPS to access the shell for running exploit tools.

**Command** ([[commands/ssh-login-to-vps]]):
```bash
ssh ███████
```

> This command initiates an SSH session to the redacted VPS hostname using provided credentials. Expected output includes a successful authentication and prompt like `user@hostname:~$`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/ssh-login-to-vps]]

## Tools Used


## Tags

- ssh
- initial-access
