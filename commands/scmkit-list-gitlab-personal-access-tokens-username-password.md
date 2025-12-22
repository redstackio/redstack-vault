---
id: 4ccd87f6-3267-4acd-8c6f-e86f1931f6a0
name: scmkit-list-gitlab-personal-access-tokens-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m listpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.113299+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credentials
  - enumeration
verified: true
validated: true
---

# scmkit-list-gitlab-personal-access-tokens-username-password

## Command

```bash
SCMKit.exe -s gitlab -m listpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Lists PATs with credentials.

## Parameters

Standard.

## Examples

Example.

## Expected Output

Token list.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
