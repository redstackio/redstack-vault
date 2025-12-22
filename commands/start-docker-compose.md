---
data: docker-compose up -d
tags:
  - setup
  - docker
type: command
output: Starting containers...
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.795Z'
id: 9b90e453-fdc0-4f01-87ca-5605ba0cf137
verified: false
validated: true
submitted: true
---
# start-docker-compose

## Command

```bash
docker-compose up -d
```

## Description

Launches the Rocket.Chat instance in detached mode using Docker Compose.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Detached/background mode | Yes |

## Examples

### Basic Usage

```bash
docker-compose up -d
```

## Expected Output

Containers up, Rocket.Chat on port 3000.

## Related

- [[commands/checkout-vulnerable-version]]
