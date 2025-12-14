---
data: >-
  curl -H "authorization:Bearer
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc"
  localhost:3000
tags:
  - test
  - http
  - jwt
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.013Z'
id: cee8dcc8-0d55-4b83-a115-e42c517a6029
verified: false
validated: true
submitted: true
---
# curl-send-jwt-token-jti1

## Command

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

## Description

Sends a GET request to the local server with a crafted JWT token (jti=1) in the Authorization header to test authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Header flag | Yes |
| authorization:Bearer ... | JWT token header | Yes |
| localhost:3000 | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

### Advanced Usage

```bash
curl -v -H "authorization:Bearer ..." localhost:3000
```

## Expected Output

"logged in as: 1"

## Related

- [[commands/curl-send-forged-jwt-token-jti2]]
