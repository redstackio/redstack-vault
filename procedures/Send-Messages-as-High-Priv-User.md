---
tags:
  - impersonation
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/post-kitcrm-send-message]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b4e7cce9-1ecd-453d-afcb-33708613921b
created_at: '2025-12-14T17:29:57.263Z'
updated_at: '2025-12-14T17:29:57.263Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Send-Messages-as-High-Priv-User

## Summary

This procedure impersonates the high-privileged user by sending new messages/instructions to KIT using the stolen token, executing actions on their behalf.

## Description

POST to /api/v2/messages with the token allows arbitrary instructions. Target: KITCRM API. Prerequisites: High-priv token. Outcome: Actions performed as high-priv, difficult attribution.

## Requirements

1. High-priv KITCRM Bearer token
2. Message content to send
3. HTTP client

## Defense

Defensive measures and detection strategies:

- Multi-factor for token actions
- Behavioral analytics on message patterns
- Attribution logging

## Objectives

1. Send test instruction
2. Confirm execution as high-priv
3. Demonstrate full compromise

## Instructions

### Step 1: Send POST Request

**Context**: Inject message with token.

**Command** ([[commands/post-kitcrm-send-message]]):
```bash
curl -X POST "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"incoming_message": "testtesthai"}'
```

> Expected output: Success response, message in history.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/post-kitcrm-send-message]]

## Tools Used


## Tags

- [[impersonation]]
- [[command-injection]]
