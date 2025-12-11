---
data: 'gitlab-rake gitlab:env:info'
tags:
  - discovery
type: command
executor: bash
platforms:
  - Linux
id: c309d058-7df0-45dc-9641-397aef025c5b
created_at: '2025-12-11T06:10:22.597Z'
updated_at: '2025-12-11T06:10:22.597Z'
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

Displays GitLab environment information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gitlab:env:info` | Rake task to show system info | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

## Expected Output

System details like Ruby version, GitLab version, etc.

## Related

- [[procedures/Gather-Environment-Information]]
