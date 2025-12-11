---
data: 'gitlab-rake gitlab:env:info'
tags:
  - recon
  - gitlab
type: command
executor: bash
platforms:
  - Linux
id: 35650534-aef7-4402-89eb-30a37673bd5e
created_at: '2025-12-11T03:47:39.855Z'
updated_at: '2025-12-11T03:47:39.855Z'
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

Runs a Rake task to display GitLab environment information, including versions and configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gitlab:env:info` | The Rake task to execute | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

## Expected Output

System details like Ruby version, Git version, GitLab version, etc.

## Related

- [[procedures/Gather-GitLab-Environment-Information]]
