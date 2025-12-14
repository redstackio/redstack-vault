---
tags:
  - information-disclosure
  - graphql-query
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-team-policy-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:26:00.178Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ab34aeb6-0613-48a6-a49e-333a9ab6102d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Query-Team-Policy-Endpoint

## Summary

This procedure executes a GraphQL query against HackerOne's API to fetch the 'policy_markdown_html' field for a specified team, disclosing policy content that may reveal private configurations.

## Description

Targeting the unauthenticated GraphQL endpoint, this involves crafting and sending queries with team handles to retrieve policy HTML. The vulnerability stems from missing authorization checks, allowing external access to internal policies. Use cases include reconnaissance on bug bounty programs. Prerequisites: Valid team handle and HTTP client. Outcomes: Policy disclosure aiding in program targeting.

## Requirements

1. Team handle (e.g., 'example' for testing)
2. Access to POST requests to https://api.hackerone.com/graphql
3. JSON payload handling for GraphQL

## Defense

Defensive measures and detection strategies:

- Enforce authentication on sensitive GraphQL fields
- Rate-limit API queries by IP
- Log and alert on policy field accesses

## Objectives

1. Retrieve team policy HTML via GraphQL
2. Expose differences in public vs. private policies
3. Gather data for further reconnaissance

## Instructions

### Step 1: Prepare GraphQL Query

**Context**: Construct the query specifying the team handle and desired fields.

**Command** ([[commands/graphql-team-policy-query]]):
```graphql
query { team(handle:"example") { name policy_markdown_html } }
```

> Send via POST with Content-Type: application/json. Expected output: {"data":{"team":{"name":"example test","policy_markdown_html":"<html content>"}}}

### Step 2: Execute Query Multiple Times

**Context**: Repeat for various handles to map policies.

**Command** ([[commands/graphql-team-policy-query]]):
```graphql
query { team(handle:"targetteam") { name policy_markdown_html } }
```

> Vary the handle parameter. Expected output: Policy variations or null based on team status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Org Information

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-team-policy-query]]

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[graphql-query]]
