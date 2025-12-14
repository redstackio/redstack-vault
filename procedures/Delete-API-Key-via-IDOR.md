---
tags:
  - idor-delete
  - credential-tampering
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-delete-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.041Z'
sub_techniques: []
id: 0ef385ad-0055-48b4-9485-34b0fc392333
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Delete-API-Key-via-IDOR

## Summary

Exploit IDOR to delete a private API key using the attacker's session, demonstrating destructive access.

## Description

Send a DELETE request to the API key endpoint with the target's API-UUID and attacker's cookies, succeeding due to missing authorization verification.

## Requirements

1. Attacker session cookies
2. ORG-UUID and API-UUID known
3. Ability to send HTTP requests (browser or curl)

## Defense

Defensive measures and detection strategies:

- Validate user permissions on DELETE operations
- Audit destructive actions with alerts
- Implement idempotency checks for key operations

## Objectives

1. Remove unauthorized key
2. Confirm no ownership check
3. Assess impact on organization

## Instructions

### Step 1: Prepare Request

**Context**: Gather identifiers.

Use copied API-UUID from view step.

> Expected: Valid UUID ready.

### Step 2: Send DELETE

**Context**: Execute removal.

Use browser console or tool to send request.

Execute [[commands/curl-delete-api-key]]:

```bash
curl -X DELETE https://target-platform.com/organization/ORG-UUID/apiKeys/API-UUID -H "Cookie: session=attacker_session_cookie" -H "Authorization: Bearer attacker_token"
```

> Expected: 200 OK, key deleted.

### Step 3: Verify Deletion

**Context**: Check list.

Re-access endpoint to confirm absence.

> Expected: Key no longer visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-api-key]]

## Tools Used


## Tags

- idor-delete
- credential-tampering
