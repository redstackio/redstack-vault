---
data: |-
  curl -X POST https://target.com/reset-verify \
    -H "Content-Type: application/json" \
    -d "{\"token\": \"reset_token\", \"code\": \"123456\"}" \
    -b cookies.txt
tags:
  - web-testing
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.547Z'
id: b7832dec-8a8c-47b3-bd5b-5937b14e74af
verified: false
validated: true
submitted: true
---
# curl-reset-verify

## Command

```bash
curl -X POST https://target.com/reset-verify \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"reset_token\", \"code\": \"123456\"}" \
  -b cookies.txt
```

## Description

This curl command verifies a password reset token and code, useful for inspecting post-reset flows to detect 2FA prompts in enumeration attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d` | Payload with token and code | Yes |
| `-b cookies.txt` | Load session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/reset-verify -d 'token=abc123&code=123456'
```

### Advanced Usage

```bash
curl -X POST https://target.com/reset-verify \
  -H "Content-Type: application/json" \
  -d '{"token": "abc123", "code": "123456"}' \
  -b cookies.txt -v
```

## Expected Output

JSON response indicating verification success or failure, potentially including 2FA challenge fields like {"requires_2fa": true, "prompt": "Enter TOTP"}.

## Related

- [[commands/curl-password-reset]]
- [[procedures/Enumerate-2FA-Status-via-Password-Reset]]
