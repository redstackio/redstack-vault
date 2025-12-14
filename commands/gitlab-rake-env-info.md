---
data: 'gitlab-rake gitlab:env:info'
tags:
  - gitlab
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.971Z'
id: 87f1bbad-fb58-4da6-b9a7-55775dc737d9
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

Runs a GitLab rake task to output detailed environment information, useful for verifying access and gathering version/system details post-RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gitlab:env:info` | Rake task name for environment info | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Advanced Usage

Run within SSH session after access.

## Expected Output

Multi-section output: System Info (OS, Ruby 2.6.3), Packages (GitLab 12.4.2-ee, PostgreSQL 10.9, Redis 3.2.12), GitLab Info, Shell Config.

## Related

- [[commands/ssh-gitlab-access]]
- [[procedures/Establish-SSH-Access-to-GitLab-Server]]
