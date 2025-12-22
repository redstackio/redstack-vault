---
id: 48fa8f4b-074c-45bf-9fc8-68ed2ed10867
name: jwt-sign-with-private-key
type: command
executor: bash
data: >-
  openssl genrsa -out $_PRIVATE_KEY 2048 && openssl rsa -in $_PRIVATE_KEY
  -pubout -out public.pem && echo
  '{"keys":[{"kty":"RSA","kid":"$_KEY_ID","n":"$(openssl rsa -pubin -in
  public.pem -modulus -noout | cut -d= -f2)","e":"AQAB"}]}' > $_JWKS_FILE
output: null
created_at: '2023-04-06T03:56:00.839943+00:00'
updated_at: '2023-04-10T20:22:36.345573+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - keygen
  - jwks
verified: true
validated: true
---

# jwt-sign-with-private-key

## Command

```bash
openssl genrsa -out $_PRIVATE_KEY 2048 && openssl rsa -in $_PRIVATE_KEY -pubout -out public.pem && echo '{"keys":[{"kty":"RSA","kid":"$_KEY_ID","n":"$(openssl rsa -pubin -in public.pem -modulus -noout | cut -d= -f2)","e":"AQAB"}]}' > $_JWKS_FILE
```

## Description

Generates an RSA private key, extracts the public key, and creates a JWKS file for hosting. Used to prepare keys for JWT signing and verification bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PRIVATE_KEY | Output file for private key (e.g., private.pem) | Yes |
| $_KEY_ID | Key ID for JWKS (e.g., 'malicious-key') | Yes |
| $_JWKS_FILE | Output JWKS file (e.g., jwks.json) | Yes |

## Examples

### Basic Usage

```bash
openssl genrsa -out private.pem 2048 && openssl rsa -in private.pem -pubout -out public.pem && echo '{"keys":[{"kty":"RSA","kid":"key1","n":"...","e":"AQAB"}]}' > jwks.json
```

### Advanced Usage

```bash
# Use existing key: openssl rsa -in existing.pem -pubout -out public.pem && ... (rest)
```

## Expected Output

Generated files: private.pem, public.pem, jwks.json with {"keys":[...]} containing RSA modulus and exponent.

## Related

- [[procedures/JWT-Token-Forgery-via-JWKS-Header-Injection]]
- [[commands/jwt-tool-sign-with-jku-injection]]
