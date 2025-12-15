---
id: uuid-c6
data: >-
  curl --header "Authorization: Bearer TOKEN"
  "https://gitlab.domain.com/api/v4/projects/15/repository/tree"
tags:
  - gitlab
  - api
  - recon
type: command
output: 'JSON array of tree entries with id, name, type, path, mode'
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.298Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-list-repository-tree

## Command

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects/15/repository/tree"
```

## Description

Lists the file and directory structure of an internal project's repository to obtain blob IDs for source access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Authorization: Bearer TOKEN"` | Token auth | Yes |
| `project_id=15` | Target project ID | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects/15/repository/tree"
```

### Advanced Usage

Specify ref:

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects/15/repository/tree?ref=main"
```

## Expected Output

JSON array with tree objects: id (SHA), name, type (blob/tree), path, mode.

## Related

- [[commands/curl-gitlab-access-source-blob-raw]]
- [[procedures/Exploit-Token-for-Internal-Access]]
