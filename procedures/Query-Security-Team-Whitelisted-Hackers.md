---
id: proc-graphql-security-query
tags:
  - graphql
  - information-disclosure
  - api
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-security-team]]'
verified: false
platforms:
  - Web
  - GraphQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:00.136Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Query-Security-Team-Whitelisted-Hackers

## Summary

This procedure exploits a lack of authorization in HackerOne's GraphQL API to query the 'security' team and disclose the total count of whitelisted hackers, revealing sensitive internal details about users with 2FA and IP restrictions.

## Description

The GraphQL API's Team object exposes the whitelisted_hackers field's total_count without proper checks, allowing unauthenticated users to access this data. This is useful in reconnaissance to gauge team security configurations and program privacy. The attack targets the public endpoint https://api.hackerone.com/graphql and returns base64-encoded IDs, team names, and counts. Prerequisites include HTTP client access; no authentication is needed, making it low-risk for detection.

## Requirements

1. Access to a tool like curl for POST requests to the GraphQL endpoint.
2. Knowledge of the target team handle (e.g., 'security').
3. Internet connectivity to HackerOne's API.

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on GraphQL resolvers for sensitive fields like whitelisted_hackers.
- Monitor API logs for anomalous queries to Team objects from unauthenticated sources.
- Use rate limiting and query complexity analysis to prevent abuse.

## Objectives

1. Disclose the number of whitelisted hackers to infer team security posture.
2. Validate unauthorized access to internal program data.
3. Collect data for further reconnaissance on program types.

## Instructions

### Step 1: Craft and Send GraphQL Query

**Context**: Prepare a GraphQL query targeting the 'security' team to fetch whitelisted_hackers total_count, exploiting the missing authorization.

**Command** ([[commands/graphql-query-security-team]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"security\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

> This command sends a POST request with the JSON payload to the GraphQL endpoint. Expected output is a JSON response with the team's details and total_count of 30, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-security-team]]

## Tools Used


## Tags

- graphql
- information-disclosure
- api-abuse
