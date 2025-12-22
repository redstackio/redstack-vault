---
id: c85f87e8-cd28-4b1a-958f-7525b0580045
name: HTTP-Request-Smuggling-Payload-for-Search-Request
type: code
language: http
verified: true
created_at: '2020-08-12T19:18:57.710520+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - payload
validated: true
---

# HTTP-Request-Smuggling-Payload-for-Search-Request

## Code

```http
0
POST /  HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
Connection: close
search=test
```

## Description

This HTTP payload is a smuggling request appended to a legitimate search POST. The leading '0' acts as a null separator, followed by a malformed POST that exploits parsing differences to inject a second request, revealing front-end header rewriting in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Content-Length | Mismatched length to confuse front-end/backend (fixed at 200) | 200 |
| search | Legitimate search term in body | test |

## Usage

Embed this payload in the body of an intercepted search request using Burp Suite Repeater or curl --data-raw. Send to trigger smuggling and observe custom response headers like x-bkdpqI-Ip.

## Detection

- WAF logs showing requests with duplicate Content-Length or unexpected body content.
- Anomalous response headers or 4xx/5xx errors from parsing mismatches.
- Network traffic analysis for HTTP/1.1 requests with Transfer-Encoding absent but long bodies.

## Related

- [[procedures/HTTP-Request-Smuggling-to-Reveal-Front-End-Rewriting-and-Access-Admin-Panel]]
- [[tools/Burp-Suite]]
