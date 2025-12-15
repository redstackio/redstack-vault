---
data: >-
  curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H
  'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data
  '{"query":"{\n currentUser{id}\n}"}'}
tags:
  - graphql
  - query
type: command
output: '{"data":{"currentUser":{"id":"gid://gitlab/User/15"}}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.489Z'
id: 72d358ee-233a-4ab3-aefc-68734f790ca0
verified: false
validated: true
submitted: true
---
# curl-graphql-currentuser-query

## Command

```bash
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n currentUser{id}\n}"}'}'
```

## Description

Sends a GraphQL query to fetch the current user's ID using a personal access token, useful for verifying API authentication in GitLab bypass tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer <<TOKEN>>'` | Bearer token for auth | Yes |
| `--data` | JSON payload with GraphQL query | Yes |
| URL | GraphQL endpoint | Yes |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n currentUser{id}\n}"}'}'
```

### Advanced Usage

Add verbose output: `-v` flag for debugging.

## Expected Output

JSON with user ID: {"data":{"currentUser":{"id":"gid://gitlab/User/15"}}}

## Related

- [[commands/curl-graphql-projects-query]]
- [[procedures/Query-GraphQL-API-with-Deactivated-Token]]
