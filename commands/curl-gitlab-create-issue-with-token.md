---
id: uuid-c3
data: >-
  curl -X POST --header "Authorization: Bearer <TOKEN>"
  "https://gitlab.domain.com/api/v4/projects/21/issues?title=iWasHere"
tags:
  - gitlab
  - api
  - issue-creation
type: command
output: JSON response with created issue details
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.306Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-create-issue-with-token

## Command

```bash
curl -X POST --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects/21/issues?title=iWasHere"
```

## Description

Creates an issue on an internal project using the token, showing write access escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `--header "Authorization: Bearer <TOKEN>"` | Token auth | Yes |
| `project_id=21` | Target internal project ID | Yes |
| `title=iWasHere` | Issue title | Yes |

## Examples

### Basic Usage

```bash
curl -X POST --header "Authorization: Bearer abc123" "https://gitlab.domain.com/api/v4/projects/21/issues?title=TestIssue"
```

### Advanced Usage

Add description:

```bash
curl -X POST --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/projects/21/issues?title=iWasHere&description=Escalation test"
```

## Expected Output

JSON with issue id, title, state, project_id, and author details.

## Related

- [[commands/curl-gitlab-create-group-with-token]]
- [[procedures/Exploit-Token-for-Internal-Access]]
