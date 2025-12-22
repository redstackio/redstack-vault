---
id: 1e52eee9-e835-421a-b47b-59500ef839e9
name: scmkit-list-gitlab-ssh-keys-username-password
type: command
executor: bash
data: 'SCMKit.exe -s gitlab -m listsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL'
output: null
created_at: '2023-04-06T03:56:25.113610+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - ssh
verified: true
validated: true
---

# scmkit-list-gitlab-ssh-keys-username-password

## Command

```bash
SCMKit.exe -s gitlab -m listsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

## Description

Lists keys with credentials.

## Parameters

Standard.

## Examples

Example.

## Expected Output

Keys listed.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
