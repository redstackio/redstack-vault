---
id: 02b089ca-6ff9-4d68-a9b6-9111d3083d51
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798685+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - query-bypass
validated: true
---

# Query-String-Embedded-URL-Redirect

## Code

```url-payload
http://www.yoursite.com?http://www.theirsite.com/
http://www.yoursite.com?folder/www.folder.com
```

## Description

Embeds URL in query value, bypassing direct URL validation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| yoursite.com?http://their | Query with embedded | target.com?evil.com |

## Usage

/redirect?url=http://yoursite.com?evil.com.

## Detection

- Decode and validate all query values for schemes.
- Restrict query content.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
