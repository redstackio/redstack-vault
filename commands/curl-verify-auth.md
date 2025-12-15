---
id: curl-verify-001
data: >-
  curl -X GET 'https://merchant.rbmonkey.com/api/shops' -H 'Authorization:
  Bearer YOUR_AUTH_TOKEN'
tags:
  - verification
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
updated_at: '2025-12-14T17:25:29.049Z'
verified: false
validated: true
submitted: true
---
# curl-verify-auth

## Command

```bash
curl -X GET 'https://merchant.rbmonkey.com/api/shops' \
  -H 'Authorization: Bearer YOUR_AUTH_TOKEN'
```

## Description

This command verifies an authenticated session by fetching the list of shops from the RBKmoney merchant API using the provided bearer token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://merchant.rbmonkey.com/api/shops` | Endpoint for shop listing | Yes |
| `-H 'Authorization: Bearer YOUR_AUTH_TOKEN'` | Auth header with token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://merchant.rbmonkey.com/api/shops' -H 'Authorization: Bearer eyJ...'
```

### Advanced Usage

```bash
curl -X GET 'https://merchant.rbmonkey.com/api/shops' -H 'Authorization: Bearer eyJ...' -v
```

## Expected Output

JSON array of shops: [{"id": 123, "name": "My Shop", ...}]

## Related

- [[commands/curl-login-merchant]]
- [[procedures/Authenticate-to-Merchant-Portal]]
