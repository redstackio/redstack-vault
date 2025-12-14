---
data: 'docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest'
tags:
  - docker
  - run
type: command
output: Container startup and Rails server logs
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.275Z'
id: c1847b20-0ff2-45c2-bd9f-53eb8aeada37
verified: false
validated: true
submitted: true
---
# docker-run-railspoc

## Command

```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

## Description

Runs the vulnerable Rails container with port mapping and interactive mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Port map 127.0.0.1:8888:3000 | Yes |
| -it | Interactive | Yes |
| --rm | Remove on exit | Yes |

## Examples

### Basic Usage

```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

## Expected Output

Container startup and server logs.

## Related

- [[commands/docker-build-railspoc]]
