---
id: cmd-uuid-002
name: docker-exec-gitlab-bash
type: command
executor: bash
data: docker exec -it gitlab /bin/bash
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.862Z'
platforms:
  - Linux
tags:
  - docker
  - shell
verified: false
validated: true
submitted: true
---

# docker-exec-gitlab-bash

## Command

```bash
docker exec -it gitlab /bin/bash
```

## Description

Executes an interactive bash shell in the 'gitlab' Docker container for internal access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive with TTY | Yes |
| `gitlab` | Container name | Yes |
| `/bin/bash` | Shell to run | Yes |

## Examples

### Basic Usage

```bash
docker exec -it gitlab /bin/bash
```

### Advanced Usage

Run a single command instead:
```bash
docker exec -it gitlab whoami
```

## Expected Output

Interactive shell prompt (e.g., root@gitlab:/#).

## Related

- [[commands/docker-run-gitlab-setup]]
- [[procedures/Access-GitLab-Container-Shell]]
