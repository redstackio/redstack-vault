---
data: docker-compose up -d
tags:
  - setup
  - docker
type: command
output: |-
  Starting rocketchat_mongo_1 ... done
  Starting rocketchat_rocketchat_1 ... done
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.410Z'
id: 8bd685bd-48b2-423a-b1d4-5e0e29aeb50c
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

Launches the vulnerable Rocket.Chat instance in detached mode using Docker Compose.

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

Containers started; instance at http://localhost:3000.

## Related

- [[commands/git-checkout-vulnerable-version]]
