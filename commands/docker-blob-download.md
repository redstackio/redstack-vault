---
data: >-
  curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/blobs/sha256:ABC123...' -H
  'Host: TARGET_IP' -H 'Accept: */*' -o layer.tar.gz
tags:
  - docker
  - download
  - blobs
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.910Z'
id: ebd57eba-e70e-4988-be49-44efa6b9d019
verified: false
validated: true
submitted: true
---
# docker-blob-download

## Command

```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/blobs/sha256:ABC123...' -H 'Host: TARGET_IP' -H 'Accept: */*' -o layer.tar.gz
```

## Description

Downloads a Docker image layer blob as a .tar.gz archive.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sha256:ABC123... | Blob digest | Yes |
| -o layer.tar.gz | Output file | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/v2/ns/repo/blobs/sha256:def -o layer.gz
```

### Advanced Usage

```bash
curl -s --output layer.tar.gz 'https://TARGET_IP/v2/ns/repo/blobs/DIGEST'
```

## Expected Output

Binary .tar.gz file downloaded.

## Related

- [[Related Procedure: Download-Docker-Image-Layers]]
