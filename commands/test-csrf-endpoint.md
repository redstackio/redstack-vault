---
id: b0312ef1-8f89-40ae-895c-eed4484061b1
name: test-csrf-endpoint
type: command
executor: bash
data: 'curl -X POST "https://target.com/api/endpoint" -d "data=value"'
output: null
created_at: '2025-12-11T06:10:22.168Z'
updated_at: '2025-12-11T06:10:22.168Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - csrf
  - web
verified: false
validated: true
submitted: true
---

# test-csrf-endpoint

## Command

```bash
curl -X POST "https://target.com/api/endpoint" -d "data=value"
```

## Description

Tests a web endpoint for CSRF by sending a POST request without tokens, checking if the action succeeds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specify POST method | Yes |
| `-d` | Data to send | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.tiktok.com/api/password/set" -d "new_password=test"
```

### Advanced Usage

```bash
curl -X POST "https://www.tiktok.com/api/password/set" -d "new_password=attacker123" -H "Origin: https://evil.com"
```

## Expected Output

Success response if no CSRF protection is present.

## Related

- [[commands/execute-csrf-payload]]
- [[procedures/Identify-CSRF-Vulnerability]]
