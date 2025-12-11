---
data: 'docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash'
tags:
  - docker
  - kibana
type: command
executor: bash
platforms:
  - Linux
id: 5a5d5ff4-d45a-44f7-be72-64d69f242bd6
created_at: '2025-12-11T03:47:47.800Z'
updated_at: '2025-12-11T03:47:47.800Z'
verified: false
validated: true
submitted: true
---
# docker-run-kibana

## Command

```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

## Description

Runs a Docker container for Kibana version 7.12.0 in interactive mode with a bash shell, used to set up the environment for accessing the headless Chromium binary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rm` | Remove container after exit | No |
| `-it` | Interactive terminal | Yes |
| `docker.elastic.co/kibana/kibana:7.12.0` | Image name and tag | Yes |
| `bash` | Command to run inside container | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

## Expected Output

Enters bash shell inside the container.

## Related

- [[procedures/Set-Up-Kibana-Docker-Environment]]
- [[commands/cd-to-headless-shell]]
