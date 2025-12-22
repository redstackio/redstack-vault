---
id: cmd-graphql-private
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
tags:
  - graphql
  - private-program
type: command
output: >-
  {"data":{"team":{"id":"███████","name":"██████████","handle":"████████","whitelisted_hackers":{"total_count":1188}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.111Z'
verified: false
validated: true
submitted: true
---
# graphql-query-private-program

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Description

Retrieves whitelisted count for a private, invitation-only program without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{...}'` | JSON with redacted private handle | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"████████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Expected Output

JSON with total_count:1188.

## Related

- [[commands/graphql-query-nonpublic-program]]
- [[procedures/Test-Whitelisted-Hackers-on-Program-Types]]
