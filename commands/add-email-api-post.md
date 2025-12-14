---
id: cmd-uuid-001
data: >-
  curl -X POST
  https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/email -H
  "Cookie: connect.sid=█████; _ga=GA1.1.518394987.16793330654" -H "User-Agent:
  Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101
  Firefox/111.0" -H "Accept: text/html" -H "Accept-Language: en-US,en;q=0.57" -H
  "Accept-Encoding: gzip, deflate" -H "Referer:
  https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings" -H
  "Content-Type: application/json" -H "X-Csrf-Token:
  0787d9f55701a244aa8f68401f2dc6aebb55a1b83ee2930743ba1324314b5c2cb87fafa7bac74afd8d4660feff2ce33d5b38fb949478c5b9f32430e863ced6b4"
  -H "Origin: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net" -H
  "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: same-origin" -H "Sec-Fetch-Site:
  same-origin" -H "X-Pwnfox-Color: blue" -H "Te: trailers" -d
  '{"email":"example@email.com"}'
tags:
  - api
  - post
  - web
type: command
output: |-
  HTTP/1.1 200 OK
  {"success": true, "message": "Email added"}
executor: curl
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.778Z'
verified: false
validated: true
submitted: true
---
# add-email-api-post

## Command

```bash
curl -X POST https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/email \
  -H "Cookie: connect.sid=█████; _ga=GA1.1.518394987.16793330654" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0" \
  -H "Accept: text/html" \
  -H "Accept-Language: en-US,en;q=0.57" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Referer: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings" \
  -H "Content-Type: application/json" \
  -H "X-Csrf-Token: 0787d9f55701a244aa8f68401f2dc6aebb55a1b83ee2930743ba1324314b5c2cb87fafa7bac74afd8d4660feff2ce33d5b38fb949478c5b9f32430e863ced6b4" \
  -H "Origin: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Sec-Fetch-Mode: same-origin" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "X-Pwnfox-Color: blue" \
  -H "Te: trailers" \
  -d '{"email":"example@email.com"}'
```

## Description

Sends a POST request to add an email address to Mozilla Monitor's breach monitoring system. Used to replicate web UI actions or in scripted attacks; requires valid session and CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Session and tracking cookies for authentication | Yes |
| `-H "X-Csrf-Token: ..."` | CSRF protection token from the session | Yes |
| `-d '{"email":"..."}'` | JSON payload with the email to add | Yes |
| `--email` (implied) | The email address (e.g., example@email.com) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/email -H "Cookie: connect.sid=your_sid" -H "X-Csrf-Token: your_token" -H "Content-Type: application/json" -d '{"email":"test@example.com"}'
```

### Advanced Usage

```bash
# With full headers for realism
curl -X POST https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/email [full headers as above] -d '{"email":"test2@example.com"}'
```

## Expected Output

HTTP 200 OK with JSON like {"success": true, "email": "example@email.com", "message": "Email added to monitoring"}. Failures return 400/403 with limit or auth errors.

## Related

- [[procedures/Capture-Email-Addition-API-Request]]
- [[procedures/Exploit-Race-Condition-with-Concurrent-Requests]]
