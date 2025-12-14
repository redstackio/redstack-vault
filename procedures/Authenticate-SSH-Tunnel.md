---
id: proc-auth-ssh-tunnel
tags:
  - ssh
  - authentication
  - tunnel
type: procedure
tools:
  - '[[tools/SSH]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:57.738Z'
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---
# Authenticate-SSH-Tunnel

## Summary

This procedure completes the SSH tunnel authentication using the attacker's credentials, ensuring the port forward remains active.

## Description

Upon executing the SSH command from the container, password or key authentication is required. Successful auth establishes the tunnel, allowing access to the Docker Registry via the external endpoint even if the initial shell terminates.

## Requirements

1. SSH tunnel command initiated
2. Valid credentials for 'attacker' user on SSH server
3. No auth timeouts in container

## Defense

Defensive measures and detection strategies:

- Enforce key-based auth with restrictions
- Log and alert on SSH auth from unexpected sources
- Disable password auth in SSH configs

## Objectives

1. Secure the tunnel connection
2. Maintain persistence post-shell
3. Validate tunnel functionality

## Instructions

### Step 1: Provide Credentials

**Context**: Respond to SSH prompt in the reverse shell.

No command; enter password when prompted.

> Expected: 'Authentication successful' or direct tunnel activation without errors.

### Step 2: Test Tunnel

**Context**: Verify port forwarding works.

From attacker's machine, use netcat or curl to probe localhost:5555.

> Expected: Connection to registry API, e.g., curl http://127.0.0.1:5555/v2/ returns {} or catalog.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used

- [[tools/SSH]]

## Tags

- authentication

---
