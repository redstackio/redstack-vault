---
type: command
executor: bash
data: python3 jwt_tool.py $_TARGET_JWT -d
tags:
  - jwt
  - decode
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# jwt-tool-decode-token

## Command

```bash
python3 jwt_tool.py $_TARGET_JWT -d
```

## Description

Decodes a JWT token to reveal its header, payload, and signature components without verification. Useful for initial inspection before tampering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_JWT | The base64-encoded JWT string to decode | Yes |
| -d | Decode mode flag | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c -d
```

### Advanced Usage

Combine with output redirection for scripting:

```bash
python3 jwt_tool.py $_TARGET_JWT -d > decoded_jwt.txt
```

## Expected Output

Header: {"alg":"RS256","typ":"JWT"}
Payload: {"login":"user","exp":1234567890}
Signature: [base64 hash]

## Related

- [[procedures/JWT-Signature-Key-Injection-Attack]]
- [[tools/jwt-tool]]
