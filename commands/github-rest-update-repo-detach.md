---
data: >-
  curl -X PATCH -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Accept:
  application/vnd.github.v3+json" https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO
  -d '{"private": true, "archived": true}'
tags:
  - api
  - rest
  - github
type: command
output: null
executor: bash
platforms:
  - Web
  - GitHub Enterprise Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.402Z'
id: 73c4ff12-ee4d-47cf-bab3-d482482affcd
verified: false
validated: true
submitted: true
---
# github-rest-update-repo-detach

## Command

```bash
curl -X PATCH -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Accept: application/vnd.github.v3+json" https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO -d '{"private": true, "archived": true}'
```

## Description

Updates a GitHub repository via REST API to initiate detachment by archiving and privatizing it, exploiting timing for race conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | HTTP method for update | Yes |
| `-H "Authorization: token ..."` | Admin token for auth | Yes |
| `-H "Accept: ..."` | API version header | Yes |
| `https://.../repos/ORG/REPO` | Target repo endpoint | Yes |
| `-d '{"private": true, "archived": true}'` | Payload to detach | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" https://ghes.example.com/api/v3/repos/myorg/myrepo -d '{"private": true, "archived": true}'
```

### Advanced Usage

Add verbose output with `-v` for debugging.

## Expected Output

HTTP 200 with JSON: {"id":123,"name":"myrepo",..."archived":true}

## Related

- [[commands/github-graphql-update-teams-repo]]
