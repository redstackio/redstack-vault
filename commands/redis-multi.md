---
id: cmd-redis-multi
data: multi
tags:
  - redis
  - transaction
type: command
output: OK
executor: redis-cli
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.687Z'
verified: false
validated: true
submitted: true
---
---

# redis-multi

## Command

```bash
redis-cli -h 127.0.0.1 -p 6379 multi
```

## Description

Starts a Redis transaction to queue multiple commands for atomic execution, used in the payload to batch queue manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| multi | Initiates transaction | Yes |

## Examples

### Basic Usage

```bash
redis-cli multi
```

### Advanced Usage

In payload: Appended via CRLF after git:// URL.

## Expected Output

OK

## Related

- [[commands/redis-exec]]
- [[procedures/Inject-CRLF-Payload-in-Mirror-URL]]

