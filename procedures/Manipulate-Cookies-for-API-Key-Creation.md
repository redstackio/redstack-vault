---
tags:
  - cookie-manipulation
  - idor-create
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-create-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:25:23.027Z'
sub_techniques: []
id: 549835da-8df6-4fce-88bf-7c3fa705f9e6
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
---
# Manipulate-Cookies-for-API-Key-Creation

## Summary

Replay the API key creation request with attacker's cookies to unauthorizedly create new keys via IDOR.

## Description

Extract attacker's session cookies, substitute them into the saved victim creation request, and resubmit to bypass ownership checks and add keys under the organization.

## Requirements

1. Saved 'Create_Req' from victim session
2. Attacker cookies extracted (dev tools)
3. ORG-UUID

## Defense

Defensive measures and detection strategies:

- Bind requests to user context (e.g., via JWT claims)
- Detect cookie tampering with integrity checks
- Log creation with source IP/user ID

## Objectives

1. Create key as unauthorized user
2. Demonstrate full manipulation
3. Enable potential persistence

## Instructions

### Step 1: Extract Cookies

**Context**: Get attacker session data.

Log in as attacker, open dev tools, copy Cookie header.

> Expected: Session cookie string.

### Step 2: Modify Request

**Context**: Swap authentication.

Edit 'Create_Req' to replace victim cookies with attacker's.

> Expected: Updated POST body ready.

### Step 3: Resubmit

**Context**: Trigger creation.

Send modified request.

Execute [[commands/curl-create-api-key]] with new cookies:

```bash
curl -X POST https://target-platform.com/organization/ORG-UUID/apiKeys -H "Cookie: session=attacker_session_cookie" -d '{"name":"Malicious Key","scopes":["full_access"] }'
```

> Expected: New key created.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used

- [[commands/curl-create-api-key]]

## Tools Used


## Tags

- cookie-manipulation
- idor-create
