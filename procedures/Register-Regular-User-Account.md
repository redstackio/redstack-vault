---
tags:
  - graphql
  - user-creation
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-register-user]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T17:25:59.701Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 667d360a-e119-46a6-baa9-a8ab5cdc738c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Register-Regular-User-Account

## Summary

This procedure uses the GraphQL Register mutation to create a standard user account, obtaining an authentication token for subsequent API interactions in an e-commerce application.

## Description

Following schema enumeration, the Register mutation allows unauthenticated user creation. In the target API at https://tng-api.watsons.com.my, this grants access to authenticated features without robust validation, setting the stage for escalation. The procedure involves crafting a mutation with email and password inputs, expecting a token in response for session-based auth.

## Requirements

1. Valid GraphQL endpoint from prior enumeration
2. Unique email and password for registration
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Enforce CAPTCHA or email verification on registration
- Rate limit mutation calls to prevent abuse
- Log and alert on rapid account creations

## Objectives

1. Gain initial authenticated access
2. Obtain session token
3. Enable further API usage

## Instructions

### Step 1: Execute Register Mutation

**Context**: Submit user details via GraphQL to create the account.

**Command** ([[commands/graphql-register-user]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "mutation { register(input: {email: \"test@example.com\", password: \"password123\"}) { user { id email } token } }"}'
```

> Successful response: {"data":{"register":{"user":{"id":"123","email":"test@example.com"},"token":"eyJ..."}}}

### Step 2: Verify Account Access

**Context**: Use the token to query a protected field, confirming authentication.

**Command** ([[commands/graphql-register-user]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -H "Authorization: Bearer eyJ..." -d '{"query": "{ me { id role } }"}'
```

> Expect user details with regular role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Create Account]]

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-register-user]]

## Tools Used

- None

## Tags

- [[graphql]]
- [[user-creation]]
- [[initial-access]]
