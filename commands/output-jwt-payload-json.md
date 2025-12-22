---
type: command
executor: bash
data: 'echo ''{"sub":"1234567890","name":"John Doe","iat":1516239022}'''
output: null
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - jwt
  - token-craft
verified: true
validated: true
---

# output-jwt-payload-json

## Command

```bash
echo '{"sub":"1234567890","name":"John Doe","iat":1516239022}'
```

## Description

Outputs a sample JSON payload for a JWT token, including subject (user ID), name, and issued-at timestamp. Customize claims for impersonation in authentication bypass attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; outputs fixed sample, but edit inline for custom claims | No |

## Examples

### Basic Usage

```bash
echo '{"sub":"1234567890","name":"John Doe","iat":1516239022}'
```

### Advanced Usage

With dynamic timestamp:

```bash
echo '{"sub":"target_user","iat":'$(date +%s)'}'
```

## Expected Output

{"sub":"1234567890","name":"John Doe","iat":1516239022}

## Related

- [[procedures/jwt-null-signature-authentication-bypass]]
- [[commands/output-jwt-null-header-json]]
