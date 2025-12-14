---
tags:
  - information-disclosure
  - graphql
  - api
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-graphql-team-report-sources]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: bfb54bb4-d23c-4b2f-9ba2-d43a1292bcff
created_at: '2025-12-14T17:30:47.342Z'
updated_at: '2025-12-14T17:30:47.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-Private-HackerOne-Programs-via-GraphQL

## Summary

This procedure exploits an authorization bypass in HackerOne's GraphQL API to query the Team object's report_sources field, disclosing whether a program is private. By sending unauthenticated POST requests to /graphql with team handles, attackers can observe empty arrays for public programs and ['HackerOne Platform'] for private ones, enabling identification of sensitive programs with external links.

## Description

The vulnerability stems from missing authorization checks on the report_sources attribute of the Team object in HackerOne's GraphQL schema. Unauthorized users can query any team by handle, retrieving _id and report_sources. Public teams return empty report_sources, while private teams include 'HackerOne Platform', leaking program privacy status. This is useful in reconnaissance to map private bug bounty programs. The target environment is the web-based HackerOne platform using GraphQL over HTTPS. Prerequisites include basic HTTP knowledge and curl; no authentication is needed. Expected outcomes: JSON responses revealing program details, potentially leading to targeted attacks on private programs.

## Requirements

1. Internet access to reach https://hackerone.com/graphql
2. curl or equivalent HTTP client
3. List of team handles (obtainable from public HackerOne directories or searches)

## Defense

Defensive measures and detection strategies:

- Implement field-level authorization in GraphQL resolvers to restrict report_sources to authenticated users with program access.
- Rate-limit unauthenticated GraphQL queries to prevent enumeration.
- Monitor API logs for anomalous Team queries from unknown IPs, alerting on patterns matching private team handles.
- Use schema introspection controls to hide sensitive fields from unauthenticated queries.

## Objectives

1. Retrieve report_sources for a given team handle without authentication.
2. Distinguish private programs (non-empty report_sources) from public ones.
3. Gather intelligence on private program exposure for further exploitation.

## Instructions

### Step 1: Prepare and Send GraphQL Query for Baseline (Non-Private Team)

**Context**: Start with a known public team to verify the empty response, confirming the API's behavior for non-sensitive data.

**Command** ([[commands/curl-graphql-team-report-sources]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"example-nonprivate\"){_id,report_sources}}"}'
```

> This command sends a POST request with the GraphQL query JSON payload. Replace 'example-nonprivate' with a real public team handle. Expected output is a JSON response with report_sources as []. If successful, it confirms access to the endpoint.

### Step 2: Query Suspected Private Team

**Context**: Test a team suspected to be private to detect the disclosure. Compare the response to the baseline.

**Command** ([[commands/curl-graphql-team-report-sources]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"example-private\"){_id,report_sources}}"}'
```

> Use a private team handle like 'example-private'. The response should include ["HackerOne Platform"] in report_sources, indicating privacy leak. Validate by checking for the non-empty array.

### Step 3: Enumerate Multiple Teams

**Context**: Scale the test across multiple handles to map private programs systematically.

**Command** ([[commands/curl-graphql-team-report-sources]]):
```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query":"query {team(handle:\"another-team\"){_id,report_sources}}"}'
```

> Repeat for additional handles. Log responses to identify patterns: empty for public, populated for private. This reveals exposed sensitive programs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-team-report-sources]]

## Tools Used


## Tags

- information-disclosure
- graphql
- api
- hackerone
