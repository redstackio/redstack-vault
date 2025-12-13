---
data: sudo docker-compose up --build
tags:
  - docker
  - setup
type: command
executor: bash
platforms:
  - Linux
id: de18328a-fed5-4d2c-914f-2cd0f31c7a01
created_at: '2025-12-13T09:01:17.103Z'
updated_at: '2025-12-13T09:01:17.103Z'
verified: false
validated: true
submitted: true
---
# docker-compose-up-build

## Command

```bash
sudo docker-compose up --build
```

## Description

Starts Docker containers for the proof-of-concept environment, building images if necessary, used to set up Node.js and ATS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `up` | Start containers | Yes |
| `--build` | Build images before starting | Yes |

## Examples

### Basic Usage

```bash
sudo docker-compose up --build
```

## Expected Output

Docker containers running, with Node on 8081 and ATS on 8080.

## Related

- [[procedures/Set-Up-PoC-Environment-for-Node-js-and-ATS]]
- [[tools/docker-compose]]
