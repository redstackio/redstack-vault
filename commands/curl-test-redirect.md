---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: 'curl -I -L "https://inventory.upserve.com/http://google.com/"'
tags:
  - web
  - redirect
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:34.994Z'
verified: false
validated: true
submitted: true
---
# curl-test-redirect

## Command

```bash
curl -I -L "https://inventory.upserve.com/http://google.com/"
```

## Description

This command tests for open redirect vulnerabilities by sending a HEAD request with follow-redirects to a crafted URL, revealing if the server processes arbitrary paths as redirect targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `-L` | Follow HTTP 3xx redirects | Yes |
| URL | Target URL with injected redirect path | Yes |

## Examples

### Basic Usage

```bash
curl -I -L "https://inventory.upserve.com/http://google.com/"
```

### Advanced Usage

```bash
curl -I -L -v "https://inventory.upserve.com/http://evil-site.com/" > redirect_test.log
```

> Adds verbose output (-v) and logs to file for analysis.

## Expected Output

HTTP/1.1 302 Found
Location: http://google.com/
... (indicating successful redirect to the injected URL)

## Related

- [[Related Procedure: Test-Open-Redirect-in-Upserve-Login]]
