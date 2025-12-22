---
id: 3ff418a3-bd63-4ef1-a1b3-94156518506d
name: scmkit-list-gitlab-snippets-api-key
type: command
executor: bash
data: SCMKit.exe -s gitlab -m listsnippet -c $_API_KEY -u $_GITLAB_URL
output: null
created_at: '2023-04-06T03:56:25.112429+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - snippets
verified: true
validated: true
---

# scmkit-list-gitlab-snippets-api-key

## Command

```bash
SCMKit.exe -s gitlab -m listsnippet -c $_API_KEY -u $_GITLAB_URL
```

## Description

Lists user-owned snippets in GitLab.

## Parameters

Standard SCMKit parameters.

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m listsnippet -c glpat-abc -u https://gitlab.example.com
```

## Expected Output

JSON list of snippets.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
