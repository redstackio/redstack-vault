---
id: uuid-c8
data: >-
  curl --header "PRIVATE-TOKEN: <TOKEN>"
  "https://gitlab.domain.com/api/v4/projects?visibility=internal"
tags:
  - gitlab
  - api
  - alternative-auth
type: command
output: JSON array of internal projects
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.294Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-list-projects-private-token

## Command

```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects?visibility=internal"
```

## Description

Alternative authentication method using PRIVATE-TOKEN header to list internal projects, useful for personal project tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "PRIVATE-TOKEN: <TOKEN>"` | Private token auth | Yes |
| `visibility=internal` | Internal filter | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: abc123" "https://gitlab.domain.com/api/v4/projects?visibility=internal"
```

### Advanced Usage

With pagination:

```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects?visibility=internal&page=1&per_page=20"
```

## Expected Output

JSON array of internal projects, similar to Bearer method.

## Related

- [[commands/curl-gitlab-list-internal-projects]]
- [[procedures/Enable-Project-Creation-for-External-User]]
