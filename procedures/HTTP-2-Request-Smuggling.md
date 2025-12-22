---
type: procedure
description: >-
  Exploit parsing discrepancies in HTTP/2 implementations to smuggle malicious
  requests past front-end proxies to back-end servers.
tactics:
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/HTTP/2 Request Smuggling]]'
  - '[[tags/Request Smuggling]]'
commands:
  - '[[commands/curl-check-http2-support]]'
tools:
  - '[[tools/cURL]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# HTTP-2-Request-Smuggling

## Summary

HTTP/2 Request Smuggling is a web vulnerability that exploits differences in how front-end proxies and back-end servers parse HTTP/2 requests and responses. By crafting a specially malformed request, an attacker can "smuggle" additional requests that are misinterpreted by the back-end, allowing bypass of security controls like WAFs, authentication, or rate limiting to access sensitive data or perform unauthorized actions.

## Description

This procedure demonstrates how to identify and exploit HTTP/2 Request Smuggling vulnerabilities. It targets environments where a front-end server (e.g., load balancer or reverse proxy) supports HTTP/2 but the back-end interprets requests differently, often due to fallback to HTTP/1.1 or improper header handling. Common scenarios include cloud-hosted web apps or API gateways. Success enables request desynchronization, leading to cache poisoning, session hijacking, or arbitrary request injection. The technique relies on sending a request with invalid or ambiguous headers that cause the front-end to consume part of the payload while the back-end processes the remainder as a new request.

## Requirements

1. Network access to a target HTTP/2-enabled web server (HTTPS typically required for HTTP/2).
2. Tools for sending custom HTTP requests, such as curl for initial probing.
3. Knowledge of the target's request parsing behavior (test via trial and error).
4. A vulnerable configuration where front-end and back-end disagree on request boundaries (e.g., via Content-Length vs. Transfer-Encoding mismatches adapted for HTTP/2).

## Defense

- Implement strict HTTP/2 header validation and reject ambiguous or malformed requests.
- Use a Web Application Firewall (WAF) configured to detect smuggling patterns, such as duplicate or invalid pseudo-headers.
- Ensure consistent protocol handling across front-end and back-end servers; disable HTTP/2 downgrade fallbacks if possible.
- Regularly update server software (e.g., nginx, Apache) to patch known HTTP/2 vulnerabilities.
- Monitor for anomalous request patterns, like multiple methods in a single frame or unexpected desynchronization.

## Objectives

1. Bypass front-end security controls to reach back-end resources directly.
2. Inject unauthorized requests to access sensitive data or perform actions as another user.
3. Demonstrate potential for cache poisoning or session manipulation.

## Instructions

### Step 1: Verify HTTP/2 Support

**Context**: Before attempting smuggling, confirm the target server supports HTTP/2 to ensure the protocol is in use and identify the connection details.

**Command** ([[commands/curl-check-http2-support]]):
```bash
curl -I --http2-prior-knowledge https://$_TARGET_URL
```

> This command performs a HEAD request using HTTP/2 prior knowledge (bypassing ALPN negotiation). Success is indicated by a response starting with "HTTP/2". If it falls back to HTTP/1.1, the server may not fully support HTTP/2, reducing exploit feasibility. Replace $_TARGET_URL with the target domain (e.g., https://www.example.com). Expected output includes server headers revealing proxy details.

### Step 2: Craft the Smuggling Payload

**Context**: Prepare a malformed HTTP/2 request that includes invalid headers followed by a smuggled HTTP/1.1 request. This exploits parsing differences where the front-end may ignore or misparse the extra content, allowing the back-end to treat it as a separate request.

Use the following payload from [[codes/HTTP-2-Request-Smuggling-Payload]]:

```http
:method GET
:path /
:authority www.example.com
header ignored\r\n\r\nGET / HTTP/1.1\r\nHost: www.example.com
```

> Customize the payload by replacing "www.example.com" with the target authority. The "header ignored\r\n\r\n" creates an early header termination, smuggling the subsequent GET request. This step ensures the payload is ready for transmission; test variations if initial attempts fail (e.g., adjust for TE.CL or CL.TE vectors adapted to HTTP/2).

### Step 3: Send the Smuggling Request and Validate

**Context**: Transmit the crafted payload to the target using an HTTP/2-capable client that supports raw request sending (e.g., extend curl with --data-raw for binary, or use specialized tools like Burp Suite). Monitor responses for signs of smuggling success, such as the back-end executing the smuggled request unexpectedly.

Instructions: Save the payload to a file (e.g., smuggling.req) and send it using a tool like h2c (if available) or a Python script with hyper library for raw HTTP/2 frames. For basic testing with curl, attempt to send via POST with raw body, but note limitations:

```bash
curl --http2 -X POST --data-binary @smuggling.req https://$_TARGET_URL/ -H "Content-Type: application/octet-stream"
```

> Observe the response for anomalies, such as a 200 OK for the smuggled path or reflected input from the injected request. If successful, the front-end may respond normally while the back-end logs or executes the hidden GET. Verify by checking access logs or response bodies for the smuggled action (e.g., access to /admin). If no effect, iterate on payload mutations.
