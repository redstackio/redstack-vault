---
id: cmd-redis-stop-replica
name: redis-replicaof-stop
type: command
executor: redis-cli
data: REPLICAOF no one\n\n
output: Replication stopped
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.312Z'
platforms:
  - Linux
tags:
  - redis
  - cleanup
verified: false
validated: true
submitted: true
---

# redis-replicaof-stop

## Command

```bash
REPLICAOF no one\n\n
```

## Description

Disables Redis replication after testing to prevent ongoing data transfer.

## Parameters

None.

## Examples

### Basic Usage

As shown.

## Expected Output

OK, replication halted.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]
