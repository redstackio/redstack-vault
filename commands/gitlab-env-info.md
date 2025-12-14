---
data: 'gitlab-rake gitlab:env:info'
tags:
  - info
  - env
type: command
executor: bash
platforms:
  - Linux
id: fd54550a-104e-4dd8-b0f7-5c3574482d1f
created_at: '2025-12-14T03:46:09.460Z'
updated_at: '2025-12-14T03:46:09.460Z'
verified: false
validated: true
submitted: true
---
# gitlab-env-info

## Command

```bash
gitlab-rake gitlab:env:info
```

## Description

Outputs GitLab environment details for vulnerability reproduction, including versions and config.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gitlab:env:info | Rake task name | Yes |

## Examples

### Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Advanced Usage

Run in GitLab Rails console if needed.

## Expected Output

Details like System: Ubuntu 18.04, Ruby Version: 2.5.3p105, GitLab Version: 11.9.8-ee, DB: PostgreSQL 9.6.11.

## Related

- [[procedures/Trigger-Web-Hook-Tests-with-Wfuzz]]
