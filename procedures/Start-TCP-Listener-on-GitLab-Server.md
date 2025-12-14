---
tags:
  - listener
  - ssrf
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/nc-listen-9999]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 064bab4b-ea19-42a8-ab20-f6cd64511228
created_at: '2025-12-14T03:46:09.474Z'
updated_at: '2025-12-14T03:46:09.474Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-TCP-Listener-on-GitLab-Server

## Summary

Deploys a netcat listener on the GitLab server to capture SSRF connections post-exploitation.

## Description

This captures incoming requests from the webhook when the ToCToU race resolves to localhost. Requires server access; runs on port 9999 to match webhook URL.

## Requirements

1. SSH access to GitLab server
2. Netcat installed
3. Port 9999 available

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized listeners on internal ports
- Firewall rules to block non-standard listeners

## Objectives

1. Receive SSRF payloads
2. Confirm exploitation success
3. Read internal responses

## Instructions

### Step 1: Access Server

**Context**: SSH into GitLab host.

**Command** (SSH):
```bash
ssh user@gitlab-server
```

> Gain shell access.

### Step 2: Start Listener

**Context**: Initiate TCP listener for incoming connections.

**Command** ([[commands/nc-listen-9999]]):
```bash
nc -vvn -l -p 9999
```

> Expected output: 'Listening on [0.0.0.0] (family 0, port 9999)'. Connection shows source from GitLab process.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-9999]]

## Tools Used

- [[tools/nc]]

## Tags

- [[listener]]
- [[tcp]]
