---
data: >-
  curl -H "Authorization: token $GH_TOKEN" -H "Accept:
  application/vnd.github.v3+json" https://api.github.com/user
tags:
  - api
  - github
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 0d7723b8-a2b0-451f-82d4-11530ec36fe9
created_at: '2025-12-11T03:48:06.062Z'
updated_at: '2025-12-11T03:48:06.062Z'
verified: false
validated: true
submitted: true
---
# curl-github-user

## Command

```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

## Description

Authenticates to the GitHub API using a token to retrieve details about the authenticated user, verifying token validity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: token $GH_TOKEN"` | Provides the GitHub token for authentication | Yes |
| `-H "Accept: application/vnd.github.v3+json"` | Specifies API version and JSON format | Yes |
| `https://api.github.com/user` | Endpoint for user details | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

## Expected Output

JSON object with user information like login, id, and email if token is valid.

## Related

- [[procedures/Validate-GitHub-Token-Authentication]]
- #curl
