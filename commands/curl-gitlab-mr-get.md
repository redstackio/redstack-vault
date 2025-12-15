---
id: cmd-curl-mr-get-001
data: >-
  curl --header "Authorization: Bearer <token>"
  "https://gitlab.example.com/api/v4/projects/<project_id>/merge_requests/<mr_id>"
tags:
  - api
  - gitlab
  - query
type: command
output: >-
  JSON response with MR details: {"id":1,"title":"Test
  MR","description":"...",...}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.094Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-mr-get

## Command

```bash
curl --header "Authorization: Bearer <token>" "https://gitlab.example.com/api/v4/projects/<project_id>/merge_requests/<mr_id>"
```

## Description

This command queries the GitLab API for Merge Request details using a personal access token, useful for testing access in vulnerability scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header` | Adds Authorization Bearer token | Yes |
| `<project_id>` | GitLab project numeric ID | Yes |
| `<mr_id>` | Merge Request IID (e.g., 1) | Yes |
| `<token>` | Personal access token string | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer glpat-abc123" "https://gitlab.com/api/v4/projects/123/merge_requests/1"
```

### Advanced Usage

```bash
curl --header "Authorization: Bearer glpat-abc123" --header "Content-Type: application/json" "https://gitlab.com/api/v4/projects/123/merge_requests/1/commits"
```

## Expected Output

JSON object containing MR metadata: id, title, description, state, assignees, etc. HTTP 200 on success; 403 if access denied.

## Related

- [[Related Procedure|procedures/Query-Merge-Request-Data-via-API]]
