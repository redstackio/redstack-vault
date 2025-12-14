---
data: 'gitlab-rake gitlab:env:info'
tags:
  - gitlab
  - env
type: command
output: 'System info, GitLab version, components like Ruby, PostgreSQL, etc.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.956Z'
id: 8df5fc71-adb4-4345-80fa-b66ce2a305ad
verified: false
validated: true
submitted: true
---
# gitlab-rake-env

## Command

```bash
gitlab-rake gitlab:env:info
```

## Description

Runs the GitLab rake task to output environment information, verifying the installation context in the root shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gitlab:env:info | Rake task for env details | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Advanced Usage

```bash
gitlab-rake gitlab:check
```

## Expected Output

'GitLab information
System: Ubuntu 20.04
GitLab version: 14.x
...
Database: PostgreSQL
Redis: Yes
...'

## Related

- [[commands/ls-explore]]
- [[procedures/Capture-and-Verify-Root-Shell]]
