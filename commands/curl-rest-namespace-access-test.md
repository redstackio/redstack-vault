---
data: >-
  curl --header "PRIVATE-TOKEN: anotherUserToken"
  'https://gitlab.com/api/v4/namespaces/16048'
tags:
  - api
  - test
  - rest
type: command
output: '{"message":"404 Namespace Not Found"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.869Z'
id: d2f21e25-62ae-4f7c-bf49-8b29ac44512e
verified: false
validated: true
submitted: true
---
# curl-rest-namespace-access-test

## Command

```bash
curl --header "PRIVATE-TOKEN: anotherUserToken" 'https://gitlab.com/api/v4/namespaces/16048'
```

## Description

This command tests access to a private GitLab namespace via REST API using an unauthorized token, expecting a denial to confirm controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: anotherUserToken"` | Authentication header with non-owner token | Yes |
| `'https://gitlab.com/api/v4/namespaces/16048'` | REST endpoint for specific namespace ID | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: anotherUserToken" 'https://gitlab.com/api/v4/namespaces/16048'
```

### Advanced Usage

Adapt for different IDs: replace 16048 with target namespace ID.

## Expected Output

JSON error: {"message":"404 Namespace Not Found"}, indicating access denied.

## Related

- [[Related Procedure]]
