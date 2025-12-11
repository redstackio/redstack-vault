---
data: docker exec -ti e1a bash
tags:
  - access
  - docker
type: command
executor: bash
platforms:
  - Linux
id: f7d5ae14-d0b8-44a1-b748-d92f1fe2d5db
created_at: '2025-12-11T03:47:39.976Z'
updated_at: '2025-12-11T03:47:39.976Z'
verified: false
validated: true
submitted: true
---
# docker-exec-bash

## Command

```bash
docker exec -ti e1a bash
```

## Description

Enters an interactive bash shell in a running Docker container for verification and access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ti` | Allocates a pseudo-TTY and keeps STDIN open | Yes |
| `e1a` | Container name or ID | Yes |
| `bash` | Command to run (bash shell) | Yes |

## Examples

### Basic Usage

```bash
docker exec -ti e1a bash
```

## Expected Output

Opens a bash prompt inside the container.

## Related

- [[procedures/Verify-Authorized-Keys-Overwrite]]
