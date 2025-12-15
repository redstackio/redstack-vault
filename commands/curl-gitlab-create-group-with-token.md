---
id: uuid-c2
data: >-
  curl -X POST --header "Authorization: Bearer <TOKEN>"
  "https://gitlab.domain.com/api/v4/groups?name=newg&path=newgroup"
tags:
  - gitlab
  - api
  - creation
type: command
output: JSON response with created group details
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.308Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-create-group-with-token

## Command

```bash
curl -X POST --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/groups?name=newg&path=newgroup"
```

## Description

Creates a new group using the escalated token, demonstrating internal creation privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `--header "Authorization: Bearer <TOKEN>"` | Bearer token auth | Yes |
| `name=newg` | Group display name | Yes |
| `path=newgroup` | URL path for group | Yes |

## Examples

### Basic Usage

```bash
curl -X POST --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/groups?name=test&path=testgroup"
```

### Advanced Usage

Include visibility:

```bash
curl -X POST --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/groups?name=newg&path=newgroup&visibility=internal"
```

## Expected Output

JSON object with group id, name, path, visibility, and creation timestamp.

## Related

- [[commands/curl-gitlab-create-issue-with-token]]
- [[procedures/Exploit-Token-for-Internal-Access]]
