---
type: code
language: http
verified: true
tags:
  - http2
  - smuggling
  - payload
  - web
platforms:
  - Web
validated: true
---

# HTTP-2-Request-Smuggling-Payload

## Code

```http
:method GET
:path /
:authority www.example.com
header ignored\r\n\r\nGET / HTTP/1.1\r\nHost: www.example.com
```

## Description

This code snippet is a malformed HTTP/2 request payload designed for request smuggling attacks. It starts with standard HTTP/2 pseudo-headers for a legitimate GET request, followed by an invalid "header ignored" line and an early termination (\r\n\r\n), which smuggles an embedded HTTP/1.1 GET request. This exploits discrepancies in how front-end proxies parse and forward the request to back-end servers, potentially allowing the smuggled request to be processed independently.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| :authority | The target host/domain to replace with the actual server | www.vulnerable-site.com |

(Note: Replace the literal "www.example.com" in the code with the target before use; the code itself remains unchanged.)

## Usage

This payload is used in HTTP/2 request smuggling procedures to bypass security controls. Save it to a file and send via an HTTP/2 client supporting raw frames (e.g., h2c tool, Python with hyper library, or Burp Suite Repeater with HTTP/2 enabled). Typically injected after verifying HTTP/2 support; monitor for desynchronized responses indicating success, such as execution of the smuggled GET to a sensitive path like /admin.

## Detection

- Log analysis for malformed HTTP/2 frames with mixed HTTP/1.1 content or duplicate pseudo-headers.
- WAF alerts on invalid header names (e.g., "header ignored") or unexpected \r\n sequences in request bodies.
- Network monitoring for multiple requests multiplexed in a single stream or abnormal response timings.
- Server error logs showing parsing failures or unexpected request methods.

## Related

- [[procedures/HTTP-2-Request-Smuggling]]
