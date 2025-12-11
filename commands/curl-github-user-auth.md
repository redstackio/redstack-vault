---
data: >-
  curl -H "Authorization: token $GH_TOKEN" -H "Accept:
  application/vnd.github.v3+json" https://api.github.com/user
tags:
  - api-query
  - github
type: command
executor: bash
platforms:
  - macOS
id: bb257cc4-2f8a-4cd8-bac9-64040e7269de
created_at: '2025-12-11T06:10:40.475Z'
updated_at: '2025-12-11T06:10:40.475Z'
verified: false
validated: true
submitted: true
---
# curl-github-user-auth

## Command

```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

## Description

Authenticates to the GitHub API and retrieves details of the authenticated user to verify token validity.

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

### Advanced Usage

```bash
curl -s -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user | jq
```

## Expected Output

JSON response with user details, such as login and id, confirming valid token.

## Related

- [[procedures/Verify-GitHub-Token-Validity]]
