---
tags:
  - graphql-query
  - domain-enum
  - shopify-plus
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/graphql-query-organization-domains]]'
platforms:
  - Web
  - Shopify Plus
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0a0f0fef-ecfc-4053-9789-7ea423fc5625
created_at: '2025-12-14T17:29:20.186Z'
updated_at: '2025-12-14T17:29:20.186Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Query-Organization-Domains-for-ID

## Summary

This procedure uses a low-privileged account to query organization domains via Shopify Plus GraphQL API, retrieving IDs for subsequent unauthorized actions.

## Description

Exploiting insufficient permission checks, the Store Management user queries the organization's domains. This step intercepts a standard API request and modifies it to fetch domain IDs. Target: /stores/api endpoint; prerequisites: active low-priv session.

## Requirements

1. Active low-priv session token
2. Intercepting proxy (e.g., Burp) for request modification
3. Organization ID (e.g., 34946971)

## Defense

Defensive measures and detection strategies:

- Implement field-level authorization in GraphQL resolvers
- Rate-limit and log sensitive queries like organization domains
- Audit API access for low-priv users querying admin data

## Objectives

1. Extract domain IDs without permission denial
2. Identify targets for SAML enforcement
3. Demonstrate info disclosure via auth bypass

## Instructions

### Step 1: Intercept API Request

**Context**: Capture a POST to the stores/api endpoint during normal navigation.

**Command** (Proxy Setup):

Use Burp or similar to intercept requests to https://shopify.plus/:org_id/stores/api.

> Send to repeater and modify payload.

### Step 2: Execute GraphQL Query

**Context**: Query for organization domains to get IDs.

**Command** ([[commands/graphql-query-organization-domains]]):
```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"query{organization{domains{id}}}"}'
```

> This sends a GraphQL query; expected output: JSON with domain IDs, e.g., {"data":{"organization":{"domains":[{"id":"gid://shopify/OrganizationDomain/123"}]}}}. No userErrors indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-organization-domains]]

## Tools Used


## Tags

- [[graphql-query]]
- [[domain-enum]]
