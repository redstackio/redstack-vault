---
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:37.347856+00:00'
updated_at: '2023-04-10T20:24:03.634843+00:00'
platforms:
  - Web
tags:
  - ssrf
  - bypass
  - localhost
validated: true
---

# ssrf-localhost-bypass-urls

## Code

```text
http://127.127.127.127
http://127.0.1.3
http://127.0.0.0
```

## Description

This code snippet provides example URLs using loopback IP variations within the 127.0.0.0/8 CIDR range to bypass localhost filters in SSRF attacks. These representations equate to 127.0.0.1 but may evade simple string-matching blocks, allowing requests to internal services.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static URLs; append ports/paths as needed (e.g., :80/internal) | http://127.127.127.127:8080/admin |

## Usage

Inject these URLs into SSRF-vulnerable parameters (e.g., image src or fetch endpoints) to force the server to request localhost resources. Test sequentially to find which evades the filter, then target specific internal endpoints like metadata services.

## Detection

- Log all outbound HTTP requests from the application server and alert on 127.x.x.x destinations.
- Implement IP normalization in filters to canonicalize variations (e.g., convert 127.127.127.127 to 127.0.0.1).
- Monitor for unusual internal fetches in application logs or WAF events.

## Related

- [[procedures/Bypass-Localhost-Filters-with-CIDR-in-SSRF]]
