---
tags:
  - rocket.chat
  - verification
  - deletion-check
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-getmessages-rocket-chat]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software Discovery]]'
updated_at: '2025-12-14T17:25:47.393Z'
skill_level: beginner
impact_level: medium
sub_techniques: []
id: 438d306d-14fd-4e22-bf30-ea524dbf2c85
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Software Discovery]]'
---
# Verify-Message-Deletion-in-Rocket.Chat

## Summary

This procedure confirms the successful deletion of the target message from the channel history, validating the IDOR exploitation by checking via UI or API.

## Description

Post-exploitation, verify erasure to ensure evidence tampering. Use admin access or API to fetch recent messages; absence of the ID confirms impact on audit trails.

## Requirements

1. Admin or viewer access to the target channel
2. Room ID
3. Optional: API tokens for message retrieval

## Defense

Defensive measures and detection strategies:

- Immutable logging for message deletions
- Alerts on deleted messages from non-members
- Regular audit of channel histories

## Objectives

1. Confirm message removal
2. Validate evasion success
3. Assess moderation impact

## Instructions

### Step 1: Check Channel UI

**Context**: Log in as admin and view the channel.

Refresh the target channel; target message should be absent.

### Step 2: API Verification

**Context**: Query messages to ensure ID is gone.

**Command** ([[commands/curl-getmessages-rocket-chat]]):
```bash
curl -X GET -H "X-Auth-Token: ADMIN_AUTH_TOKEN" -H "X-User-Id: ADMIN_USER_ID" https://rocket-chat.example.com/api/v1/channels.messages?roomId=TARGET_ROOM_ID&count=50
```

> Response JSON lists messages; search for target ID - it should not appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Software Discovery]] Software Discovery (verifying changes)

### Sub-Techniques


## Commands Used

- [[commands/curl-getmessages-rocket-chat]]

## Tools Used


## Tags

- [[verification]]
- [[audit-tampering]]
