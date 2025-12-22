---
id: 7c401dec-11e2-47dc-b395-0fcb5e55eed0
name: scmkit-search-gitlab-files-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m searchfile -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.112208+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - files
verified: true
validated: true
---

# scmkit-search-gitlab-files-username-password

## Command

```bash
SCMKit.exe -s gitlab -m searchfile -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_SEARCH_TERM
```

## Description

File search in GitLab using credentials.

## Parameters

Similar to API key version.

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m searchfile -c user:pass -u https://gitlab.example.com -o secret
```

## Expected Output

File matches.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
