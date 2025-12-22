---
id: 2f0bb7e7-5066-43a0-bd6e-eeb613627ec8
name: http-get-request-null-origin
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:54.577201+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - cors
  - exploitation
  - http-request
validated: true
---

# http-get-request-null-origin

## Code

```http
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: null
Cookie: sessionid=...
```

## Description

This HTTP request snippet crafts a GET request with Origin set to null and includes a session cookie, used to test for CORS misconfigurations by sending it via tools like netcat, telnet, or as a raw payload in a proxy. It simulates a cross-origin fetch from a null origin to trigger header reflection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Host | Target domain | victim.example.com |
| /endpoint | Path to the vulnerable endpoint | /api/profile |
| sessionid=... | Authentication cookie value | sessionid=abc123 |

## Usage

Use this raw HTTP request in a tool like netcat (nc victim.example.com 80 < request.txt) or embed in JavaScript fetch() for browser-based testing. In a procedure like CORS exploitation, send this to verify if the response allows data read from a malicious site.

## Detection

- Server logs showing requests with Origin: null.
- WAF rules alerting on unusual Origin headers or cross-origin patterns.
- Browser console errors or network tab showing reflected CORS headers.

## Related

- [[procedures/CORS-Misconfiguration-Exploitation-Null-Origin]]
