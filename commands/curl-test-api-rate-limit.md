---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST 'https://api.vk.com/method/auth.signup' -d
  'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'
tags:
  - api-testing
  - rate-limit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.518Z'
verified: false
validated: true
submitted: true
---
# curl-test-api-rate-limit

## Command

```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'
```

## Description

This command sends a single POST request to VK.com's auth.signup API endpoint to test for rate limiting during user registration, using a test phone number to trigger SMS verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://api.vk.com/method/auth.signup'` | API endpoint URL | Yes |
| `-d 'phone=1234567890...'` | POST data including phone, client_id, scope, redirect_uri, and API version | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'
```

### Advanced Usage

```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' -H 'User-Agent: Mozilla/5.0'
```

## Expected Output

JSON response like {"response":{"success":1}}, with no 429 or rate limit errors; SMS may be sent to the phone.

## Related

- [[Related Procedure|procedures/Identify-Rate-Limit-Bypass-in-Auth-Signup-API]]
