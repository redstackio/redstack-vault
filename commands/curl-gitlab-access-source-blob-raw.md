---
id: uuid-c4
data: >-
  curl --header "Authorization: Bearer <TOKEN>"
  "https://gitlab.domain.com/api/v4/projects/19/repository/blobs/83d9398518bdf1519b7b8fbbb3fa3e305a8554ef/raw"
tags:
  - gitlab
  - api
  - source-disclosure
type: command
output: Raw file content of the blob
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.303Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-access-source-blob-raw

## Command

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects/19/repository/blobs/83d9398518bdf1519b7b8fbbb3fa3e305a8554ef/raw"
```

## Description

Retrieves raw source code from an internal project's repository blob using the token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Authorization: Bearer <TOKEN>"` | Bearer auth | Yes |
| `project_id=19` | Internal project ID | Yes |
| `blob_sha=83d9398518bdf1519b7b8fbbb3fa3e305a8554ef` | Commit SHA of blob | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects/19/repository/blobs/abcsha/raw"
```

### Advanced Usage

Pipe to file:

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects/19/repository/blobs/83d9398518bdf1519b7b8fbbb3fa3e305a8554ef/raw" > leaked_file.txt
```

## Expected Output

Plain text raw content of the file (e.g., source code).

## Related

- [[commands/curl-gitlab-get-blob-details]]
- [[procedures/Exploit-Token-for-Internal-Access]]
