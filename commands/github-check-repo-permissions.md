---
data: >-
  curl -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Accept:
  application/vnd.github.v3+json"
  https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO/collaborators/YOUR_USERNAME/permission
tags:
  - api
  - verification
  - github
type: command
output: null
executor: bash
platforms:
  - Web
  - GitHub Enterprise Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.379Z'
id: 6513444a-8fd4-4e42-960b-0263be2d76e0
verified: false
validated: true
submitted: true
---
# github-check-repo-permissions

## Command

```bash
curl -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Accept: application/vnd.github.v3+json" https://YOUR_GHES_HOST/api/v3/repos/ORG/REPO/collaborators/YOUR_USERNAME/permission
```

## Description

Queries GitHub REST API for a user's permissions on a repository to verify access levels post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: ..."` | Token header | Yes |
| `-H "Accept: ..."` | API version | Yes |
| `https://.../repos/ORG/REPO/collaborators/USERNAME/permission` | Permissions endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github.v3+json" https://ghes.example.com/api/v3/repos/myorg/myrepo/collaborators/user123/permission
```

### Advanced Usage

Use `-s` for silent output parsing.

## Expected Output

JSON: {"permission":"admin","role_name":"admin"}

## Related

- [[commands/github-graphql-update-teams-repo]]
