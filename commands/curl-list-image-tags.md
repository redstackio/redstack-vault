---
type: command
executor: bash
data: >-
  curl -s -k --user "$_USERNAME:$_PASSWORD"
  $_REGISTRY_URL/v2/$_REPO_NAME/tags/list
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - discovery
  - enumeration
verified: true
validated: true
---

# curl-list-image-tags

## Command

```bash
curl -s -k --user "$_USERNAME:$_PASSWORD" $_REGISTRY_URL/v2/$_REPO_NAME/tags/list
```

## Description

Lists all tags for a specific repository in the registry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for basic auth | Yes (if auth required) |
| $_PASSWORD | Password for basic auth | Yes (if auth required) |
| $_REPO_NAME | Repository name (e.g., wordpress-image) | Yes |
| $_REGISTRY_URL | Base URL | Yes |
| -s -k | Silent and skip SSL | No |

## Examples

### With Auth

```bash
curl -s -k --user "admin:admin" http://docker.registry.local/v2/wordpress-image/tags/list
```

## Expected Output

```
{"name":"wordpress-image","tags":["latest","v1.0"]}
```

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
