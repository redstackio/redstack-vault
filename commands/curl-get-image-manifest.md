---
type: command
executor: bash
data: >-
  curl -s -k --user "$_USERNAME:$_PASSWORD"
  $_REGISTRY_URL/v2/$_REPO_NAME/manifests/$_TAG
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - discovery
  - manifest
verified: true
validated: true
---

# curl-get-image-manifest

## Command

```bash
curl -s -k --user "$_USERNAME:$_PASSWORD" $_REGISTRY_URL/v2/$_REPO_NAME/manifests/$_TAG
```

## Description

Fetches the manifest for an image tag, revealing layer digests and config.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Auth username | Conditional |
| $_PASSWORD | Auth password | Conditional |
| $_REPO_NAME | Repository | Yes |
| $_TAG | Tag (e.g., latest) | Yes |
| $_REGISTRY_URL | Base URL | Yes |

## Examples

### Basic

```bash
curl -s -k --user "admin:admin" http://docker.registry.local/v2/wordpress-image/manifests/latest
```

## Expected Output

JSON manifest with {"config":{"digest":"sha256:..."}, "layers":[{"digest":"sha256:..."}]}

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
