---
data: >-
  curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/manifests/3.0.1' -H 'Host:
  TARGET_IP' -H 'Accept: */*'
tags:
  - docker
  - manifest
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.914Z'
id: a474aadd-87d3-49bc-bf5c-7338d9ddf658
verified: false
validated: true
submitted: true
---
# docker-manifest-retrieve

## Command

```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/manifests/3.0.1' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

## Description

Retrieves the manifest for a Docker image tag, including layer digests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 3.0.1 | Image tag | Yes |
| NAMESPACE/REPO | Repository | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/v2/ns/repo/manifests/latest
```

### Advanced Usage

```bash
curl -s https://TARGET_IP/v2/ns/repo/manifests/3.0.1 | jq '.fsLayers'
```

## Expected Output

JSON manifest with fsLayers array.

## Related

- [[Related Procedure: Retrieve-Docker-Image-Manifest]]
