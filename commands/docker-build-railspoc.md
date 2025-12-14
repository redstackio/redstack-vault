---
data: 'docker build -t local/railspoc:latest .'
tags:
  - docker
  - build
type: command
output: Build logs
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.278Z'
id: f04cc1eb-924e-43af-b562-06d37e3f617b
verified: false
validated: true
submitted: true
---
# docker-build-railspoc

## Command

```bash
docker build -t local/railspoc:latest .
```

## Description

Builds the Docker image for the vulnerable Rails app from current directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t | Tag local/railspoc:latest | Yes |

## Examples

### Basic Usage

```bash
docker build -t local/railspoc:latest .
```

## Expected Output

Build logs ending in success.

## Related

- [[commands/docker-run-railspoc]]
