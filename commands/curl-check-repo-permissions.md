---
data: >-
  curl -H "Authorization: token YOUR_TOKEN" -H "Accept:
  application/vnd.github+json"
  https://ghe.example.com/api/v3/repos/target-org/REPO/collaborators/USERNAME/permission
tags:
  - verification
  - permissions
type: command
output: '{"permission": "admin"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.330Z'
id: db957899-436d-4dbe-ac54-720ff831f898
verified: false
validated: true
submitted: true
---
# curl-check-repo-permissions

## Command

```bash
curl -H "Authorization: token YOUR_TOKEN" -H "Accept: application/vnd.github+json" https://ghe.example.com/api/v3/repos/target-org/REPO/collaborators/USERNAME/permission
```

## Description

Queries a user's permission level on a GitHub repository via REST API, used to verify retained access after exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: token YOUR_TOKEN"` | Auth header | Yes |
| `-H "Accept: application/vnd.github+json"` | API version | Yes |
| `https://ghe.example.com/api/v3/repos/target-org/REPO/collaborators/USERNAME/permission` | Endpoint for permission check | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github+json" https://ghe.example.com/api/v3/repos/target-org/my-repo/collaborators/adminuser/permission
```

### Advanced Usage

```bash
curl -H "Authorization: token ghp_abc123" -H "Accept: application/vnd.github+json" -s https://ghe.example.com/api/v3/repos/target-org/my-repo/collaborators/adminuser/permission
```

## Expected Output

JSON like {"permission": "admin"} or "push"/"pull"; 404 if no access.

## Related

- [[Related Procedure: Verify-Retained-Admin-Access-on-Transferred-Repository]]
