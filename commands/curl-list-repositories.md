---
type: command
executor: bash
data: curl -s -k $_REGISTRY_URL/v2/_catalog
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

# curl-list-repositories

## Command

```bash
curl -s -k $_REGISTRY_URL/v2/_catalog
```

## Description

Retrieves a list of all repositories in the Docker registry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGISTRY_URL | Base URL of the registry | Yes |
| -s | Silent mode, no progress meter | No |
| -k | Skip SSL verification | No |

## Examples

### Basic Usage

```bash
curl -s -k http://docker.registry.local/v2/_catalog
```

## Expected Output

```
{"repositories":["library/nginx","wordpress-image"]}
```

JSON array of repo names. Empty if auth required.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
