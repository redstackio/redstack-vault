---
data: sudo gitlab-ctl tail
tags:
  - monitoring
type: command
executor: bash
platforms:
  - Linux
id: 3d11ce1f-ce68-4fd9-8b70-8c3a18e4eb0b
created_at: '2025-12-11T03:48:06.001Z'
updated_at: '2025-12-11T03:48:06.001Z'
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

Tails GitLab service logs for real-time monitoring.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) |  | No |

## Examples

### Basic Usage

```bash
sudo gitlab-ctl tail
```

## Expected Output

Streaming logs

## Related

- [[procedures/Setup-GitLab-Environment-for-Testing]]
