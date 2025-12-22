---
tags:
  - graphql
  - api-discovery
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/graphql-team-policy-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.183Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 208d9621-d5c2-46c8-855c-6a4b32c8b7ca
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover-GraphQL-Policy-Field

## Summary

This procedure identifies the 'policy_markdown_html' field in HackerOne's GraphQL API schema, introduced on May 19, 2020, enabling subsequent enumeration of team policies for information disclosure.

## Description

In the context of reconnaissance against HackerOne-hosted bug bounty programs, this step involves monitoring API changes or performing schema introspection to detect new fields that may expose sensitive data. The field in question lacks proper access controls, allowing unauthenticated queries to reveal internal policies. Prerequisites include access to the public GraphQL endpoint and knowledge of GraphQL querying basics. Expected outcomes include confirmation of field availability, setting the stage for targeted queries.

## Requirements

1. Public internet access to HackerOne API
2. GraphQL client or tool like curl for schema introspection
3. Awareness of API change timelines (e.g., field intro date)

## Defense

Defensive measures and detection strategies:

- Implement GraphQL schema introspection limits or disable for unauthenticated users
- Monitor API query logs for unusual field accesses
- Regularly audit new fields for access control enforcement

## Objectives

1. Confirm presence of vulnerable field in GraphQL schema
2. Document introduction date for historical context
3. Prepare for policy enumeration queries

## Instructions

### Step 1: Introspect GraphQL Schema

**Context**: Use GraphQL introspection to query the schema and identify the 'policy_markdown_html' field on the Team type.

**Command** ([[commands/graphql-introspect-schema]]):
```graphql
query IntrospectionQuery { __schema { types { name fields { name } } } }
```

> This query returns the schema structure; search for 'Team' type and 'policy_markdown_html' field. Expected output: JSON with field listed under Team.

### Step 2: Test Basic Team Query

**Context**: Send a simple team query to verify field responsiveness.

**Command** ([[commands/graphql-team-policy-query]]):
```graphql
query { team(handle:"example") { name } }
```

> Extend to include policy_markdown_html once confirmed. Expected output: Basic team data, confirming endpoint accessibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-team-policy-query]]

## Tools Used

- None

## Tags

- [[graphql]]
- [[api-discovery]]
- [[Reconnaissance]]
