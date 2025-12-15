---
id: cmd-docker-run-mattermost
data: >-
  docker run --name mattermost-preview -d --publish 8065:8065
  mattermost/mattermost-preview -m=4G
tags:
  - setup
  - docker
type: command
output: >-
  Container ID and running status; Mattermost server accessible at
  http://localhost:8065
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.345Z'
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

Starts a Docker container with the Mattermost preview image in detached mode, mapping port 8065, and limiting memory to 4GB for vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--name mattermost-preview` | Names the container | Yes |
| `-d` | Detached mode | Yes |
| `--publish 8065:8065` | Port mapping | Yes |
| `-m=4G` | Memory limit | Yes |

## Examples

### Basic Usage

```bash
docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G
```

### Advanced Usage

Add volume for persistence: `docker run ... -v /path/to/data:/mattermost/data`

## Expected Output

Container ID printed, e.g., "abc123def456"; use `docker ps` to confirm running.

## Related

- [[procedures/Set-Up-Mattermost-Docker-Environment]]
