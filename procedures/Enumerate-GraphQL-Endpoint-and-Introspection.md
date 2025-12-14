---
tags:
  - graphql
  - introspection
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/graphql-introspect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:59.706Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 29f40697-0faa-4eec-b816-3983b27a9bb2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-GraphQL-Endpoint-and-Introspection

## Summary

This procedure discovers a GraphQL API endpoint and uses introspection to reveal the full schema, including all available queries and mutations, enabling attackers to map out the API without authentication.

## Description

In scenarios where GraphQL introspection is enabled on public-facing APIs, attackers can query the __schema type to extract detailed information about the API structure. This was exploited on https://tng-api.watsons.com.my, exposing mutations like Register and CreateAdminUser. The procedure assumes HTTP access and uses standard tools to send GraphQL queries, providing a foundation for further exploitation in e-commerce or web applications.

## Requirements

1. Network access to the target URL (e.g., https://tng-api.watsons.com.my/graphql)
2. HTTP client like curl
3. Basic knowledge of GraphQL query syntax

## Defense

Defensive measures and detection strategies:

- Disable GraphQL introspection in production (set query depth limits or remove __schema)
- Implement rate limiting on API endpoints to detect enumeration attempts
- Monitor for unusual GraphQL queries in logs

## Objectives

1. Identify the GraphQL endpoint
2. Extract schema details for attack planning
3. Confirm exposure of sensitive mutations

## Instructions

### Step 1: Probe for GraphQL Endpoint

**Context**: Send a basic POST request to test if /graphql responds with a valid GraphQL server.

**Command** ([[commands/graphql-introspect]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "query { __typename }"}'
```

> This returns the typename if GraphQL is present; expect {"data":{"__typename":"Query"}} on success.

### Step 2: Perform Full Introspection

**Context**: Query the schema to list all types, queries, and mutations.

**Command** ([[commands/graphql-introspect]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "query { __schema { queryType { name } mutationType { name } types { name description } } }"}'
```

> Output includes array of types, revealing endpoints like Register and CreateAdminUser.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-introspect]]

## Tools Used

- None

## Tags

- [[graphql]]
- [[introspection]]
- [[recon]]
