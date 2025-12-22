---
id: ed957dcd-8d54-4cca-b2a6-edded50ede1e
name: scmkit-create-gitlab-personal-access-token-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m createpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.113036+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - credentials
verified: true
validated: true
---

# scmkit-create-gitlab-personal-access-token-username-password

## Command

```bash
SCMKit.exe -s gitlab -m createpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Creates PAT with basic auth.

## Parameters

Standard.

## Examples

Example usage.

## Expected Output

Token generated.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
