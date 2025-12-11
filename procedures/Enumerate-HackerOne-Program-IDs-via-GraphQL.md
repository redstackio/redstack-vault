---
tags:
  - enumeration
  - graphql
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-asset-group-name]]'
  - '[[commands/graphql-query-asset-group-details]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c1f0e726-67d2-4d23-831f-e923427c416b
created_at: '2025-12-11T03:48:05.936Z'
updated_at: '2025-12-11T03:48:05.936Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1213]]'
---
# Enumerate HackerOne Program IDs via GraphQL

## Summary

This procedure enumerates program IDs from HackerOne's GraphQL endpoint by querying teams with a null state, revealing IDs and handles for both public and private programs.

## Description

The procedure exploits a public GraphQL query to fetch a list of teams, including their internal IDs, which can be used to construct Global IDs for further exploitation. It targets the /graphql endpoint and requires no authentication, making it suitable for reconnaissance in bug bounty scenarios.

## Requirements

1. Access to the HackerOne GraphQL endpoint (/graphql)
2. Ability to send HTTP POST requests with JSON payloads
3. No prior credentials needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on GraphQL queries
- Restrict queries to authenticated users only

## Objectives

1. Obtain enumerable program IDs for GID construction
2. Identify private programs through handles
3. Gather data for subsequent IDOR exploitation

## Instructions

### Step 1: Send Enumeration Query

**Context**: Fetch the list of teams with null state to get program IDs and handles.

**Command** ([[commands/graphql-enumerate-programs]]):
```json
{"query":"{teams(where:{state:{_eq:null}}){total_count,nodes{_id,handle}}}"}
```

> This command sends a GraphQL query to retrieve total count and nodes with _id and handle; expect a JSON list of programs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/graphql-enumerate-programs]]

## Tools Used



## Tags

- #enumeration
- [[commands/graphql-enumerate-programs]]
