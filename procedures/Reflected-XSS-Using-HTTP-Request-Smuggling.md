---
id: 7132288a-ffc2-4049-b8b5-b844f19ef0cf
name: Reflected-XSS-Using-HTTP-Request-Smuggling
type: procedure
verified: true
submitted: true
created_at: '2020-08-16T18:48:44.398483+00:00'
updated_at: '2023-05-26T01:25:20.287823+00:00'
platforms:
  - Web
tags:
  - owasp
  - owasp top 10
  - Web Applications
  - xss
  - http-request-smuggling
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Reflected-XSS-Using-HTTP-Request-Smuggling

## Summary

This procedure demonstrates how to exploit HTTP Request Smuggling vulnerabilities to inject a reflected XSS payload via a manipulated User-Agent header in a secondary request. By smuggling a second HTTP request within the body of the first, the attacker can bypass front-end parsing and cause the back-end server to reflect the malicious User-Agent, leading to JavaScript execution in the victim's browser.

## Description

HTTP Request Smuggling occurs when front-end and back-end servers interpret HTTP request headers differently, such as in Content-Length vs. Transfer-Encoding ambiguities. This procedure targets web applications that reflect the User-Agent header in responses (e.g., in forms or error pages) and are vulnerable to smuggling. The attack crafts a request where a smuggled GET request includes a User-Agent header containing an XSS payload like `<script>alert(document.domain)</script>`. When the back-end processes the smuggled request, it reflects the payload, executing it client-side. This is effective against applications behind load balancers or proxies. Prerequisites include a vulnerable endpoint and the ability to intercept/modify traffic.

## Requirements

1. A web application vulnerable to HTTP Request Smuggling (e.g., CL.TE or TE.CL variants) that reflects the User-Agent header in its responses.
2. Network access to the target application, typically over HTTP/HTTPS on port 80/443.
3. A proxy tool like [[tools/Burp-Suite]] for intercepting and crafting requests.
4. Knowledge of the target's HTTP parsing behavior (testable via tools like Burp).

## Defense

Defensive measures and detection strategies:

- Normalize HTTP requests at the front-end to eliminate ambiguities between Content-Length and Transfer-Encoding.
- Use a Web Application Firewall (WAF) to detect and block malformed requests with conflicting headers.
- Avoid reflecting unsanitized headers like User-Agent in responses; sanitize or encode outputs to prevent XSS.
- Monitor for duplicate or anomalous requests in server logs, such as multiple requests in a single TCP stream.
- Enable strict HTTP/1.1 parsing and reject requests with both Content-Length and Transfer-Encoding headers.

## Objectives

1. Identify a smuggling-vulnerable endpoint that reflects User-Agent.
2. Craft and send a smuggled request injecting an XSS payload in the User-Agent.
3. Achieve client-side JavaScript execution via reflected XSS.
4. Confirm payload execution without direct access to the back-end.

## Instructions

### Step 1: Intercept and Analyze Normal Request

**Context**: Begin by proxying traffic through Burp Suite to capture a standard request to the target endpoint. Inspect the response in the browser's view-source to confirm the User-Agent header is reflected (e.g., in a form or page element). This verifies the reflection point for XSS.

Use [[tools/Burp-Suite]] to intercept the request:

1. Configure your browser to proxy through Burp (default: 127.0.0.1:8080).
2. Navigate to the target page (e.g., a search or login form) and trigger a request.
3. In Burp Proxy > HTTP History, select the request and forward it.
4. View the page source in the browser to locate the reflected User-Agent.

**Expected Output**: Request intercepted in Burp showing standard headers; page source reveals User-Agent echoed back unsanitized.

### Step 2: Craft Smuggled Request with XSS Payload

**Context**: Using the intercepted request as a base, craft a smuggling payload in Burp Repeater. This step exploits a parsing difference (e.g., TE.CL smuggling) by including a second GET request in the body of the first POST. Replace the User-Agent in the smuggled request with an XSS payload to inject malicious JavaScript that will be reflected.

Use the payload from [[codes/HTTP-Request-Smuggling-User-Agent-XSS-Payload]]:

1. In Burp Repeater, paste the smuggling payload.
2. Replace placeholders like `$_TARGET_HOST` with the actual domain (e.g., vulnerable-site.com) and `$_XSS_PAYLOAD` with `<script>alert(document.domain)</script>`.
3. Send the request and observe the response.

```http
POST /$_ENDPOINT HTTP/1.1
Host: $_TARGET_HOST
Content-Length: 13
Transfer-Encoding: chunked

0

GET /$_ENDPOINT HTTP/1.1
Host: $_TARGET_HOST
User-Agent: $_XSS_PAYLOAD

```

**Expected Output**: The front-end sees a short POST body, but the back-end interprets the trailing data as a new GET request, processing the malicious User-Agent.

### Step 3: Verify XSS Execution

**Context**: Forward the smuggled request and check the response for reflection of the injected User-Agent. The XSS payload should execute in the browser, confirming successful smuggling and injection. This step validates the attack by observing the alert or other payload effects.

1. In Burp Repeater, send the crafted request.
2. Inspect the response body for the reflected User-Agent containing the XSS.
3. If proxied through the browser, reload or trigger the endpoint to see the alert box.

**Expected Output**: Response includes the smuggled request's output with the XSS payload reflected; browser executes `<script>alert(document.domain)</script>`, popping an alert.
