---
id: cmd-docker-run
data: 'docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest'
tags:
  - run
  - docker
type: command
output: Rails server startup logs
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.734Z'
verified: false
validated: true
submitted: true
---
# docker-run-rails-poc

## Command

```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

## Description

Runs the Rails PoC container, mapping port 3000 to 8888 on localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -it | Interactive terminal | Yes |
| --rm | Remove container on exit | Yes |
| -p | Port mapping: 127.0.0.1:8888:3000 | Yes |

## Examples

### Basic Usage

```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

## Expected Output

=> Booting Puma
=> Rails 7.0.4 application starting in production

## Related

- [[commands/docker-build-rails-poc]]
- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]
