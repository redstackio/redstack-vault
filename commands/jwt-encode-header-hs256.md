---
type: command
executor: bash
data: 'echo -n ''{"typ":"JWT","alg":"HS256"}'' | base64 -w 0'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - jwt
  - encoding
verified: true
validated: true
---

# jwt-encode-header-hs256

## Command

```bash
echo -n '{"typ":"JWT","alg":"HS256"}' | base64 -w 0
```

## Description

Encodes the standard JWT header for HMAC-SHA256 (HS256) algorithm into base64 format without line wraps. This is the first part of a JWT token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed header for HS256; customize JSON for other algs | No |

## Examples

### Basic Usage

```bash
echo -n '{"typ":"JWT","alg":"HS256"}' | base64 -w 0
```

### Advanced Usage

For RS256: echo -n '{"typ":"JWT","alg":"RS256"}' | base64 -w 0

## Expected Output

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

## Related

- [[procedures/Create-and-Verify-JWT-Tokens-for-Forgery]]
