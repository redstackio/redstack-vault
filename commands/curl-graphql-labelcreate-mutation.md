---
data: >-
  curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type:
  application/json' -H 'Accept: application/json' -H 'Authorization: Bearer
  <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n
  labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n
  errors\n label{\n id\n }\n }\n}"}'}
tags:
  - graphql
  - mutation
type: command
output: 'Success with label ID, no errors'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.472Z'
id: af779044-29e0-403d-a71a-3228c81e35e8
verified: false
validated: true
submitted: true
---
# curl-graphql-labelcreate-mutation

## Command

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n errors\n label{\n id\n }\n }\n}"}'}'
```

## Description

Performs a GraphQL mutation to create a label in a project using a deactivated token, testing write access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | Mutation payload | Yes |
| `-H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>'` | Token | Yes |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n errors\n label{\n id\n }\n }\n}"}'}'
```

## Expected Output

{"data":{"labelCreate":{"label":{"id":"gid://gitlab/Label/123"},"errors":[]}}}

## Related

- [[commands/curl-add-user-to-project]]
- [[procedures/Perform-GraphQL-Mutation-with-Deactivated-Token]]
