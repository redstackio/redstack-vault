---
data: 'gitlab-rake gitlab:env:info'
tags:
  - gitlab
  - info
  - recon
type: command
output: >-
  System and GitLab version details, such as Ruby version, GitLab version, DB
  adapter, etc.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.641Z'
id: d0bc7b00-7e15-4296-8d8d-6d8e8dfa476e
verified: false
validated: true
submitted: true
---
# gitlab-rake-gitlab-env-info

## Command

```bash
gitlab-rake gitlab:env:info
```

## Description

This command-line task outputs detailed environment information for a GitLab installation, useful for reporting or verifying setup in vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters needed | No |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Advanced Usage

Run as root or gitlab user on the server.

## Expected Output

System information: git version 2.31.1, ruby 2.7.2p230, rails version 6.0.3.6, etc., including DB adapter and Sidekiq details.

## Related

- [[Related Procedure: Enable-Custom-Emoji-Feature-Flag-in-GitLab]]
