---
data: >-
  curl -X POST -H "Authorization: Bearer $TOKEN" -F "file=@import.tar.gz"
  https://gitlab.example.com/api/v4/import/gitlab_projects/create
tags:
  - api
  - upload
  - gitlab
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 69e979f5-30a3-40d4-a5dc-e509e4edba4f
created_at: '2025-12-14T17:24:19.268Z'
updated_at: '2025-12-14T17:24:19.268Z'
verified: false
validated: true
submitted: true
---
# curl-upload-import-file

## Command

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -F "file=@import.tar.gz" https://gitlab.example.com/api/v4/import/gitlab_projects/create
```

## Description

This command uploads a GitLab project import file (tar.gz) via the REST API to the import endpoint, authenticating with a personal access token and using multipart form data for the file. It triggers file storage in the shared tmp directory and enqueues a Sidekiq job.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Auth header with GitLab token | Yes |
| `-F "file=@import.tar.gz"` | Form field for file upload, @path to local file | Yes |
| `https://gitlab.example.com/api/v4/import/gitlab_projects/create` | Target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer abc123" -F "file=@import.tar.gz" https://gitlab.example.com/api/v4/import/gitlab_projects/create
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer abc123" -H "Content-Type: multipart/form-data" -F "file=@import.tar.gz" -F "project_id=123" https://gitlab.example.com/api/v4/import/gitlab_projects/create
```

## Expected Output

Successful response: HTTP 201 Created with JSON like {"id":123, "status":"started"}. Failure: 401 Unauthorized or 422 Validation error. The file is copied to shared storage upon success.

## Related

- [[Related Procedure: Upload-Import-File-to-GitLab]]
