---
data: docker exec -ti e1a bash
tags:
  - access
type: command
executor: bash
platforms:
  - Linux
id: deaf2051-bc06-4e83-9c67-68878055df21
created_at: '2025-12-11T06:10:22.627Z'
updated_at: '2025-12-11T06:10:22.627Z'
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

Enters an interactive bash shell in a running Docker container for verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exec` | Run a command in a running container | Yes |
| `-ti` | Allocate a pseudo-TTY and keep STDIN open | Yes |
| `e1a` | Container name | Yes |
| `bash` | Command to run | Yes |

## Examples

### Basic Usage

```bash
docker exec -ti container bash
```

## Expected Output

Opens a bash shell inside the container.

## Related

- [[procedures/Verify-File-Overwrite]]
