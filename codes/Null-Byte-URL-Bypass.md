---
id: 51690bb4-a589-4b9a-a229-d2733de6e2f3
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798505+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - null-byte
  - string-termination
validated: true
---

# Null-Byte-URL-Bypass

## Code

```url-payload
//google%00.com
```

## Description

%00 terminates string in some parsers, allowing suffix bypass in filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| google%00.com | Blocked domain with null | evil%00.com |

## Usage

/redirect?url=//evil%00.com. Filter sees //evil.

## Detection

- Strip or reject %00 in URL parsing.
- Use secure string handling without null termination.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
