---
id: ae48e147-85f1-4e57-ae20-a318ce8ce833
name: scmkit-search-github-repositories-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s github -m searchrepo -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.111850+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - discovery
verified: true
validated: true
---

# scmkit-search-github-repositories-username-password

## Command

```bash
SCMKit.exe -s github -m searchrepo -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o $_SEARCH_TERM
```

## Description

Searches GitHub repositories using username/password; adaptable for multi-SCM enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s github | SCM system | Yes |
| -m searchrepo | Search mode | Yes |
| -c $_USERNAME:$_PASSWORD | Credentials | Yes |
| -u $_GITHUB_URL | GitHub URL | Yes |
| -o $_SEARCH_TERM | Search keyword | Yes |

## Examples

### Basic Usage

```bash
SCMKit.exe -s github -m searchrepo -c user:pass -u https://github.com -o api-key
```

## Expected Output

Matching repositories list.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
