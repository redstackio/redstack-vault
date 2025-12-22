---
id: f0efef77-e1c3-4ac8-9d99-05afa56d3d46
name: scmkit-create-gitlab-ssh-key-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m createsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
  -o "$_SSH_PUBLIC_KEY"
output: null
created_at: '2023-04-06T03:56:25.113514+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - ssh
verified: true
validated: true
---

# scmkit-create-gitlab-ssh-key-username-password

## Command

```bash
SCMKit.exe -s gitlab -m createsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o "$_SSH_PUBLIC_KEY"
```

## Description

Creates SSH key with basic auth.

## Parameters

Standard.

## Examples

Example.

## Expected Output

Success.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
