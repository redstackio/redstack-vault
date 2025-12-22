---
id: d15794cd-08b0-4359-94f0-85d510788de4
name: scmkit-list-gitlab-runners-username-password
type: command
executor: bash
data: 'SCMKit.exe -s gitlab -m listrunner -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL'
output: null
created_at: '2023-04-06T03:56:25.112541+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - ci-cd
verified: true
validated: true
---

# scmkit-list-gitlab-runners-username-password

## Command

```bash
SCMKit.exe -s gitlab -m listrunner -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

## Description

Lists runners with credentials.

## Parameters

Standard.

## Examples

Basic example.

## Expected Output

Runner details.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
