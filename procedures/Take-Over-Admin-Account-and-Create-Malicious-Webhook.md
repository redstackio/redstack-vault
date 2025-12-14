---
tags:
  - admin-takeover
  - webhook-rce
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Lateral Movement]]'
  - '[[Execution]]'
commands:
  - '[[commands/python3-post-auth-nosqli]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Domain Accounts]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:14.816Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: 64966dd9-5fcc-432a-ae95-3e9f23d80b1f
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Domain Accounts]]'
  - '[[JavaScript]]'
---
# Take-Over-Admin-Account-and-Create-Malicious-Webhook

## Summary

This procedure logs in as the compromised admin and creates an incoming webhook configured to execute arbitrary JavaScript code on the server.

## Description

With admin creds, POST to /api/v1/integrations.create with a script payload (e.g., spawning a shell) sets up an unsandboxed webhook. The feature runs JS in the Node.js process context. Outcome: Webhook ready for RCE triggers.

## Requirements

1. Admin credentials from takeover
2. Access to integrations API
3. Malicious JS payload prepared

## Defense

Defensive measures and detection strategies:

- Sandbox webhook scripts or disable JS execution
- Review and approve all incoming integrations
- Monitor for webhook creation by admins
- Restrict script capabilities in webhooks

## Objectives

1. Establish admin control
2. Deploy RCE vector
3. Enable command execution

## Instructions

### Step 1: Create Malicious Webhook

**Context**: As admin, configure webhook with RCE script.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script authenticates as admin and creates webhook. Expected output: Webhook URL and ID for triggering.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]
- [[Execution]]

### Techniques

- [[Domain Accounts]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- admin-takeover
- webhook-rce
