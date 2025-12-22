---
data: >-
  curl -v https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host:
  example.com"
tags:
  - http
  - header-manipulation
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.575Z'
id: 0ce28058-2028-43f1-be32-a6c2673fabe0
verified: false
validated: true
submitted: true
---
# curl-modify-headers

## Command

```bash
curl -v https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host: example.com"
```

## Description

This curl command sends an HTTP GET request to the target URL with a custom X-Forwarded-Host header to test for open redirect vulnerabilities, displaying verbose output to inspect responses and redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers and details | Yes |
| `-H "Host: link.omise.co"` | Sets the Host header to match the target | Yes |
| `-H "X-Forwarded-Host: example.com"` | Injects the manipulated header for redirect control | Yes |
| `https://link.omise.co/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -v https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host: example.com"
```

### Advanced Usage

```bash
curl -v -L https://link.omise.co/ -H "Host: link.omise.co" -H "X-Forwarded-Host: example.com" -o /dev/null
```

Follows the redirect (-L) and discards output (-o).

## Expected Output

Verbose output showing the request headers, server response (e.g., HTTP/1.1 302 Found), and Location header pointing to http://example.com, confirming the redirect.

## Related

- [[Related Procedure]]
