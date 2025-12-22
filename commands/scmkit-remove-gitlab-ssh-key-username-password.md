---
id: 2b61a395-7804-42fe-8f1b-07d07d61f108
name: scmkit-remove-gitlab-ssh-key-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m removesshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
  -o $_SSH_KEY_ID
output: null
created_at: '2023-04-06T03:56:25.113704+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - cleanup
  - ssh
verified: true
validated: true
---

# scmkit-remove-gitlab-ssh-key-username-password

## Command

```bash
SCMKit.exe -s gitlab -m removesshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_SSH_KEY_ID
```

## Description

Removes key with auth.

## Parameters

Standard.

## Examples

Example.

## Expected Output

Success.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
