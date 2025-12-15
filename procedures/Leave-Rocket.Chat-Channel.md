---
tags:
  - rocket.chat
  - channel-leave
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-leavechannel-rocket-chat]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:25:47.404Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: c5c178da-2332-46e5-8ccd-ea755ae3ef4e
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Leave-Rocket.Chat-Channel

## Summary

This procedure removes the user from a Rocket.Chat channel, simulating departure or ban to test post-membership access, removing direct UI controls like delete options.

## Description

Part of the IDOR exploitation chain, leaving the channel ensures the user lacks permissions, highlighting the API's failure to validate membership. Targets the leaveRoom method; outcomes include loss of channel visibility and no UI delete access.

## Requirements

1. Authenticated session in the target channel
2. Room ID (rid)
3. Access to /api/v1/method.call

## Defense

Defensive measures and detection strategies:

- Enforce strict permission checks on leaveRoom to log exits
- Alert on rapid join/leave patterns
- Audit channel membership changes

## Objectives

1. Simulate user ban or voluntary exit
2. Remove direct access to channel messages
3. Set up for unauthorized API actions

## Instructions

### Step 1: Invoke Leave Room

**Context**: Use API or UI to exit the channel.

**Command** ([[commands/curl-leavechannel-rocket-chat]]):
```bash
curl -X POST -H "X-Auth-Token: YOUR_AUTH_TOKEN" -H "X-User-Id: YOUR_USER_ID" -H "Content-Type: application/json" https://rocket-chat.example.com/api/v1/method.call -d '{"msg":"method","method":"leaveRoom","params":[{"rid":"TARGET_ROOM_ID"}],"id":"unique_id_2"}'
```

> Response: {"success": true}. Channel disappears from user's list.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used

- [[commands/curl-leavechannel-rocket-chat]]

## Tools Used


## Tags

- [[rocket.chat]]
- [[channel-management]]
