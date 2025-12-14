---
id: uuid-5
data: 'docker run -p 8081:80 nextcloud:latest'
tags:
  - setup
  - container
type: command
output: 'Nextcloud instance running and accessible at http://localhost:8081'
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.331Z'
verified: false
validated: true
submitted: true
---
# docker-run-nextcloud

## Command

```bash
docker run -p 8081:80 nextcloud:latest
```

## Description

This command starts a Docker container with the latest Nextcloud image, mapping the host's port 8081 to the container's port 80, enabling local web access for vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 8081:80` | Maps host port 8081 to container port 80 for HTTP access | Yes |
| `nextcloud:latest` | Specifies the official Nextcloud Docker image tag | Yes |

## Examples

### Basic Usage

```bash
docker run -p 8081:80 nextcloud:latest
```

### Advanced Usage

```bash
docker run -d -p 8081:80 --name nextcloud-test nextcloud:latest
```

> Adds detached mode (-d) and names the container.

## Expected Output

Docker logs show the container starting, Apache initializing, and Nextcloud ready. Access http://localhost:8081 to see the setup page or login.

## Related

- [[Related Procedure: Set-Up-Nextcloud-Instance-with-Docker]]
