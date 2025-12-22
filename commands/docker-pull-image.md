---
type: command
executor: bash
data: 'docker pull $_REGISTRY_HOST/$_REPO_NAME:$_TAG'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - pull
  - docker
verified: true
validated: true
---

# docker-pull-image

## Command

```bash
docker pull $_REGISTRY_HOST/$_REPO_NAME:$_TAG
```

## Description

Pulls a specific image tag from the registry to the local Docker daemon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGISTRY_HOST | Registry host | Yes |
| $_REPO_NAME | Image repository | Yes |
| $_TAG | Image tag (default: latest) | No |

## Examples

### Pull Specific Image

```bash
docker pull docker.registry.local/wordpress-image
```

## Expected Output

```
latest: Pulling from wordpress-image
Digest: sha256:...
Status: Downloaded newer image for docker.registry.local/wordpress-image:latest
```

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
