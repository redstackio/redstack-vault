---
id: cmd-uuid-2
data: >-
  curl -X GET 'https://phabricator.example.com/api/user.search' -d
  'output=json&__conduit__={"token":"api-token-here"}&constraints[usernames]=[\"targetuser\"]'
tags:
  - phid-extract
  - phabricator
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.055Z'
verified: false
validated: true
submitted: true
---
# curl-get-phabricator-user-phid

## Command

```bash
curl -X GET 'https://phabricator.example.com/api/user.search' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&constraints[usernames]=[\"targetuser\"]'
```

## Description

Queries the Phabricator user.search API to retrieve a user's PHID by username for spoofing preparation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `-d '...'` | Query constraints | Yes |
| `token` | API token | Yes |
| `constraints[usernames]` | Array of usernames to search | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://phabricator.example.com/api/user.search' -d 'output=json&__conduit__={"token":"api-token-here"}&constraints[usernames]=[\"targetuser\"]'
```

### Advanced Usage

```bash
curl -X GET 'https://phabricator.example.com/api/user.search' -d 'output=json&__conduit__={"token":"api-token-here"}&constraints[usernames]=[\"user1\",\"user2\"]'
```

## Expected Output

{"result":{"data":[{"phid":"PHID-USER-abc123","fields":{"username":"targetuser"}}]}}

## Related

- [[Related Procedure]]
