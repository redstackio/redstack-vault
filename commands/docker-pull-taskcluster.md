---
data: 'docker pull taskcluster/taskcluster:v15.0.0-20-g0eca18b7c'
tags:
  - docker
  - pull
type: command
executor: bash
platforms:
  - Linux
  - Docker
id: d74ecf05-5f56-4bb6-aaff-56e6d95ac95f
created_at: '2025-12-14T17:31:42.938Z'
updated_at: '2025-12-14T17:31:42.938Z'
verified: false
validated: true
submitted: true
---
# docker-pull-taskcluster

## Command

```bash
docker pull taskcluster/taskcluster:v15.0.0-20-g0eca18b7c
```

## Description

Pulls a specific TaskCluster Docker image from Docker Hub by tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `taskcluster/taskcluster` | Repository name | Yes |
| `:v15.0.0-20-g0eca18b7c` | Image tag | Yes |

## Examples

### Basic Usage

```bash
docker pull taskcluster/taskcluster:v15.0.0-20-g0eca18b7c
```

### Advanced Usage

```bash
docker pull taskcluster/taskcluster:c061025dc
```

## Expected Output

Status messages like "v15.0.0-20-g0eca18b7c: Pulling from taskcluster/taskcluster" followed by layer downloads and "Status: Downloaded newer image".

## Related

- [[commands/docker-inspect-image-file]]
