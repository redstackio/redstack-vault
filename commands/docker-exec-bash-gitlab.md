---
id: uuid-docker-exec
data: docker exec -it gitlab /bin/bash
tags:
  - docker
  - shell-access
type: command
output: Interactive bash prompt inside the container
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:24.486Z'
verified: false
validated: true
submitted: true
---
# docker-exec-bash-gitlab

## Command

```bash
docker exec -it gitlab /bin/bash
```

## Description

Executes an interactive bash shell inside the running GitLab container for administrative tasks like accessing Rails console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive mode with TTY | Yes |
| `gitlab` | Container name | Yes |
| `/bin/bash` | Shell to start | Yes |

## Examples

### Basic Usage

```bash
docker exec -it gitlab /bin/bash
```

### Advanced Usage

Exec with specific user:

```bash
docker exec -it --user root gitlab /bin/bash
```

## Expected Output

Interactive bash prompt (e.g., root@gitlab:/#) inside the container environment.

## Related

- [[Related Procedure: Enable-Vue-Issuables-List-Feature-Flag]]
