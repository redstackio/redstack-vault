---
data: docker-compose up -d
tags:
  - setup
  - docker
type: command
output: Containers started
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.549Z'
id: b1cc88f8-c417-44f8-a89a-0f01fe1fa85a
verified: false
validated: true
submitted: true
---
# start-rocketchat-docker

## Command

```bash
docker-compose up -d
```

## Description

Starts the vulnerable Rocket.Chat instance using Docker Compose in detached mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Detached mode | Yes |

## Examples

### Basic Usage

```bash
docker-compose up -d
```

## Expected Output

Creating network... Creating volume... Starting containers...

## Related

- [[commands/checkout-vulnerable-tag]]
