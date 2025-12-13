---
data: docker-compose up -d
tags:
  - docker
type: command
executor: bash
platforms:
  - Linux
id: 838d4d53-2cf2-4d3b-80eb-282bf90a3245
created_at: '2025-12-13T09:01:22.347Z'
updated_at: '2025-12-13T09:01:22.347Z'
verified: false
validated: true
submitted: true
---
# Docker Compose Up

## Command

```bash
docker-compose up -d
```

## Description

Starts Docker containers in detached mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Detached mode | Yes |

## Examples

### Basic Usage

```bash
docker-compose up -d
```

## Expected Output

Containers started.

## Related

- [[procedures/Setup-Vulnerable-Tomcat-Environment]]
