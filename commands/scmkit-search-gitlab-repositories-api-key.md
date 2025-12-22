---
id: a0d8d26b-d139-4511-9a8e-b8adc6fe75da
name: scmkit-search-gitlab-repositories-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m searchrepo -c $_API_KEY -u $_GITLAB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.111905+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - discovery
verified: true
validated: true
---

# scmkit-search-gitlab-repositories-api-key

## Command

```bash
SCMKit.exe -s gitlab -m searchrepo -c $_API_KEY -u $_GITLAB_URL -o $_SEARCH_TERM
```

## Description

Searches GitLab repositories for a specific term using API key authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s gitlab | SCM system | Yes |
| -m searchrepo | Search repositories mode | Yes |
| -c $_API_KEY | API key | Yes |
| -u $_GITLAB_URL | GitLab URL | Yes |
| -o $_SEARCH_TERM | Keyword to search (e.g., "secret") | Yes |

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m searchrepo -c glpat-abc -u https://gitlab.example.com -o password
```

## Expected Output

Filtered repositories matching the term.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
