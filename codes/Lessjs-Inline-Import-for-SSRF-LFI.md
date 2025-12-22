---
type: code
language: less
verified: true
tags:
  - ssti
  - ssrf
  - lfi
  - payload
platforms:
  - Web
validated: true
---

# Lessjs-Inline-Import-for-SSRF-LFI

## Code

```less
@import (inline) "http://localhost";
// or
@import (inline) "/etc/passwd";
```

## Description

This Lessjs code snippet exploits the inline import feature to perform Server Side Template Injection (SSTI). The first variant triggers Server Side Request Forgery (SSRF) by forcing the server to fetch a remote or internal URL during CSS compilation. The second variant enables Local File Inclusion (LFI) by including local file contents directly into the compiled CSS output. Use this in user-controlled Lessjs inputs to leak data or access unauthorized resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL/Path | Target URL for SSRF or file path for LFI | `http://169.254.169.254/latest/meta-data/` (AWS metadata) or `/etc/shadow` |

## Usage

Inject this code into any application endpoint that compiles Lessjs server-side, such as CSS upload forms or dynamic theme editors. Replace the URL/path with target internals (e.g., metadata services for SSRF) or sensitive files (e.g., config files for LFI). Observe the compiled CSS for embedded content, which exfiltrates the fetched data. Chain with URL encoding if inputs are sanitized.

## Detection

- Monitor Lessjs compilation logs for unexpected import URLs or file paths.
- WAF rules to block @import statements with http/https schemes or absolute file paths in CSS inputs.
- Anomaly detection in network traffic for internal requests originating from the web server.
- Review compiled CSS outputs for non-CSS content like file dumps or HTML snippets.

## Related

- [[procedures/Exploit-Lessjs-SSTI-via-Inline-Import]]
