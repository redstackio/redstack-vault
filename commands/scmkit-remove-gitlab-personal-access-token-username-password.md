---
id: c91f454d-7338-4f9d-b129-9f97efce00ac
name: scmkit-remove-gitlab-personal-access-token-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m removepat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o
  $_PAT_ID
output: null
created_at: '2023-04-06T03:56:25.113189+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - cleanup
  - credentials
verified: true
validated: true
---

# scmkit-remove-gitlab-personal-access-token-username-password

## Command

```bash
SCMKit.exe -s gitlab -m removepat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_PAT_ID
```

## Description

Removes a specific PAT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o $_PAT_ID | ID of PAT to remove | Yes |

## Examples

Remove token.

## Expected Output

Removal confirmation.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
