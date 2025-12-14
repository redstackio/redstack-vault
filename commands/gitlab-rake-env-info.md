---
id: cmd-uuid-005
name: gitlab-rake-env-info
type: command
executor: bash
data: 'gitlab-rake gitlab:env:info'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.851Z'
platforms:
  - Linux
tags:
  - gitlab
  - info
verified: false
validated: true
submitted: true
---

# gitlab-rake-env-info

## Command

```bash
gitlab-rake gitlab:env:info
```

## Description

Outputs detailed environment information for the GitLab instance, useful for verifying version and configuration post-setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gitlab:env:info` | Rake task for env details | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Advanced Usage

Run in specific Rails environment:
```bash
RAILS_ENV=production gitlab-rake gitlab:env:info
```

## Expected Output

System info including GitLab version (e.g., 12.3.5), Ruby 2.6.3, PostgreSQL 10.9, Redis 3.2.12.

## Related

- [[procedures/Setup-GitLab-Docker-Container]]
