---
id: f196f50e-4d20-4fc8-827c-c2675f4a704a
name: HTTP-Request-Smuggling-TE-CL-to-Bypass-Front-End-Controls
type: procedure
verified: true
submitted: false
created_at: '2020-08-12T03:49:41.954433+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
  - Web
tags:
  - http-request-smuggling
  - web-applications
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# HTTP-Request-Smuggling-TE-CL-to-Bypass-Front-End-Controls

## Summary

This procedure demonstrates HTTP request smuggling using Transfer-Encoding: Chunked (TE.CL) to bypass front-end security controls when the backend server does not support Transfer-Encoding. It allows an attacker to access restricted areas, such as an admin panel, by manipulating request headers and body to confuse the front-end proxy while the backend processes the smuggled request correctly.

## Description

HTTP request smuggling exploits discrepancies in how front-end (e.g., load balancer or proxy) and backend servers parse HTTP requests, particularly when mixing Transfer-Encoding: chunked and Content-Length headers. In this TE.CL variant, the front-end ignores Transfer-Encoding and uses Content-Length, while the backend processes the chunked body, leading to desynchronization. This can smuggle unauthorized requests, such as accessing /admin, bypassing authentication checks. The technique is effective against web applications where the front-end enforces access controls but the backend does not validate them properly. Prerequisites include the ability to intercept and modify requests, typically in a lab or controlled environment simulating a vulnerable setup.

## Requirements

- Access to a proxy tool like Burp Suite for intercepting and modifying HTTP requests.
- A target web application with a front-end proxy that supports Content-Length but ignores Transfer-Encoding, and a backend that processes chunked encoding.
- Network access to the target server (e.g., localhost or remote host).
- Basic knowledge of HTTP protocol and Burp Suite Repeater functionality.

## Defense

- Ensure consistent HTTP parsing between front-end and backend servers (e.g., disable Transfer-Encoding on front-end or enforce strict header validation).
- Implement request normalization and validation at the front-end to reject ambiguous requests.
- Monitor for anomalous request patterns, such as mismatched Content-Length and Transfer-Encoding headers, using WAF logs.
- Use HTTP/2 or higher where smuggling is harder due to binary framing.

## Objectives

1. Intercept and modify legitimate requests to introduce smuggling payloads.
2. Bypass front-end access controls to reach restricted endpoints like /admin.
3. Gain unauthorized access to admin functionality on the backend.

## Instructions

### Step 1: Intercept and Observe Normal Request

**Context**: Begin by capturing a standard POST request to a protected endpoint, such as /admin, using Burp Suite. This establishes the baseline response, which should indicate unauthorized access due to front-end controls. Ensure the "Update Content-Length" option is disabled in Burp to manually control headers.

Intercept the request in Burp Suite Proxy and forward it to the Repeater tab for modification.

### Step 2: Craft and Send Smuggling Payload

**Context**: Modify the intercepted request by prepending a chunked transfer-encoding payload to smuggle an unauthorized request. This exploits the parsing difference: the front-end consumes the Content-Length portion, leaving the chunked backend request to be processed separately.

Use the smuggling request payload from [[codes/HTTP-Smuggling-TE-CL-Basic-Request]]:

```
60
POST /admin HTTP/1.1
Content-Type:  application/x-www-form-urlencoded
Content-Length: 15 
x=1
0
```

Send the modified request via Burp Repeater and observe the response, which should still deny access as the front-end processes the initial chunk incorrectly.

### Step 3: Enhance Payload with Host Header and Access Admin

**Context**: Refine the smuggling payload by adding a Host header to direct the smuggled request properly to the backend, allowing access to the admin panel. This step completes the bypass by ensuring the backend interprets the full smuggled POST to /admin.

Modify the request using the enhanced payload from [[codes/HTTP-Smuggling-TE-CL-Request-with-Host]]:

```
60
POST /admin HTTP/1.1
Host: localhost
Content-Type:  application/x-www-form-urlencoded
Content-Length: 15 
x=1
0
```

Send via Burp Repeater. The front-end should process the prefix, but the backend executes the smuggled /admin request, granting access.
