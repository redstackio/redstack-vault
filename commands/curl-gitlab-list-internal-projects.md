---
id: uuid-c5
data: >-
  curl --header "Authorization: Bearer TOKEN"
  "https://gitlab.domain.com/api/v4/projects?visibility=internal"
tags:
  - gitlab
  - api
  - recon
type: command
output: JSON array of internal projects with IDs
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.301Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-list-internal-projects

## Command

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects?visibility=internal"
```

## Description

Filters and lists only internal visibility projects using the token, identifying targets for further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Authorization: Bearer TOKEN"` | Token auth | Yes |
| `visibility=internal` | Filter for internal projects | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects?visibility=internal"
```

### Advanced Usage

Limit results:

```bash
curl --header "Authorization: Bearer TOKEN" "https://gitlab.domain.com/api/v4/projects?visibility=internal&per_page=50"
```

## Expected Output

JSON array of projects filtered to internal visibility, including IDs and names.

## Related

- [[commands/curl-gitlab-list-projects-with-token]]
- [[procedures/Exploit-Token-for-Internal-Access]]
