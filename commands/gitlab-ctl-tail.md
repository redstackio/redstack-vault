---
id: cmd-gitlab-ctl-tail
data: sudo gitlab-ctl tail
tags:
  - logs
  - monitoring
  - gitlab
type: command
output: Live log output from GitLab services
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.588Z'
verified: false
validated: true
submitted: true
---
# gitlab-ctl-tail

## Command

```bash
sudo gitlab-ctl tail
```

## Description

Tails all GitLab service logs (e.g., sidekiq, nginx, rails) in real-time using the gitlab-ctl tool, useful for observing exploitation during bulk imports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Elevated privileges | Yes |
| gitlab-ctl | GitLab control utility | Yes |
| tail | Follow logs continuously | Yes |

## Examples

### Basic Usage

```bash
sudo gitlab-ctl tail
```

### Advanced Usage

Tail specific service: `sudo gitlab-ctl tail sidekiq`.

## Expected Output

Multi-pane output streaming logs from services; Ctrl+C to stop.

## Related

- [[procedures/Monitor-GitLab-Logs-for-Exploitation]]
