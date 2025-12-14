---
data: >-
  curl -X GET "https://api.line.me/v2/bot/group/{account_id}/summary" -H
  "Authorization: Bearer {access_token}" | grep -o 'groupId":"[^"]*'
tags:
  - web
  - discovery
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: fac112f4-1b27-4464-a3ce-6d0a1d284461
created_at: '2025-12-14T17:30:58.611Z'
updated_at: '2025-12-14T17:30:58.611Z'
verified: false
validated: true
submitted: true
---
# curl-extract-group-id

## Command

```bash
curl -X GET "https://api.line.me/v2/bot/group/{account_id}/summary" -H "Authorization: Bearer {access_token}" | grep -o 'groupId":"[^"]*'
```

## Description

This command fetches a LINE Official Account summary via API and extracts the group ID from the JSON response using grep, useful for IDOR discovery in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{account_id}` | The account identifier to query | Yes |
| `{access_token}` | Bearer token for API access (omit if unauthenticated) | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.line.me/v2/bot/group/abc123/summary" -H "Authorization: Bearer xyz789" | grep -o 'groupId":"[^"]*'
```

### Advanced Usage

```bash
for id in {1000000000..1000000100}; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" "https://api.line.me/v2/bot/group/$id/summary"; done | grep 200
```

## Expected Output

groupId":"1234567890abcdef" indicating the extracted ID.

## Related

- [[Related Procedure]]
