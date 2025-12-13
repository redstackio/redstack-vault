---
data: >-
  docker exec -it hrs_tomcat_11 /bin/sh -c "cat
  /usr/local/tomcat/logs/localhost*"
tags:
  - docker
  - logging
type: command
executor: bash
platforms:
  - Linux
id: a21ec81d-6050-44cd-b915-d00c4e105fa8
created_at: '2025-12-13T09:01:22.395Z'
updated_at: '2025-12-13T09:01:22.395Z'
verified: false
validated: true
submitted: true
---
# docker-exec-cat-tomcat-logs

## Command

```bash
docker exec -it hrs_tomcat_11 /bin/sh -c "cat /usr/local/tomcat/logs/localhost*"
```

## Description

Executes a shell command inside the running Docker container to display the contents of Tomcat's localhost access logs, used to verify the success of the request smuggling by checking if the smuggled request appears in the logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive mode with pseudo-TTY | Yes |
| `/bin/sh -c` | Run command in shell | Yes |
| `cat /usr/local/tomcat/logs/localhost*` | Concatenate and display log files | Yes |

## Examples

### Basic Usage

```bash
docker exec -it hrs_tomcat_11 /bin/sh -c "cat /usr/local/tomcat/logs/localhost*"
```

## Expected Output

Log entries showing processed requests, e.g., 'POST /benign_path HTTP/1.1' 404 and 'GET /evil_path HTTP/1.1' 404.

## Related

- [[procedures/Verify-Exploitation-by-Checking-Tomcat-Logs]]
- [[tools/Docker]]
