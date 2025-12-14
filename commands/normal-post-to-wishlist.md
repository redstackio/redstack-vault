---
id: 123e4567-e89b-12d3-a456-426614174006
name: normal-post-to-wishlist
type: command
executor: bash
data: >-
  curl -X POST
  'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id'
  -H 'Content-Type: application/x-www-form-urlencoded' -d
  'wishlistComment=:comment_string'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.916Z'
platforms:
  - Linux
  - Web
tags:
  - web-request
  - post
verified: false
validated: true
submitted: true
---

# normal-post-to-wishlist

## Command

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=:comment_string'
```

## Description

Sends a normal POST request to add a comment to a wishlist item on teavana.com, demonstrating the endpoint's basic functionality and reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:id` | Wishlist item ID (e.g., C1005285074) | Yes |
| `:comment_string` | The comment text to add | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'wishlistComment=Test comment'
```

### Advanced Usage

Add cookies for authenticated request:

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=abc123' \
  -d 'wishlistComment=Hello world'
```

## Expected Output

HTTP 200 OK with HTML response containing the reflected comment in a textarea element, or a redirect to the wishlist page.

## Related

- [[commands/post-xss-payload-to-wishlist]]
- [[procedures/Identify-Wishlist-Comment-Endpoint]]
