---
id: uuid-gitlab-env
data: 'sudo gitlab-rake gitlab:env:info'
tags:
  - gitlab
  - environment
type: command
output: null
executor: bash
platforms:
  - Linux
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.126Z'
verified: false
validated: true
submitted: true
---
# gitlab-env-info

## Command

```bash
sudo gitlab-rake gitlab:env:info
```

## Description

Rake task to gather GitLab environment details including versions and configuration for vulnerability reproduction reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default info collection | No |

## Examples

### Basic Usage

```bash
sudo gitlab-rake gitlab:env:info
```

## Expected Output

System information: OS (Ubuntu 16.04), Ruby (2.6.5), GitLab (12.10.0-ee), PostgreSQL (11.7), etc.

## Related

- [[procedures/Verify-Repository-Deletion]]
