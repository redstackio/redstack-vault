---
type: procedure
description: >-
  Exploit HTTP request smuggling vulnerability using Transfer-Encoding and
  Content-Length header discrepancies between front-end and back-end servers.
verified: true
submitted: true
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

# HTTP-Request-Smuggling-TE-CL

## Summary

This procedure demonstrates HTTP request smuggling by exploiting a discrepancy where the front-end server parses requests using the Transfer-Encoding header while the back-end server uses Content-Length. This allows smuggling a malicious second request (e.g., a prefixed 'GPOST' method) into the stream, leading to desynchronization and potential bypass of security controls or execution of unintended requests.

## Description

HTTP request smuggling occurs when front-end (e.g., load balancer or proxy) and back-end servers interpret HTTP request headers differently. In the TE.CL variant, the front-end honors Transfer-Encoding: chunked, treating the body as chunked data, while the back-end uses Content-Length, misinterpreting the smuggled request as the body. This can result in the back-end processing a hidden request, such as an invalid method like 'GPOST', causing errors that confirm the vulnerability. This technique is useful for bypassing WAFs, poisoning caches, or accessing admin functions. It targets web applications behind proxies and requires tools like Burp Suite for interception and manipulation.

## Requirements

1. Access to a vulnerable web application (e.g., PortSwigger Web Security Academy lab).
2. Burp Suite Professional or Community Edition installed and configured as a proxy.
3. Network access to intercept traffic between client and target server.
4. Basic understanding of HTTP protocol and chunked encoding.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP headers by removing or standardizing Transfer-Encoding and Content-Length on front-end servers.
- Use strict parsing libraries that reject ambiguous requests (e.g., enforce single header type).
- Implement request smuggling detection in WAFs by monitoring for duplicate or conflicting headers.
- Log and alert on chunked requests with low Content-Length values or unrecognized methods like 'GPOST'.

## Objectives

1. Intercept and modify HTTP requests to exploit header parsing differences.
2. Smuggle a secondary request to desynchronize front-end and back-end processing.
3. Confirm vulnerability by observing error responses from the back-end.
4. Potential for further exploitation like session hijacking or cache poisoning.

## Instructions

### Step 1: Intercept the Initial Request

**Context**: Use Burp Suite to capture a legitimate POST request to the target endpoint. This establishes the baseline traffic and allows modification in the next steps. Why: Interception is necessary to craft the smuggling payload without alerting the application.

Intercept the request using Burp Suite's Proxy tab by configuring your browser to route traffic through Burp (default: 127.0.0.1:8080).

**Expected Output**: The request appears in the Proxy > HTTP history, showing details like POST / HTTP/1.1, Host, Content-Type, etc.

### Step 2: Send to Repeater

**Context**: Forward the intercepted request to Burp Repeater for isolated testing and modification. Why: Repeater allows sending modified requests multiple times without re-intercepting, facilitating iteration on the payload.

Right-click the intercepted request in Proxy and select "Send to Repeater". The request loads in the Repeater tab.

**Expected Output**: Repeater window displays the raw request and response panels, ready for editing.

### Step 3: Modify Request with Smuggling Payload

**Context**: Replace the request body with the TE.CL smuggling payload to exploit the parsing difference. Why: The chunked encoding tricks the front-end into forwarding extra data as a new request, which the back-end interprets separately.

Replace the entire request with the smuggling payload from [[codes/HTTP-Request-Smuggling-TE-CL-Payload]]:

```http
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1
0
```

Update the Host header with the actual target domain.

**Expected Output**: No immediate error on send; the response may appear normal from the front-end.

### Step 4: Send and Observe Desynchronization

**Context**: Transmit the modified request multiple times to trigger back-end processing of the smuggled request. Why: Repeated sends amplify the desynchronization, making the back-end error visible in subsequent legitimate requests.

Click "Send" in Repeater 2-3 times. Then, send a normal POST request (e.g., x=1) in a new Repeater tab.

**Expected Output**: The normal request's response shows an error like "Unrecognized method GPOST", indicating the smuggled request was processed by the back-end.

### Step 5: Verify and Iterate

**Context**: Confirm the vulnerability and test variations. Why: Validation ensures the exploit works; iterations can target specific back-end behaviors.

If no error, adjust chunk size (e.g., change '5c' to match smuggled request length) and retry. Check server logs if accessible.

**Expected Output**: Consistent "GPOST" errors on follow-up requests confirm successful smuggling.

## Expected Output

Successful execution produces front-end responses that appear normal, but subsequent requests trigger back-end errors like "Unrecognized method GPOST". This desynchronization confirms the vulnerability, with potential for further exploits like accessing hidden endpoints.
