---
id: 92e5efb0-1b09-49c0-a688-5eca0ba1a572
name: scmkit-create-gitlab-personal-access-token-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m createpat -c $_API_KEY -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.113145+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - credentials
verified: true
validated: true
---

# scmkit-create-gitlab-personal-access-token-api-key

## Command

```bash
SCMKit.exe -s gitlab -m createpat -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Creates a personal access token for a user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m createpat | Create PAT mode | Yes |
| -o $_TARGET_USERNAME | Target user | Yes |

## Examples

Basic creation.

## Expected Output

New token: glpat-newtoken.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
