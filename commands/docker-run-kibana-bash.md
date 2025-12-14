---
data: 'docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash'
tags:
  - docker
  - kibana
type: command
output: bash-4.4# prompt inside container
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.217Z'
id: 32341434-fa65-4def-ae51-1f60c5d7e8b3
verified: false
validated: true
submitted: true
---
# docker-run-kibana-bash

## Command

```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

## Description

Launches a Kibana 7.12.0 Docker container in interactive bash mode to access the embedded Chromium for testing RCE in the reporting plugin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rm` | Remove container after exit | Yes |
| `-it` | Interactive terminal with TTY | Yes |
| Image | docker.elastic.co/kibana/kibana:7.12.0 | Yes |
| `bash` | Entry point to bash shell | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

### Advanced Usage

```bash
docker run --rm -it -p 5601:5601 docker.elastic.co/kibana/kibana:7.12.0 bash
```

## Expected Output

Enters container with 'bash-4.4#' prompt, ready for navigation to Chromium directory.

## Related

- [[commands/cd-to-chromium-directory]]
- [[procedures/Run-Kibana-Docker-Container-and-Test-Chromium]]
