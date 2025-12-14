---
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -H "X-Auth-Token: YOUR_TOKEN" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64) AppleWebKit/537.36" -d '{"query":"mutation
  Claim_credential_mutation($input_0:ClaimCredentialInput!,$types_1:[ErrorTypeEnum]!,$first_2:Int!)
  {claimCredential(input:$input_0) {clientMutationId,...F4,...F5}} fragment F0
  on Team {id,claimed_credential {credentials,account_details,id}} fragment F1
  on Node {id} fragment F2 on ResourceInterface {...F0,...F1} fragment F3 on
  Team {id} fragment F4 on ClaimCredentialPayload {team {id,...F2,...F3}}
  fragment F5 on ClaimCredentialPayload {team {claimed_credential
  {id},id},was_successful,_errors4fkckF:errors(types:$types_1,first:$first_2)
  {edges {node {type,field,message,id},cursor},pageInfo
  {hasNextPage,hasPreviousPage}}}}","variables":{"input_0":{"team_id":"BASE64_TEAM_ID","clientMutationId":"1"},"types_1":"ARGUMENT","first_2":100}}'
tags:
  - graphql
  - mutation
  - curl
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.918Z'
id: bb620912-915a-45d7-9cd2-52fe2128341a
verified: false
validated: true
submitted: true
---
# claim-credential-graphql-mutation

## Command

```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: YOUR_TOKEN" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -d '{"query":"mutation Claim_credential_mutation($input_0:ClaimCredentialInput!,$types_1:[ErrorTypeEnum]!,$first_2:Int!) {claimCredential(input:$input_0) {clientMutationId,...F4,...F5}} fragment F0 on Team {id,claimed_credential {credentials,account_details,id}} fragment F1 on Node {id} fragment F2 on ResourceInterface {...F0,...F1} fragment F3 on Team {id} fragment F4 on ClaimCredentialPayload {team {id,...F2,...F3}} fragment F5 on ClaimCredentialPayload {team {claimed_credential {id},id},was_successful,_errors4fkckF:errors(types:$types_1,first:$first_2) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}}","variables":{"input_0":{"team_id":"BASE64_TEAM_ID","clientMutationId":"1"},"types_1":"ARGUMENT","first_2":100}}'
```

## Description

This curl command executes a GraphQL mutation to claim test credentials for a HackerOne program. It targets the /graphql endpoint with authentication and variables for team claiming.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-H "X-Auth-Token: YOUR_TOKEN"` | Authentication header | Yes |
| `team_id` in variables | Base64-encoded team/program ID | Yes |
| `clientMutationId` | Unique ID for the request (e.g., "1") | Yes |
| `first_2` | Number of errors to fetch (100) | No |
| `types_1` | Error type filter ("ARGUMENT") | No |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "X-Auth-Token: abc123" -d '{...variables with team_id}'
```

### Advanced Usage

Use with Burp or proxy for interception; increment clientMutationId for uniqueness in batches.

## Expected Output

JSON response like: {"data":{"claimCredential":{"clientMutationId":"1","team":{"claimed_credential":{"credentials":{"email":"test@example.com","password":"pass"},"id":"123"}},"was_successful":true}}}

## Related

- [[procedures/Send-Initial-GraphQL-Claim-Credential-Mutation]]
- [[procedures/Send-Concurrent-Requests-with-Burp-Intruder]]
