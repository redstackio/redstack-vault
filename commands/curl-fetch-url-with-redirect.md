---
data: 'curl -I https://skyliner.io//blackfan.ru/'
tags:
  - web-testing
  - redirect-check
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.374Z'
id: 36364d78-8257-48da-a877-1605d68cc820
verified: false
validated: true
submitted: true
---
# curl-fetch-url-with-redirect

## Command

```bash
curl -I https://skyliner.io//blackfan.ru/
```

## Description

This command uses curl to perform a HEAD request on a manipulated URL, checking for open redirect vulnerabilities by examining the response headers, particularly the Location field in 301 redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD request) | Yes |
| `https://skyliner.io//blackfan.ru/` | The target URL with double slash manipulation | Yes |

## Examples

### Basic Usage

```bash
curl -I https://skyliner.io//blackfan.ru/
```

### Advanced Usage

```bash
curl -I -L https://qa.skyliner.io//example.com/  # Follow redirect with -L for full trace
```

## Expected Output

HTTP/1.1 301 Moved Permanently
Location: //blackfan.ru
Server: ...
...

A 301 status with a protocol-relative Location header indicates a successful open redirect test.

## Related

- [[Related Procedure|procedures/Test-Open-Redirect-via-Double-Slash-Manipulation]]
