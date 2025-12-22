---
id: proc-prepare-graphql-client
tags:
  - graphql
  - api-setup
  - hackerone
type: procedure
tools:
  - '[[tools/GraphQL-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/basic-graphql-me-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.565Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare GraphQL Client for HackerOne API

## Summary

This procedure sets up a GraphQL client to interact with the HackerOne API, enabling the execution of custom queries for vulnerability testing, specifically targeting endpoints like opportunities_search.

## Description

In the context of testing GraphQL APIs for access control issues, preparing a client involves configuring authentication and endpoint details. The HackerOne GraphQL API is public-facing but may require session-based auth for full access. This step ensures readiness for sending aggregation queries that could expose private data due to unfiltered 'aggs' handling. Prerequisites include a HackerOne account for authentication.

## Requirements

1. Access to a GraphQL client tool (e.g., Insomnia, Postman, or curl).
2. HackerOne account credentials or API token for authentication.
3. Network connectivity to https://api.hackerone.com/graphql.

## Defense

Defensive measures and detection strategies:

- Implement API gateway rate limiting to detect anomalous query patterns.
- Log all GraphQL queries and monitor for aggregation usage on sensitive fields.
- Enforce schema-level access controls to restrict 'aggs' based on user permissions.

## Objectives

1. Establish authenticated connection to the GraphQL endpoint.
2. Verify basic query functionality.
3. Prepare for advanced aggregation queries.

## Instructions

### Step 1: Install and Configure Client

**Context**: Select and set up the GraphQL client, configuring the base URL and auth headers.

**Command** ([[commands/basic-graphql-me-query]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_HACKERONE_TOKEN" \
  -d '{"query": "query { me { id } }"}'
```

> This command tests the connection by querying the current user's ID. Expected output: {"data":{"me":{"id":"123"}}} or null if unauthenticated. Replace YOUR_HACKERONE_TOKEN with a valid token obtained from HackerOne settings.

### Step 2: Verify Endpoint Accessibility

**Context**: Confirm the client can reach the opportunities_search endpoint with a simple query.

**Command** ([[commands/basic-graphql-me-query]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { opportunities_search(query:{}) { edges { node { handle } } } }"}'
```

> Run without auth to check public access. Expected output: Limited public results. Success confirms endpoint is reachable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/basic-graphql-me-query]]

## Tools Used

- [[tools/GraphQL-Client]]

## Tags

- graphql
- api-setup
