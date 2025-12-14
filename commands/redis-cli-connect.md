---
id: cmd-redis-connect
data: redis-cli -h localhost -p 6379
tags:
  - redis
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.481Z'
verified: false
validated: true
submitted: true
---
# redis-cli-connect

## Command

```bash
redis-cli -h localhost -p 6379
```

## Description

Establishes a connection to a Redis server using the Redis CLI, allowing interaction with databases and queues like Sidekiq in GitLab. Use this to access internal job queues for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-h <host>` | Redis server hostname (default: localhost) | No |
| `-p <port>` | Redis server port (default: 6379) | No |

## Examples

### Basic Usage

```bash
redis-cli -h localhost -p 6379
```

### Advanced Usage

```bash
redis-cli -h 192.168.1.100 -p 6379 -a password
```

## Expected Output

Interactive prompt like `localhost:6379>`, ready for Redis commands. Errors if connection fails (e.g., connection refused).

## Related

- [[commands/rpush-gitlab-shell-job]]
- [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]
