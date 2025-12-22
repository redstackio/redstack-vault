---
type: command
executor: bash
data: >-
  curl -s -k --user "$_USERNAME:$_PASSWORD"
  "$_REGISTRY_URL/v2/$_REPO_NAME/blobs/$_BLOB_DIGEST" > $_OUTPUT_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - download
  - blob
verified: true
validated: true
---

# curl-download-blob

## Command

```bash
curl -s -k --user "$_USERNAME:$_PASSWORD" "$_REGISTRY_URL/v2/$_REPO_NAME/blobs/$_BLOB_DIGEST" > $_OUTPUT_FILE
```

## Description

Downloads a specific image layer blob by its digest to a local file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username | Conditional |
| $_PASSWORD | Password | Conditional |
| $_REPO_NAME | Repo name | Yes |
| $_BLOB_DIGEST | SHA256 digest from manifest | Yes |
| $_OUTPUT_FILE | Local output file (e.g., layer.tar.gz) | Yes |
| $_REGISTRY_URL | Base URL | Yes |

## Examples

### Download Layer

```bash
curl -s -k --user 'admin:admin' 'http://docker.registry.local/v2/wordpress-image/blobs/sha256:c314c5effb61c9e9c534c81a6970590ef4697b8439ec6bb4ab277833f7315058' > layer.tar.gz
```

## Expected Output

Binary data saved to file; no stdout. Verify with file $_OUTPUT_FILE (gzip compressed tar).

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
