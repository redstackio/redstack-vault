---
id: uuid-c7
data: >-
  curl --header "Authorization: Bearer TOKEN"
  "https://gitlab.domain.com/api/v4/projects/15/repository/blobs/995aa640bef8ad391a5cd9f8ca82c9d481d34cbb"
tags:
  - gitlab
  - api
  - source-disclosure
type: command
output: 'JSON with size, encoding (base64), content, sha'
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.296Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-get-blob-details

## Command

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects/15/repository/blobs/995aa640bef8ad391a5cd9f8ca82c9d481d34cbb"
```

## Description

Retrieves detailed blob information, including base64-encoded content, from an internal repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Authorization: Bearer TOKEN"` | Token auth | Yes |
| `project_id=15` | Project ID | Yes |
| `sha=995aa640bef8ad391a5cd9f8ca82c9d481d34cbb` | Blob SHA from tree | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects/15/repository/blobs/abcsha"
```

### Advanced Usage

Save base64 content:

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects/15/repository/blobs/995aa640bef8ad391a5cd9f8ca82c9d481d34cbb" | jq '.content' | base64 -d > file.txt
```

## Expected Output

JSON: { "id": sha, "size": bytes, "encoding": "base64", "content": base64_string, ... }

## Related

- [[commands/curl-gitlab-list-repository-tree]]
- [[procedures/Exploit-Token-for-Internal-Access]]
