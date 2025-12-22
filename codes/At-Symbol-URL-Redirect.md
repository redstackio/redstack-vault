---
id: 207d7248-ccca-498f-9e43-3f045afbfecf
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798601+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - basic-auth-bypass
validated: true
---

# At-Symbol-URL-Redirect

## Code

```url-payload
http://www.theirsite.com@yoursite.com/
```

## Description

@ fakes credentials, using post-@ as host for redirect.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| theirsite.com@yoursite.com | Fake auth to malicious host | legit.com@evil.com |

## Usage

/redirect?url=http://legit.com@evil.com.

## Detection

- Parse and validate host separately from auth.
- Reject @ in non-auth contexts.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
