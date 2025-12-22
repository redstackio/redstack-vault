---
id: f953f20e-2b66-489d-a393-d9712dc407ff
name: crlf-injection-url-payload
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:55.272930+00:00'
updated_at: '2023-04-06T03:55:55.278991+00:00'
platforms:
  - Web
tags:
  - crlf-injection
  - payload
validated: true
---

# CRLF Injection URL Payload

## Code

```http
http://www.example.net/%0D%0ASet-Cookie:mycookie=myvalue
```

## Description

This HTTP URL payload incorporates a CRLF sequence (%0D%0A) followed by a Set-Cookie directive. When supplied as a parameter value in a request to a vulnerable endpoint, it splits the response header and injects a new cookie, allowing attackers to overwrite or add session cookies for hijacking purposes. The payload terminates the existing header (e.g., Location) and appends the malicious cookie without breaking the overall response structure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %0D%0A | Encoded CRLF sequence to split headers | %0D%0A |
| mycookie | Name of the injected cookie | mycookie |
| myvalue | Value of the cookie (can include JavaScript for exfiltration) | myvalue |

## Usage

Embed this payload in a URL parameter (e.g., ?redirect=) of a GET or POST request to an endpoint that echoes input into response headers. Use tools like curl or Burp Suite to send it. Upon success, the victim's browser sets the cookie, enabling session theft. Test in a lab environment first to avoid disrupting production systems.

## Detection

- WAF rules blocking %0D or %0A in URL parameters.
- Server logs showing anomalous header lengths or multiple Set-Cookie directives.
- Browser developer tools revealing unexpected cookies from legitimate domains.
- Network monitoring for requests with encoded line breaks.

## Related

- [[procedures/crlf-injection-for-cookie-stealing]]
- [[commands/curl-send-crlf-injection-request]]
