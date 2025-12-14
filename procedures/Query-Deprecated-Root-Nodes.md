---
id: proc-query-deprecated-nodes
tags:
  - graphql
  - deprecated-query
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/query-deprecated-team-node]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:53.440Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Query-Deprecated-Root-Nodes

## Summary

This procedure crafts and executes GraphQL queries using deprecated root-level nodes to access unintended data, such as team details including internal IDs and metrics, despite deprecation flags.

## Description

Deprecated nodes in GraphQL schemas are flagged but often remain queryable if resolvers are not removed, leading to violations of secure design. Targeting HackerOne's 'team' node with a handle like 'security' exposes fields like _id (database PK), about, base_bounty, and bug_count. Prerequisites: Schema knowledge and HTTP client. Outcomes: Disclosure of sensitive entity data not meant for public access.

## Requirements

1. Knowledge of deprecated node names from schema analysis
2. Specific arguments like 'handle' for the node
3. Access to the GraphQL endpoint

## Defense

Defensive measures and detection strategies:

- Remove or restrict resolvers for deprecated fields in the schema
- Implement query validation to block deprecated root usage
- Audit logs for queries targeting deprecated nodes

## Objectives

1. Access data via deprecated entry points
2. Exfiltrate entity details like team info
3. Demonstrate design principle violations

## Instructions

### Step 1: Construct Query for Team Node

**Context**: Build a query using the deprecated 'team' root node with a known handle.

**Command** ([[commands/query-deprecated-team-node]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,_id,about,base_bounty,bug_count}}"}' -o team_data.json
```

> Retrieves team data; expected output includes id, _id (e.g., "13"), about text, bounty, and bug count.

### Step 2: Parse and Verify Data

**Context**: Inspect the response for leaked internal fields.

**Command** (jq extract):
```bash
jq '.data.team' team_data.json
```

> Confirms exposure of sensitive fields like _id.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/query-deprecated-team-node]]

## Tools Used

- None

## Tags

- deprecated-node
- graphql-query
- entity-leak
