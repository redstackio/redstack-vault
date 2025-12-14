---
tags:
  - rocket.chat
  - request-interception
  - api
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sendmessage-rocket-chat]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.401Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: eacb022e-31b4-44c3-ad94-be7fabb48278
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-DeleteMessage-Request-Structure-in-Rocket.Chat

## Summary

This procedure involves sending and deleting a message in an accessible channel to intercept the deleteMessage API request structure, providing a template for IDOR modification.

## Description

To bypass direct access, capture a legitimate delete request from another channel using proxy tools. This reveals the JSON payload format for deleteMessage, including the 'id' parameter, which lacks proper validation in the vulnerable endpoint.

## Requirements

1. Access to a different channel with delete permissions
2. Interception tool like Burp Suite
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Proxy all API traffic for anomaly detection
- Validate request origins beyond auth tokens
- Log delete attempts with message IDs

## Objectives

1. Obtain valid deleteMessage payload template
2. Identify modifiable parameters like 'id'
3. Enable IDOR exploitation

## Instructions

### Step 1: Send Test Message in Alternate Channel

**Context**: Post a message to capture later.

**Command** ([[commands/curl-sendmessage-rocket-chat]]):
```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"sendMessage","params":[{"rid":"ALTERNATE_ROOM_ID","msg":"Test for delete capture"}],"id":"unique_id_4"}'
```

> Extract test message ID from response.

### Step 2: Delete and Intercept

**Context**: Delete via UI and capture request in Burp.

Use Burp to proxy the delete action; note the payload: {"method": "deleteMessage", "params": [{"_id": "test_id"}] }.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-sendmessage-rocket-chat]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-capture]]
- [[api-interception]]
