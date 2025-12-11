---
id: 9c426b09-3059-4c49-9892-fafdf50d2f16
name: gitlab-env-info
type: command
executor: bash
data: 'sudo gitlab-rake gitlab:env:info'
output: null
created_at: '2025-12-11T06:10:28.488Z'
updated_at: '2025-12-11T06:10:28.488Z'
platforms:
  - Linux
tags:
  - gitlab
  - diagnostic
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

Displays GitLab environment information including system details, versions, and configurations, used to provide context in vulnerability reports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters needed | No |

## Examples

### Basic Usage

```bash
sudo gitlab-rake gitlab:env:info
```

## Expected Output

System information output including Ruby version, Git version, DB adapter, etc., such as:
Ruby Version: 2.5.3p105
GitLab version: 11.9.4-ee

## Related

- [[tools/GitLab]]
