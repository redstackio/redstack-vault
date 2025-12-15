---
id: cmd-uuid-1
data: >-
  curl -X POST -H "Cookie: auth_token=your_session_cookie" -H "X-CSRFToken:
  extracted_token" -d ""
  https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
tags:
  - web
  - test
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.606Z'
verified: false
validated: true
submitted: true
---
# curl-post-csrf-test

## Command

```bash
curl -X POST -H "Cookie: auth_token=your_session_cookie" -H "X-CSRFToken: extracted_token" -d "" https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
```

## Description

This command tests a POST request to Chaturbate's show cancellation endpoint with a CSRF token to verify protection. Use it to confirm that missing tokens result in rejection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Cookie: ..."` | Sets session cookie for authentication | Yes |
| `-H "X-CSRFToken: ..."` | Provides CSRF token header | Yes for valid test |
| `-d ""` | Empty body for the request | No |
| URL | Target endpoint with username | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Cookie: auth_token=abc123" -H "X-CSRFToken: def456" https://chaturbate.com/tipping/group_show_cancel/test_user/
```

### Advanced Usage

```bash
curl -X POST -H "Cookie: auth_token=abc123" -H "X-CSRFToken: def456" -d "reason=manual" -v https://chaturbate.com/tipping/group_show_cancel/test_user/
```

## Expected Output

Successful: HTTP 200 or redirect indicating cancellation. Failed (no token): HTTP 403 Forbidden with CSRF error message.

## Related

- [[Related Procedure|procedures/Identify-CSRF-Protected-Endpoint-in-Chaturbate]]
