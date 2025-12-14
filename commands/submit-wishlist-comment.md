---
id: cmd-uuid-001
data: >-
  curl -X POST
  'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]'
  -d 'wishlistComment=[COMMENT]' -H 'Cookie: [AUTH_COOKIE]'
tags:
  - http-post
  - comment-submit
type: command
output: HTML response with 'Your comment is saved' and reflected textarea
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.155Z'
verified: false
validated: true
submitted: true
---
# Submit Wishlist Comment

## Command

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]' -d 'wishlistComment=[COMMENT]' -H 'Cookie: [AUTH_COOKIE]'
```

## Description

Submits a comment to a Teavana wishlist item via POST, reflecting the input in the response. Used for legitimate testing or capturing IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[ID]` | Dynamic wishlist comment ID | Yes |
| `wishlistComment=[COMMENT]` | The comment text | Yes |
| `-H 'Cookie: [AUTH_COOKIE]'` | Authentication cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/12345' -d 'wishlistComment=Test comment' -H 'Cookie: sid=abc123'
```

### Advanced Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/12345' -d 'wishlistComment=Test' -H 'Cookie: sid=abc123' -v
```

## Expected Output

Server responds with HTML including <textarea>wishlistComment value</textarea> and success message.

## Related

- [[commands/inject-xss-comment]]
- [[procedures/Inject-XSS-Payload-in-Wishlist-Comment]]
