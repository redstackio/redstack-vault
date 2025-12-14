---
id: cmd-curl-verify-fix
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"example-soft-launch\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
tags:
  - graphql
  - verification
type: command
output: 'Returns 0 for non-members, 1 for whitelisted hackers in soft-launched teams'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.105Z'
verified: false
validated: true
submitted: true
---
# curl-verify-graphql-fix

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-soft-launch\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Description

Verifies the fix by querying a soft-launched team post-remediation to check restricted total_count.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{...}'` | JSON with soft-launched handle | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-soft-launch\"){id,name,handle,whitelisted_hackers{total_count}}}"}'
```

## Expected Output

JSON with total_count:0 for non-members or 1 for authorized.

## Related

- [[commands/graphql-query-security-team]]
- [[procedures/Verify-GraphQL-Fix-for-Whitelisted-Hackers]]
