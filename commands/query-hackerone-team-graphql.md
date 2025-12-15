---
data: >-
  curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer
  $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") {
  i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql
tags:
  - graphql
  - api
  - query
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.575Z'
id: 30dbe48f-6a11-4020-9610-7a69bee1e7b9
verified: false
validated: true
submitted: true
---
# query-hackerone-team-graphql

## Command

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql
```

## Description

This command queries HackerOne's GraphQL API to fetch the 'i_cannot_create_jira_webhook_reasons' field from a specified Team object, enabling detection of private program existence through response analysis. Use it to probe company handles for information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TOKEN` | HackerOne API bearer token | Yes |
| `$COMPANY` | Target company handle (e.g., "google") | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Auth header | Yes |
| `-d '{...}'` | GraphQL query payload | Yes |

## Examples

### Basic Usage

Query a single company:

```bash
TOKEN="your_token" COMPANY="acme"
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql
```

### Advanced Usage

Pipe to jq for parsing:

```bash
TOKEN="your_token" COMPANY="acme"
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query":"query { team(handle: \"$COMPANY\") { i_cannot_create_jira_webhook_reasons } }"}' https://api.hackerone.com/graphql | jq '.data.team.i_cannot_create_jira_webhook_reasons'
```

## Expected Output

JSON response like: {"data":{"team":{"i_cannot_create_jira_webhook_reasons":["CANNOT_VIEW","FEATURE_GATED","PROGRAM_PERMISSION_REQUIRED"]}}} or without "FEATURE_GATED" for programs.

## Related

- [[procedures/Query-HackerOne-GraphQL-Team-Object]]
