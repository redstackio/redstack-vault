---
id: cmd-vimeo-verify-001
data: >-
  curl -X POST https://vimeo.com/messages -H "User-Agent: Mozilla/5.0 (Windows
  NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Content-Type: application/x-www-form-urlencoded; charset=utf-8" -H "Referer:
  https://vimeo.com/messages" -H "Cookie: [YOUR_SESSION_COOKIE]" -d
  "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[YOUR_CSRF_TOKEN]"
tags:
  - auth-bypass
  - verification
  - http-post
type: command
output: '{"display_message":"You are unauthorized for this action."}'
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.796Z'
verified: false
validated: true
submitted: true
---
# vimeo-verify-fix-401

## Command

```bash
curl -X POST https://vimeo.com/messages \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
  -H "Referer: https://vimeo.com/messages" \
  -H "Cookie: [YOUR_SESSION_COOKIE]" \
  -d "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[YOUR_CSRF_TOKEN]"
```

## Description

This command reattempts the unauthorized POST after the vulnerability fix to verify enforcement of authorization, expecting a 401 response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `name` | Sender name (e.g., 'Jens>') | Yes |
| `text` | Message content (e.g., 'blaat') | Yes |
| `action` | 'send_message' | Yes |
| `lightbox` | 'true' | Yes |
| `user` | Target user ID | Yes |
| `token` | CSRF token | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://vimeo.com/messages -H "Cookie: [COOKIE]" -d "name=Test&text=Hello&action=send_message&lightbox=true&user=12345&token=[TOKEN]"
```

### Advanced Usage

With full headers:

```bash
curl -X POST https://vimeo.com/messages -H "User-Agent: ..." -H "Cookie: [COOKIE]" -d "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[TOKEN]"
```

## Expected Output

HTTP 401 Unauthorized with JSON body {"display_message":"You are unauthorized for this action."}.

## Related

- [[procedures/Bypass-Vimeo-Messaging-Authorization-with-POST-Request]]
