---
id: cmd-periscope-original-login
data: |-
  GET /i/twitter/login?csrf=████ HTTP/1.1
  Host: www.periscope.tv
  User-Agent: █████████
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://www.periscope.tv/
  Cookie: ...
tags:
  - oauth
  - login
type: command
output: HTML response initiating OAuth
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.671Z'
verified: false
validated: true
submitted: true
---
# original-oauth-login-request

## Command

```http
GET /i/twitter/login?csrf=████ HTTP/1.1
Host: www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
Cookie: ...
```

## Description

Sends the initial HTTP GET request to Periscope TV's Twitter OAuth login endpoint to start the flow and obtain a CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| csrf | CSRF protection token | Yes |
| Host | Target domain | Yes |
| User-Agent | Browser identifier | Yes |
| Referer | Origin page | Yes |
| Cookie | Session cookies | Yes |

## Examples

### Basic Usage

```http
GET /i/twitter/login?csrf=abc123 HTTP/1.1
Host: www.periscope.tv
...
```

### Advanced Usage

Include full headers as shown for realistic simulation.

## Expected Output

HTML page with OAuth initiation elements, including meta tags or forms.

## Related

- [[Related Procedure]]
