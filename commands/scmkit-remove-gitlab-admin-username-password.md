---
id: f1f7a8af-fb85-4608-88ab-15954b4150f3
name: scmkit-remove-gitlab-admin-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m removeadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
  -o $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:25.112916+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - privilege-escalation
verified: true
validated: true
---

# scmkit-remove-gitlab-admin-username-password

## Command

```bash
SCMKit.exe -s gitlab -m removeadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

## Description

Demotes admin role.

## Parameters

Standard.

## Examples

```bash
SCMKit.exe -s gitlab -m removeadmin -c user:pass -u https://gitlab.example.com -o targetuser
```

## Expected Output

Demotion message.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
