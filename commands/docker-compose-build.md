---
data: docker-compose build
tags:
  - docker
type: command
executor: bash
platforms:
  - Linux
id: ad11e3c1-a69f-486a-b7dc-e4913ddfad65
created_at: '2025-12-13T09:01:22.350Z'
updated_at: '2025-12-13T09:01:22.350Z'
verified: false
validated: true
submitted: true
---
# Docker Compose Build

## Command

```bash
docker-compose build
```

## Description

Builds Docker images defined in docker-compose.yml for the Tomcat environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | N/A | No |

## Examples

### Basic Usage

```bash
docker-compose build
```

## Expected Output

Docker images built successfully.

## Related

- [[procedures/Setup-Vulnerable-Tomcat-Environment]]
