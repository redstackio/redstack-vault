---
id: new-id-for-privs
name: scmkit-get-gitlab-token-privileges-api-key
type: command
executor: bash
data: SCMKit.exe -s gitlab -m privs -c $_API_KEY -u $_GITLAB_URL
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - privileges
  - discovery
verified: true
validated: true
---

# scmkit-get-gitlab-token-privileges-api-key

## Command

```bash
SCMKit.exe -s gitlab -m privs -c $_API_KEY -u $_GITLAB_URL
```

## Description

Retrieves privileges and scopes for a GitLab API key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m privs | Privileges mode | Yes |

## Examples

```bash
SCMKit.exe -s gitlab -m privs -c glpat-abc -u https://gitlab.example.com
```

## Expected Output

Scopes like {"scopes": ["read_api"]}.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
