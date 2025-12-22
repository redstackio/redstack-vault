---
id: proc-8x8-impersonation-test-001
tags:
  - access-control-bypass
  - admin-impersonation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-post-invite]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:47.044Z'
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
# Test Invite Sending on Behalf of Another Admin

## Summary

This procedure tests the improper access control in 8x8 Connect by attempting to send an invite using another admin's User ID, confirming the vulnerability allows actions restricted to the target user.

## Description

Authenticated as one admin, the attacker modifies the API request to target /api/v1/users/<Other Admin ID>/invites. The platform fails to validate that the acting user matches the target ID, permitting the invite to proceed. This demonstrates horizontal privilege escalation between admins. Prerequisites include obtaining another admin's User ID (e.g., via enumeration or known values). Success leads to unauthorized invites, paving the way for escalation.

## Requirements

1. Admin authentication token
2. Knowledge of another admin's User ID
3. HTTP client for API requests

## Defense

Defensive measures and detection strategies:

- Add user ID validation in API handlers to ensure acting user == target user
- Monitor for cross-User ID API calls in logs
- Use role-based access control (RBAC) with fine-grained permissions

## Objectives

1. Bypass authorization for another admin's actions
2. Confirm invite functionality without restrictions
3. Identify potential for broader exploitation

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain and set the admin Bearer token for requests.

Log in to 8x8 Connect and extract the token from session storage or headers.

### Step 2: Execute Impersonated Invite

**Context**: Send the POST request targeting the other admin's ID to test bypass.

Execute [[commands/curl-post-invite]] with the other admin's ID:

```bash
curl -X POST https://connect.8x8.com/api/v1/users/<Other Admin ID>/invites \
  -H "Authorization: Bearer <your-admin-token>" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "role": "admin"}'
```

> The command sends invite details; expect a 200 response if vulnerable.

**Expected Output**: JSON response confirming invite creation, e.g., {"status": "sent"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/curl-post-invite]]

## Tools Used


## Tags

- [[access-control-bypass]]
- [[admin-impersonation]]
