---
id: 0cac8a34-b27b-4480-9b20-625e2a59d00b
name: scmkit-list-gitlab-runners-api-key
type: command
executor: bash
data: SCMKit.exe -s gitlab -m listrunner -c $_API_KEY -u $_GITLAB_URL
output: null
created_at: '2023-04-06T03:56:25.112619+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - ci-cd
verified: true
validated: true
---

# scmkit-list-gitlab-runners-api-key

## Command

```bash
SCMKit.exe -s gitlab -m listrunner -c $_API_KEY -u $_GITLAB_URL
```

## Description

Lists available GitLab runners for CI/CD analysis.

## Parameters

Standard.

## Examples

```bash
SCMKit.exe -s gitlab -m listrunner -c glpat-abc -u https://gitlab.example.com
```

## Expected Output

Runner list with IDs and descriptions.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
