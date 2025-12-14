---
id: uuid-c1
data: >-
  curl --header "Authorization: Bearer <TOKEN>"
  "https://gitlab.domain.com/api/v4/projects"
tags:
  - gitlab
  - api
  - recon
type: command
output: 'JSON array of projects, including internal visibility projects'
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.310Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-list-projects-with-token

## Command

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects"
```

## Description

Lists all projects accessible with the project token, revealing internal ones due to bot user privileges. Use after token creation to probe scope.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header "Authorization: Bearer <TOKEN>"` | Authenticates the request using the Bearer token | Yes |
| Endpoint URL | GitLab API path for projects | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects"
```

### Advanced Usage

Add query params for filtering:

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects?per_page=100"
```

## Expected Output

JSON array of project objects with id, name, visibility (including internal), path, etc.

## Related

- [[commands/curl-gitlab-list-internal-projects]]
- [[procedures/Exploit-Token-for-Internal-Access]]
