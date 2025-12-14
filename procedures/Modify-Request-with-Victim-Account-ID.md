---
tags:
  - request-modification
  - idor
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/expire-user-sessions-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.800Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 3a8002bc-ff90-4e19-9de5-53ded3f34761
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-with-Victim-Account-ID

## Summary

This procedure tampers with the captured HTTP request by replacing the account ID with the victim's, enabling the IDOR exploitation to target unauthorized sessions.

## Description

The core of the IDOR vulnerability lies in the lack of authorization checks on the account ID parameter. By editing the request path in a proxy tool, the attacker redirects the session expiration to any target account, bypassing access controls.

## Requirements

1. Captured baseline request from previous step
2. Known victim account ID (e.g., obtained via enumeration or prior recon)
3. Proxy tool for editing (e.g., [[tools/Burp-Suite]])

## Defense

Defensive measures and detection strategies:

- Validate that the requesting user's ID matches the targeted account ID on all admin endpoints
- Log and alert on requests where account IDs mismatch
- Implement proper access control lists (ACLs) for object references

## Objectives

1. Replace attacker ID with victim ID in request path
2. Preserve other parameters like authenticity token
3. Prepare request for server submission

## Instructions

### Step 1: Edit URL Path

**Context**: Locate and modify the account ID in the request URL.

In Burp Repeater, change /admin/settings/account/expire_specific_users_sessions/{attacker_id} to /{victim_id}.

> Example: Replace 7641433 with victim's ID like 1234567.

### Step 2: Verify Parameters

**Context**: Ensure the request body and headers remain valid.

Confirm params: utf8=%E2%9C%93&_method=patch&authenticity_token={token}. Optionally simulate with [[commands/expire-user-sessions-curl]]:

```bash
curl -X POST 'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/1234567' \
  -H 'Cookie: _shopify_s=session_token' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=abc123'
```

> Expected output: Request formatted correctly without syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/expire-user-sessions-curl]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-modification]]
- [[idor]]
- [[shopify]]
