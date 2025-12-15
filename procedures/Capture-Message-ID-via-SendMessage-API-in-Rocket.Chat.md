---
tags:
  - rocket.chat
  - api
  - message-id
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
updated_at: '2025-12-14T17:25:47.410Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 0d65651c-d15f-43e4-a09c-cad6ee30fbf3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Message-ID-via-SendMessage-API-in-Rocket.Chat

## Summary

This procedure sends a message to a Rocket.Chat channel using the sendMessage API and captures the resulting unique message ID from the response, which is essential for targeting in subsequent IDOR exploitation.

## Description

In the context of exploiting IDOR in Rocket.Chat, this step establishes the target by posting a message and extracting its ID. The procedure assumes an authenticated session and targets a specific room ID. Expected outcome is a valid message ID that can be used to reference the object directly via API without proper authorization checks later.

## Requirements

1. Authenticated Rocket.Chat session with channel join permissions (X-Auth-Token and X-User-Id headers)
2. Target room ID (rid) for the channel
3. API access to /api/v1/method.call endpoint
4. Tool like curl or Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on sendMessage API to prevent abuse
- Log all message creations with user IDs for audit trails
- Monitor for unusual message patterns from authenticated users

## Objectives

1. Create a traceable message in the target channel
2. Extract the message ID for IDOR targeting
3. Prepare for post-departure deletion

## Instructions

### Step 1: Authenticate and Prepare Request

**Context**: Ensure valid authentication tokens and identify the target room ID via Rocket.Chat UI or API.

No command needed; obtain tokens from login response.

### Step 2: Send Message and Capture ID

**Context**: Use the sendMessage method to post a test message and parse the response for the ID.

**Command** ([[commands/curl-sendmessage-rocket-chat]]):
```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"sendMessage","params":[{"rid":"TARGET_ROOM_ID","msg":"Test message for ID capture"}],"id":"unique_id_1"}'
```

> This command sends a JSON payload invoking sendMessage. The response includes {"msg": "result", "result": {"_id": "CZZqd6rMsiqbsqa9h"}}, where _id is the message ID. Use jq or similar to extract it.

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

- [[rocket.chat]]
- [[api]]
- [[message-capture]]
