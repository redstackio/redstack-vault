---
id: cmd-docker-mattermost-001
data: >-
  docker run --name mattermost-preview -d --publish 8065:8065
  mattermost/mattermost-preview -m=4G
tags:
  - setup
  - docker
type: command
output: 'Container ID and running status; server accessible at http://localhost:8065'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T05:32:10.467Z'
verified: false
validated: true
submitted: true
---
# docker-run-mattermost

## Command

```bash
docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G
```

## Description

This command starts a Mattermost preview server in a detached Docker container with a 4GB memory limit, publishing port 8065 for access. It is used to set up a vulnerable environment for DoS testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--name mattermost-preview` | Specifies the container name | Yes |
| `-d` | Runs in detached (background) mode | Yes |
| `--publish 8065:8065` | Maps host port 8065 to container port 8065 | Yes |
| `-m=4G` | Sets memory limit to 4GB | Yes |
| `mattermost/mattermost-preview` | The Docker image to use | Yes |

## Examples

### Basic Usage

```bash
docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G
```

### Advanced Usage

```bash
docker run --name mattermost-preview -d --publish 8065:8065 --memory=4g --cpus=2 mattermost/mattermost-preview
```

## Expected Output

A long hexadecimal container ID is printed, followed by confirmation of the container running. Use `docker ps` to verify status.

## Related

- [[procedures/Setup-Mattermost-Docker-Environment]]
