---
id: 496ac5cd-3995-4f39-8e5c-873636f2c35c
name: HTTP-Request-Smuggling-Obfuscating-TE-Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-12T03:10:39.271680+00:00'
updated_at: '2023-05-26T15:59:38.172684+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - http-request-smuggling
  - known-vulnerability
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

# HTTP-Request-Smuggling-Obfuscating-TE-Header

## Summary

This procedure demonstrates HTTP Request Smuggling by obfuscating the Transfer-Encoding (TE) header to cause a discrepancy in how the front-end and back-end servers parse the request. By adding a duplicate TE header with an invalid value, one server ignores the valid 'chunked' encoding while the other processes it, allowing smuggling of malicious payloads to the back-end.

## Description

HTTP Request Smuggling exploits differences in how front-end (e.g., load balancer or proxy) and back-end servers interpret HTTP headers, particularly Transfer-Encoding and Content-Length. In this variant, both servers support Transfer-Encoding, but the front-end is tricked into ignoring the valid 'Transfer-Encoding: chunked' header by including a duplicate 'Transfer-encoding: cow' (case variation and invalid value). The back-end still honors the chunked encoding, enabling the smuggled request (a second POST) to be processed unexpectedly. This can lead to bypassing security controls, session hijacking, or cache poisoning. It targets web applications behind proxies and requires interception tools like Burp Suite to craft and observe the requests.

## Requirements

1. Access to a vulnerable web application that uses a front-end proxy supporting but misparsing Transfer-Encoding headers.
2. Burp Suite or equivalent proxy tool installed and configured to intercept traffic.
3. Network access to the target host (e.g., via browser or direct HTTP client).
4. Basic understanding of HTTP/1.1 protocol and chunked transfer encoding.

## Defense

Defensive measures and detection strategies:

- Normalize HTTP headers by enforcing strict case-insensitive parsing and rejecting duplicate Transfer-Encoding headers at the front-end.
- Use consistent Content-Length and Transfer-Encoding handling across all servers; prefer Content-Length over chunked encoding where possible.
- Implement request smuggling detection via web application firewalls (WAFs) that validate header consistency and block ambiguous requests.
- Monitor for irregular request patterns, such as unexpected chunked data or duplicate headers, using logging and anomaly detection tools.

## Objectives

1. Obfuscate the Transfer-Encoding header to create a parsing discrepancy between front-end and back-end servers.
2. Smuggle a secondary HTTP request within the body of the primary request.
3. Confirm successful smuggling by observing the back-end's response to the hidden payload.
4. Achieve potential bypass of front-end security controls for further exploitation.

## Instructions

### Step 1: Intercept the Base Request

**Context**: Begin by capturing a legitimate POST request to the target endpoint using a proxy tool. This establishes the baseline for modification and ensures you can observe how the unmodified request is handled.

Use Burp Suite to intercept traffic from your browser or client.

> Navigate to the target application, trigger a POST request (e.g., form submission), and intercept it in Burp's Proxy tab.

### Step 2: Forward to Repeater for Modification

**Context**: Send the intercepted request to Burp Repeater to allow safe experimentation without affecting the live session. This isolates the testing environment.

**Tool** ([[tools/Burp-Suite]]):

> Right-click the intercepted request in the Proxy history and select "Send to Repeater". This loads the request into the Repeater tab for editing.

### Step 3: Craft the Smuggled Request with Obfuscated TE Header

**Context**: Modify the request to include both a valid Transfer-Encoding: chunked and an obfuscated Transfer-encoding: cow. This causes the front-end to ignore chunked encoding (falling back to Content-Length), while the back-end processes the chunked data, interpreting the trailing chunk as a new request.

**Code** ([[codes/HTTP-Request-Smuggling-TE-Obfuscation-Payload]]):

```
POST / HTTP/1.1
Host: your-lab-id.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked
Transfer-encoding: cow
5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
x=1 
0
```

> Paste the modified request into the Repeater Raw tab. The '5c' indicates a 92-byte chunk (hex for the smuggled POST length), followed by the hidden 'GPOST' request (prefixed with 'G' to avoid immediate parsing issues), and ending with a zero-length chunk ('0'). Send the request and observe the response.

### Step 4: Analyze the Response

**Context**: Verify the smuggling by checking if the back-end processed the hidden request. A successful response will reflect execution of the smuggled POST, such as updated form data or error messages indicating the secondary request was handled.

> In Burp Repeater, send the request multiple times if needed to poison caches or confirm consistency. Compare responses to the baseline unmodified request.

## Expected Output

Upon successful execution, the server response will indicate that the smuggled request was processed by the back-end, often showing effects like processed form data from the hidden POST (e.g., 'x=1' parameter acknowledged) or desynchronized subsequent requests. Look for HTTP 200 OK with unexpected content or errors revealing back-end handling.
