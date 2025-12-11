---
data: 'sudo gitlab-rake gitlab:env:info'
tags:
  - gitlab
  - recon
type: command
executor: bash
platforms:
  - Linux
id: 466b83c8-12aa-4995-a909-c7b50fee2a5b
created_at: '2025-12-11T03:47:56.424Z'
updated_at: '2025-12-11T03:47:56.424Z'
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

This command outputs detailed information about the GitLab environment, including system details, versions, and configurations, used for reproducibility in vulnerability reports.

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

System information such as OS, Ruby version, GitLab version, PostgreSQL version, Redis version, etc.

## Related

- [[procedures/Exploit-Stored-XSS-in-GitLab-Kroki]]
