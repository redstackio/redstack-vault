---
id: d48c5d55-79d8-4db1-9905-da69ed818092
name: scmkit-remove-gitlab-ssh-key-api-token
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m removesshkey -c $_API_TOKEN -u $_GITLAB_URL -o
  $_SSH_KEY_ID
output: null
created_at: '2023-04-06T03:56:25.113763+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - cleanup
  - ssh
verified: true
validated: true
---

# scmkit-remove-gitlab-ssh-key-api-token

## Command

```bash
SCMKit.exe -s gitlab -m removesshkey -c $_API_TOKEN -u $_GITLAB_URL -o $_SSH_KEY_ID
```

## Description

Removes an SSH key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o $_SSH_KEY_ID | Key ID | Yes |

## Examples

Remove key.

## Expected Output

Removed.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
