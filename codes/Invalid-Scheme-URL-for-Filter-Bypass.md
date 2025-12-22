---
id: a249893b-4d47-42f9-b1d2-118fb051c91d
name: Invalid-Scheme-URL-for-Filter-Bypass
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:37.608011+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - ssrf
  - bypass
  - payload
validated: true
---

# Invalid-Scheme-URL-for-Filter-Bypass

## Code

```powershell
0://evil.com:80;http://google.com:80/ 
```

## Description

This code snippet is a malformed URL payload designed to bypass PHP's filter_var() function in SSRF scenarios. The '0://' invalid scheme targets internal hosts/ports, while the semicolon-chained legitimate URL (http://google.com:80/) satisfies validation checks, allowing the SSRF request to proceed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| evil.com | Replace with internal target hostname/IP | 127.0.0.1 or 169.254.169.254 |
| 80 | Target port for scanning | 22, 80, 443, 3306 |
| google.com:80/ | Benign external URL to chain for validation | Any trusted domain:port/path |

## Usage

Embed this payload in SSRF-vulnerable parameters (e.g., via [[commands/curl-send-ssrf-payload]]) to force server-side requests to internal resources. Iterate ports by substituting values to scan for open services. Used in procedures like [[procedures/Bypass-PHP-Filter-Var-for-SSRF-Port-Scanning]] for internal discovery.

## Detection

- Log analysis for invalid URL schemes like '0://' or unusual semicolon-chained URLs in application inputs.
- WAF rules blocking non-standard protocols or internal IP references in payloads.
- Network monitoring for internal connections originating from web servers to unexpected ports.

## Related

- [[procedures/Bypass-PHP-Filter-Var-for-SSRF-Port-Scanning]]
- [[tools/URL-Port-Scanner]]
