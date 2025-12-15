---
id: cmd-curl-mr-todo-post-001
data: >-
  curl --request POST --header "Authorization: Bearer <token>" --header
  "Content-Type: application/json" -d
  '{"target_type":"MergeRequest","target_id":<mr_id>}'
  "https://gitlab.example.com/api/v4/projects/<project_id>/merge_requests/<mr_id>/todo"
tags:
  - api
  - gitlab
  - post
  - interaction
type: command
output: 'JSON response: {"id":456,"project_id":123,...}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.093Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-mr-todo-post

## Command

```bash
curl --request POST --header "Authorization: Bearer <token>" --header "Content-Type: application/json" -d '{"target_type":"MergeRequest","target_id":<mr_id>}' "https://gitlab.example.com/api/v4/projects/<project_id>/merge_requests/<mr_id>/todo"
```

## Description

This command creates a TODO for a Merge Request via GitLab API, demonstrating interaction capabilities in access control tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--request POST` | Specifies POST method | Yes |
| `--header` | Authorization and Content-Type | Yes |
| `-d` | JSON payload with target details | Yes |
| `<project_id>` | Project ID | Yes |
| `<mr_id>` | MR IID | Yes |
| `<token>` | Access token | Yes |

## Examples

### Basic Usage

```bash
curl --request POST --header "Authorization: Bearer glpat-abc123" --header "Content-Type: application/json" -d '{"target_type":"MergeRequest","target_id":1}' "https://gitlab.com/api/v4/projects/123/merge_requests/1/todo"
```

### Advanced Usage

Add verbose output: curl -v with above flags.

## Expected Output

JSON for created TODO: {"id":456,"body":"New TODO for MR","author":{...}}. HTTP 201 on success.

## Related

- [[Related Procedure|procedures/Query-Merge-Request-Data-via-API]]
