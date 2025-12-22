---
id: cmd-uuid-004
data: >-
  curl -H "Authorization: Bearer $TOKEN" -v
  'http://gitlab-vm.local/api/v4/projects/204' | jq .import_error
tags:
  - gitlab-api
  - error
  - jq
type: command
output: '"Fetching remote upstream failed: ... 405"'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.521Z'
verified: false
validated: true
submitted: true
---
# curl-check-import-error

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" -v 'http://gitlab-vm.local/api/v4/projects/204' | jq .import_error
```

## Description

Retrieves project details and pipes to jq to extract import_error containing SSRF leak.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Auth | Yes |
| `-v` | Verbose | No |
| `jq .import_error` | Extract error field | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer $TOKEN" 'http://gitlab.example/api/v4/projects/123' | jq .import_error
```

## Expected Output

JSON string with error details including internal response.

## Related

- [[Related Procedure: Check-Import-Status-for-SSRF-Result]]
