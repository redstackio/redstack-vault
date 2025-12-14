---
id: cmd-redis-exec
data: exec
tags:
  - redis
  - transaction
type: command
output: OK
executor: redis-cli
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.670Z'
verified: false
validated: true
submitted: true
---
---

# redis-exec

## Command

```bash
redis-cli -h 127.0.0.1 -p 6379 exec
```

## Description

Executes all queued commands in the Redis transaction, applying the queue injection for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| exec | Executes transaction | Yes |

## Examples

### Basic Usage

```bash
redis-cli exec
```

### Advanced Usage

After MULTI and commands in payload.

## Expected Output

OK

## Related

- [[commands/redis-multi]]
- [[procedures/Inject-CRLF-Payload-in-Mirror-URL]]

