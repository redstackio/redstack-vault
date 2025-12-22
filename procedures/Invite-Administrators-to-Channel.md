---
tags:
  - lateral-movement
  - social-engineering
  - admin-invite
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Internal Proxy]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d0d410f7-7859-4a1d-9a14-d282a8941d6a
created_at: '2025-12-14T03:47:13.123Z'
updated_at: '2025-12-14T03:47:13.123Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Internal Proxy]]'
---
# Invite-Administrators-to-Channel

## Summary

This procedure adds administrator users to the test channel to ensure they view the malicious XSS payload, using social lures like promising 'yummy cookies'.

## Description

Targeting admins increases impact by exposing high-privilege sessions to XSS. Invites can be direct via UI or API, often paired with enticing messages. This step relies on social engineering for views. Outcome: Admins join and interact, triggering the payload.

## Requirements

1. Access to the created channel
2. Knowledge of admin usernames or IDs
3. Permissions to invite users (channel membership)

## Defense

Defensive measures and detection strategies:

- Alert on invites to high-privilege users in new channels
- Train admins on suspicious invites (e.g., themed lures)
- Enable invite approvals or notifications for sensitive channels

## Objectives

1. Expose admin sessions to the stored XSS
2. Facilitate cookie theft from privileged accounts
3. Enable wormable spread if admins forward messages

## Instructions

### Step 1: Direct Invite via UI

**Context**: Use the channel settings to add admins.

1. Open the '#cookies' channel.
2. Click channel info > Members > Add Members.
3. Search and select admin users.
4. Optionally, send a lure message: "Come get some yummy cookies!"

> Admins receive invite notification.

### Step 2: API Invite

**Context**: Bulk invite via API for efficiency.

```bash
curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/channels.invite -d '{"roomName": "cookies", "userName": "admin1,admin2"}'
```

> Expected output: {"success": true}.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Internal Proxy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[lateral-movement]]
- [[social-engineering]]
- [[admin-invite]]
