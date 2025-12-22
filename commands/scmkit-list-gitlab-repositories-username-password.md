---
id: e893b4c2-047a-4eeb-85c0-54c82a0449fa
name: scmkit-list-gitlab-repositories-username-password
type: command
executor: bash
data: 'SCMKit.exe -s gitlab -m listrepo -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL'
output: null
created_at: '2023-04-06T03:56:25.111685+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - discovery
  - enumeration
verified: true
validated: true
---

# scmkit-list-gitlab-repositories-username-password

## Command

```bash
SCMKit.exe -s gitlab -m listrepo -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

## Description

Lists accessible GitLab repositories using username and password authentication via SCMKit. Ideal for scenarios without API keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s gitlab | SCM system | Yes |
| -m listrepo | List repositories mode | Yes |
| -c $_USERNAME:$_PASSWORD | Credentials in format username:password | Yes |
| -u $_GITLAB_URL | GitLab instance URL | Yes |

## Examples

### Basic Usage

```bash
SCMKit.exe -s gitlab -m listrepo -c user:pass -u https://gitlab.example.com
```

## Expected Output

Similar JSON structure as API key variant, listing project details.

## Related

- [[procedures/GitLab-Repository-Enumeration-and-Search]]
- [[commands/scmkit-list-gitlab-repositories-api-key]]
