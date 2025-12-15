---
id: cmd-docker-nextcloud
data: 'docker run -p 8081:80 nextcloud:latest'
tags:
  - setup
  - docker
  - container
type: command
output: >-
  Starting Nextcloud container logs, e.g., 'Nextcloud container is starting...'
  and server ready on port 80.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.866Z'
verified: false
validated: true
submitted: true
---
# docker-run-nextcloud-setup

## Command

```bash
docker run -p 8081:80 nextcloud:latest
```

## Description

This command launches a Docker container from the official Nextcloud image, mapping the host's port 8081 to the container's port 80, allowing local access to the Nextcloud web application for vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 8081:80` | Maps host port 8081 to container port 80 for HTTP access | Yes |
| `nextcloud:latest` | Uses the latest official Nextcloud image from Docker Hub | Yes |

## Examples

### Basic Usage

```bash
docker run -p 8081:80 nextcloud:latest
```

### Advanced Usage

```bash
docker run -d -p 8081:80 --name nextcloud-test nextcloud:latest
```

> The -d flag runs in detached mode, and --name assigns a container name for easier management.

## Expected Output

Docker pulls the image if not present, then starts the container with Apache logs: "[Sun Oct 01 ...] AH00558: apache2: Could not reliably determine the server's fully qualified domain name..." followed by "Nextcloud or one of the apps require unencrypted connections..." warnings. The instance is accessible at http://localhost:8081 upon completion.

## Related

- [[Related Procedure|procedures/Setup-Nextcloud-Instance-with-Docker]]
