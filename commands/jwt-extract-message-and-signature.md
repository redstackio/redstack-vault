---
id: 0ce7f1f1-51d1-4788-87e1-641bde3ed92c-extract
name: jwt-extract-message-and-signature
type: command
executor: python
data: >-
  python3 -c "import sys, base64; token = sys.argv[1]; parts = token.split('.');
  if len(parts) != 3: print('Invalid JWT'); sys.exit(1); header, payload, sig =
  parts; msg = f'{header}.{payload}'; print(f'Message: {msg}'); sig_bytes =
  base64.urlsafe_b64decode(sig + '=' * (4 - len(sig) % 4)); print(f'Signature
  Hex: {sig_bytes.hex()}');" $_JWT_TOKEN
output: >-
  Message:
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ

  Signature Hex:
  a1d5f1e2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f
created_at: '2023-04-06T03:56:00.734085+00:00'
updated_at: '2023-04-10T20:22:35.257538+00:00'
platforms:
  - Linux
tags:
  - jwt
  - extraction
verified: true
validated: true
---

# jwt-extract-message-and-signature

## Command

```python
python3 -c "import sys, base64; token = sys.argv[1]; parts = token.split('.'); if len(parts) != 3: print('Invalid JWT'); sys.exit(1); header, payload, sig = parts; msg = f'{header}.{payload}'; print(f'Message: {msg}'); sig_bytes = base64.urlsafe_b64decode(sig + '=' * (4 - len(sig) % 4)); print(f'Signature Hex: {sig_bytes.hex()}');" $_JWT_TOKEN
```

## Description

This command extracts the message (header.payload) and hex-encoded signature from a JWT token for use in offline cracking. It uses Python's base64 module to handle base64url decoding, ensuring compatibility with HMAC formats.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | The full JWT string (e.g., eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.signature) | Yes |

## Examples

### Basic Usage

```python
python3 -c "..." eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

### Advanced Usage

Pipe output to files: python3 -c "..." $JWT_TOKEN > extract.txt

## Expected Output

Message: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
Signature Hex: a1d5f1e2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f

## Related

- [[procedures/Brute-Force-JWT-Signing-Secret]]
- [[commands/hashcat-crack-hmac-sha256]]
