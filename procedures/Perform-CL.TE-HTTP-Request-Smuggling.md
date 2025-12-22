---
id: a65b54fa-786b-4643-b643-c76457d0df48
name: Perform-CL.TE-HTTP-Request-Smuggling
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.953452+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - request-smuggling
  - http
  - web-vulnerability
  - cl-te
commands:
  - '[[commands/curl-send-prefix-request]]'
  - '[[commands/curl-send-smuggled-request]]'
platforms:
  - Web
tools:
  - '[[tools/cURL]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# Perform-CL.TE-HTTP-Request-Smuggling

## Summary

CL.TE HTTP Request Smuggling exploits a mismatch between how a front-end proxy interprets Content-Length (CL) headers and how a back-end server processes Transfer-Encoding (TE) headers. This allows an attacker to smuggle a malicious request past security controls, potentially bypassing authentication, accessing admin panels, or poisoning caches to affect other users.

## Description

In a CL.TE vulnerability, the front-end (e.g., a load balancer) parses requests using Content-Length, while the back-end treats them as chunked Transfer-Encoding. By sending a request with both headers, the front-end consumes a fixed length, but the back-end interprets the remainder as a new request. This technique is useful in web penetration testing to bypass web application firewalls (WAFs), perform unauthorized actions, or hijack sessions. It requires identifying a vulnerable endpoint, typically a POST or PUT method supporting both headers. Success depends on precise length calculations to ensure the smuggled payload aligns correctly.

## Requirements

1. Network access to a web application behind a proxy or load balancer vulnerable to CL.TE smuggling.
2. Knowledge of the target endpoint (e.g., /login or /api) that accepts POST requests with body content.
3. Tools like curl for crafting requests or Burp Suite for interception and manipulation.
4. Basic understanding of HTTP headers and chunked encoding.

## Defense

- Ensure consistent header parsing across front-end and back-end servers (e.g., disable TE on front-end or normalize to CL).
- Deploy a WAF with request smuggling detection rules, such as checking for conflicting CL and TE headers.
- Implement strict HTTP/1.1 compliance and reject ambiguous requests.
- Monitor for anomalous request patterns, like unexpected chunked bodies in non-chunked contexts.

## Objectives

1. Craft and send a smuggled request to bypass front-end security controls.
2. Execute unauthorized actions on the back-end, such as accessing restricted resources.
3. Demonstrate potential for cache poisoning or session hijacking affecting other users.

## Instructions

### Step 1: Identify Vulnerable Endpoint and Calculate Lengths

**Context**: Determine the target URL and compute the exact body lengths for the prefix and smuggled requests to ensure proper smuggling. The prefix request should have a body shorter than its CL to leave room for the smuggled request.

Use [[commands/curl-send-prefix-request]] to test the endpoint and measure responses:

```bash
curl -X POST -H "Host: target.com" -H "Content-Length: 10" -H "Transfer-Encoding: chunked" -d "prefixbody" https://target.com/vulnerable-endpoint
```

> This sends a prefix request with CL=10 and a 9-byte body ("prefixbody" is 9 chars), causing the back-end to wait for more data. Observe if the server hangs or responds abnormally, indicating vulnerability.

### Step 2: Craft and Send the Smuggled Request

**Context**: Send the second request immediately after the prefix, using the calculated chunk size. The smuggled request (e.g., a GET to /admin) will be appended and processed by the back-end as part of the first request's body but interpreted separately.

Calculate chunk size: Length of smuggled body + 5 (for TE.CL chunk extension). Then use [[commands/curl-send-smuggled-request]]:

```bash
curl -X POST -H "Host: target.com" -H "Content-Length: 20" -H "Transfer-Encoding: chunked" -d "smuggledGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" https://target.com/vulnerable-endpoint
```

> Here, CL=20 assumes a 15-byte smuggled body plus padding. The back-end sees the smuggled GET as the next chunk, executing it unauthorized. Verify by checking if /admin content is returned or cached.
