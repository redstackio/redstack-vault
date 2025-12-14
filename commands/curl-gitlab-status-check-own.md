---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: |-
  curl --request POST \
    --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=2' \
    --header 'Authorization: Bearer <TOKEN>'
tags:
  - api
  - gitlab
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:20.665Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-status-check-own

## Command

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```

## Description

This command retrieves status check information for the attacker's own external status check (ID 2) using the correct SHA, verifying legitimate API access before attempting IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | API endpoint with ATTACKID, correct sha=<SHA>, and external_status_check_id=2 | Yes |
| `--header 'Authorization: Bearer <TOKEN>'` | Authenticates with the token | Yes |
| `<ATTACKID>` | Project ID | Yes |
| `<SHA>` | Valid commit SHA from error response | Yes |
| `<TOKEN>` | Access token | Yes |

## Examples

### Basic Usage

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/123/merge_requests/1/status_check_responses?sha=abcdef123&external_status_check_id=2' \
  --header 'Authorization: Bearer glpat-abc123'
```

### Advanced Usage

Pipe to jq for JSON parsing:

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>' | jq .
```

## Expected Output

JSON response with merge request details and external_status_check object containing project name, ID, status check name, and external URL for the attacker's project.

## Related

- [[commands/curl-gitlab-status-check-error-sha]]
- [[procedures/Exploit-IDOR-in-GitLab-Status-Check-API]]
