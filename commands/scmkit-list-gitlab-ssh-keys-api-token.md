---
id: 4da48782-6d39-4f69-b583-68e799a1f8e7
name: scmkit-list-gitlab-ssh-keys-api-token
type: command
executor: bash
data: SCMKit.exe -s gitlab -m listsshkey -c $_API_TOKEN -u $_GITLAB_URL
output: null
created_at: '2023-04-06T03:56:25.113654+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - ssh
verified: true
validated: true
---

# scmkit-list-gitlab-ssh-keys-api-token

## Command

```bash
SCMKit.exe -s gitlab -m listsshkey -c $_API_TOKEN -u $_GITLAB_URL
```

## Description

Lists SSH keys.

## Parameters

Standard.

## Examples

List keys.

## Expected Output

Key list with IDs.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
