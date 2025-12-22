---
id: 56bb9e04-7bad-4e0f-9030-3140afe0d502
name: scmkit-list-gitlab-personal-access-tokens-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m listpat -c $_API_KEY -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.113349+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credentials
  - enumeration
verified: true
validated: true
---

# scmkit-list-gitlab-personal-access-tokens-api-key

## Command

```bash
SCMKit.exe -s gitlab -m listpat -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Lists PATs for a user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o $_TARGET_USERNAME | User to list for | Yes |

## Examples

List tokens.

## Expected Output

Array of tokens.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
