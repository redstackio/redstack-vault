---
id: proc-dust-read-unauth-001
tags:
  - broken-access-control
  - data-exfiltration
  - dust-tt
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-dust-read-conversation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.892Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Read-Unauthorized-Conversation

## Summary

This procedure exploits the lack of server-side ownership verification in Dust.tt's conversation API to read private details of any conversation in the workspace, including messages and metadata.

## Description

The GET /api/w/<Workspace-id>/assistant/conversations/<conversation-id> endpoint fails to check if the requester owns the conversation, allowing any authenticated user to retrieve sensitive data like owner info, title, visibility, and content. This compromises confidentiality for all workspace members.

## Requirements

1. Authenticated session token from Dust.tt login
2. Valid workspace ID and target conversation ID
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Implement server-side permission checks verifying user ownership or role
- Log all conversation access attempts and alert on cross-user reads
- Use role-based access control (RBAC) for API endpoints

## Objectives

1. Retrieve unauthorized conversation data
2. Confirm lack of access controls
3. Exfiltrate private messages and metadata

## Instructions

### Step 1: Prepare API Request

**Context**: Construct the GET request with authentication headers.

Ensure you have the session token and IDs; replace placeholders in the command.

### Step 2: Execute Read Request

**Context**: Send the request to fetch conversation details.

**Command** ([[commands/curl-dust-read-conversation]]):
```bash
curl -X GET "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json"
```

> This command retrieves the full conversation object. Expected output: JSON with fields like {"conversation": {"id": 123, "sId": "conv_abc123", "owner": {...}, "title": "Private Admin Chat", "visibility": "private", ... }}. Success if data from non-owned conversation is returned without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

-

## Commands Used

- [[commands/curl-dust-read-conversation]]

## Tools Used

-

## Tags

- [[broken-access-control]]
- [[dust-tt]]
