---
id: c4c8512c-9634-400c-ac08-fa126ac48006
name: HTTP-Request-Smuggling-CL-TE
type: procedure
verified: true
submitted: true
created_at: '2020-08-11T17:14:00.296169+00:00'
updated_at: '2023-05-26T01:06:44.183021+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# HTTP-Request-Smuggling-CL-TE

## Summary

This procedure demonstrates an HTTP Request Smuggling attack exploiting a Content-Length (CL) and Transfer-Encoding (TE) header mismatch between front-end and back-end servers. The front-end parses using CL while the back-end uses TE, allowing request desynchronization to smuggle malicious payloads and potentially hijack subsequent requests.

## Description

HTTP Request Smuggling occurs when front-end and back-end servers interpret ambiguous HTTP requests differently, leading to desynchronized parsing. In this CL.TE variant, the attacker sends a request with both Content-Length: 6 and Transfer-Encoding: chunked, followed by a zero-length chunk (0\r\n) and a dangling 'G' character. The front-end treats the body as 6 bytes up to the 'G', but the back-end interprets the chunked encoding, consuming only the zero chunk and leaving the 'G' to prefix the next legitimate request, causing errors like 'Unrecognized method GPOST'. This can lead to cache poisoning, bypassing security controls, or session hijacking in multi-user environments. Use this in web penetration testing against proxies or load balancers.

## Requirements

1. Burp Suite Professional or Community Edition installed and configured as a proxy.
2. Network access to intercept and proxy traffic to the target web application.
3. A legitimate HTTP request that can be intercepted (e.g., a POST to the target endpoint).
4. Target application vulnerable to CL.TE smuggling (front-end honors CL, back-end honors TE).

## Defense

Defensive measures and detection strategies:

- Normalize HTTP headers by removing or rejecting ambiguous combinations like CL and TE in the same request.
- Use strict HTTP/1.1 parsing on both front-end and back-end servers to enforce consistent header handling.
- Implement request logging and anomaly detection for desynchronized requests or unusual method prefixes (e.g., GPOST).
- Deploy Web Application Firewalls (WAFs) with rules to detect chunked encoding mismatches.

## Objectives

1. Exploit header parsing differences to smuggle a payload that desynchronizes request handling.
2. Observe the impact on subsequent requests, such as method prefixing or response poisoning.
3. Verify vulnerability to confirm potential for further attacks like cache manipulation.
4. Expected outcome: Server responds with errors indicating smuggled payload interference, such as 'Unrecognized method GPOST'.

## Instructions

### Step 1: Intercept the Legitimate Request

**Context**: Configure Burp Suite to capture outgoing traffic and intercept a standard POST request to the target endpoint. This provides a base request to modify for smuggling.

Use [[tools/Burp-Suite]] to enable interception in the Proxy tab.

> Launch Burp Suite, navigate to the Proxy > Intercept tab, and toggle 'Intercept is on'. Browse or submit a POST request to the target (e.g., / endpoint) to trigger interception.

### Step 2: Forward and Send to Repeater

**Context**: Forward the intercepted request to proceed with normal flow, then duplicate it in Repeater for modification without affecting the live session.

In the Intercept tab, click 'Forward' to release the request. Then, right-click the request in the Proxy > HTTP history tab and select 'Send to Repeater'.

> This isolates the request in the Repeater tab for safe experimentation.

### Step 3: Modify Request with Smuggling Payload

**Context**: Replace the request body and headers to include both CL and TE, creating the desynchronization. The payload uses a zero chunk to terminate TE parsing early, leaving the trailing 'G' for the next request.

Insert the smuggling payload using [[codes/HTTP-Request-Smuggling-CL-TE-Payload]]:

```
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked
0
G 
```

> Ensure the Host header matches the target domain. The Content-Length: 6 accounts for '0\r\nG \r\n', but TE chunked parsing ignores it after the zero chunk.

### Step 4: Send and Observe Responses

**Context**: Transmit the modified request multiple times to trigger the smuggling effect on subsequent legitimate requests. Monitor for signs of desynchronization in responses.

In the Repeater tab, click 'Send' 2-3 times. Then, send a normal POST request (e.g., via browser or another tool) and observe the response.

> The smuggled 'G' should prefix the next request's method, resulting in a 400 Bad Request or similar error like 'Unrecognized method GPOST' in the response body or status.

## Expected Output

Successful execution produces a response indicating parsing errors, such as:

HTTP/1.1 400 Bad Request
...
Unrecognized method GPOST

This confirms the back-end misinterpreted the request boundaries due to the smuggling.
