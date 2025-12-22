---
id: 05fb2e89-cab9-4bdc-9dd6-94bca8c9bd12
name: decode-jwt-with-jwt-tool
type: command
executor: bash
data: python3 jwt_tool.py $_JWT_TOKEN -X a
output: null
created_at: '2023-04-06T03:56:00.609698+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - decode
verified: true
validated: true
---

# decode-jwt-with-jwt-tool

## Command

```bash
python3 jwt_tool.py $_JWT_TOKEN -X a
```

## Description

This command uses the jwt_tool to decode a JWT token, displaying its header, payload, and signature in a human-readable format. The -X a flag enables basic inspection mode, useful for analyzing token structure before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | The full JWT token string to decode (e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9...) | Yes |
| -X a | Inspection mode flag for decoding and displaying token parts | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6InRlc3QiLCJpYXQiOiIxNTA3NzU1NTcwIn0.YWUyMGU4YTI2ZGEyZTQ1MzYzOWRkMjI5YzIyZmZhZWM0NmRlMWVhNTM3NTQwYWY2MGU5ZGMwNjBmMmU1ODQ3OQ -X a
```

### Advanced Usage

For more detailed analysis, chain with other flags like -T for tampering checks:

```bash
python3 jwt_tool.py $_JWT_TOKEN -X a -T
```

## Expected Output

Header: {"alg": "HS256", "typ": "JWT"}

Payload: {"login": "test", "iat": "1507755570"}

Signature: YWUyMGU4YTI2ZGEyZTQ1MzYzOWRkMjI5YzIyZmZhZWM0NmRlMWVhNTM3NTQwYWY2MGU5ZGMwNjBmMmU1ODQ3OQ

The tool outputs parsed sections, helping identify modifiable claims and the current algorithm.

## Related

- [[procedures/Exploit-JWT-None-Algorithm-Vulnerability]]
- [[tools/jwt-tool]]
