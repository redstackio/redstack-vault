---
id: cmd-docker-compose-up
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
updated_at: '2025-12-14T03:46:19.900Z'
verified: false
validated: true
submitted: true
---
# docker-compose-up-detached

## Command

```bash
docker-compose up -d
```

## Description

Launches the vulnerable Rocket.Chat instance and MongoDB in detached mode using Docker Compose for local testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Detached (background) mode | Yes |

## Examples

### Basic Usage

```bash
docker-compose up -d
```

## Expected Output

Containers started; Rocket.Chat accessible on http://localhost:3000.

## Related

- [[commands/git-checkout-vulnerable-version]]
