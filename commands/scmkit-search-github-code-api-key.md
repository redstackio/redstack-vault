---
id: f125bbd2-c496-46c3-89a8-f4a062afeea9
name: scmkit-search-github-code-api-key
type: command
executor: bash
data: >-
  SCMKit.exe -s github -m searchcode -c $_API_KEY -u $_GITHUB_URL -o
  $_SEARCH_TERM
output: null
created_at: '2023-04-06T03:56:25.112133+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - search
  - secrets
verified: true
validated: true
---

# scmkit-search-github-code-api-key

## Command

```bash
SCMKit.exe -s github -m searchcode -c $_API_KEY -u $_GITHUB_URL -o $_SEARCH_TERM
```

## Description

Searches code content in GitHub for keywords to find exposed secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s github | SCM system | Yes |
| -m searchcode | Code search mode | Yes |
| -c $_API_KEY | API key | Yes |
| -u $_GITHUB_URL | URL | Yes |
| -o $_SEARCH_TERM | Search term | Yes |

## Examples

### Basic Usage

```bash
SCMKit.exe -s github -m searchcode -c ghp-abc -u https://github.com -o private_key
```

## Expected Output

Code snippets or files containing the term.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
