---
id: cmd-uuid-001
name: docker-run-gitlab-setup
type: command
executor: bash
data: >-
  docker run --detach --hostname gitlab.example.com --publish 443:443 --publish
  80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.866Z'
platforms:
  - Linux
tags:
  - docker
  - setup
verified: false
validated: true
submitted: true
---

# docker-run-gitlab-setup

## Command

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

## Description

Deploys a GitLab CE container in detached mode with hostname and port mappings for reproduction of SSRF vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--detach` | Run in background | Yes |
| `--hostname gitlab.example.com` | Set container hostname | Yes |
| `--publish 443:443` | Map HTTPS port | Yes |
| `--publish 80:80` | Map HTTP port | Yes |
| `--publish 22:22` | Map SSH port | Yes |
| `--name gitlab` | Name the container | Yes |
| `gitlab/gitlab-ce:latest` | Image to use | Yes |

## Examples

### Basic Usage

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

### Advanced Usage

Add volume mounts for persistence:
```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab -v /srv/gitlab/config:/etc/gitlab gitlab/gitlab-ce:latest
```

## Expected Output

Container ID (e.g., "a1b2c3d4e5f6...") and startup logs if not detached.

## Related

- [[commands/docker-exec-gitlab-bash]]
- [[procedures/Setup-GitLab-Docker-Container]]
