---
id: 93703f47-9da6-48dd-a348-5da8b540b77f
name: scmkit-list-gitlab-snippets-username-password
type: command
executor: bash
data: 'SCMKit.exe -s gitlab -m listsnippet -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL'
output: null
created_at: '2023-04-06T03:56:25.112379+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - snippets
verified: true
validated: true
---

# scmkit-list-gitlab-snippets-username-password

## Command

```bash
SCMKit.exe -s gitlab -m listsnippet -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

## Description

Lists snippets with basic auth.

## Parameters

Standard.

## Examples

Basic usage example as above.

## Expected Output

Snippet details.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
