---
type: command
executor: bash
data: 'docker run -it $_REGISTRY_HOST/$_REPO_NAME:$_TAG /bin/bash'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - run
  - container
verified: true
validated: true
---

# docker-run-container

## Command

```bash
docker run -it $_REGISTRY_HOST/$_REPO_NAME:$_TAG /bin/bash
```

## Description

Runs a pulled image as an interactive container with a bash shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGISTRY_HOST | Registry host | Yes |
| $_REPO_NAME | Repo name | Yes |
| $_TAG | Tag | No |
| -it | Interactive with TTY | No |
| /bin/bash | Entry command | No |

## Examples

### Interactive Run

```bash
docker run -it docker.registry.local/wordpress-image /bin/bash
```

## Expected Output

Drops into container shell: root@container:/# 

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
