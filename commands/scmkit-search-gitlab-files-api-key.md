---
id: 5cae740d-d4f3-43a8-8634-c0f1004586be
name: scmkit-search-gitlab-files-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s gitlab -m searchfile -c $_API_KEY -u $_GITLAB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.112279+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - files
verified: true
validated: true
---

# scmkit-search-gitlab-files-api-key

## Command

```bash
SCMKit.exe -s gitlab -m searchfile -c $_API_KEY -u $_GITLAB_URL -o $_SEARCH_TERM
```

## Description

Searches file names in GitLab repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o $_SEARCH_TERM | File name keyword | Yes |

(Other parameters as standard.)

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m searchfile -c glpat-abc -u https://gitlab.example.com -o config
```

## Expected Output

List of matching files with paths.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
