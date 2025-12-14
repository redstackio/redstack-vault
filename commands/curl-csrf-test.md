---
data: >-
  curl -X POST 'https://eats.uber.com/api/add-credit-card' -H 'Cookie:
  session=valid_session_cookie' -d
  'card_number=4111111111111111&expiry=12/25&cvc=123' --insecure
tags:
  - web
  - testing
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.843Z'
id: 8bb74427-3275-43ef-b601-5ff2d497cddc
verified: false
validated: true
submitted: true
---
# curl-csrf-test

## Command

```bash
curl -X POST 'https://eats.uber.com/api/add-credit-card' -H 'Cookie: session=valid_session_cookie' -d 'card_number=4111111111111111&expiry=12/25&cvc=123' --insecure
```

## Description

This command tests a web endpoint for CSRF protection by sending a POST request without a CSRF token, using a valid session cookie to simulate an authenticated user. Use it to verify if the server accepts forged requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://eats.uber.com/api/add-credit-card'` | Target endpoint URL | Yes |
| `-H 'Cookie: session=valid_session_cookie'` | Authenticates the request | Yes |
| `-d 'card_number=...&expiry=...&cvc=...'` | POST data payload | Yes |
| `--insecure` | Skips SSL verification for testing | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://eats.uber.com/api/add-credit-card' -H 'Cookie: session=abc123' -d 'card_number=4111111111111111&expiry=12/25&cvc=123' --insecure
```

### Advanced Usage

```bash
curl -X POST 'https://eats.uber.com/api/add-credit-card' -H 'Cookie: session=abc123' -H 'Referer: https://attacker.com' -d 'card_number=4111111111111111&expiry=12/25&cvc=123' --insecure -v
```

## Expected Output

Successful response (e.g., HTTP 200 with JSON confirming card addition) indicates missing CSRF protection. Failure would show a 403 or token error.

## Related

- [[Related Procedure: Test-for-CSRF-on-Credit-Card-Endpoint]]
