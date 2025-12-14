---
data: >-
  docker run --detach --hostname gitlab.example.com --publish 443:443 --publish
  80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
tags:
  - setup
  - container
type: command
output: Container ID and running GitLab instance
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.362Z'
id: e89c1f01-9c6a-4a9d-8af6-9984e9e4eb9b
verified: false
validated: true
submitted: true
---
# docker-run-gitlab-instance

## Command

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

## Description

Starts a detached GitLab CE container with specified hostname and exposed ports for HTTPS, HTTP, and SSH, used for local vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--detach` | Run container in background | Yes |
| `--hostname` | Set container hostname to gitlab.example.com | Yes |
| `--name gitlab` | Name the container 'gitlab' | Yes |
| `--publish 22:22` | Expose SSH port | Yes |
| `--publish 80:80` | Expose HTTP port | Yes |
| `--publish 443:443` | Expose HTTPS port | Yes |
| `gitlab/gitlab-ce:latest` | Use latest GitLab Community Edition image | Yes |

## Examples

### Basic Usage

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

### Advanced Usage

Add volume mounts for persistence:

```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab -v /srv/gitlab:/var/opt/gitlab gitlab/gitlab-ce:latest
```

## Expected Output

Container ID printed, e.g., 'a1b2c3d4e5f6...', and GitLab starts initializing (logs show progress).

## Related

- [[Related Procedure|procedures/Setup-GitLab-Instance-with-Docker]]
