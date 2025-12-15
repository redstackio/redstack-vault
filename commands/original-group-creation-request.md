---
data: >-
  curl -X POST "http://www.localize.io/pages/create_project/3F" -H "User-Agent:
  Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Referer: http://www.localize.io/pages/create_project/82" -H "Cookie:
  PHPSESSID=srdrqpfu6k679bna6e2rtrsrq7" -H "Connection: keep-alive" -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "CSRFToken=NTc4NTUxMjY1MzUxZTllOGIwYWM4MC4yMjE1MjUxNw%3D%3D&addGroup%5Bname%5D=Test"
tags:
  - http
  - post
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.725Z'
id: 279182ce-e297-4a5a-9eee-01ecbae6fee3
verified: false
validated: true
submitted: true
---
# original-group-creation-request

## Command

```bash
curl -X POST "http://www.localize.io/pages/create_project/3F" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.2; rv:28.0) Gecko/20100101 Firefox/28.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Referer: http://www.localize.io/pages/create_project/82" \
  -H "Cookie: PHPSESSID=srdrqpfu6k679bna6e2rtrsrq7" \
  -H "Connection: keep-alive" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "CSRFToken=NTc4NTUxMjY1MzUxZTllOGIwYWM4MC4yMjE1MjUxNw%3D%3D&addGroup%5Bname%5D=Test"
```

## Description

This command sends an HTTP POST request to create a group in the user's own project (ID '3F') on Localize.io. It includes necessary headers for a browser-like request and form data with CSRF protection and group name. Use this as a baseline before modifying for IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `URL path` | Endpoint with own project ID (e.g., /pages/create_project/3F) | Yes |
| `-H User-Agent` | Mimics browser user agent | Yes |
| `-H Cookie` | Session cookie (PHPSESSID) | Yes |
| `-d CSRFToken` | Anti-CSRF token value | Yes |
| `-d addGroup[name]` | Group name (e.g., 'Test') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://www.localize.io/pages/create_project/3F" -H "Cookie: PHPSESSID=your_session" -d "CSRFToken=your_token&addGroup[name]=Test" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

Include full headers as shown in the main command for realism in proxy testing.

## Expected Output

HTTP 200 OK response or redirect to project page, with the new group created in the own project. Body may include success message or updated project HTML.

## Related

- [[commands/modified-idor-group-creation-request]]
- [[procedures/Exploit-IDOR-for-Unauthorized-Group-Creation]]
