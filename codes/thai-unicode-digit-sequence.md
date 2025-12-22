---
type: code
language: plaintext
verified: true
platforms:
  - web
tags:
  - unicode
  - bypass
  - ssrf
validated: true
---

# Thai Unicode Digit Sequence

## Code

```plaintext
๐๑๒๓๔๕๖๗๘๙
```

## Description

This static string represents the digits 0-9 using Thai Unicode characters (U+0E50 to U+0E59). It serves as a reference for substituting digits in SSRF payloads to evade ASCII-only filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; use individual characters from the sequence | ๐ for 0, ๑ for 1 |

## Usage

In an SSRF attack, replace ASCII digits in internal URLs with these characters. For localhost (127.0.0.1): 'http://127.๐.๐.๑'. For AWS metadata (169.254.169.254): 'http://๑๖๙.๒๕๔.๑๖๙.๒๕๔'. Embed in HTTP requests via tools like curl. Ensure UTF-8 encoding to preserve characters.

## Detection

- Inspect URL parameters for non-ASCII Unicode characters in numeric positions.
- Implement Unicode normalization (NFKC) in filters to map these to standard digits.
- Monitor application logs for requests to internal IPs after decoding payloads.

## Related

- [[procedures/unicode-bypass-of-server-side-request-forgery-filters]]
