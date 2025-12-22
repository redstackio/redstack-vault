---
id: 1de743ee-95eb-43ee-acb8-568da5082ac8
name: scmkit-search-github-code-username-password
type: command
executor: bash
data: >-
  SCMKit.exe -s github -m searchcode -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.112028+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - secrets
verified: true
validated: true
---

# scmkit-search-github-code-username-password

## Command

```bash
SCMKit.exe -s github -m searchcode -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o $_SEARCH_TERM
```

## Description

Searches GitHub code using basic auth.

## Parameters

Similar to API key variant.

## Examples

### Basic Usage

```bash
SCMKit.exe -s github -m searchcode -c user:pass -u https://github.com -o password
```

## Expected Output

Search results with code matches.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
